from __future__ import annotations

from collections import defaultdict
from statistics import median

from .records import Record


def quality_floor(records: list[Record], minimum: float) -> list[Record]:
    return [x for x in records if x.task_score >= minimum]


def _scale(value: float, low: float, high: float, invert: bool = False) -> float:
    if high == low:
        return 1.0
    result = (value - low) / (high - low)
    return 1.0 - result if invert else result


def normalized_table(records: list[Record]) -> list[dict]:
    if not records:
        return []
    memory = [x.peak_memory_gb for x in records]
    load = [x.load_seconds for x in records]
    prompt = [x.prompt_seconds for x in records]
    decode = [x.decode_tps for x in records]
    quality = [x.task_score for x in records]

    out = []
    for row in records:
        out.append({
            **row.__dict__,
            "memory_efficiency": _scale(row.peak_memory_gb, min(memory), max(memory), invert=True),
            "load_efficiency": _scale(row.load_seconds, min(load), max(load), invert=True),
            "prompt_efficiency": _scale(row.prompt_seconds, min(prompt), max(prompt), invert=True),
            "decode_efficiency": _scale(row.decode_tps, min(decode), max(decode)),
            "quality_normalized": _scale(row.task_score, min(quality), max(quality)),
        })
    return out


def group_summary(records: list[Record]) -> list[dict]:
    groups: dict[tuple[str, str], list[Record]] = defaultdict(list)
    for row in records:
        groups[(row.model_family, row.quant)].append(row)
    out = []
    for (family, quant), rows in sorted(groups.items()):
        out.append({
            "model_family": family,
            "quant": quant,
            "runs": len(rows),
            "median_memory_gb": median(x.peak_memory_gb for x in rows),
            "median_load_s": median(x.load_seconds for x in rows),
            "median_prompt_s": median(x.prompt_seconds for x in rows),
            "median_decode_tps": median(x.decode_tps for x in rows),
            "median_score": median(x.task_score for x in rows),
        })
    return out

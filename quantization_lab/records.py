from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Record:
    model_family: str
    variant: str
    quant: str
    runtime: str
    size_gb: float
    peak_memory_gb: float
    load_seconds: float
    prompt_seconds: float
    decode_tps: float
    total_seconds: float
    task_score: float
    context_tokens: int
    prompt_tokens: int = 0
    output_tokens: int = 0


def dominates(a: Record, b: Record) -> bool:
    no_worse = (
        a.peak_memory_gb <= b.peak_memory_gb
        and a.size_gb <= b.size_gb
        and a.load_seconds <= b.load_seconds
        and a.prompt_seconds <= b.prompt_seconds
        and a.decode_tps >= b.decode_tps
        and a.task_score >= b.task_score
    )
    strictly_better = (
        a.peak_memory_gb < b.peak_memory_gb
        or a.size_gb < b.size_gb
        or a.load_seconds < b.load_seconds
        or a.prompt_seconds < b.prompt_seconds
        or a.decode_tps > b.decode_tps
        or a.task_score > b.task_score
    )
    return no_worse and strictly_better


def frontier(records: list[Record]) -> list[Record]:
    return [
        candidate
        for candidate in records
        if not any(
            dominates(other, candidate)
            for other in records
            if other != candidate
        )
    ]

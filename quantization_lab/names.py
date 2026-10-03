from pathlib import Path
import re


PATTERNS = [
    re.compile(r"(?i)(Q[2-8](?:_[A-Z0-9]+)?)"),
    re.compile(r"(?i)([2-8]bit)"),
    re.compile(r"(?i)(int[2-8])"),
]


def infer_quantization(filename: str) -> str | None:
    name = Path(filename).name
    for pattern in PATTERNS:
        match = pattern.search(name)
        if match:
            return match.group(1).upper()
    return None


def model_files(path: str) -> list[dict]:
    root = Path(path)
    rows = []
    for item in sorted(root.rglob("*")):
        if not item.is_file():
            continue
        if item.suffix.lower() not in {".gguf", ".safetensors"}:
            continue
        rows.append({
            "path": str(item),
            "size_gb": item.stat().st_size / (1024 ** 3),
            "quant": infer_quantization(item.name),
        })
    return rows

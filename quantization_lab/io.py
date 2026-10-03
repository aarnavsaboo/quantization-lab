from pathlib import Path
import json
from .records import Record


def load(path: str) -> list[Record]:
    rows = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(Record(**json.loads(line)))
    return rows


def dump(path: str, rows: list[Record]) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        "".join(json.dumps(row.__dict__, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )

from dataclasses import asdict, dataclass
from hashlib import sha1
from itertools import product
import json


@dataclass(frozen=True)
class Experiment:
    id: str
    model_family: str
    variant: str
    runtime: str
    prompt_file: str
    output_tokens: int
    repeat: int

    def to_dict(self):
        return asdict(self)


def expand(config: dict) -> list[Experiment]:
    rows = []
    for variant, prompt, output_tokens, repeat in product(
        config["variants"],
        config["prompt_files"],
        config.get("output_tokens", [128]),
        range(int(config.get("repeats", 3))),
    ):
        payload = {
            "model_family": config["model_family"],
            "variant": variant,
            "runtime": config.get("runtime", "local"),
            "prompt_file": prompt,
            "output_tokens": int(output_tokens),
            "repeat": repeat,
        }
        ident = sha1(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:16]
        rows.append(Experiment(id=ident, **payload))
    return rows

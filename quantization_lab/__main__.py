from argparse import ArgumentParser
from pathlib import Path
import json

from .analysis import group_summary, normalized_table, quality_floor
from .io import load
from .names import model_files
from .records import frontier


def main():
    parser = ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    inspect = sub.add_parser("inspect")
    inspect.add_argument("path")

    front = sub.add_parser("frontier")
    front.add_argument("path")

    table = sub.add_parser("table")
    table.add_argument("path")
    table.add_argument("--quality-floor", type=float, default=0.0)
    table.add_argument("--normalized", action="store_true")

    args = parser.parse_args()

    if args.cmd == "inspect":
        print(json.dumps(model_files(args.path), indent=2))
        return

    rows = load(args.path)
    if args.cmd == "frontier":
        data = [x.__dict__ for x in frontier(rows)]
    else:
        filtered = quality_floor(rows, args.quality_floor)
        data = normalized_table(filtered) if args.normalized else group_summary(filtered)
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()

from argparse import ArgumentParser
from datetime import datetime
from tabulate import tabulate

import json
import os
import sys

## TODO

def main() -> None:
    parser = ArgumentParser(description="CLI tool")
    # parser.add_subparsers
    parser.add_argument("name", help="Your name")
    parser.add_argument("--greet", help="Custom greeting", default="Hello")

    args = parser.parse_args()

    print(f"{args.greet}, {args.name}")

if __name__ == "__main__":
    main()
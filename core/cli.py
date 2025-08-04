from argparse import ArgumentParser
from datetime import datetime
from tabulate import tabulate

import json
import os
import sys

## TODO
## Task properties: | id | description | status | createdAt | updatedAt |

def main() -> None:
    parser = ArgumentParser(description="CLI tool")
    # parser.add_subparsers
    parser.add_argument("name", help="Your name")
    parser.add_argument("--greet", help="Custom greeting", default="Hello")

    args = parser.parse_args()

    print(f"{args.greet}, {args.name}")

def load_database():
    pass

def save_database():
    pass

def add_task():
    pass

def delete_task():
    pass

def update_task():
    pass

## list all tasks
## list by all tasks by progression
def list_tasks():
    pass

def change_status():
    pass

if __name__ == "__main__":
    main()
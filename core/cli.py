import argparse

parser = argparse.ArgumentParser(description="A simple CLI tool")
parser.add_argument("name", help="Your name")
parser.add_argument("--greet", help="Custom greeting", default="Hello")

args = parser.parse_args()

print(f"{args.greet}, {args.name}!")
"""CLI for sql-agent-text2sql."""
from __future__ import annotations

import argparse

from .agent import dump_trace, run_agent

def main() -> None:
    p = argparse.ArgumentParser(description="Natural language to SQL agent over a sample SQLite database with safe read-only execution.")
    p.add_argument("question", nargs="?", default="Calculate 12*(3+4)")
    p.add_argument("--trace", action="store_true")
    args = p.parse_args()
    result = run_agent(args.question)
    print(result.answer)
    if args.trace:
        print(dump_trace(result))

if __name__ == "__main__":
    main()

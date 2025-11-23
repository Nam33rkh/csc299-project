# Technical Plan

- Programming Language: Python 3.10+
- Package system: uv + pyproject.toml
- CLI parsing: argparse
- Testing: pytest
- Data model:
  - Task(id, title, notes, done)
- Storage:
  - tasks.json (local JSON file)
- Commands:
  - add
  - list
  - complete
  - delete
  - search (--query)
- Output formatting: simple console printing
- Goal: match the structure and behavior of the class demo.

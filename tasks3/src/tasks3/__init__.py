def inc(n: int) -> int:
    return n + 1

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

DB_DEFAULT = Path("./tasks3_db.json")

@dataclass
class Task:
    id: int
    title: str
    notes: str = ""

def load_db(path: Path = DB_DEFAULT) -> List[Task]:
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Task(**row) for row in data]

def save_db(tasks: List[Task], path: Path = DB_DEFAULT) -> None:
    path.write_text(json.dumps([asdict(t) for t in tasks], indent=2), encoding="utf-8")

def add_task(title: str, notes: str = "", path: Path = DB_DEFAULT) -> Task:
    tasks = load_db(path)
    next_id = (max((t.id for t in tasks), default=0) + 1)
    task = Task(id=next_id, title=title, notes=notes)
    tasks.append(task)
    save_db(tasks, path)
    return task

def list_tasks(query: str | None = None, path: Path = DB_DEFAULT) -> List[Task]:
    tasks = load_db(path)
    if query:
        q = query.lower()
        tasks = [t for t in tasks if q in t.title.lower() or q in t.notes.lower()]
    return tasks

def main():
    parser = argparse.ArgumentParser(prog="tasks3", description="Tiny JSON task manager")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="Add a task")
    p_add.add_argument("title")
    p_add.add_argument("--notes", default="")

    p_list = sub.add_parser("list", help="List tasks")
    p_list.add_argument("--query", default=None)

    args = parser.parse_args()
    if args.cmd == "add":
        t = add_task(args.title, args.notes)
        print(f"Added #{t.id}: {t.title}")
    elif args.cmd == "list":
        for t in list_tasks(args.query):
            print(f"[{t.id}] {t.title}" + (f" — {t.notes}" if t.notes else ""))

if __name__ == "__main__":
    main()

import argparse, json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

DB_DEFAULT = Path("./tasks.json")

@dataclass
class Task:
    id: int
    title: str
    notes: str = ""
    done: bool = False

def load_db(path: Path = DB_DEFAULT) -> List[Task]:
    if not path.exists():
        return []
    return [Task(**row) for row in json.loads(path.read_text(encoding="utf-8"))]

def save_db(tasks: List[Task], path: Path = DB_DEFAULT) -> None:
    path.write_text(json.dumps([asdict(t) for t in tasks], indent=2), encoding="utf-8")

def next_id(tasks: List[Task]) -> int:
    return max((t.id for t in tasks), default=0) + 1

def cmd_add(title: str, notes: str = "", path: Path = DB_DEFAULT) -> Task:
    tasks = load_db(path)
    t = Task(id=next_id(tasks), title=title, notes=notes)
    tasks.append(t)
    save_db(tasks, path)
    return t

def cmd_list(query: str | None = None, path: Path = DB_DEFAULT) -> List[Task]:
    tasks = load_db(path)
    if query:
        q = query.lower()
        tasks = [t for t in tasks if q in t.title.lower() or q in t.notes.lower()]
    return tasks

def cmd_complete(task_id: int, path: Path = DB_DEFAULT) -> bool:
    tasks = load_db(path)
    for t in tasks:
        if t.id == task_id:
            t.done = True
            save_db(tasks, path)
            return True
    return False

def cmd_delete(task_id: int, path: Path = DB_DEFAULT) -> bool:
    tasks = load_db(path)
    new = [t for t in tasks if t.id != task_id]
    if len(new) == len(tasks):
        return False
    save_db(new, path)
    return True

def main():
    p = argparse.ArgumentParser(prog="tasks5", description="Spec-kit tasks manager")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="Add a task")
    a.add_argument("title")
    a.add_argument("--notes", default="")

    l = sub.add_parser("list", help="List tasks")
    l.add_argument("--query", default=None)

    c = sub.add_parser("complete", help="Mark a task as done")
    c.add_argument("id", type=int)

    d = sub.add_parser("delete", help="Delete a task")
    d.add_argument("id", type=int)

    args = p.parse_args()

    if args.cmd == "add":
        t = cmd_add(args.title, args.notes)
        print(f"Added #{t.id}: {t.title}")
    elif args.cmd == "list":
        for t in cmd_list(args.query):
            status = "✓" if t.done else " "
            extra = f" — {t.notes}" if t.notes else ""
            print(f"[{t.id}] [{status}] {t.title}{extra}")
    elif args.cmd == "complete":
        print("Completed" if cmd_complete(args.id) else "Not found")
    elif args.cmd == "delete":
        print("Deleted" if cmd_delete(args.id) else "Not found")

if __name__ == "__main__":
    main()

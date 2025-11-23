from pathlib import Path
from tasks5 import cmd_add, cmd_list, cmd_complete, cmd_delete, load_db

def test_add_and_list(tmp_path: Path):
    db = tmp_path / "db.json"
    cmd_add("Write spec", "for CLI", db)
    cmd_add("Plan tests", path=db)
    titles = [t.title for t in cmd_list(path=db)]
    assert titles == ["Write spec", "Plan tests"]

def test_search_and_complete(tmp_path: Path):
    db = tmp_path / "db.json"
    cmd_add("Homework", "Data Structures", db)
    cmd_add("Groceries", "apples", db)
    hits = cmd_list(query="data", path=db)
    assert len(hits) == 1 and hits[0].title == "Homework"
    ok = cmd_complete(hits[0].id, db)
    assert ok
    assert [t.done for t in load_db(db) if t.title == "Homework"][0] is True

def test_delete(tmp_path: Path):
    db = tmp_path / "db.json"
    a = cmd_add("Temp", path=db)
    assert cmd_delete(a.id, db) is True
    assert cmd_delete(999, db) is False
    assert cmd_list(path=db) == []

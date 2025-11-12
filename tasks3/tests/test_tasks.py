from pathlib import Path
from tasks3 import add_task, list_tasks, save_db, load_db

def test_add_and_list_roundtrip(tmp_path: Path):
    db = tmp_path / "db.json"
    t1 = add_task("Write README", "include run instructions", db)
    t2 = add_task("Implement search", "query by title/notes", db)
    assert t1.id == 1 and t2.id == 2
    titles = [t.title for t in list_tasks(path=db)]
    assert titles == ["Write README", "Implement search"]

def test_search_queries_title_and_notes(tmp_path: Path):
    db = tmp_path / "db.json"
    add_task("Groceries", "buy apples", db)
    add_task("Homework", "Data Structures", db)
    add_task("Workout", "leg day", db)
    hits = list_tasks(query="data", path=db)
    assert len(hits) == 1 and hits[0].title == "Homework"

def test_save_load_empty(tmp_path: Path):
    db = tmp_path / "db.json"
    save_db([], db)
    assert load_db(db) == []

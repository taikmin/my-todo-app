import json
import uuid
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "todos.json"


def _load() -> list[dict]:
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def _save(todos: list[dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")


def get_all() -> list[dict]:
    return _load()


def add(title: str, priority: str = "보통", due_date: str = "") -> dict:
    todos = _load()
    todo = {
        "id": str(uuid.uuid4()),
        "title": title.strip(),
        "priority": priority,
        "due_date": due_date,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    todos.append(todo)
    _save(todos)
    return todo


def toggle_done(todo_id: str) -> None:
    todos = _load()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = not t["done"]
            break
    _save(todos)


def delete(todo_id: str) -> None:
    todos = [t for t in _load() if t["id"] != todo_id]
    _save(todos)


def update(todo_id: str, title: str, priority: str, due_date: str) -> None:
    todos = _load()
    for t in todos:
        if t["id"] == todo_id:
            t["title"] = title.strip()
            t["priority"] = priority
            t["due_date"] = due_date
            break
    _save(todos)


def delete_done() -> int:
    todos = _load()
    before = len(todos)
    todos = [t for t in todos if not t["done"]]
    _save(todos)
    return before - len(todos)

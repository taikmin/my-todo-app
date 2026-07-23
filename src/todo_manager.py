import uuid
from datetime import datetime

import streamlit as st
from supabase import create_client


@st.cache_resource
def _client():
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])


def get_all() -> list[dict]:
    result = _client().table("todos").select("*").order("created_at").execute()
    return result.data


def add(title: str, priority: str = "보통", due_date: str = "") -> dict:
    todo = {
        "id": str(uuid.uuid4()),
        "title": title.strip(),
        "priority": priority,
        "due_date": due_date,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    _client().table("todos").insert(todo).execute()
    return todo


def toggle_done(todo_id: str) -> None:
    result = _client().table("todos").select("done").eq("id", todo_id).single().execute()
    current = result.data["done"]
    _client().table("todos").update({"done": not current}).eq("id", todo_id).execute()


def delete(todo_id: str) -> None:
    _client().table("todos").delete().eq("id", todo_id).execute()


def update(todo_id: str, title: str, priority: str, due_date: str) -> None:
    _client().table("todos").update({
        "title": title.strip(),
        "priority": priority,
        "due_date": due_date,
    }).eq("id", todo_id).execute()


def delete_done() -> int:
    result = _client().table("todos").select("id").eq("done", True).execute()
    count = len(result.data)
    _client().table("todos").delete().eq("done", True).execute()
    return count

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from datetime import date

import streamlit as st
import todo_manager as tm

PRIORITY_EMOJI = {"높음": "🔴", "보통": "🟡", "낮음": "🟢"}

st.set_page_config(page_title="나의 할일", page_icon="✅", layout="centered")

st.markdown("""
<style>
/* 공통 */
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

/* 제목 버튼 - 텍스트처럼 왼쪽 정렬 */
div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:nth-child(2) button[data-testid="baseButton-secondary"],
div[data-testid="stColumns"] > div[data-testid="stColumn"]:nth-child(2) button[data-testid="baseButton-secondary"] {
    display: flex !important;
    justify-content: flex-start !important;
    align-items: center !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: inherit !important;
    padding: 0.1rem 0.2rem !important;
    font-size: 1rem !important;
    font-weight: normal !important;
    width: 100% !important;
    cursor: pointer !important;
    min-height: unset !important;
}
div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:nth-child(2) button[data-testid="baseButton-secondary"] > div,
div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:nth-child(2) button[data-testid="baseButton-secondary"] p {
    text-align: left !important;
    width: 100% !important;
}
div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:nth-child(2) button[data-testid="baseButton-secondary"]:hover {
    background: transparent !important;
    color: #ff4b4b !important;
    text-decoration: underline !important;
}

/* 모바일 최적화 */
@media (max-width: 640px) {
    h1 { font-size: 1.4rem !important; }
    h2 { font-size: 1.1rem !important; }
    .stButton > button {
        min-height: 2.6rem;
        font-size: 0.85rem;
        padding: 0.25rem 0.4rem;
    }
    .stTextInput input, .stSelectbox select {
        font-size: 1rem;
        min-height: 2.6rem;
    }
    .stCheckbox > label { font-size: 1rem; }
    .stDateInput input { min-height: 2.6rem; }
    .stRadio label { font-size: 0.9rem; }
}
</style>
""", unsafe_allow_html=True)

st.title("✅ 나의 할일 프로그램")

# --- 할일 추가 ---
with st.form("add_form", clear_on_submit=True):
    st.subheader("새 할일 추가")
    col1, col2 = st.columns([3, 1])
    with col1:
        new_title = st.text_input("할일 내용", placeholder="예) 보고서 작성")
    with col2:
        new_priority = st.selectbox("우선순위", ["높음", "보통", "낮음"], index=1)
    new_due = st.date_input("마감일 (선택)", value=None)
    submitted = st.form_submit_button("추가", use_container_width=True, type="primary")

if submitted:
    if new_title.strip():
        due_str = new_due.strftime("%Y-%m-%d") if new_due else ""
        tm.add(new_title, new_priority, due_str)
        st.success("추가되었습니다!")
        st.rerun()
    else:
        st.warning("내용을 입력하세요.")

st.divider()

# --- 필터 ---
col_f1, col_f2 = st.columns([2, 1])
with col_f1:
    filter_status = st.radio(
        "보기",
        ["전체", "미완료", "완료"],
        horizontal=True,
        label_visibility="collapsed",
    )
with col_f2:
    if st.button("완료 항목 삭제", type="primary"):
        removed = tm.delete_done()
        st.toast(f"완료된 {removed}개 항목을 삭제했습니다.")
        st.rerun()

# --- 할일 목록 ---
todos = tm.get_all()

if filter_status == "미완료":
    todos = [t for t in todos if not t["done"]]
elif filter_status == "완료":
    todos = [t for t in todos if t["done"]]

priority_order = {"높음": 0, "보통": 1, "낮음": 2}
todos_sorted = sorted(todos, key=lambda t: (t["done"], priority_order.get(t["priority"], 1)))

if not todos_sorted:
    st.info("할일이 없습니다. 위에서 추가해보세요!")
else:
    total = len(tm.get_all())
    done_count = sum(1 for t in tm.get_all() if t["done"])
    st.caption(f"전체 {total}개 · 완료 {done_count}개 · 미완료 {total - done_count}개")
    if total > 0:
        st.progress(done_count / total)

    if "editing_id" not in st.session_state:
        st.session_state.editing_id = None

    for todo in todos_sorted:
        emoji = PRIORITY_EMOJI.get(todo["priority"], "🟡")
        due_text = f"  · 마감 {todo['due_date']}" if todo.get("due_date") else ""
        label = f"~~{todo['title']}~~" if todo["done"] else todo["title"]

        if st.session_state.editing_id == todo["id"]:
            with st.form(key=f"edit_form_{todo['id']}"):
                st.markdown("**편집 중**")
                e_col1, e_col2 = st.columns([3, 1])
                with e_col1:
                    e_title = st.text_input("할일 내용", value=todo["title"])
                with e_col2:
                    priorities = ["높음", "보통", "낮음"]
                    e_priority = st.selectbox(
                        "우선순위",
                        priorities,
                        index=priorities.index(todo["priority"]) if todo["priority"] in priorities else 1,
                    )
                default_due = date.fromisoformat(todo["due_date"]) if todo.get("due_date") else None
                e_due = st.date_input("마감일 (선택)", value=default_due)
                b_save, b_cancel = st.columns(2)
                with b_save:
                    saved = st.form_submit_button("저장", use_container_width=True, type="primary")
                with b_cancel:
                    cancelled = st.form_submit_button("취소", use_container_width=True)
            if saved:
                due_str = e_due.strftime("%Y-%m-%d") if e_due else ""
                tm.update(todo["id"], e_title, e_priority, due_str)
                st.session_state.editing_id = None
                st.rerun()
            if cancelled:
                st.session_state.editing_id = None
                st.rerun()
        else:
            col_check, col_label, col_del = st.columns([0.5, 9, 1])
            with col_check:
                checked = st.checkbox(
                    "", value=todo["done"], key=f"chk_{todo['id']}", label_visibility="collapsed"
                )
                if checked != todo["done"]:
                    tm.toggle_done(todo["id"])
                    st.rerun()
            with col_label:
                if st.button(f"{emoji} {label}{due_text}", key=f"title_{todo['id']}", use_container_width=True):
                    st.session_state.editing_id = todo["id"]
                    st.rerun()
            with col_del:
                if st.button("🗑️", key=f"del_{todo['id']}", use_container_width=True):
                    tm.delete(todo["id"])
                    st.rerun()

# Lessons — 교훈 & 안티패턴 모음

> 반복하지 말아야 할 실수, 검증된 패턴을 기록합니다.
> 새 교훈 발견 시: 여기에 기록 → CLAUDE.md 금지사항에 규칙 추가.

---

## L-01: (예시) CSV 인코딩 문제

**세션**: S001 | **심각도**: Medium

한글이 포함된 CSV를 `pd.read_csv()`로 읽을 때 `UnicodeDecodeError` 발생.

**해법**: `encoding='utf-8-sig'` 또는 `encoding='cp949'` 명시.

**규칙 추가**: CLAUDE.md에 "CSV 읽을 때 encoding 명시" 추가.

---

## L-02: (예시) Streamlit 세션 상태 초기화 문제

**세션**: S001 | **심각도**: High

`st.file_uploader`로 파일을 올린 후 다른 위젯을 조작하면 파일이 사라짐.

**해법**: `st.session_state`에 데이터를 저장해야 함.

**규칙 추가**: CLAUDE.md에 "Streamlit에서 데이터는 반드시 session_state 사용" 추가.

---

## (새 교훈 발생 시 여기에 추가)

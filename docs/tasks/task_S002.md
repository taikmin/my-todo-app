# Task S002 — 편집 기능 추가 + 계획 파일 정리

**날짜**: 2026-07-23
**목표**: 할일 편집 기능 구현, 프로젝트 파일 실제 코드 기준으로 정리
**상태**: 완료 ✅

## 작업 목록
- [x] 프로젝트 현황 파악 (기존 코드·데이터 리뷰)
- [x] `src/todo_manager.py`: `update()` 함수 추가
- [x] `app.py`: 편집 버튼 + 인라인 폼 UI 추가
- [x] plan.md v2.0 재작성 (할일 앱 기준)
- [x] task.md 업데이트
- [x] progress.md 업데이트
- [x] SESSION_HISTORY.md 업데이트 (S002 추가)
- [x] docs/tasks/task_S002.md 생성

## 메모
- 편집 폼은 `st.form` + `session_state.editing_id` 조합으로 구현
- 한 번에 하나의 항목만 편집 가능 (다른 편집 버튼 클릭 시 자동 전환됨)

# Progress — 현재 상황

**최종 업데이트**: 2026-07-23 (Session S002)

---

## 전체 진행률

| Phase | 상태 | 비고 |
|-------|------|------|
| Phase 1: 뼈대 | ✅ 완료 | Gate 통과 |
| Phase 2: 핵심 기능 | ✅ 완료 | Gate 통과 |
| Phase 3: 고급 기능 | ⬜ 대기 | |
| Phase 4: 마무리 | ⬜ 대기 | |

---

## 최근 세션 (S002) — 2026-07-23

### 완료
- 프로젝트 재가동 확인 (기존 코드 리뷰)
- 할일 편집 기능 구현
  - `src/todo_manager.py`: `update()` 함수 추가
  - `app.py`: 인라인 편집 폼 UI 추가 (제목·우선순위·마감일 수정 가능)
  - `session_state.editing_id`로 하나씩만 편집 가능하게 제어

### 현재 상태
- 실제 데이터 존재 (`data/todos.json` — 2개 항목)
- CRUD 완전 구현: 추가·조회·완료체크·편집·삭제
- Phase 2 기능 모두 완료 (Gate 통과 가능)

### 다음 할 일
- pytest 테스트 작성 (Phase 4 선행 가능)
- 다중 그래프/필터링 등 고급 기능 (Phase 3) — 현 프로젝트가 할일 앱이므로 재논의 필요
- 계획 파일을 실제 프로젝트(할일 앱)에 맞게 정리

### 이슈/결정
- plan.md/task.md가 CSV 시각화 앱 기준으로 작성돼 있어 실제 코드(할일 앱)와 불일치
  → S002에서 plan.md를 실제 프로젝트 기준으로 수정함

---

## 이전 세션 (S001) — 2026-XX-XX

### 완료
- 프로젝트 구조 생성 (src/, tests/, data/)
- CSV 업로드 + 데이터 미리보기 구현 (초기 방향)
- Phase 1 Gate 통과 ✅
- `app.py`, `src/todo_manager.py` 기본 구현

### 이슈
- Streamlit session_state 이해 필요 → lessons.md L-02

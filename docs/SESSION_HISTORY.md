# Session History — 세션 기록 (아카이브)

> 각 세션의 상세 기록을 시간순으로 저장합니다 (append-only).
> - `progress.md` = **현재** 스냅샷 (최근 2~3 세션만 상세)
> - `SESSION_HISTORY.md` = **전체** 이력 아카이브 (영구 보존)
> - `docs/tasks/task_S{N}.md` = 세션별 task 파일 (영구 보존)
>
> **운영 규칙**:
> - 새 세션 시작 시: progress.md에서 오래된 세션을 여기로 이동
> - progress.md에는 최근 2~3 세션만 남기고, 나머지는 여기에 아카이브
> - task 파일은 `docs/tasks/task_S{N}.md`로 영구 보존 (삭제 금지)

---

## Index

| 세션 | 날짜 | 주요 작업 |
|------|------|----------|
| S001 | 2026-XX-XX | Phase 1 완료, 기본 CRUD 구현 시작 |
| S002 | 2026-07-23 | 프로젝트 재가동, 편집 기능 추가, 계획 파일 정리 |

---

## Session S001 (2026-XX-XX)

**목표**: Phase 1~2 구현 시작
**모델**: Sonnet

### 완료
- 프로젝트 구조 생성 (src/, tests/, data/)
- CLAUDE.md, plan.md, task.md 작성
- `app.py` 기본 UI 구현 (추가·조회·체크·삭제·진행률 바)
- `src/todo_manager.py` 데이터 레이어 구현 (JSON 저장)
- Phase 1 Gate 통과 ✅

### 이슈
- Streamlit session_state 이해 필요 → lessons.md L-02 기록

### 다음 세션
- 편집 기능 추가, 테스트 작성

---

## Session S002 (2026-07-23)

**목표**: 편집 기능 추가 + 프로젝트 파일 실제 코드 기준으로 정리
**모델**: claude-sonnet-4-6

### 완료
- 프로젝트 현황 파악 (기존 코드 리뷰)
- **할일 편집 기능 구현**
  - `src/todo_manager.py`: `update(todo_id, title, priority, due_date)` 함수 추가
  - `app.py`: 인라인 편집 폼 UI 추가 (편집 버튼 → 폼 펼침 → 저장/취소)
  - `session_state.editing_id`로 동시 편집 1개로 제한
- **계획 파일 정리**
  - plan.md v2.0: CSV 시각화 → 할일 앱으로 재정의, Phase 3 재작성
  - task.md: 실제 완료 항목 반영, Phase 3/4 재정의
  - progress.md: 현재 상태 업데이트
  - SESSION_HISTORY.md: S002 기록 추가

### 현재 상태
- CRUD 완전 구현 (추가·편집·완료체크·삭제)
- 실 데이터 존재 (`data/todos.json` 2개 항목)
- Phase 2 Gate 완료 ✅

### 다음 세션
- pytest 테스트 작성 (`src/todo_manager.py` 단위 테스트)
- Phase 3 고급 기능 중 우선순위 선택

---

## (다음 세션은 여기에 append)

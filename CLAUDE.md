# My Project — Claude Code 규칙

> 이 파일은 Claude가 세션 시작 시 자동으로 읽는 "업무 매뉴얼"입니다.
> 프로젝트를 진행하면서 규칙과 교훈을 여기에 추가하세요.

## 프로젝트 개요
- **프로젝트명**: (여기에 프로젝트 이름)
- **목표**: (한 줄 설명)
- **기술 스택**: Python 3.11, Streamlit, pytest
- **구조**: `src/`에 소스, `tests/`에 테스트

## 핵심 규칙

### 워크플로우 (반드시 준수)
1. **Plan 먼저** — 코드 구현 전에 plan.md 작성/확인
2. **Task 체크** — task.md의 체크리스트를 하나씩 완료
3. **테스트 실행** — 코드 수정 후 반드시 pytest 실행
4. **통과하면 커밋** — 테스트 통과 후에만 git commit

### /clear 전 필수 (절대 규칙)
- `/clear` 전에 반드시 아래 3개 파일을 업데이트:
  1. `progress.md` — 현재 진행 상황 스냅샷
  2. `plan.md` — 계획 변경사항 반영
  3. `task.md` — 완료 항목 체크 + 남은 항목 확인
- 이 규칙을 지키지 않으면 다음 세션에서 맥락이 소실됩니다

### 금지사항
- (예: solve_ivp 사용 금지 — RK4 직접 구현)
- (예: 외부 API 키를 코드에 하드코딩 금지)
- 테스트 없이 커밋 금지
- **Streamlit 커스텀 CSS에서 `data-testid`·`nth-child` 선택자 금지**
  → 버전 업그레이드 시 조용히 깨짐. `key=`를 주고 `[class*="st-key-{key}"]`로 지정할 것 (L-03)
- **텍스트가 들어가는 버튼에 고정 높이 금지** → `height: auto` + `white-space: normal` (L-04)

### 팀 모드 규칙
- 팀원 생성/삭제는 **반드시 사용자 허락 후에만**
- "일단 하고 보고" 금지 → "먼저 물어보고 허락받고 실행"

## 커밋 메시지 규칙
```
[TaskID] 핵심 변경사항

Co-Authored-By: Claude <noreply@anthropic.com>
```

## 참고 파일
| 파일 | 용도 |
|------|------|
| `plan.md` | 프로젝트 전체 계획 |
| `task.md` | 현재 작업 체크리스트 |
| `progress.md` | 진행 상황 스냅샷 |
| `lessons.md` | 실수에서 배운 교훈 |
| `decisions.md` | 설계 결정 기록 |
| `references/` | 외부 조사 자료 |

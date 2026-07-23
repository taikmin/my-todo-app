# Decisions — 설계 결정 기록 (ADR-lite)

> 왜 이런 선택을 했는지 기록합니다.
> 나중에 "왜 이렇게 했지?" 하고 돌아볼 때 유용합니다.

---

## DEC-01: 그래프 라이브러리 — Plotly 선택

**날짜**: 2026-XX-XX | **세션**: S001

### Context
- Streamlit 앱에서 그래프를 표시해야 함
- 사용자가 마우스로 줌/팬/호버 가능해야 함

### Decision
- **Plotly** 선택

### Alternatives Considered
- A) Matplotlib — 정적 이미지, 인터랙티브 불가 → 기각
- B) Altair — Streamlit 지원 좋으나 대용량 데이터에 느림 → 대안 유지
- C) Plotly — 인터랙티브 + Streamlit 네이티브 → **채택**

---

## DEC-02: 데이터 저장 — JSON 선택

**날짜**: 2026-XX-XX | **세션**: S001

### Context
- TODO 앱에서 할 일 데이터를 영구 저장해야 함
- SQLite vs JSON vs CSV 비교

### Decision
- **JSON** 선택 (단순 구조, 외부 의존성 없음)

### Alternatives Considered
- A) SQLite — 과도 (이 규모에선 불필요)
- B) CSV — 구조적 데이터 표현 어려움
- C) JSON — 간단, Python dict와 직접 매핑 → **채택**

---

## (새 결정 시 여기에 추가)

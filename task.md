# Task — Session S002

**날짜**: 2026-07-23
**목표**: 편집 기능 추가 + 프로젝트 파일 정리
**상태**: 완료

---

## Phase 1: 프로젝트 뼈대
- [x] 폴더 구조 생성 (src/, tests/, data/)
- [x] requirements.txt 작성
- [x] 기본 Streamlit 앱 뼈대
- [x] **GATE**: streamlit run app.py 정상 표시 ✅

## Phase 2: 핵심 기능
- [x] 할일 추가 (제목·우선순위·마감일)
- [x] 할일 목록 조회 (필터·정렬·진행률 바)
- [x] 완료 체크/해제
- [x] 할일 삭제 (개별·완료 일괄)
- [x] **할일 편집** (S002 추가) ← 이번 세션 완료
- [x] **GATE**: CRUD 전체 동작 확인 ✅

## Phase 3: 고급 기능
- [ ] 카테고리/태그 분류
- [ ] 검색 기능
- [ ] 마감일 임박 알림 표시
- [ ] 데이터 내보내기 (CSV/JSON)
- [ ] **GATE**: 위 기능 중 2개 이상 동작 확인

## Phase 4: 마무리
- [ ] 테스트 작성 (pytest — todo_manager.py 단위 테스트)
- [ ] 에러 핸들링 (빈 제목, 잘못된 날짜 등)
- [ ] README.md 작성
- [ ] **GATE**: pytest 전체 통과

---

## 메모
- plan.md Phase 3는 실제 프로젝트(할일 앱) 방향으로 재작성함
- 다음 세션 우선순위: pytest 테스트 작성 → Phase 4 Gate

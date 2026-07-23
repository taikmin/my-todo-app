# Task — Session S003

**날짜**: 2026-07-23
**목표**: Supabase 연동 + 모바일 배포 + UI 개선
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
- [x] 할일 편집 (S002 추가)
- [x] **GATE**: CRUD 전체 동작 확인 ✅

## Phase 3: 배포 및 모바일 (S003 신규)
- [x] Supabase DB 연동 (JSON → Cloud DB)
- [x] 기존 데이터 마이그레이션 (migrate.py)
- [x] Streamlit Cloud 배포
- [x] 모바일 반응형 CSS 추가
- [x] 편집 버튼 제거 → 제목 클릭으로 수정
- [x] 편집·삭제 버튼 같은 행에 배치
- [ ] 제목 버튼 왼쪽 정렬 (CSS 미해결 — 다음 세션)

## Phase 4: 마무리
- [ ] 테스트 작성 (pytest — todo_manager.py 단위 테스트)
- [ ] 에러 핸들링 (빈 제목, 잘못된 날짜 등)
- [ ] README.md 작성
- [ ] **GATE**: pytest 전체 통과

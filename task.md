# Task — Session S004

**날짜**: 2026-07-31
**목표**: 모바일에서 긴 제목 편집 불가 버그 수정
**상태**: 완료 (배포 반영은 미완)

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
- [x] 제목 버튼 왼쪽 정렬 (S004 해결 — testid 변경이 원인이었음)

## Phase 3.5: 모바일 버그 수정 (S004)
- [x] 긴 제목이 2줄 넘어갈 때 편집 진입 불가 버그 수정
- [x] 제목 버튼 CSS 선택자를 key 기반(`st-key-title_`)으로 교체
- [x] 체크박스·삭제 버튼 세로 중앙 정렬
- [x] **GATE**: 폰에서 긴 제목 표시·편집 진입 확인 ✅
- [ ] Streamlit Cloud 배포 반영 (git push) — 다음 세션

## Phase 4: 마무리
- [ ] 테스트 작성 (pytest — todo_manager.py 단위 테스트)
- [ ] 에러 핸들링 (빈 제목, 잘못된 날짜 등)
- [ ] README.md 작성
- [ ] run.bat의 Python 경로 문제 수정
- [ ] plan.md / task.md의 Phase 3 정의 불일치 정리
- [ ] **GATE**: pytest 전체 통과

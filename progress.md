# Progress — 현재 상황

**최종 업데이트**: 2026-07-23 (Session S003)

---

## 전체 진행률

| Phase | 상태 | 비고 |
|-------|------|------|
| Phase 1: 뼈대 | ✅ 완료 | Gate 통과 |
| Phase 2: 핵심 기능 | ✅ 완료 | Gate 통과 |
| Phase 3: 배포·모바일 | ✅ 대부분 완료 | 제목 왼쪽 정렬만 미해결 |
| Phase 4: 마무리 | ⬜ 대기 | |

---

## 최근 세션 (S003) — 2026-07-23

### 완료
- **Supabase 연동**: todo_manager.py를 JSON 파일 → Supabase Cloud DB로 교체
- **데이터 마이그레이션**: migrate.py로 기존 5개 항목 Supabase로 이전
- **Streamlit Cloud 배포**: https://my-todo-app-elrsqe6nwm3jvnct8kxhqg.streamlit.app/
- **모바일 반응형 CSS**: 버튼 터치 크기, 폰트 크기 최적화
- **UI 개선**:
  - 편집 버튼(✏️) 제거 → 제목 클릭으로 수정 모드 진입
  - 삭제 버튼(🗑️)만 오른쪽에 표시
  - Android 홈 화면에 앱으로 추가 가능

### 미해결
- 제목 버튼 왼쪽 정렬 문제 (CSS 선택자가 Streamlit 내부 구조와 불일치 가능성)

### 현재 상태
- PC·폰 모두 동일한 URL로 접속 가능
- Supabase DB에 데이터 저장 (앱 재시작해도 유지)
- Android Chrome에서 홈 화면 추가 시 앱처럼 실행

### 다음 할 일
1. 제목 버튼 왼쪽 정렬 CSS 해결 (F12 Inspector로 실제 HTML 구조 확인 필요)
2. Phase 4: pytest 테스트 작성
3. 에러 핸들링

---

## 인프라 정보
| 항목 | 값 |
|------|-----|
| 앱 URL | https://my-todo-app-elrsqe6nwm3jvnct8kxhqg.streamlit.app/ |
| GitHub | https://github.com/taikmin/my-todo-app |
| Supabase URL | https://hcjzaxbgmzbqzyelhzwl.supabase.co |
| Supabase 키 위치 | .streamlit/secrets.toml (로컬), Streamlit Cloud Secrets (배포) |

---

## 이전 세션 (S002) — 2026-07-23

### 완료
- 할일 편집 기능 구현 (update() 함수 + 인라인 편집 폼)
- plan.md를 실제 프로젝트 기준으로 재정의

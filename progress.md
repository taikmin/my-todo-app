# Progress — 현재 상황

**최종 업데이트**: 2026-07-31 (Session S004)

---

## 전체 진행률

| Phase | 상태 | 비고 |
|-------|------|------|
| Phase 1: 뼈대 | ✅ 완료 | Gate 통과 |
| Phase 2: 핵심 기능 | ✅ 완료 | Gate 통과 |
| Phase 3: 배포·모바일 | ✅ 완료 | 제목 정렬·모바일 줄바꿈 해결 (S004) |
| Phase 4: 마무리 | ⬜ 대기 | 테스트·에러 핸들링·README |

---

## 최근 세션 (S004) — 2026-07-31

### 완료
- **모바일 긴 제목 편집 불가 버그 수정** (app.py CSS)
  - 근본 원인 1: 선택자가 `button[data-testid="baseButton-secondary"]`였는데
    Streamlit 1.39부터 testid가 `stBaseButton-secondary`로 변경 → **CSS가 전혀 적용되지 않고 있었음**
    (S003의 "제목 왼쪽 정렬 미해결"도 동일 원인)
  - 근본 원인 2: 모바일 `.stButton > button { min-height: 2.6rem }` + 버튼 기본 한 줄 처리로
    제목 2번째 줄이 잘려 탭 영역 소실. PC는 폭이 넓어 증상이 안 보였음
  - 해법: 선택자를 `[class*="st-key-title_"]`로 교체 (key 기반, 버전 변화에 강함)
    + `white-space: normal`, `height: auto`, `overflow-wrap: anywhere`
    + `st.columns(..., vertical_alignment="center")`로 다중 행 정렬
- 빈 라벨 경고 제거 (`st.checkbox("")` → `"완료"` + collapsed)
- **로컬 실행 환경 확인**: Python 3.12.10 (PATH 미등록), 의존성 설치 완료

### 검증
- 폰(같은 Wi-Fi, http://<로컬IP>:8501)에서 긴 제목 2줄 표시 + 탭 편집 진입 정상 확인
- 서버 HTTP 200, Traceback 0건

### 다음 할 일
1. Streamlit Cloud에 배포 반영 (git push) — **아직 배포본에는 미반영**
2. Phase 4: pytest 테스트 작성 (todo_manager.py), 에러 핸들링, README.md
3. plan.md와 task.md의 Phase 3 정의 불일치 정리 (아래 참고)

### 알려진 이슈
- `run.bat`이 `streamlit`을 PATH에서 찾는데, 이 PC는 `python`이 Microsoft Store 스텁에 가려져 실패.
  실제 경로: `C:\Users\TMLEE\AppData\Local\Programs\Python\Python312\python.exe -m streamlit run app.py`
- plan.md의 Phase 3 = "고급 기능(카테고리·검색·내보내기)" vs task.md의 Phase 3 = "배포·모바일" — 정의가 다름

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

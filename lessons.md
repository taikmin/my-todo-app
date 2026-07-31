# Lessons — 교훈 & 안티패턴 모음

> 반복하지 말아야 할 실수, 검증된 패턴을 기록합니다.
> 새 교훈 발견 시: 여기에 기록 → CLAUDE.md 금지사항에 규칙 추가.

---

## L-01: (예시) CSV 인코딩 문제

**세션**: S001 | **심각도**: Medium

한글이 포함된 CSV를 `pd.read_csv()`로 읽을 때 `UnicodeDecodeError` 발생.

**해법**: `encoding='utf-8-sig'` 또는 `encoding='cp949'` 명시.

**규칙 추가**: CLAUDE.md에 "CSV 읽을 때 encoding 명시" 추가.

---

## L-02: (예시) Streamlit 세션 상태 초기화 문제

**세션**: S001 | **심각도**: High

`st.file_uploader`로 파일을 올린 후 다른 위젯을 조작하면 파일이 사라짐.

**해법**: `st.session_state`에 데이터를 저장해야 함.

**규칙 추가**: CLAUDE.md에 "Streamlit에서 데이터는 반드시 session_state 사용" 추가.

---

## L-03: Streamlit 커스텀 CSS — data-testid는 버전마다 바뀐다

**세션**: S003→S004 | **심각도**: High

제목 버튼 왼쪽 정렬 CSS를 S003에서 작성했으나 전혀 먹지 않았고, 한 세션을 통째로 날렸다.
원인은 선택자 `button[data-testid="baseButton-secondary"]` — Streamlit 1.39부터 testid가
`stBaseButton-secondary`로 바뀌어서 규칙 전체가 조용히 무시되고 있었다.
CSS는 선택자가 안 맞아도 **에러를 내지 않기 때문에** "적용됐는데 우선순위 문제"로 착각하기 쉽다.

**해법**:
- `key=`를 준 위젯은 `st-key-{key}` 클래스가 붙는다 (1.39+). 이걸 쓸 것:
  `[class*="st-key-title_"] button { ... }`
- `nth-child`나 `data-testid` 추측 금지 — DOM 구조/속성명은 버전 업그레이드 시 깨진다
- CSS가 안 먹으면 `!important`를 더 붙이기 전에 **선택자가 실제로 매칭되는지부터** 확인
  (F12 → Elements → 해당 요소의 Styles 패널에 규칙이 보이는지)

**규칙 추가**: CLAUDE.md 금지사항에 "Streamlit CSS에서 data-testid/nth-child 선택자 금지, key 기반 사용" 추가.

---

## L-04: 모바일 전용 버그는 "고정 높이 + 한 줄 가정"에서 나온다

**세션**: S004 | **심각도**: Medium

PC에서는 멀쩡한데 폰에서만 긴 제목의 편집 진입이 안 됐다.
`min-height: 2.6rem` 고정 + 버튼 라벨 기본 한 줄 처리 탓에, 좁은 화면에서 2번째 줄이
잘려 나가며 탭 영역까지 사라진 것. PC는 폭이 넓어 제목이 한 줄에 들어가니 증상이 안 보였다.

**해법**: 텍스트가 들어가는 버튼에는 `height: auto` + `white-space: normal` + `overflow-wrap: anywhere`.
`min-height`는 터치 크기 확보용으로만 쓰고, 최대 높이를 막지 말 것.

**교훈**: 반응형 CSS는 폰 실기기(또는 F12 디바이스 모드)에서 **긴 텍스트로** 확인해야 한다.
짧은 샘플 데이터로는 절대 안 잡힌다.

---

## (새 교훈 발생 시 여기에 추가)

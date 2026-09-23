# 더 메이커 공통 디자인 — "학습지" 테마

파이보 랩 · Sense Lab · Teach Lab · Edge Lab · Factory Lab 이
**한 제품처럼 보이게** 하는 규격입니다. 이 저장소가 **유일한 원본**이에요.

| 파일 | 무엇 |
|---|---|
| [`themaker-ui.css`](./themaker-ui.css) | 디자인 킷 본체. 이 한 파일만 복사해 쓰면 됩니다 |
| [`preview.html`](./preview.html) | 컴포넌트 실물. 서버로 띄워 확인합니다 |
| `assets/fonts/` | Pretendard (셀프호스팅). 서비스에도 같은 것이 들어갑니다 |

```bash
python3 -m http.server 8080      # 그리고 http://localhost:8080/preview.html
```

## 새 서비스에서 쓰기

1. `themaker-ui.css` 를 `css/themaker-ui.css` 로 복사합니다. **복사본은 고치지 않습니다.**
2. `assets/fonts/` 를 그대로 복사합니다.
3. 서비스 전용 스타일만 `css/app.css` 에 따로 얹습니다.

```html
<link rel="stylesheet" href="assets/fonts/pretendard.css">
<link rel="stylesheet" href="css/themaker-ui.css">
<link rel="stylesheet" href="css/app.css">
```

CI 에 복사본이 어긋났는지 보는 검사를 넣습니다. 태그로 고정해 두면
이 저장소가 바뀌어도 서비스 CI 가 갑자기 깨지지 않아요.

```yaml
- name: 디자인 킷 복사본이 원본과 같은가
  run: |
    curl -sSfL -o /tmp/kit.css \
      https://raw.githubusercontent.com/themakerrobot/themaker-ui/v1.0.0/themaker-ui.css
    diff -u /tmp/kit.css css/themaker-ui.css
```

킷을 새 버전으로 올릴 때는 그 태그 번호를 바꾸고 `css/themaker-ui.css` 를 다시 복사합니다.

## 컨셉

**초등 교실의 활동지(학습지).** 미색 종이 바탕 + 옅은 점무늬, 갈색 괘선,
남색 펜으로 쓴 답, 빨간 펜의 채점. 헤더는 활동지 머리표(이름 칸)처럼
갈색 외곽선 상자이고, 서비스명은 명조체입니다.

## 색 (토큰만 사용 — 새 색 금지)

| 토큰 | 값 | 쓰임 |
|---|---|---|
| `--paper` / `--bg` | `#FBF7EF` | 전체 배경 (점무늬 포함) |
| `--panel` | `#FFFFFF` | 패널·카드 |
| `--panel2` | `#FBFAF5` | 패널 안 옅은 면 |
| `--line` / `--line-soft` | `#9A8F7D` / `#DCD5C6` | 테두리 / 구분선 |
| `--line-d` | `#4A3F2E` | 헤더 외곽선 |
| `--ink` `--ink2` `--ink3` | `#2A2620` `#4A423A` `#6B6255` | 본문 / 보조 / 힌트 |
| `--acc` (`--pen-blue`) | `#1F5F7A` | 주 색: 주 버튼, 선택, 활성 탭 |
| `--acc-ink` | `#12455C` | 주 색의 진한 글자·호버 |
| `--acc-soft` | `#E6EEF6` | 선택된 면 |
| `--ok` / `--ok-soft` | `#2E7D4F` / `#EEF5EF` | 성공·통과 |
| `--warn` (`--pen-red`) | `#B4451C` | 경고·지우기 호버 |

## 글꼴

- 본문: **Pretendard** (셀프호스팅, `--sans`)
- 서비스명(헤더 h1): **Gowun Batang 계열** (`--serif`) — 없으면 명조 폴백
- 숫자는 `.num` (tabular-nums)
- 새 폰트 도입 금지

## 컴포넌트 (클래스 → 쓰임)

- **헤더**: `header > h1(로고+서비스명) + .navlink(탭, .on=현재) + .badge + .hbtn + #langToggle`
- **단계 표시**: `.steps > .stp(.on/.done) + .stpline` — "1 만들기 → 2 모으기 …"
- **본문**: `.mk-main > .pan-side + .pan-wide + .pan-out` (좁음/넓음/좁음 3단)
- **패널**: `.pan > .ph(제목) + .pb(내용)` / 구획 나누기 `.sec2 > .st`
- **버튼** `.db`: 기본(외곽선) / `.go`(주 동작, 남색 채움) / `.on`(토글 눌림) /
  `.warn`(강한 경고 채움) / `.danger`(조용한 지우기 — 호버 때만 경고색)
- **헤더 아이콘 버튼** `.hbtn`: 도움말·전체화면처럼 글자 없는 32px 버튼
- **입력**: `.inp` (텍스트·셀렉트 공용), 슬라이더는 기본 `input[type=range]`
- **카드**: `.cls`·`.mradio` (`.on`=선택) — 종류·모델 고르기
- **표**: `.mk-table`, 얇은 목록 줄 `.saved`, 파일 놓기 `.dropzone`
- **진행률**: `.prg > .lb + .track > .fill`
- **확률 막대**: `.bar(.top=1등만 강조) > .bl + .bt > .bf` — 1등만 색을 준다
- **큰 답**: `.answer` (`.sure`=확신 / `.idk`=안내·모름)
- **순서도**: `.seq-node(시작/성공) + .seq-arrow + .seq-step(.cur/.done)`
- **토스트**: `.toast(.on)` — 2초 뒤 사라지는 알림

## 문구 규칙 (초등 눈높이)

- 해요체 존댓말. 한 문장 20자 이내, 한 화면에 지시 하나
- 부정문보다 긍정문 ("누르지 마세요" → "다 모은 뒤에 눌러요")
- 에러도 아이 말로 ("카메라가 안 보여요. 연결을 확인해 주세요")
- 결과가 나빠도 나무라지 않기 ("아직 헷갈려 해요. 예시를 더 모아 볼까요?")
- 용어는 쉬운 말: 종류(클래스) · 예시(샘플) · 배우기(학습) · 맞힌 비율(정확도) ·
  헷갈린 표(혼동 행렬) · 확신 정도(임계값) · 모르겠어요(임계값 미달) · 안 보여요(미검출)

## 금지

- 그라디언트 남발, 이모지 장식, 알약형 상태 배지 남발
- 새 색상 팔레트·새 폰트 도입
- 절대경로(`/...`)·계정명 하드코딩 — 전부 상대경로
- 복사본(`css/themaker-ui.css`)을 서비스에서 직접 고치기 — 여기를 고치고 다시 복사합니다

## 반응형

- 1100px 이하: 3단 패널이 세로로 쌓임
- 700px 이하: 글자 한 단계 확대, 입력칸 16px(iOS 확대 방지), 헤더 가로 스크롤

## 킷을 고칠 때

1. `themaker-ui.css` 를 고치고 `preview.html` 로 눈으로 확인합니다.
2. `CHANGELOG.md` 에 적고 태그를 올립니다 (`v1.1.0`).
3. 쓰는 서비스마다 `css/themaker-ui.css` 를 다시 복사하고 CI 의 태그 번호를 바꿉니다.
   화면이 바뀌는 변경이면 서비스 쪽에서 전후 화면을 비교하고 올립니다.

토큰 값이나 컴포넌트 모양이 바뀌면 **MINOR**, 오타·주석은 **PATCH**,
클래스 이름을 바꾸거나 없애서 서비스가 깨지면 **MAJOR** 입니다.

## 쓰는 곳

- [teach-lab](https://github.com/themakerrobot/teach-lab)
- [sense-lab](https://github.com/themakerrobot/sense-lab)
- pibo-lab · edge-lab · factory-lab (아직 옮기지 않음)

## 라이선스

MIT. Pretendard 는 SIL Open Font License 1.1 (`assets/fonts/pretendard.css` 머리말 참고).

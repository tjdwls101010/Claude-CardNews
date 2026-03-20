---
name: card-news
description: 주제나 내용을 받아 디자인적으로 세련되고 정보 전달에 최적화된 카드뉴스 이미지를 생성하는 스킬. HTML로 디자인하고 PNG로 변환하며, Nano Banana API로 맞춤 일러스트를 생성한다. 카드뉴스, 인포그래픽, SNS 콘텐츠, 정보 요약 카드, 카드 디자인, 인스타 카드, 슬라이드 디자인 등을 요청할 때 반드시 이 스킬을 사용할 것.
---

# Card News Generator

사용자가 제시한 주제/내용을 바탕으로 디자인적으로 훌륭하면서 정보 전달에 최적화된 카드뉴스 시리즈(5~10장)를 생성한다.

## 기술 스택

- **디자인**: HTML (단일 파일, inline CSS/SVG) + Paperlogy 폰트 (9 웨이트)
- **일러스트**: Nano Banana API (gemini-3.1-flash-image-preview)
- **배경 제거**: rembg (선택적)
- **PNG 변환**: Playwright
- **카드 크기**: 1080x1350px (4:5, 인스타그램 세로)

스크립트 경로: 이 스킬 파일 기준 `scripts/` 디렉토리
폰트 경로: 이 스킬 파일 기준 `assets/fonts/` 디렉토리

## 워크플로우

**각 Phase에서 AskUserQuestion으로 사용자와 적극 소통한다.**

### Phase 1: 콘텐츠 분석

1. 사용자의 주제/내용에서 **핵심 메시지 3개** 추출
2. 전문 용어를 중학생이 이해할 수 있는 수준으로 평이화
3. 카드 시리즈 구조 기획 (몇 장, 각 장의 역할)
   - 1장: 커버 (주제 + 임팩트 비주얼)
   - 2~N-1장: 본문 카드 (핵심 내용)
   - N장: 엔딩 (인용/비전 문구로 마무리 — "감사합니다" 금지)
4. 제목은 **"주제"가 아닌 "결론"**으로 작성 (Tesla Rule)
   - X: "온도와 습도의 영향"
   - O: "가축 생장을 위해 온도 25도, 습도 60% 유지가 필수적"

-> **AskUserQuestion**: 카드 구성안 (장수, 각 장의 주제/역할) 제시하고 사용자 확인/수정

### Phase 2: 디자인 기획

1. **색상 팔레트** 결정 (3색 제한)
   - primary (브랜드/주제에서 추출) + accent + neutral
   - 80% 중립톤 + 20% 강조색 원칙
   - CSS 변수로 잠금: `--primary`, `--accent`, `--neutral`, `--text`, `--bg`

2. **전체 톤/무드** 방향 결정

3. **레이아웃 패턴** — 콘텐츠 의미 구조에 맞게 선택:
   - 타임라인/인과관계 -> 좌우(LR) 레이아웃
   - 서사/결론-이유 -> 상하(TB) 레이아웃
   - 제목-이미지-설명 -> Z형 레이아웃

4. 각 카드별 **일러스트 배치와 이미지 비율** 결정:
   - 카드 전체 배경 -> 4:5
   - 상단/하단 배너 -> 16:9 또는 3:2
   - 사이드 배치 -> 2:3 또는 3:4
   - 아이콘/심볼 -> 1:1

-> **AskUserQuestion**: 색상 팔레트, 디자인 톤 선택지 제시 (예: "다크+시안" vs "밝은+파스텔" vs "미니멀 모노톤")

### Phase 3: 일러스트 생성 (Nano Banana)

`references/image-prompt-guide.md`를 참조하여 프롬프트를 작성한다. 프롬프트는 반드시 영문, 서술형으로.

#### Step 3-1: 스타일 확립 (첫 번째 카드)

1. **2~3가지 스타일 변형** 프롬프트를 작성하여 **배치 모드로 병렬 생성**
   ```bash
   source scripts/.venv/bin/activate
   # batch.json 작성 후 병렬 실행 (동시에 여러 이미지 생성)
   python scripts/generate_image.py --batch batch.json
   ```
   `batch.json` 예시:
   ```json
   [
     {"prompt": "A 3D clay style icon of ...", "output": "card1_v1.png", "aspect_ratio": "1:1"},
     {"prompt": "A flat design icon of ...", "output": "card1_v2.png", "aspect_ratio": "1:1"},
     {"prompt": "An isometric scene of ...", "output": "card1_v3.png", "aspect_ratio": "1:1"}
   ]
   ```
   단일 이미지만 필요한 경우:
   ```bash
   python scripts/generate_image.py --prompt "..." --aspect-ratio "1:1" --output card1_v1.png
   ```
2. 생성된 이미지들을 **Read로 직접 확인**하여 비교
3. -> **AskUserQuestion**: 어떤 스타일이 좋은지 사용자 선택
4. 선택된 이미지가 80% 이상 만족스러우면 **이미지 편집 모드**로 미세 조정:
   ```bash
   python scripts/generate_image.py --prompt "Change the background to navy blue" --input card1_v1.png --output card1_final.png
   ```
5. 최종 확정된 이미지가 시리즈의 **스타일 레퍼런스**가 됨

#### Step 3-2: 나머지 카드 일러스트 (스타일 일관성 유지)

이전 카드의 확정 이미지를 **레퍼런스로 함께 제공**. 여러 카드 일러스트도 **배치 모드로 병렬 생성**:
```bash
# 나머지 카드 일러스트를 한 번에 생성
python scripts/generate_image.py --batch remaining_cards.json
```
`remaining_cards.json` 예시:
```json
[
  {"prompt": "..., same visual style as reference", "refs": ["card1_final.png"], "output": "card2_illust.png", "aspect_ratio": "1:1"},
  {"prompt": "..., same visual style as reference", "refs": ["card1_final.png"], "output": "card3_illust.png", "aspect_ratio": "1:1"},
  {"prompt": "..., same visual style as reference", "refs": ["card1_final.png"], "output": "card4_illust.png", "aspect_ratio": "16:9"}
]
```
단일 이미지:
```bash
python scripts/generate_image.py \
  --prompt "A 3D clay style icon of a growing plant, same visual style as reference" \
  --refs card1_final.png \
  --aspect-ratio "1:1" \
  --output card2_illust.png
```

#### Step 3-3: 배경 처리 (매우 중요)

생성된 이미지를 Read로 확인 후 배경 제거 여부를 판단한다. **다크 배경 카드에서 흰 배경 이미지를 그대로 사용하면 "붙여넣은" 느낌이 나므로, 대부분의 경우 배경 제거가 필요하다.**

판단 기준:
- 카드 배경이 어둡고 이미지 배경이 밝음 -> **반드시 rembg로 배경 제거**
- 카드 배경이 밝고 이미지 배경도 밝음 -> 제거 불필요
- 이미지가 카드 전체 배경으로 사용됨 -> 제거 불필요
- 이미지가 텍스트 위에 부유해야 함 -> **반드시 rembg로 배경 제거**

```bash
source scripts/.venv/bin/activate
# 단일 파일
rembg i input.png output.png

# 여러 이미지를 한 번에 처리 (디렉토리 모드)
rembg p ./images_raw/ ./images/
```

배경 제거 후 이미지를 카드에 자연스럽게 통합하는 CSS 기법:
- **White Glow** (어두운 배경): `filter: drop-shadow(0 0 30px rgba(255,255,255,0.2))`
- **Soft Shadow** (밝은 배경): `filter: drop-shadow(0 8px 20px rgba(0,0,0,0.3))`
- **배경과 블렌딩**: 이미지 아래에 `radial-gradient`로 은은한 광원 효과

### Phase 4: HTML 생성 + 미리보기

`references/css-patterns.md`에서 기본 템플릿과 패턴을 참조한다.

1. **카드당 1 HTML 파일** 생성 (1080x1350px)
2. 일러스트는 **별도 이미지 파일**로 저장하고 HTML에서 경로 참조 (`<img src="...">`)
3. 장식 요소는 inline SVG + CSS

**디자인 품질 체크리스트 (각 카드 생성 시 반드시 확인):**
- [ ] 이미지 배경이 카드 배경과 자연스럽게 통합되는가? (흰 배경 잔류 없는지)
- [ ] gradient mask 또는 glassmorphism이 텍스트 가독성을 확보하는가?
- [ ] gray dimming이 비핵심 텍스트에 적용되었는가?
- [ ] 코너 앵커 (페이지번호, 로고 등)가 배치되었는가?
- [ ] 여백이 균형 잡혀 있는가? (과도한 빈 공간 없는지)
- [ ] 핵심 키워드가 `<span>`으로 강조되었는가?
- [ ] 이미지에 white glow 또는 drop-shadow가 적용되었는가?

4. **첫 1~2장을 먼저 생성**하여 브라우저에서 열어 확인:
   ```bash
   open card_01.html
   ```
5. -> **AskUserQuestion**: 미리보기 결과에 대한 피드백 (수정 사항, 만족 여부)
6. 피드백 반영 후 나머지 카드 생성

### Phase 5: 최종 변환

```bash
source scripts/.venv/bin/activate
python scripts/html_to_png.py ./output/
```

-> **AskUserQuestion**: 최종 결과 만족 여부, 개별 카드 수정 요청

---

## HTML 생성 규칙

### 기본 구조

- 외부 URL 참조 금지 (CDN, 웹폰트 등 인터넷 의존 금지)
- 일러스트는 **별도 이미지 파일로 저장하고 상대경로/절대경로로 참조** (`<img src="./images/card1_illust.png">`)
  - base64 embed는 파일 크기를 불필요하게 키우므로 사용하지 않는다
  - Playwright가 로컬 파일 경로를 해석하므로 PNG 변환에 문제 없음
- `@font-face`로 `assets/fonts/` 내 Paperlogy TTF를 **절대경로** 참조
- 고정 뷰포트: `<div style="width:1080px; height:1350px; overflow:hidden; position:relative;">`
- `word-break: keep-all` (한국어 줄바꿈)
- CSS Grid/Flexbox 기반 레이아웃

### Paperlogy 폰트 사용 가이드

한 카드에 **최대 3개 웨이트**만 사용한다. 웨이트 간 대비를 크게 준다 (400+500 금지, 400+800 권장).

| 역할 | 웨이트 | font-weight | 용도 |
|------|--------|-------------|------|
| 메인 제목 | ExtraBold/Black | 800~900 | 카드의 핵심 메시지 |
| 서브 제목 | Bold/SemiBold | 600~700 | 섹션 구분 |
| 본문 | Regular/Medium | 400~500 | 설명 텍스트 |
| 보조/캡션 | Light/ExtraLight | 200~300 | 출처, 페이지 번호 |
| 장식 | Thin | 100 | 배경 워터마크 (opacity 5%) |

추가 규칙:
- 제목: `letter-spacing: -0.03em ~ -0.05em` (글자 뭉침으로 임팩트)
- 시리즈 전체에서 동일 웨이트 조합 유지

---

## 필수 디자인 원칙 (페이퍼로지 기반)

이것이 디자인의 주요 기준이다. `references/design-principles.md`에 상세 내용이 있으며, 아래는 반드시 지켜야 할 핵심 원칙이다.

### 타이포그래피
- **Gray Dimming으로 강조**: 강조할 텍스트에 색을 입히는 대신, 비핵심 텍스트를 `color: #888`로 약화시킨다
- 빨간색 강조 금지 (경고/위험 인상)
- 한 문장 내에서도 핵심 키워드만 `<span>`으로 감싸 weight/color 차별화

### 색상
- **슬라이드당 3색 제한** (primary + accent + neutral)
- 80% 중립톤 + 20% 강조색
- 브랜드/주제에서 dominant color 추출하여 팔레트 구성
- CSS 변수로 잠금 후 전체 일관 적용

### 배경 + 가독성
- 이미지 위 텍스트: **gradient mask** 필수 (`linear-gradient`를 텍스트 방향에 맞춰 배치)
- 복잡한 배경: **glassmorphism** (`backdrop-filter: blur(10px); background: rgba(255,255,255,0.15)`)
- 배경은 "무대"지 "주연"이 아니다 — 텍스트 밀도가 높으면 배경 역할 축소

### 그림자 / 깊이
- Soft shadow: `box-shadow: 0 4px 15px rgba(0,0,0,0.4)` (opacity 40-50%, blur 넓게)
- 어두운 배경에서 White Glow: `filter: drop-shadow(0 0 20px rgba(255,255,255,0.3))`
- Z-index 레이어링: 배경(z:1) -> 텍스트(z:2) -> 컷아웃 이미지(z:3)

### 레이아웃
- **Big-Medium-Small** 크기 위계 (60-30-10%)
- 코너 앵커: 네 모서리에 작은 요소 (페이지번호, 로고, 장식) 배치 -> 안정감
- 빈 공간에 장식 SVG나 **배경 타이포그래피 워터마크** (opacity 5%, font-size 15rem) 배치

### 콘텐츠
- 제목 = 결론 (주제 금지)
- 핵심 키워드 3개 추출하여 시각적으로 분리 배치
- 시리즈 시작과 끝을 동일 비주얼/메시지로 마무리 (Bookending)
- "감사합니다" 대신 인용/비전 문구로 끝내기 (Cinematic Ending)

### 아이콘 / 에셋
- 시리즈 내 동일 스타일 (전부 flat 또는 전부 3D clay — 혼합 금지)
- stroke width, fill style, corner radius 통일

### Dimming 효과
- 리스트에서 특정 항목 강조 시: 활성 항목만 `opacity: 1`, 나머지 `opacity: 0.3`

---

## 상세 레퍼런스

더 세부적인 기법과 코드 예제는 아래 파일을 참조:

- `references/design-principles.md` — 페이퍼로지 디자인 원칙 전체 (가장 중요한 레퍼런스)
- `references/css-patterns.md` — 바로 사용 가능한 CSS 코드 스니펫
- `references/image-prompt-guide.md` — Nano Banana 이미지 프롬프트 작성 가이드

# Card News Design Principles (페이퍼로지 기반)

> 이 문서는 HTML/CSS 기반 카드뉴스(1080x1350px, 4:5 비율, 인스타그램 최적화) 생성 시 적용해야 할 핵심 디자인 원칙을 정리한 것이다.
> 페이퍼로지 디자인 리뷰 영상 및 저서에서 도출한 형식지(명시적 규칙)와 암묵지(디자이너의 직관)를 CSS 구현 코드와 함께 수록한다.

---

## 1. Typography Engine (타이포그래피 엔진)

### 1-1. 폰트 굵기(Weight) 규칙 -- Paperlogy 100~900

**원칙:** `font-weight: bold` 사용을 금지한다. 반드시 Paperlogy 가변 폰트의 수치 기반 굵기(100~900)를 명시적으로 지정한다.

**굵기별 용도:**
- `100~200` (ExtraLight/Light): 장식용 배경 워터마크 텍스트, 출처 표기
- `300~400` (Light/Regular): 본문 텍스트, 부연 설명
- `500~600` (Medium/SemiBold): 소제목, 강조가 필요한 본문
- `700~800` (Bold/ExtraBold): 메인 타이틀, 핵심 키워드
- `900` (Black): 표지 제목, 임팩트가 필요한 단어

```css
/* 기본 타이포그래피 시스템 */
:root {
  --font-primary: 'Paperlogy', sans-serif;
  --weight-light: 300;
  --weight-regular: 400;
  --weight-medium: 500;
  --weight-bold: 700;
  --weight-extrabold: 800;
  --weight-black: 900;
}

h1 {
  font-family: var(--font-primary);
  font-weight: var(--weight-extrabold); /* 800 명시 */
}

.body-text {
  font-family: var(--font-primary);
  font-weight: var(--weight-regular); /* 400 명시 */
}

/* 절대 사용하지 않는 패턴 */
/* font-weight: bold;  -- 금지 */
/* <b> 태그 직접 사용 -- 금지 */
```

**사용 시점:** 모든 텍스트 요소에 반드시 적용
**금지 사항:** `font-weight: bold` 키워드 사용, `<b>` 태그 남용

---

### 1-2. 자간(Letter-spacing) 규칙

**원칙:** 타이틀 텍스트는 자간을 좁혀서 시각적 '덩어리감(Chunk)'을 만든다. 본문은 기본값을 유지하거나 약간 넓힌다.

```css
/* 제목: 자간을 좁혀서 덩어리감 부여 */
h1, h2, .title {
  letter-spacing: -0.03em;
}

/* 큰 숫자/임팩트 텍스트: 더 좁게 */
.impact-number {
  letter-spacing: -0.05em;
}

/* 본문: 기본값 또는 약간 넓게 */
.body-text {
  letter-spacing: 0;
}

/* 소형 캡션/라벨: 넓혀서 가독성 확보 */
.caption, .label {
  letter-spacing: 0.05em;
  font-size: 0.75rem;
  text-transform: uppercase;
}
```

**사용 시점:** 제목(h1, h2)에는 반드시 음수 자간 적용
**금지 사항:** 본문 텍스트에 과도한 음수 자간 적용 (가독성 저하)

---

### 1-3. 그레이 디밍 기법 (Gray Dimming -- 역발상 강조)

**원칙:** 강조할 텍스트에 빨간색을 입히는 대신, 비핵심 텍스트를 회색으로 죽여서 핵심이 자연스럽게 부각되게 한다. 초보자는 강조에 '빨간색'을 쓰지만, 이는 경고/위험의 느낌을 준다. 프로는 강조할 부분은 그대로 두고 나머지를 회색으로 처리한다.

```css
/* 비핵심 텍스트 디밍 */
.dimmed {
  color: #999999;
}

/* 핵심 텍스트는 메인 컬러 유지 */
.highlighted {
  color: var(--text-primary); /* 흰색 또는 검은색 */
  font-weight: var(--weight-bold);
}

/* 실제 적용 예시 -- 한 문장 내 강조 */
/* HTML: <p class="dimmed">입에 <span class="highlighted">단 것</span>이 몸에도 <span class="highlighted">좋다</span></p> */
.dimmed .highlighted {
  color: var(--text-primary);
  font-weight: var(--weight-extrabold);
}
```

**사용 시점:** 한 문장이나 목록에서 특정 키워드만 강조해야 할 때
**금지 사항:** 강조를 위해 빨간색(`#FF0000` 계열)을 사용하는 것. 특별한 지시가 없으면 레드 계열은 강조색에서 완전히 배제한다.

---

### 1-4. 세리프(Serif) vs 산세리프(Sans-serif) 사용 기준

**원칙:** 전체 문서의 95%는 산세리프(Paperlogy)를 사용한다. 세리프나 손글씨 폰트는 다음 경우에만 포인트로 사용한다.

| 상황 | 폰트 유형 | 예시 |
|------|----------|------|
| 정보 전달, 데이터, 본문 | 산세리프 (Paperlogy) | 모든 기본 텍스트 |
| 감성적 질문, 인용구 | 세리프 또는 손글씨 | "콘텐츠 기획자란 무엇인가?" |
| 특정 브랜드 언급 | 해당 브랜드 폰트 | 배달의민족 -> 한나체 |
| 배경 워터마크 | 필기체(Cursive) 또는 극굵은 산세리프 | "Contents", "Introduction" |

```css
/* 감성적 텍스트 감지 시 폰트 변경 */
.emotional-text {
  font-family: 'Nanum Myeongjo', serif;
  font-style: italic;
  font-weight: var(--weight-light);
}

/* 인용구 */
.quote {
  font-family: 'Nanum Myeongjo', serif;
  font-weight: var(--weight-regular);
  font-size: 1.4rem;
  line-height: 1.8;
  border-left: 3px solid var(--color-accent);
  padding-left: 1.2rem;
}
```

**사용 시점:** 감성적 전환이 필요한 순간, 인용구, 질문형 문장
**금지 사항:** 세리프 폰트를 본문 전체에 적용, 한 카드에 3개 이상의 폰트 혼용

---

### 1-5. 배경 타이포그래피 워터마크 기법

**원칙:** 빈 공간이 허전할 때, 해당 페이지의 영문 키워드를 극도로 크고 극도로 투명하게 배경에 깐다. 이는 현대 웹 디자인(랜딩 페이지)에서 매우 자주 사용되는 기법이다.

```css
.bg-typography {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: var(--font-primary);
  font-weight: var(--weight-black); /* 900 */
  font-size: 12rem; /* 극도로 크게 */
  color: rgba(255, 255, 255, 0.05); /* 투명도 5% -- 은은하게 */
  z-index: 0; /* 모든 콘텐츠 뒤에 배치 */
  white-space: nowrap;
  pointer-events: none;
  user-select: none;
  letter-spacing: -0.03em;
  text-transform: uppercase;
}

/* 어두운 배경일 때 */
.dark-bg .bg-typography {
  color: rgba(255, 255, 255, 0.04);
}

/* 밝은 배경일 때 */
.light-bg .bg-typography {
  color: rgba(0, 0, 0, 0.03);
}
```

**사용 시점:** 표지, 목차, 챕터 간지(Divider) 슬라이드처럼 텍스트 밀도가 낮은 페이지
**금지 사항:** 투명도 10% 이상으로 설정 (배경이 아니라 전면 요소처럼 보임), 본문 텍스트와 겹쳐서 가독성을 해치는 배치

---

## 2. Color Pipeline (컬러 파이프라인)

### 2-1. 주제/브랜드에서 대표 컬러 추출

**원칙:** 브랜드 로고나 메인 이미지에서 지배적인 컬러(Dominant Color) 1개를 추출하고, 이를 전체 카드뉴스의 포인트 컬러로 사용한다. 주제가 명확한 경우(예: 스포티파이 -> 초록, 카카오 -> 노란색) 해당 브랜드 컬러를 직접 지정한다.

```css
/* 추출된 컬러를 CSS 변수로 고정 */
:root {
  --color-primary: #1DB954;   /* 브랜드/주제에서 추출한 메인 컬러 */
  --color-accent: #1ED760;    /* 메인 컬러의 밝은 변형 */
  --color-neutral: #191414;   /* 무채색 기반 배경 */
}

/* 모든 강조 요소는 이 변수만 참조 */
.highlight { color: var(--color-primary); }
.accent-bg { background-color: var(--color-accent); }
.card-bg { background-color: var(--color-neutral); }
```

**사용 시점:** 카드뉴스 생성 초기 단계에서 1회 결정, 이후 전체 카드에 일관 적용
**금지 사항:** 카드마다 다른 포인트 컬러를 사용하는 것

---

### 2-2. 3색 제한 규칙 (The Rule of 3 Colors)

**원칙:** 하나의 카드에 사용하는 색상은 절대 3가지를 초과하지 않는다. 메인 컬러(Primary) + 강조 컬러(Accent) + 무채색(Neutral)으로 구성한다.

```css
:root {
  /* 딱 3가지만 정의 -- 이 외의 컬러 추가 금지 */
  --color-primary: #2563EB;     /* 메인 포인트 컬러 (파란색 계열) */
  --color-accent: #60A5FA;      /* 보조 포인트 (메인의 밝은 변형) */
  --color-neutral-dark: #1F2937;  /* 어두운 무채색 */
  --color-neutral-mid: #6B7280;   /* 중간 무채색 */
  --color-neutral-light: #F3F4F6; /* 밝은 무채색 */

  /* 텍스트 컬러도 무채색 기반 */
  --text-primary: #FFFFFF;
  --text-secondary: #9CA3AF;
  --text-muted: #6B7280;
}
```

**사용 시점:** 모든 카드뉴스에 적용하는 절대 규칙
**금지 사항:** 4가지 이상의 유채색 사용, 무지개 같은 다색 배합

---

### 2-3. 80% 무채색 톤 원칙

**원칙:** 카드 전체 면적의 약 80%는 무채색(흑/백/회색)으로 채우고, 유채색은 20% 이내에서만 사용한다. 이렇게 해야 포인트 컬러가 실제로 '포인트'로 기능한다.

```css
/* 배경은 무채색 */
.card {
  width: 1080px;
  height: 1350px;
  background-color: #0F0F0F; /* 거의 검은색 */
  color: #FFFFFF;
}

/* 포인트 컬러는 작은 영역에만 */
.accent-bar {
  width: 60px;
  height: 4px;
  background-color: var(--color-primary);
  margin-bottom: 1rem;
}

.keyword {
  color: var(--color-primary);
  /* 전체 텍스트 중 핵심 단어 1~2개에만 적용 */
}
```

**사용 시점:** 항상
**금지 사항:** 배경 전체를 유채색으로 채우는 것 (챕터 간지 예외), 포인트 컬러를 본문 전체에 입히는 것

---

### 2-4. CSS 변수 잠금(Locking) 패턴

**원칙:** 첫 번째 카드에서 결정된 컬러 팔레트를 `:root`에 CSS 변수로 고정하고, 이후 모든 카드에서 이 변수만 참조하도록 강제한다. 하드코딩된 색상값 사용을 금지한다.

```css
/* :root에서 1회 정의 -- 전체 카드에 공유 */
:root {
  --color-primary: #2563EB;
  --color-accent: #60A5FA;
  --color-bg: #0F0F0F;
  --color-surface: #1A1A2E;
  --color-text: #FFFFFF;
  --color-text-dim: #888888;
  --color-border: rgba(255, 255, 255, 0.1);
}

/* 올바른 사용 */
.title { color: var(--color-text); }
.subtitle { color: var(--color-text-dim); }
.highlight { color: var(--color-primary); }

/* 금지되는 사용 */
/* .title { color: #FF5733; }  -- 하드코딩 금지 */
/* .box { background: pink; }  -- 변수 미참조 금지 */
```

**사용 시점:** 모든 카드뉴스의 모든 색상 지정에 적용
**금지 사항:** 인라인 스타일에 하드코딩된 색상, `:root` 변수를 무시한 직접 색상 지정

---

### 2-5. 배경 명도(Luminance) 기반 로고/텍스트 동적 반전

**원칙:** 배경이 어두우면 로고와 텍스트를 흰색으로, 배경이 밝으면 검은색으로 자동 변환한다. 스포티파이 사례처럼, 가독성이 브랜드 고유 컬러보다 우선한다.

```css
/* 어두운 배경일 때 -- 로고를 완전 흰색으로 */
.dark-bg .logo {
  filter: brightness(0) invert(1);
}

/* 밝은 배경일 때 -- 로고를 완전 검은색으로 */
.light-bg .logo {
  filter: brightness(0);
}

/* 텍스트 자동 반전 */
.dark-bg { color: #FFFFFF; }
.light-bg { color: #111111; }

/* 중간 톤 배경일 때 -- 텍스트에 그림자 추가로 가독성 확보 */
.mid-bg .text-overlay {
  color: #FFFFFF;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
}
```

**사용 시점:** 배경 이미지 위에 로고나 텍스트를 올릴 때 반드시 적용
**금지 사항:** 어두운 배경에 어두운 텍스트, 밝은 배경에 밝은 텍스트 (대비 부족)

---

## 3. Layout Decision Logic (레이아웃 의사결정 로직)

### 3-1. 콘텐츠 구조 -> 레이아웃 패턴 매핑

**원칙:** 텍스트의 의미적 구조(시간순, 서사, 위계)를 분석하여 최적의 레이아웃 패턴을 자동 선택한다. 사람은 화면을 Z형, 좌->우(LR), 위->아래(TB) 순으로 읽는다.

| 콘텐츠 구조 | 레이아웃 패턴 | CSS Grid 구현 |
|------------|-------------|--------------|
| 타임라인, 인과관계, Before/After | 좌우(LR) 배치 | `grid-template-columns: 1fr 1fr` |
| 서사(내러티브), 결론->이유->예시 | 상하(TB) 배치 | `grid-template-rows: auto 1fr auto` |
| 제목+이미지+설명, 위계가 뚜렷한 정보 | Z형 배치 | `grid-template-areas` 활용 |
| 비교, 대조 | 좌우 대칭 | `grid-template-columns: 1fr 1fr` + 중앙 구분선 |
| 나열, 목록 | 그리드 카드형 | `grid-template-columns: repeat(2, 1fr)` |

```css
/* Z형 레이아웃 (가장 범용적) */
.layout-z {
  display: grid;
  grid-template-areas:
    "title  title"
    "image  desc"
    "footer footer";
  grid-template-columns: 1.2fr 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 1.5rem;
  padding: 3rem;
}

/* 좌우(LR) 레이아웃 -- 타임라인/비교용 */
.layout-lr {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  padding: 3rem;
  align-items: center;
}

/* 상하(TB) 레이아웃 -- 서사/결론 우선용 */
.layout-tb {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 3rem;
  gap: 2rem;
}
```

**사용 시점:** 카드 구성 초기 단계에서 콘텐츠 분석 후 결정
**금지 사항:** 시간순 데이터를 상하로 배치, 결론 중심 콘텐츠를 좌우로 분할

---

### 3-2. Big-Medium-Small 사이징 (60-30-10% 규칙)

**원칙:** 한 화면의 모든 요소를 세 단계 크기로 강제 분류한다. '어중간한 크기'는 허용하지 않는다. 모든 것이 같은 크기면 눈이 피로하다.

- **Big (60%):** 시선을 끄는 메인 비주얼 (큰 이미지, 핵심 숫자, 메인 타이틀)
- **Medium (30%):** 전달할 핵심 텍스트 데이터 (소제목, 본문 요약)
- **Small (10%):** 메타 데이터 (페이지 번호, 출처, 로고, 날짜)

```css
/* Big: 메인 타이틀 */
.element-big {
  font-size: 3.5rem;
  font-weight: var(--weight-extrabold);
  line-height: 1.1;
  letter-spacing: -0.03em;
}

/* Medium: 본문/소제목 */
.element-medium {
  font-size: 1.25rem;
  font-weight: var(--weight-regular);
  line-height: 1.6;
}

/* Small: 메타 데이터 */
.element-small {
  font-size: 0.75rem;
  font-weight: var(--weight-light);
  color: var(--color-text-dim);
  letter-spacing: 0.05em;
}

/* 큰 숫자 임팩트 (Big 요소의 변형) */
.impact-number {
  font-size: 6rem;
  font-weight: var(--weight-black);
  letter-spacing: -0.05em;
  line-height: 1;
}
```

**사용 시점:** 모든 카드에 적용하는 절대 규칙
**금지 사항:** 모든 텍스트를 비슷한 크기로 배치, Big 요소 없이 Medium만으로 구성

---

### 3-3. 코너 앵커(Corner Anchors) -- 시각적 안정감

**원칙:** 카드의 네 귀퉁이에 작은 텍스트나 기호를 배치하면 시각적 경계선이 형성되어 레이아웃의 안정감이 급상승한다.

```css
.card {
  position: relative;
  width: 1080px;
  height: 1350px;
}

/* 좌측 상단: 브랜드/로고 */
.anchor-top-left {
  position: absolute;
  top: 2.5rem;
  left: 2.5rem;
  font-size: 0.8rem;
  font-weight: var(--weight-medium);
  color: var(--color-text-dim);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

/* 우측 상단: 카테고리/날짜 */
.anchor-top-right {
  position: absolute;
  top: 2.5rem;
  right: 2.5rem;
  font-size: 0.75rem;
  color: var(--color-text-dim);
}

/* 좌측 하단: 페이지 번호 */
.anchor-bottom-left {
  position: absolute;
  bottom: 2.5rem;
  left: 2.5rem;
  font-size: 0.75rem;
  color: var(--color-text-dim);
}

/* 우측 하단: 장식용 마크 또는 출처 */
.anchor-bottom-right {
  position: absolute;
  bottom: 2.5rem;
  right: 2.5rem;
  font-size: 0.75rem;
  color: var(--color-text-dim);
}

/* 페이지 번호 스타일링 -- 현재 번호만 강조 */
.page-number .current {
  color: var(--color-text);
  font-weight: var(--weight-bold);
}
.page-number .separator,
.page-number .total {
  color: var(--color-text-dim);
}
/* 예: <span class="current">03</span><span class="separator"> / </span><span class="total">08</span> */
```

**사용 시점:** 모든 카드에 적용 (최소 2개 코너에는 앵커 배치)
**금지 사항:** 앵커 요소가 너무 크거나 눈에 튀는 것 (Small 요소여야 함)

---

### 3-4. 4분면 시각적 무게 균형

**원칙:** 화면을 4분할 했을 때, 한쪽 덩어리만 비정상적으로 무겁고 나머지가 비어 있으면 불안정하게 보인다. 비어 있는 사분면에는 장식용 SVG 도형이나 배경 요소를 배치하여 무게를 맞춘다.

```css
/* 빈 공간을 채우는 장식 요소 */
.decorative-shape {
  position: absolute;
  opacity: 0.08;
  pointer-events: none;
  user-select: none;
}

/* 원형 장식 -- 빈 사분면에 배치 */
.deco-circle {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  border: 2px solid var(--color-primary);
  opacity: 0.1;
}

/* 선형 장식 */
.deco-line {
  width: 120px;
  height: 2px;
  background-color: var(--color-primary);
  opacity: 0.15;
}

/* 점 패턴 장식 */
.deco-dots {
  display: grid;
  grid-template-columns: repeat(3, 6px);
  gap: 8px;
}
.deco-dots span {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: var(--color-text-dim);
  opacity: 0.3;
}
```

**사용 시점:** 메인 콘텐츠 배치 후, 시각적으로 비어 보이는 영역이 있을 때
**금지 사항:** 장식 요소가 콘텐츠보다 눈에 띄는 것, 장식 요소 과다 사용

---

### 3-5. 그리드 파괴(Grid-Breaking) -- 의도적 오버플로우

**원칙:** 숫자나 장식 요소를 텍스트 박스 경계 밖으로 삐져나가게 배치하면 정적인 레이아웃에 역동성이 생긴다. 단, '의도적인 파괴'여야 하며, 실수로 삐져나간 것처럼 보이면 안 된다.

```css
/* 넘버링이 카드 경계를 돌파하는 레이아웃 */
.numbered-item {
  position: relative;
  padding-left: 4rem;
  margin-bottom: 2rem;
}

.numbered-item .number {
  position: absolute;
  left: -1.5rem; /* 컨테이너 밖으로 의도적 돌출 */
  top: 50%;
  transform: translateY(-50%);
  font-size: 5rem;
  font-weight: var(--weight-black);
  color: var(--color-primary);
  opacity: 0.15;
  line-height: 1;
}

/* 이미지가 카드 가장자리를 넘어가는 효과 */
.overflow-image {
  position: absolute;
  right: -2rem; /* 오른쪽으로 돌출 */
  bottom: 0;
  width: 60%;
  /* 카드에 overflow: hidden 적용하여 깔끔하게 잘림 */
}

.card {
  overflow: hidden; /* 돌출 요소를 카드 경계에서 깔끔하게 절단 */
}
```

**사용 시점:** 넘버링 리스트, 대형 장식 텍스트, 배경 이미지의 일부를 돌출시킬 때
**금지 사항:** 핵심 텍스트를 잘리게 하는 것, 모든 요소에 오버플로우를 적용하는 것 (포인트 1~2개만)

---

## 4. Background & Readability (배경 및 가독성)

### 4-1. 그라데이션 마스크 기법 (Gradient Mask)

**원칙:** 배경 이미지 위에 텍스트를 올릴 때, 텍스트 뒤에 배경 톤에서 투명으로 빠지는 그라데이션을 깔아 가독성을 확보한다. 동시에 배경 이미지의 시선 분산을 방지(역할 축소)하고, 이미지가 배경에 자연스럽게 녹아드는 효과를 준다.

```css
/* 기본 그라데이션 마스크 -- 하단 텍스트용 */
.gradient-mask-bottom::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60%;
  background: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.95) 0%,
    rgba(0, 0, 0, 0.7) 40%,
    rgba(0, 0, 0, 0) 100%
  );
  z-index: 1;
  pointer-events: none;
}

/* 좌측 텍스트용 (이미지가 우측에 있을 때) */
.gradient-mask-left::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 60%;
  background: linear-gradient(
    to right,
    rgba(0, 0, 0, 1) 0%,
    rgba(0, 0, 0, 0.6) 50%,
    rgba(0, 0, 0, 0) 100%
  );
  z-index: 1;
}

/* 전체 화면 오버레이 (이미지 위 텍스트 전체 보호) */
.gradient-mask-full::after {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1;
}

/* 텍스트는 반드시 마스크 위에 배치 */
.gradient-mask-bottom .content,
.gradient-mask-left .content,
.gradient-mask-full .content {
  position: relative;
  z-index: 2;
}
```

**사용 시점:** 배경 이미지 위에 텍스트를 올릴 때 반드시 적용. 그라데이션 방향은 텍스트 위치에 따라 동적으로 결정한다.
**금지 사항:** 그라데이션 없이 이미지 위에 텍스트를 직접 올리는 것

---

### 4-2. 글래스모피즘 (Glassmorphism)

**원칙:** 복잡한 배경(지도, 복잡한 사진 등) 위에 텍스트를 올릴 때, 반투명한 유리판 효과를 주어 배경의 맥락은 살리되 텍스트 가독성을 확보한다.

```css
.glass-panel {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  padding: 2rem;
}

/* 어두운 배경 위의 밝은 글래스 */
.glass-light {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
}

/* 밝은 배경 위의 어두운 글래스 */
.glass-dark {
  background: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
}
```

**사용 시점:** 복잡한 이미지 배경 위에 텍스트 블록을 올릴 때, 배경의 맥락(예: 지도, 도시 풍경)을 유지해야 할 때
**금지 사항:** 단색 배경에 글래스모피즘 적용 (의미 없음), blur 값이 너무 높아 배경이 완전히 안 보이는 것

---

### 4-3. 반투명 오버레이 (Semi-transparent Overlay)

**원칙:** 이미지 전체를 살리면서 텍스트 가독성이 필요할 때, 이미지 위에 단색 반투명 레이어를 깐다.

```css
/* 이미지 컨테이너 */
.image-overlay-container {
  position: relative;
  background-image: url('...');
  background-size: cover;
  background-position: center;
}

/* 반투명 오버레이 */
.image-overlay-container::before {
  content: '';
  position: absolute;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.55);
  z-index: 1;
}

/* 브랜드 컬러 오버레이 */
.brand-overlay::before {
  content: '';
  position: absolute;
  inset: 0;
  background-color: rgba(37, 99, 235, 0.75); /* 브랜드 컬러 + 투명도 */
  z-index: 1;
}

.image-overlay-container .content {
  position: relative;
  z-index: 2;
}
```

**사용 시점:** 풀블리드(full-bleed) 이미지 배경에 텍스트를 올릴 때
**금지 사항:** 오버레이 투명도가 너무 낮아(0.1 이하) 텍스트가 안 보이는 것

---

### 4-4. 배경 역할 축소 원칙

**원칙:** 배경(Background)은 '주연'이 아니라 '무대'다. 초보자는 화려한 이미지를 꽉 채워 넣고 싶어 하지만, 프로는 이미지가 텍스트를 방해할 것 같으면 과감하게 그라데이션으로 덮거나 여백으로 밀어낸다.

```css
/* 텍스트 밀도가 높을 때 -- 배경을 강하게 억제 */
.text-heavy .bg-image {
  opacity: 0.15;
  filter: blur(3px);
}

/* 텍스트 밀도가 낮을 때 -- 배경을 살림 */
.text-light .bg-image {
  opacity: 0.6;
  filter: none;
}

/* 은유적 배경 (맥락 전달용) */
.contextual-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  opacity: 0.1; /* 극도로 낮은 투명도 */
  z-index: 0;
}
```

**사용 시점:** 텍스트 양이 많은 정보 전달형 카드
**금지 사항:** 텍스트가 많은데 배경 이미지를 강하게 유지하는 것

---

### 4-5. 텍스트 밀도 증가 시 이미지 디밍/블러

**원칙:** 텍스트 영역의 면적이 넓어질수록 배경 이미지의 명도를 낮추거나 블러를 강화한다.

```css
/* 텍스트 밀도별 배경 처리 단계 */

/* 1단계: 텍스트 소량 (제목만) */
.density-low .bg-image {
  filter: brightness(0.7);
}

/* 2단계: 텍스트 중간 (제목 + 본문 2~3줄) */
.density-medium .bg-image {
  filter: brightness(0.4) blur(2px);
}

/* 3단계: 텍스트 다량 (본문 5줄 이상) */
.density-high .bg-image {
  filter: brightness(0.2) blur(5px);
}

/* 동적 필터 적용 패턴 */
.bg-image {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  z-index: 0;
  transition: filter 0.3s ease;
}
```

**사용 시점:** 배경 이미지 위에 텍스트를 올리는 모든 경우
**금지 사항:** 텍스트 양과 무관하게 배경을 동일한 밝기로 유지하는 것

---

## 5. Shadow & Depth (그림자 및 입체감)

### 5-1. 소프트 섀도우 규칙 (Soft Drop Shadow)

**원칙:** 그림자는 투명도를 높이고(40~50%) 블러를 넓혀서 은은하게 퍼지게 만든다. 진하고 딱딱한 그림자는 아마추어의 표식이다.

```css
/* 올바른 소프트 섀도우 */
.soft-shadow {
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
}

/* 텍스트 소프트 섀도우 */
.text-soft-shadow {
  text-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
}

/* 카드/패널 소프트 섀도우 */
.card-shadow {
  box-shadow:
    0 4px 6px rgba(0, 0, 0, 0.05),
    0 12px 24px rgba(0, 0, 0, 0.1);
}

/* 호버/강조 시 더 깊은 섀도우 */
.elevated-shadow {
  box-shadow:
    0 8px 16px rgba(0, 0, 0, 0.08),
    0 24px 48px rgba(0, 0, 0, 0.15);
}

/* -- 금지 패턴 -- */
/* box-shadow: 2px 2px 5px black;  -- 너무 진하고 딱딱함 */
/* text-shadow: 1px 1px 0 #000;    -- 90년대 웹 느낌 */
```

**사용 시점:** 카드, 패널, 이미지 프레임 등 떠 있는 느낌이 필요한 요소
**금지 사항:** 블러 없는 선명한 그림자, 투명도 0.8 이상의 진한 그림자, `black` 키워드 사용

---

### 5-2. 어두운 배경에서의 화이트 글로우 (White Glow)

**원칙:** 어두운 배경에 배경이 제거된(누끼) 인물/사물 PNG를 올릴 때, 검은 그림자 대신 흰색 그림자를 주면 후광(Glow) 효과가 나며 피사체가 고급스럽게 부각된다.

```css
/* 어두운 배경 위 PNG 이미지의 화이트 글로우 */
.white-glow {
  filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.25));
}

/* 더 강한 글로우 (히어로 이미지용) */
.white-glow-strong {
  filter: drop-shadow(0 0 40px rgba(255, 255, 255, 0.35));
}

/* 브랜드 컬러 글로우 */
.brand-glow {
  filter: drop-shadow(0 0 30px rgba(37, 99, 235, 0.4));
}

/* 복합 글로우 (흰색 + 브랜드 컬러) */
.dual-glow {
  filter:
    drop-shadow(0 0 15px rgba(255, 255, 255, 0.2))
    drop-shadow(0 0 40px rgba(37, 99, 235, 0.3));
}
```

**사용 시점:** 어두운(#000~#333) 배경에 투명 배경 PNG 이미지를 배치할 때
**금지 사항:** 밝은 배경에 화이트 글로우 적용 (안 보임), 글로우 투명도 0.6 이상 (번지는 느낌)

---

### 5-3. Z-index 레이어링 (배경 -> 텍스트 -> 누끼 이미지)

**원칙:** 인물/사물 이미지를 배치할 때, '배경 - 텍스트/로고 - 누끼 이미지'의 3단 샌드위치 구조를 사용하여 평면적인 카드에 3D 같은 입체감을 부여한다.

```css
.card {
  position: relative;
  overflow: hidden;
}

/* Layer 1: 배경 이미지 */
.layer-bg {
  position: absolute;
  inset: 0;
  z-index: 1;
  background-size: cover;
  background-position: center;
}

/* Layer 2: 그라데이션 오버레이 */
.layer-overlay {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.8) 0%,
    rgba(0, 0, 0, 0) 60%
  );
}

/* Layer 3: 텍스트/로고 (피사체 뒤에 위치) */
.layer-text {
  position: relative;
  z-index: 3;
}

/* Layer 4: 누끼(배경 제거) 이미지 (최상위) */
.layer-cutout {
  position: absolute;
  z-index: 4;
  /* 텍스트 위로 올라와 입체감 생성 */
}
```

**사용 시점:** 인물 사진이나 제품 이미지가 있는 표지/프로필 카드
**금지 사항:** 4개 이상의 레이어를 겹치는 것 (복잡해짐), 레이어 순서가 논리적이지 않은 것

---

### 5-4. 투명 PNG를 위한 Drop-shadow 필터

**원칙:** 투명 배경 PNG 이미지에는 `box-shadow`가 아닌 `filter: drop-shadow()`를 사용해야 이미지 실루엣에 맞는 그림자가 생긴다.

```css
/* box-shadow는 사각 박스 전체에 그림자 -- 투명 PNG에 부적합 */
/* .png-image { box-shadow: 0 4px 8px rgba(0,0,0,0.3); }  -- 금지 */

/* drop-shadow는 이미지 실루엣을 따라 그림자 -- 투명 PNG에 적합 */
.png-image {
  filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.3));
}

/* 어두운 배경에서는 밝은 drop-shadow */
.dark-bg .png-image {
  filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.25));
}

/* 밝은 배경에서는 어두운 drop-shadow */
.light-bg .png-image {
  filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.15));
}
```

**사용 시점:** 투명 배경이 있는 PNG/SVG 이미지에 그림자를 줄 때
**금지 사항:** 투명 PNG에 `box-shadow` 사용 (사각형 그림자가 생김)

---

## 6. Content Structuring (콘텐츠 구조화)

### 6-1. 테슬라 규칙 (Tesla Rule): 제목은 결론이다

**원칙:** 제목에 '주제'가 아니라 '결론'을 적는다. 청중이 머리를 써서 해석하게 만들지 않는다. 일론 머스크는 "10년간 일자리 창출 현황"이 아니라 "테슬라는 10년 동안 125,000개의 일자리를 창출했습니다"라고 쓴다.

**적용 방법:**
- 명사형 종결(~현황, ~분석, ~비교)을 절대 사용하지 않는다.
- 핵심 수치가 있으면 반드시 제목에 포함한다.
- 제목만 읽어도 해당 카드의 메시지를 완전히 이해할 수 있어야 한다.

| 나쁜 예 (주제형) | 좋은 예 (결론형) |
|----------------|----------------|
| 국내 전기차 시장 현황 | 국내 전기차 판매량, 전년 대비 42% 급증 |
| 소비자 선호도 분석 | MZ세대 10명 중 7명이 친환경 제품을 선택한다 |
| 매출 추이 | 3분기 매출 200억 돌파, 역대 최고 실적 달성 |

**사용 시점:** 모든 카드의 메인 타이틀(h1)에 적용
**금지 사항:** "~에 대하여", "~현황", "~분석", "~비교" 등의 명사형 종결 제목

---

### 6-2. 3 키워드 추출

**원칙:** 긴 서술형 문장은 핵심 명사형 키워드 3개로 압축한다. 서술어는 모두 제거한다. 3개의 독립된 텍스트 블록으로 분리하여 배치한다.

```css
/* 3 키워드 레이아웃 */
.keyword-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  text-align: center;
}

.keyword-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
}

.keyword-box .number {
  font-size: 2.5rem;
  font-weight: var(--weight-black);
  color: var(--color-primary);
  letter-spacing: -0.03em;
}

.keyword-box .label {
  font-size: 0.9rem;
  font-weight: var(--weight-medium);
  color: var(--color-text-dim);
}
```

**사용 시점:** 정보를 요약하거나 핵심 포인트를 전달할 때
**금지 사항:** 4개 이상의 키워드 나열 (인지 과부하), 서술형 문장을 그대로 박스에 넣는 것

---

### 6-3. 전문 용어의 중학생 수준 순화

**원칙:** 하수는 어려운 전문 용어를 남발하여 자신이 똑똑해 보이려 하지만, 고수(스포티파이)는 중학생도 알아들을 수 있는 쉬운 단어로 말한다. "전문 용어 남발은 프레젠테이션의 적이다."

**적용 방법:**
- 업계 전문 용어나 어려운 한자어를 발견하면 일상어로 변환한다.
- 약어(Abbreviation)를 처음 사용할 때는 반드시 풀어서 설명한다.
- 한 문장에 전문 용어는 최대 1개까지만 허용한다.

| 변환 전 | 변환 후 |
|--------|--------|
| ROI가 극대화됩니다 | 투자 대비 수익이 크게 늘어납니다 |
| KPI 달성률 향상 | 핵심 목표 달성률 향상 |
| 시너지를 창출한다 | 함께하면 더 큰 성과를 낸다 |

**사용 시점:** 모든 텍스트 전처리 단계에서 적용
**금지 사항:** 전문가 대상 카드뉴스에서 과도한 순화 (대상에 따라 조절)

---

### 6-4. 질문 -> 답변 페이지네이션 (Pagination for Impact)

**원칙:** 놀라운 수치나 반전 요소가 있다면, 한 장에 모두 담지 않는다. 첫 장에서 질문/호기심을 유발하고, 다음 장에서 답변/결과를 보여준다.

**구조:**
```
[카드 A] "3년 만에 몇 배 성장했을까?"
  -> 배경: 어둡고 미니멀, 큰 물음표 또는 호기심 유발 이미지

[카드 B] "6배 성장"
  -> 배경: 밝고 임팩트 있는 디자인, 거대한 숫자 + 상승 그래프
```

```css
/* 질문 카드 스타일 */
.question-card {
  background-color: var(--color-bg);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.question-card .question {
  font-size: 2.2rem;
  font-weight: var(--weight-bold);
  line-height: 1.4;
  color: var(--color-text);
}

/* 답변 카드 스타일 -- 임팩트 극대화 */
.answer-card {
  background-color: var(--color-primary);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.answer-card .answer-number {
  font-size: 8rem;
  font-weight: var(--weight-black);
  letter-spacing: -0.05em;
  color: #FFFFFF;
  line-height: 1;
}
```

**사용 시점:** 놀라운 수치, 반전 요소, Before/After 비교
**금지 사항:** 모든 정보를 질문-답변 형식으로 만드는 것 (남용하면 지루해짐), 질문이 3장 이상 연속되는 것

---

### 6-5. 감성적 간지(Emotional Divider) 배치

**원칙:** 딱딱한 데이터와 텍스트만 연속되면 독자가 지친다. 챕터가 바뀔 때마다 감성적인 이미지와 은유적 카피가 적힌 '간지(Divider)'를 삽입하여 뇌를 쉬게 해 준다.

```css
/* 간지(Divider) 슬라이드 */
.divider-card {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  overflow: hidden;
}

/* 꽉 찬 배경 이미지 */
.divider-card .bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  z-index: 0;
}

/* 어두운 오버레이 */
.divider-card .bg::after {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
}

/* 챕터 제목 */
.divider-card .chapter-title {
  position: relative;
  z-index: 2;
  font-size: 2.5rem;
  font-weight: var(--weight-extrabold);
  color: #FFFFFF;
  letter-spacing: -0.02em;
}

/* 감성적 서브 카피 */
.divider-card .sub-copy {
  position: relative;
  z-index: 2;
  font-size: 1rem;
  font-weight: var(--weight-light);
  color: rgba(255, 255, 255, 0.7);
  margin-top: 1rem;
  font-family: 'Nanum Myeongjo', serif; /* 감성적 서체 */
}
```

**사용 시점:** 대주제(H1 레벨)가 바뀔 때마다 반드시 삽입
**금지 사항:** 간지에 세부 정보나 데이터를 넣는 것 (순수 감성 전환용), 챕터 전환 시 배경색/텍스트색을 본문과 동일하게 유지하는 것

---

### 6-6. 수미상관 기법 (Bookending)

**원칙:** 첫 번째 카드(인트로)에 사용한 이미지/배경/분위기를 마지막 카드(아웃트로)에 동일하게 재사용하면, 콘텐츠가 한 편의 영화처럼 완결되는 느낌을 준다.

**구현 방법:**
- 인트로에 사용된 배경 이미지 URL을 변수로 저장한다.
- 아웃트로에서 동일한 이미지를 재사용한다.
- 아웃트로에는 감성적인 마무리 문장이나 CTA(Call to Action)를 배치한다.

```css
/* 인트로와 아웃트로가 동일한 CSS 변수 참조 */
:root {
  --hero-bg-image: url('...');
}

.intro-card,
.outro-card {
  background-image: var(--hero-bg-image);
  background-size: cover;
  background-position: center;
}
```

**사용 시점:** 5장 이상의 카드뉴스 시리즈에서 마무리를 할 때
**금지 사항:** 인트로/아웃트로 이미지가 완전히 다른 톤인 것

---

### 6-7. 시네마틱 엔딩 (Cinematic Ending)

**원칙:** "감사합니다", "Thank You", "Q&A"로 끝나는 것은 여운이 없다. 전체 콘텐츠의 맥락에서 가장 감동적이거나 비전이 담긴 한 문장, 또는 유명인의 명언으로 마무리한다.

| 나쁜 엔딩 | 좋은 엔딩 |
|----------|----------|
| 감사합니다 | "우리가 만드는 미래는 이미 시작되었습니다" |
| Thank You | 프로젝트의 핵심 비전을 담은 한 문장 |
| Q&A 시간입니다 | 맥락에 맞는 유명인의 명언 + 서명 |

```css
/* 시네마틱 엔딩 카드 */
.cinematic-ending {
  background-color: #000000;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 4rem;
}

.cinematic-ending .closing-quote {
  font-family: 'Nanum Myeongjo', serif;
  font-size: 1.8rem;
  font-weight: var(--weight-regular);
  color: #FFFFFF;
  line-height: 1.8;
  max-width: 80%;
}

.cinematic-ending .attribution {
  margin-top: 2rem;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.5);
  font-weight: var(--weight-light);
}
```

**사용 시점:** 카드뉴스의 마지막 장
**금지 사항:** "감사합니다" 한 줄만 덩그러니 쓰는 것, 뻔한 인사말로 마무리하는 것

---

## 7. Icon & Asset Consistency (아이콘 및 에셋 일관성)

### 7-1. 단일 아이콘 패밀리 규칙 (Single Icon Family)

**원칙:** 하나의 카드뉴스 시리즈에서 아이콘은 반드시 동일한 패밀리(Pack)에서만 가져온다. 서로 다른 스타일의 아이콘을 섞으면 난잡해진다.

**선택 기준:**
- 전체 카드뉴스의 톤에 맞는 아이콘 스타일을 첫 카드에서 결정한다.
- 이후 모든 카드에서 동일한 스타일만 사용한다.

| 스타일 | 특징 | 적합한 톤 |
|--------|------|----------|
| Line (선형) | 깔끔, 미니멀 | 비즈니스, 테크 |
| Filled (채움형) | 견고, 직관적 | 정보 전달, 교육 |
| Duotone (이중톤) | 세련, 모던 | 브랜딩, 마케팅 |

**사용 시점:** 첫 카드 디자인 시 결정, 전체 시리즈에 일관 적용
**금지 사항:** 1번 카드는 Line 아이콘, 2번 카드는 Filled 아이콘 사용

---

### 7-2. Stroke/Fill/Corner 일관성 -- CSS 변수 통제

**원칙:** 모든 아이콘과 도형 요소의 선 두께(stroke-width), 채우기 방식(fill/outline), 모서리 곡률(border-radius)을 CSS 변수로 통일한다.

```css
:root {
  /* 아이콘/에셋 스타일 변수 -- 첫 카드에서 1회 결정 */
  --icon-size: 48px;
  --icon-stroke-width: 1.5px;
  --icon-color: var(--color-primary);
  --icon-bg: rgba(37, 99, 235, 0.1);
  --icon-radius: 12px;

  /* 전체 도형 모서리 곡률 통일 */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-full: 9999px;
}

/* 아이콘 컨테이너 */
.icon-container {
  width: var(--icon-size);
  height: var(--icon-size);
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--icon-bg);
  border-radius: var(--icon-radius);
}

/* SVG 아이콘 스타일 강제 통일 */
.icon-container svg {
  width: 24px;
  height: 24px;
  stroke: var(--icon-color);
  stroke-width: var(--icon-stroke-width);
  fill: none; /* Line 스타일 강제 */
}

/* 모든 카드/패널의 모서리 곡률 통일 */
.panel { border-radius: var(--radius-md); }
.tag { border-radius: var(--radius-full); }
.image-frame { border-radius: var(--radius-lg); }
```

**사용 시점:** 아이콘, 도형, 카드 패널 등 모든 시각 요소에 적용
**금지 사항:** 요소마다 다른 border-radius 사용, SVG 아이콘의 stroke-width가 제각각인 것

---

### 7-3. 3D와 Flat 스타일 혼용 금지

**원칙:** 하나의 카드뉴스 시리즈 내에서 3D 렌더링 아이콘과 Flat(평면) 아이콘을 절대 섞지 않는다. 톤이 완전히 깨진다.

**결정 기준:**
- 비즈니스/정보 전달 -> Flat 또는 Line 스타일
- 캐주얼/감성 -> 3D Clay 또는 Illustrated 스타일
- 한 번 결정하면 시리즈 끝까지 유지

**사용 시점:** 첫 카드 디자인 시 결정, 전체 시리즈에 적용
**금지 사항:** 1번 카드에 3D 이모지 쓰고, 3번 카드에 Flat 아이콘 쓰는 것

---

### 7-4. 컬러 팔레트의 아이콘 적용

**원칙:** 아이콘의 색상도 반드시 2-1에서 정한 컬러 팔레트(--color-primary, --color-accent) 범위 내에서만 사용한다. 아이콘 원본 색상을 그대로 쓰지 않는다.

```css
/* 아이콘 색상을 브랜드 팔레트로 강제 오버라이드 */
.icon svg path {
  fill: var(--color-primary);
}

.icon svg {
  stroke: var(--color-primary);
}

/* 비활성 아이콘은 무채색 */
.icon-inactive svg path {
  fill: var(--color-text-dim);
}

/* CSS filter로 아이콘 색상 변환 (래스터 이미지 아이콘용) */
.icon-img {
  filter: brightness(0) saturate(100%);
  /* 이후 원하는 색상으로 재착색 */
}
```

**사용 시점:** 외부에서 가져온 모든 아이콘에 적용
**금지 사항:** 아이콘 원본의 다양한 색상을 그대로 유지하는 것 (팔레트 파괴)

---

## 8. Advanced Techniques (고급 기법)

### 8-1. 디밍 효과 (Dimming Effect)

**원칙:** 여러 항목 중 하나를 깊게 설명할 때, 설명하는 항목만 밝게 두고 나머지는 투명도를 낮춰(opacity 0.3) 시선을 강제 유도한다. 카드뉴스에서 여러 장에 걸쳐 하나씩 설명할 때 특히 효과적이다.

```css
/* 전체 항목 기본 상태 */
.item-list .item {
  opacity: 0.3;
  transition: opacity 0.3s ease;
}

/* 활성화된(현재 설명 중인) 항목 */
.item-list .item.active {
  opacity: 1;
  font-weight: var(--weight-bold);
}

/* 실전 예시: 5개 항목 중 3번째를 설명하는 카드 */
/*
  1. 항목 A  (opacity: 0.3)
  2. 항목 B  (opacity: 0.3)
  3. 항목 C  (opacity: 1, bold, color: primary)  <-- 현재 설명 중
  4. 항목 D  (opacity: 0.3)
  5. 항목 E  (opacity: 0.3)
*/

.item.active {
  opacity: 1;
  color: var(--color-primary);
  font-weight: var(--weight-bold);
  transform: scale(1.02);
}

.item:not(.active) {
  opacity: 0.3;
  color: var(--color-text-dim);
}
```

**사용 시점:** 목록에서 하나씩 순차적으로 설명하는 시리즈 카드, 비교 분석에서 특정 항목을 부각시킬 때
**금지 사항:** 디밍 대상이 없는데 불필요하게 적용, opacity 0.1 이하 (완전히 안 보임)

---

### 8-2. 디바이스 목업 프레이밍 (Device Mockup Framing)

**원칙:** 앱 화면, 웹사이트 캡처, 영상 등을 그냥 네모난 이미지로 올리면 촌스럽다. CSS로 구현된 디바이스 프레임(스마트폰, 브라우저 등) 안에 넣으면 순식간에 세련되어 보인다.

```css
/* 스마트폰 목업 프레임 (CSS 전용) */
.phone-mockup {
  position: relative;
  width: 280px;
  aspect-ratio: 9 / 19.5;
  background: #1a1a1a;
  border-radius: 36px;
  padding: 12px;
  box-shadow:
    0 0 0 2px #333,
    0 20px 60px rgba(0, 0, 0, 0.4);
}

.phone-mockup .screen {
  width: 100%;
  height: 100%;
  border-radius: 24px;
  overflow: hidden;
  background-size: cover;
  background-position: top center;
}

/* 노치 */
.phone-mockup::before {
  content: '';
  position: absolute;
  top: 12px;
  left: 50%;
  transform: translateX(-50%);
  width: 35%;
  height: 28px;
  background: #1a1a1a;
  border-radius: 0 0 16px 16px;
  z-index: 10;
}

/* 브라우저 창 목업 */
.browser-mockup {
  background: #2a2a2a;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.3);
}

.browser-mockup .toolbar {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 10px 14px;
  background: #3a3a3a;
}

.browser-mockup .toolbar .dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.browser-mockup .toolbar .dot:nth-child(1) { background: #ff5f57; }
.browser-mockup .toolbar .dot:nth-child(2) { background: #ffbd2e; }
.browser-mockup .toolbar .dot:nth-child(3) { background: #28ca41; }

.browser-mockup .viewport {
  width: 100%;
  aspect-ratio: 16 / 10;
  background-size: cover;
  background-position: top center;
}
```

**사용 시점:** 앱 화면, 웹사이트, SNS 게시물 등 디지털 콘텐츠를 보여줄 때
**금지 사항:** 모든 이미지를 목업에 넣는 것 (풍경 사진은 목업 불필요), 목업 크기가 카드의 80% 이상을 차지하는 것

---

### 8-3. 배경 타이포그래피 워터마크 (상세 구현)

**원칙:** 1-5에서 다룬 워터마크 기법의 심화 버전. 다양한 배치 패턴과 효과를 포함한다.

```css
/* 패턴 1: 중앙 워터마크 */
.watermark-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 12rem;
  font-weight: var(--weight-black);
  color: rgba(255, 255, 255, 0.04);
  white-space: nowrap;
  pointer-events: none;
  z-index: 0;
}

/* 패턴 2: 회전 워터마크 */
.watermark-rotated {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-15deg);
  font-size: 10rem;
  font-weight: var(--weight-black);
  color: rgba(255, 255, 255, 0.03);
  white-space: nowrap;
  pointer-events: none;
  z-index: 0;
}

/* 패턴 3: 하단 고정 워터마크 */
.watermark-bottom {
  position: absolute;
  bottom: -2rem;
  right: -1rem;
  font-size: 14rem;
  font-weight: var(--weight-black);
  color: rgba(255, 255, 255, 0.03);
  line-height: 1;
  pointer-events: none;
  z-index: 0;
}

/* 패턴 4: 반복 패턴 워터마크 */
.watermark-pattern {
  position: absolute;
  inset: 0;
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  justify-content: center;
  gap: 2rem;
  opacity: 0.02;
  pointer-events: none;
  z-index: 0;
  transform: rotate(-10deg);
  overflow: hidden;
}
```

**사용 시점:** 표지, 간지, 엔딩 등 텍스트 밀도가 낮은 카드
**금지 사항:** 본문이 많은 카드에 워터마크 사용 (가독성 방해), 투명도 8% 이상 (주의 분산)

---

### 8-4. 매쉬 그라데이션 (Mesh Gradient) 배경

**원칙:** 단색 배경은 심심하고 사진 배경은 텍스트를 방해할 때, 여러 색상이 오로라처럼 부드럽게 섞인 매쉬 그라데이션을 사용한다.

```css
/* 기본 매쉬 그라데이션 -- radial-gradient 중첩 */
.mesh-gradient {
  background-color: #0a0a0a;
  background-image:
    radial-gradient(
      ellipse at 20% 50%,
      rgba(37, 99, 235, 0.3) 0%,
      transparent 50%
    ),
    radial-gradient(
      ellipse at 80% 20%,
      rgba(139, 92, 246, 0.25) 0%,
      transparent 50%
    ),
    radial-gradient(
      ellipse at 60% 80%,
      rgba(6, 182, 212, 0.2) 0%,
      transparent 50%
    );
}

/* 따뜻한 톤 매쉬 그라데이션 */
.mesh-gradient-warm {
  background-color: #0a0a0a;
  background-image:
    radial-gradient(
      ellipse at 30% 40%,
      rgba(234, 88, 12, 0.25) 0%,
      transparent 50%
    ),
    radial-gradient(
      ellipse at 70% 70%,
      rgba(168, 85, 247, 0.2) 0%,
      transparent 50%
    ),
    radial-gradient(
      ellipse at 50% 10%,
      rgba(239, 68, 68, 0.15) 0%,
      transparent 50%
    );
}

/* 미니멀 매쉬 (단색 기반) */
.mesh-gradient-subtle {
  background-color: var(--color-bg);
  background-image:
    radial-gradient(
      ellipse at 30% 50%,
      rgba(37, 99, 235, 0.08) 0%,
      transparent 60%
    );
}
```

**사용 시점:** 표지, 간지 등 분위기 있는 배경이 필요하지만 이미지를 쓸 수 없을 때
**금지 사항:** 3개 이상의 유채색을 매쉬에 사용 (난잡해짐), 데이터 중심 카드에 화려한 매쉬 적용 (주의 분산)

---

## 부록: 카드뉴스 기본 프레임 (1080x1350px)

```css
/* 카드뉴스 기본 컨테이너 */
.card-news {
  width: 1080px;
  height: 1350px;
  position: relative;
  overflow: hidden;
  font-family: var(--font-primary);
  background-color: var(--color-bg);
  color: var(--color-text);
}

/* 안전 영역 (Safe Area) -- 콘텐츠는 이 안에 배치 */
.card-news .safe-area {
  position: absolute;
  top: 60px;
  right: 60px;
  bottom: 60px;
  left: 60px;
  display: flex;
  flex-direction: column;
}

/* 전체 CSS 변수 시스템 */
:root {
  /* Typography */
  --font-primary: 'Paperlogy', sans-serif;
  --font-serif: 'Nanum Myeongjo', serif;
  --weight-light: 300;
  --weight-regular: 400;
  --weight-medium: 500;
  --weight-bold: 700;
  --weight-extrabold: 800;
  --weight-black: 900;

  /* Colors -- 카드뉴스 생성 시 동적으로 결정 */
  --color-primary: #2563EB;
  --color-accent: #60A5FA;
  --color-bg: #0F0F0F;
  --color-surface: #1A1A2E;
  --color-text: #FFFFFF;
  --color-text-dim: #888888;
  --color-text-muted: #555555;
  --color-border: rgba(255, 255, 255, 0.1);

  /* Spacing */
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 1.5rem;
  --space-lg: 2.5rem;
  --space-xl: 4rem;

  /* Border Radius */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-full: 9999px;

  /* Icon System */
  --icon-size: 48px;
  --icon-stroke-width: 1.5px;
  --icon-color: var(--color-primary);

  /* Shadow */
  --shadow-soft: 0 8px 32px rgba(0, 0, 0, 0.12);
  --shadow-elevated: 0 16px 48px rgba(0, 0, 0, 0.2);
}
```

---

## 부록: 체크리스트 (카드 생성 시 검증 항목)

카드뉴스 HTML을 생성한 후, 아래 항목을 반드시 검증한다.

### Typography
- [ ] `font-weight: bold` 대신 수치(400, 700, 800 등)를 사용하고 있는가
- [ ] 제목에 `letter-spacing` 음수값이 적용되어 있는가
- [ ] Big-Medium-Small 3단계 크기 위계가 명확한가
- [ ] 폰트 종류가 2개(산세리프 + 세리프) 이내인가

### Color
- [ ] 유채색이 3가지 이내인가
- [ ] 모든 색상이 CSS 변수를 참조하고 있는가 (하드코딩 없는가)
- [ ] 배경 대비 텍스트 가독성이 확보되어 있는가
- [ ] 강조에 빨간색을 사용하지 않았는가

### Layout
- [ ] 코너 앵커가 최소 2개 배치되어 있는가
- [ ] 4분면의 시각적 무게가 균형 잡혀 있는가
- [ ] 콘텐츠 구조에 맞는 레이아웃 패턴(Z/LR/TB)이 적용되었는가

### Background
- [ ] 이미지 위 텍스트에 그라데이션 마스크 또는 오버레이가 적용되어 있는가
- [ ] 텍스트 밀도에 따라 배경 밝기가 조절되어 있는가

### Content
- [ ] 제목이 결론형 문장인가 (명사형 종결이 아닌가)
- [ ] 전문 용어가 쉬운 표현으로 순화되었는가
- [ ] 마지막 카드가 "감사합니다"가 아닌 시네마틱 엔딩인가

### Consistency
- [ ] 아이콘 스타일(Line/Filled)이 전체 시리즈에서 통일되어 있는가
- [ ] 그림자 스타일이 소프트 섀도우 규칙을 따르는가
- [ ] 모서리 곡률(border-radius)이 전체에서 일관되는가

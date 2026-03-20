# CSS Patterns for Card News

카드뉴스 생성 시 바로 복사하여 사용할 수 있는 CSS 코드 스니펫 모음.
모든 패턴은 1080x1350px (4:5 비율) 카드뉴스 기준이며, Paperlogy 폰트 기반이다.

---

## 1. Base Template

카드뉴스 HTML 파일의 기본 보일러플레이트. 모든 카드는 이 구조에서 시작한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Card News</title>
<style>

/* ================================================
   Paperlogy 폰트 선언 (9단계 굵기, 100-900)
   FONTS_DIR 은 실제 절대 경로로 치환하여 사용
   ================================================ */
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-1Thin.ttf') format('truetype'); font-weight: 100; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-2ExtraLight.ttf') format('truetype'); font-weight: 200; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-3Light.ttf') format('truetype'); font-weight: 300; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-4Regular.ttf') format('truetype'); font-weight: 400; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-5Medium.ttf') format('truetype'); font-weight: 500; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-6SemiBold.ttf') format('truetype'); font-weight: 600; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-7Bold.ttf') format('truetype'); font-weight: 700; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-8ExtraBold.ttf') format('truetype'); font-weight: 800; font-style: normal; }
@font-face { font-family: 'Paperlogy'; src: url('FONTS_DIR/Paperlogy-9Black.ttf') format('truetype'); font-weight: 900; font-style: normal; }

/* ================================================
   리셋 및 기본 설정
   ================================================ */
*, *::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: #f0f0f0;
    font-family: 'Paperlogy', sans-serif;
    font-weight: 400;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* ================================================
   루트 컨테이너 (1080x1350px, 4:5 비율)
   ================================================ */
.card {
    position: relative;
    width: 1080px;
    height: 1350px;
    overflow: hidden;
    background: var(--bg-color, #FFFFFF);
    color: var(--text-color, #1A1A1A);
}

/* ================================================
   CSS 변수 템플릿 - 컬러 팔레트
   프로젝트별로 이 값들만 교체하면 전체 톤이 바뀐다.
   3색 제한 원칙: primary, secondary, accent 만 사용.
   ================================================ */
:root {
    /* 배경/전경 기본색 */
    --bg-color: #FFFFFF;
    --text-color: #1A1A1A;

    /* 3색 팔레트 (프로젝트별 교체) */
    --primary-color: #2B2B2B;      /* 메인 컬러 - 제목, 강조 요소 */
    --secondary-color: #6B6B6B;    /* 보조 컬러 - 서브 텍스트, 구분선 */
    --accent-color: #3A7BDE;       /* 포인트 컬러 - 키워드 강조, 하이라이트 */

    /* 디밍용 그레이 (강조의 역발상: 주변을 죽여서 핵심을 살린다) */
    --dim-gray: #AAAAAA;
    --light-gray: #E5E5E5;

    /* 간격 기준값 */
    --pad: 72px;                   /* 카드 내부 기본 패딩 */
    --pad-sm: 36px;                /* 좁은 패딩 */
}

/* ================================================
   한국어 텍스트 기본 처리
   ================================================ */
.card {
    word-break: keep-all;          /* 한국어 단어 단위 줄바꿈 */
    line-height: 1.5;
    letter-spacing: -0.02em;       /* 본문 기본 자간 약간 좁힘 */
}

</style>
</head>
<body>

<div class="card">
    <!-- 카드 콘텐츠가 여기에 들어간다 -->
</div>

</body>
</html>
```

---

## 2. Typography Presets

타이포그래피는 카드뉴스 품질의 핵심이다.
자간(letter-spacing)을 좁혀 "덩어리감"을 만들고, font-weight 수치를 명확히 지정한다.
`font-weight: bold` 대신 반드시 숫자(100~900)를 사용한다.

### 2-1. 메인 타이틀

```css
/* 메인 타이틀 - 카드의 가장 큰 텍스트. 결론형 문장을 넣는다. */
.title-main {
    font-family: 'Paperlogy', sans-serif;
    font-weight: 900;              /* Black - 최대 두께로 시각적 임팩트 */
    font-size: 64px;
    line-height: 1.2;
    letter-spacing: -0.05em;       /* 자간을 확 좁혀서 덩어리감 부여 */
    color: var(--text-color);
    word-break: keep-all;
}

/* 약간 가벼운 메인 타이틀 변형 */
.title-main--light {
    font-weight: 800;              /* ExtraBold */
    font-size: 56px;
}
```

### 2-2. 서브타이틀

```css
/* 서브타이틀 - 섹션 제목, 소주제 */
.title-sub {
    font-family: 'Paperlogy', sans-serif;
    font-weight: 700;              /* Bold */
    font-size: 36px;
    line-height: 1.3;
    letter-spacing: -0.03em;
    color: var(--primary-color);
}

/* 세미볼드 변형 - 좀 더 부드러운 느낌 */
.title-sub--soft {
    font-weight: 600;              /* SemiBold */
    font-size: 32px;
}
```

### 2-3. 본문 텍스트

```css
/* 본문 - 설명, 내용 전달용 */
.text-body {
    font-family: 'Paperlogy', sans-serif;
    font-weight: 400;              /* Regular */
    font-size: 28px;
    line-height: 1.6;
    letter-spacing: -0.02em;
    color: var(--text-color);
    word-break: keep-all;
}

/* 본문 미디엄 - 약간 강조된 본문 */
.text-body--medium {
    font-weight: 500;              /* Medium */
}
```

### 2-4. 캡션

```css
/* 캡션 - 출처, 부연설명, 메타 정보 */
.text-caption {
    font-family: 'Paperlogy', sans-serif;
    font-weight: 300;              /* Light */
    font-size: 20px;
    line-height: 1.4;
    letter-spacing: -0.01em;
    color: var(--secondary-color);
}

/* 극세 캡션 - 아주 작은 보조 텍스트 */
.text-caption--thin {
    font-weight: 200;              /* ExtraLight */
    font-size: 18px;
}
```

### 2-5. 그레이 디밍 헬퍼

강조할 때 빨간색을 칠하는 대신, 주변 텍스트를 회색으로 죽이는 "역발상 하이라이팅" 기법.
프로 디자이너의 핵심 테크닉이다.

```css
/* 비핵심 텍스트를 회색으로 톤다운 - 핵심 텍스트가 자연스럽게 부각된다 */
.dim {
    color: var(--dim-gray) !important;
}

/* 더 연한 디밍 */
.dim--light {
    color: #CCCCCC !important;
}

/* 슬라이드 간 연결 시, 이전 항목을 어둡게 처리하는 디밍 */
.dim--inactive {
    opacity: 0.3;
    transition: opacity 0.3s ease;
}

/* 활성 항목은 밝게 유지 */
.dim--active {
    opacity: 1;
    font-weight: 700;
}
```

### 2-6. 키워드 하이라이트

한 문장 안에서 핵심 키워드 1~2개만 `<span>`으로 감싸서 강조한다.

```css
/* 키워드 강조 - accent 컬러 + 굵기 상승 */
.highlight {
    color: var(--accent-color);
    font-weight: 700;
}

/* 배경 하이라이트 - 형광펜 효과 */
.highlight--bg {
    background: linear-gradient(transparent 50%, rgba(58, 123, 222, 0.15) 50%);
    padding: 0 4px;
    font-weight: 600;
}

/* 밑줄 하이라이트 */
.highlight--underline {
    text-decoration: underline;
    text-decoration-color: var(--accent-color);
    text-underline-offset: 6px;
    text-decoration-thickness: 3px;
    font-weight: 600;
}
```

**HTML 사용 예시:**
```html
<p class="text-body">
    <span class="dim">입에</span>
    <span class="highlight">단 것</span>
    <span class="dim">이 몸에도</span>
    <span class="highlight">좋다</span>
</p>
```

---

## 3. Layout Patterns

### 3-1. Full-Bleed 단일 컬럼

텍스트가 화면 전체를 차지하는 레이아웃. 임팩트 있는 메시지 전달에 사용.

```css
/* 풀블리드 단일 컬럼 레이아웃 */
.layout-fullbleed {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: var(--pad);
    text-align: center;
}
```

```html
<!-- 풀블리드 단일 컬럼 HTML 구조 -->
<div class="card">
    <div class="layout-fullbleed">
        <h1 class="title-main">핵심 메시지를 여기에</h1>
        <p class="text-body" style="margin-top: 32px;">보조 설명 텍스트</p>
    </div>
</div>
```

### 3-2. 2단 분할 (텍스트 + 이미지)

좌우 분할 레이아웃. 시간적 흐름이나 인과관계 설명에 적합.

```css
/* 2단 분할 레이아웃 - 좌: 텍스트, 우: 이미지 */
.layout-split {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
}

/* 텍스트 영역 */
.layout-split__text {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: var(--pad);
}

/* 이미지 영역 */
.layout-split__image {
    width: 100%;
    height: 100%;
    overflow: hidden;
}

.layout-split__image img {
    width: 100%;
    height: 100%;
    object-fit: cover;             /* 비율 유지하면서 영역 채움 */
}
```

```html
<!-- 2단 분할 HTML 구조 -->
<div class="card">
    <div class="layout-split">
        <div class="layout-split__text">
            <h2 class="title-sub">섹션 제목</h2>
            <p class="text-body" style="margin-top: 24px;">설명 내용</p>
        </div>
        <div class="layout-split__image">
            <img src="IMAGE_PATH" alt="">
        </div>
    </div>
</div>
```

### 3-3. 상단 이미지 + 하단 텍스트

결론-이유-예시 구조에 적합한 상하 분할 레이아웃.

```css
/* 상단 이미지 + 하단 텍스트 레이아웃 */
.layout-top-image {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-rows: 55% 45%;   /* 이미지가 약간 더 큰 비율 */
}

/* 이미지 영역 */
.layout-top-image__visual {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
}

.layout-top-image__visual img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* 텍스트 영역 */
.layout-top-image__content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: var(--pad) var(--pad) var(--pad) var(--pad);
}
```

```html
<!-- 상단 이미지 + 하단 텍스트 HTML 구조 -->
<div class="card">
    <div class="layout-top-image">
        <div class="layout-top-image__visual">
            <img src="IMAGE_PATH" alt="">
        </div>
        <div class="layout-top-image__content">
            <h2 class="title-sub">제목</h2>
            <p class="text-body" style="margin-top: 20px;">본문 내용</p>
        </div>
    </div>
</div>
```

### 3-4. 센터 포커스

화면 중앙에 핵심 요소를 크게 배치. Big-Medium-Small 위계를 활용한다.

```css
/* 센터 포커스 레이아웃 */
.layout-center {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: var(--pad);
    text-align: center;
}

/* Big - 시선을 끄는 메인 비주얼 (화면의 50~60%) */
.layout-center__hero {
    font-size: 120px;
    font-weight: 900;
    letter-spacing: -0.05em;
    line-height: 1.1;
    color: var(--accent-color);
    margin-bottom: 40px;
}

/* Medium - 핵심 텍스트 (화면의 30%) */
.layout-center__body {
    font-size: 32px;
    font-weight: 500;
    line-height: 1.5;
    color: var(--text-color);
    max-width: 800px;
}

/* Small - 메타 데이터 (화면의 10%) */
.layout-center__meta {
    font-size: 20px;
    font-weight: 300;
    color: var(--secondary-color);
    margin-top: 40px;
}
```

```html
<!-- 센터 포커스 HTML 구조 (숫자 강조 예시) -->
<div class="card">
    <div class="layout-center">
        <div class="layout-center__hero">6x</div>
        <div class="layout-center__body">3년 만에 6배 성장을 달성했습니다</div>
        <div class="layout-center__meta">2023년 기준 | 연간 매출 보고서</div>
    </div>
</div>
```

### 3-5. 그리드 기반 다중 항목

여러 항목을 균등하게 배치. 시각적 균형을 자동으로 맞춘다.

```css
/* 그리드 기반 다중 항목 레이아웃 */
.layout-grid {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: var(--pad);
}

/* 그리드 헤더 영역 */
.layout-grid__header {
    margin-bottom: 48px;
}

/* 아이템 그리드 - auto-fit으로 균등 분할 */
.layout-grid__items {
    flex: 1;
    display: grid;
    grid-template-columns: repeat(2, 1fr);   /* 2열 기본 */
    gap: 32px;
    align-content: center;
}

/* 3열 변형 */
.layout-grid__items--col3 {
    grid-template-columns: repeat(3, 1fr);
}

/* 각 아이템 카드 */
.layout-grid__item {
    background: var(--light-gray);
    border-radius: 20px;
    padding: 36px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.layout-grid__item-title {
    font-weight: 700;
    font-size: 28px;
    margin-bottom: 12px;
    color: var(--primary-color);
}

.layout-grid__item-desc {
    font-weight: 400;
    font-size: 22px;
    line-height: 1.5;
    color: var(--secondary-color);
}
```

```html
<!-- 그리드 다중 항목 HTML 구조 -->
<div class="card">
    <div class="layout-grid">
        <div class="layout-grid__header">
            <h2 class="title-sub">핵심 포인트 4가지</h2>
        </div>
        <div class="layout-grid__items">
            <div class="layout-grid__item">
                <div class="layout-grid__item-title">01</div>
                <div class="layout-grid__item-desc">첫 번째 항목 설명</div>
            </div>
            <div class="layout-grid__item">
                <div class="layout-grid__item-title">02</div>
                <div class="layout-grid__item-desc">두 번째 항목 설명</div>
            </div>
            <div class="layout-grid__item">
                <div class="layout-grid__item-title">03</div>
                <div class="layout-grid__item-desc">세 번째 항목 설명</div>
            </div>
            <div class="layout-grid__item">
                <div class="layout-grid__item-title">04</div>
                <div class="layout-grid__item-desc">네 번째 항목 설명</div>
            </div>
        </div>
    </div>
</div>
```

### 3-6. 코너 앵커 포지셔닝

카드 네 귀퉁이에 작은 요소(페이지 번호, 로고, 장식)를 배치하여 시각적 안정감을 부여한다.
"사방에 못을 박는 블라인드 텍스트" 기법.

```css
/* 코너 앵커 시스템 - 카드 네 귀퉁이에 요소 배치 */

/* 좌상단 앵커 (보통 로고나 브랜드명) */
.anchor-tl {
    position: absolute;
    top: var(--pad-sm);
    left: var(--pad-sm);
    font-weight: 600;
    font-size: 18px;
    color: var(--secondary-color);
    z-index: 10;
}

/* 우상단 앵커 (보통 페이지 번호) */
.anchor-tr {
    position: absolute;
    top: var(--pad-sm);
    right: var(--pad-sm);
    font-weight: 300;
    font-size: 18px;
    color: var(--secondary-color);
    z-index: 10;
}

/* 좌하단 앵커 (보통 출처, 날짜) */
.anchor-bl {
    position: absolute;
    bottom: var(--pad-sm);
    left: var(--pad-sm);
    font-weight: 300;
    font-size: 16px;
    color: var(--secondary-color);
    z-index: 10;
}

/* 우하단 앵커 (보통 장식 기호) */
.anchor-br {
    position: absolute;
    bottom: var(--pad-sm);
    right: var(--pad-sm);
    font-weight: 200;
    font-size: 20px;
    color: var(--secondary-color);
    z-index: 10;
}

/* 장식용 십자 마크 */
.anchor-cross {
    font-weight: 200;
    font-size: 24px;
    color: var(--dim-gray);
}
```

```html
<!-- 코너 앵커 HTML 구조 -->
<div class="card">
    <!-- 4개 코너 앵커 -->
    <div class="anchor-tl">BrandName</div>
    <div class="anchor-tr">01</div>
    <div class="anchor-bl">2026.03</div>
    <div class="anchor-br"><span class="anchor-cross">+</span></div>

    <!-- 메인 콘텐츠 -->
    <div class="layout-fullbleed">
        <h1 class="title-main">본문 내용</h1>
    </div>
</div>
```

---

## 4. Visual Effects

### 4-1. 그라데이션 마스크 (이미지 위 텍스트 가독성 확보)

배경 이미지 위에 텍스트를 올릴 때, 그라데이션으로 이미지의 역할을 축소하여
텍스트 가독성을 확보한다. 방향은 텍스트 위치에 따라 선택.

```css
/* 그라데이션 마스크 - 하단에서 상단으로 (텍스트가 하단에 올 때) */
.gradient-mask--bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 60%;
    background: linear-gradient(
        to top,
        rgba(0, 0, 0, 0.85) 0%,
        rgba(0, 0, 0, 0.5) 40%,
        rgba(0, 0, 0, 0) 100%
    );
    z-index: 1;
}

/* 그라데이션 마스크 - 좌측에서 우측으로 (텍스트가 좌측에 올 때) */
.gradient-mask--left {
    position: absolute;
    top: 0;
    left: 0;
    width: 60%;
    height: 100%;
    background: linear-gradient(
        to right,
        rgba(0, 0, 0, 0.9) 0%,
        rgba(0, 0, 0, 0.6) 40%,
        rgba(0, 0, 0, 0) 100%
    );
    z-index: 1;
}

/* 그라데이션 마스크 - 전체 덮기 (이미지를 완전히 배경으로 밀어낼 때) */
.gradient-mask--full {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1;
}

/* 그라데이션 위의 텍스트는 반드시 z-index를 높게 설정 */
.gradient-mask--content {
    position: relative;
    z-index: 2;
    color: #FFFFFF;
}
```

```html
<!-- 그라데이션 마스크 사용 예시 -->
<div class="card">
    <!-- 배경 이미지 -->
    <img src="IMAGE_PATH" alt="" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">

    <!-- 하단 그라데이션 마스크 -->
    <div class="gradient-mask--bottom"></div>

    <!-- 텍스트 (그라데이션 위에 배치) -->
    <div class="gradient-mask--content" style="position: absolute; bottom: 0; left: 0; padding: 72px;">
        <h1 class="title-main" style="color: #fff;">제목 텍스트</h1>
        <p class="text-body" style="color: rgba(255,255,255,0.8); margin-top: 20px;">부제 텍스트</p>
    </div>
</div>
```

### 4-2. 글래스모피즘 카드

복잡한 배경 위에 반투명 유리판을 올린 효과. 배경의 맥락은 유지하면서 텍스트 가독성을 확보.

```css
/* 글래스모피즘 패널 - 밝은 배경용 */
.glass-panel {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 24px;
    padding: 48px;
}

/* 글래스모피즘 패널 - 어두운 배경용 */
.glass-panel--dark {
    background: rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    padding: 48px;
    color: #FFFFFF;
}

/* 글래스모피즘 패널 - 강한 블러 (텍스트 많을 때) */
.glass-panel--heavy {
    background: rgba(255, 255, 255, 0.35);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.4);
    border-radius: 24px;
    padding: 48px;
}
```

```html
<!-- 글래스모피즘 사용 예시 -->
<div class="card" style="background: url('IMAGE_PATH') center/cover no-repeat;">
    <div style="display: flex; justify-content: center; align-items: center; width: 100%; height: 100%; padding: 72px;">
        <div class="glass-panel">
            <h2 class="title-sub">유리 효과 위의 텍스트</h2>
            <p class="text-body" style="margin-top: 20px;">가독성이 확보된 본문</p>
        </div>
    </div>
</div>
```

### 4-3. 소프트 섀도우 프리셋

그림자 투명도를 높이고(알파 0.4~0.5) blur를 넓게 퍼뜨려 고급스러운 느낌을 낸다.
진하고 딱딱한 그림자는 촌스러움의 원인.

```css
/* --- 밝은 배경용 소프트 섀도우 --- */

/* 텍스트 소프트 섀도우 */
.shadow-text--light {
    text-shadow: 0px 2px 12px rgba(0, 0, 0, 0.08);
}

/* 박스 소프트 섀도우 - 약하게 */
.shadow-box--light-sm {
    box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.06);
}

/* 박스 소프트 섀도우 - 보통 */
.shadow-box--light-md {
    box-shadow: 0px 8px 32px rgba(0, 0, 0, 0.1);
}

/* 박스 소프트 섀도우 - 강하게 */
.shadow-box--light-lg {
    box-shadow: 0px 16px 48px rgba(0, 0, 0, 0.12);
}

/* --- 어두운 배경용 소프트 섀도우 --- */

/* 텍스트 소프트 섀도우 (어두운 배경) */
.shadow-text--dark {
    text-shadow: 0px 4px 15px rgba(0, 0, 0, 0.4);
}

/* 박스 소프트 섀도우 - 어두운 배경용 */
.shadow-box--dark-md {
    box-shadow: 0px 8px 32px rgba(0, 0, 0, 0.4);
}

.shadow-box--dark-lg {
    box-shadow: 0px 16px 60px rgba(0, 0, 0, 0.5);
}
```

### 4-4. 화이트 글로우 이펙트 (어두운 배경용)

어두운 배경에서 피사체나 텍스트 뒤에 흰색 후광을 주어 고급스럽게 부각시킨다.

```css
/* 화이트 글로우 - 이미지에 적용 (drop-shadow로 PNG 윤곽 따라 빛남) */
.glow-white {
    filter: drop-shadow(0px 0px 30px rgba(255, 255, 255, 0.3));
}

/* 화이트 글로우 - 강하게 */
.glow-white--strong {
    filter: drop-shadow(0px 0px 50px rgba(255, 255, 255, 0.5));
}

/* 화이트 글로우 - 텍스트에 적용 */
.glow-white--text {
    text-shadow:
        0px 0px 20px rgba(255, 255, 255, 0.3),
        0px 0px 40px rgba(255, 255, 255, 0.15);
}

/* 화이트 글로우 - 박스에 적용 */
.glow-white--box {
    box-shadow:
        0px 0px 30px rgba(255, 255, 255, 0.15),
        0px 0px 60px rgba(255, 255, 255, 0.08);
}

/* 컬러 글로우 - accent 컬러로 빛나는 효과 */
.glow-accent {
    filter: drop-shadow(0px 0px 30px var(--accent-color));
}
```

### 4-5. 배경 타이포그래피 워터마크

빈 공간에 영문 키워드를 극단적으로 크게 깔고 투명도 5%로 배경 장식 효과를 준다.
웹 랜딩페이지에서 흔히 사용되는 트렌디한 기법.

```css
/* 배경 타이포그래피 워터마크 */
.bg-watermark {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: 'Paperlogy', sans-serif;
    font-weight: 900;
    font-size: 240px;              /* 극단적으로 큰 사이즈 */
    color: rgba(0, 0, 0, 0.05);   /* 투명도 5% - 배경처럼 은은하게 */
    white-space: nowrap;
    z-index: 0;                    /* 다른 콘텐츠 뒤로 배치 */
    pointer-events: none;          /* 클릭 이벤트 투과 */
    user-select: none;
    letter-spacing: -0.03em;
    line-height: 1;
}

/* 워터마크 - 어두운 배경용 (흰색 글자) */
.bg-watermark--light {
    color: rgba(255, 255, 255, 0.05);
}

/* 워터마크 - 회전 변형 */
.bg-watermark--rotated {
    transform: translate(-50%, -50%) rotate(-15deg);
}

/* 워터마크 - 상단 정렬 변형 */
.bg-watermark--top {
    top: 15%;
    transform: translate(-50%, -50%);
}
```

```html
<!-- 배경 타이포그래피 워터마크 사용 예시 -->
<div class="card">
    <!-- 워터마크 (가장 뒤에 깔림) -->
    <div class="bg-watermark">CONTENTS</div>

    <!-- 실제 콘텐츠 -->
    <div class="layout-fullbleed" style="position: relative; z-index: 1;">
        <h1 class="title-main">목차</h1>
    </div>
</div>
```

### 4-6. 디밍 오버레이

배경 이미지의 밝기를 낮추거나 색을 입혀 텍스트 가독성을 확보하는 오버레이.

```css
/* 디밍 오버레이 - 검은색 반투명 */
.overlay-dim {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.45);
    z-index: 1;
}

/* 디밍 오버레이 - 강하게 (텍스트가 많을 때) */
.overlay-dim--heavy {
    background: rgba(0, 0, 0, 0.65);
}

/* 디밍 오버레이 - 연하게 (이미지를 살리고 싶을 때) */
.overlay-dim--light {
    background: rgba(0, 0, 0, 0.25);
}

/* 디밍 오버레이 - 브랜드 컬러 오버레이 */
.overlay-brand {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: var(--accent-color);
    opacity: 0.75;
    mix-blend-mode: multiply;
    z-index: 1;
}

/* 오버레이 위 콘텐츠용 */
.overlay-content {
    position: relative;
    z-index: 2;
}
```

---

## 5. Card Series Patterns

카드뉴스는 여러 장이 시리즈로 이어지므로, 표지/본문/마무리의 일관된 패턴이 필요하다.

### 5-1. 커버 카드 (첫 번째 카드)

시선을 압도하는 첫 장. 풀블리드 이미지 + 그라데이션 + 큰 제목 조합.
수미상관 연출을 위해 커버 배경 이미지를 엔딩 카드에서도 재사용할 수 있다.

```css
/* 커버 카드 레이아웃 */
.card-cover {
    position: relative;
    width: 100%;
    height: 100%;
}

/* 커버 배경 이미지 */
.card-cover__bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 0;
}

/* 커버 그라데이션 (하단에서 상단으로 어두워짐) */
.card-cover__gradient {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 70%;
    background: linear-gradient(
        to top,
        rgba(0, 0, 0, 0.8) 0%,
        rgba(0, 0, 0, 0.4) 50%,
        rgba(0, 0, 0, 0) 100%
    );
    z-index: 1;
}

/* 커버 텍스트 영역 (하단 배치) */
.card-cover__content {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 0 var(--pad) 80px var(--pad);
    z-index: 2;
    color: #FFFFFF;
}

/* 커버 메인 타이틀 */
.card-cover__title {
    font-weight: 900;
    font-size: 72px;
    line-height: 1.15;
    letter-spacing: -0.05em;
    color: #FFFFFF;
    word-break: keep-all;
}

/* 커버 부제 */
.card-cover__subtitle {
    font-weight: 400;
    font-size: 28px;
    line-height: 1.4;
    color: rgba(255, 255, 255, 0.75);
    margin-top: 24px;
}

/* 커버 태그/카테고리 라벨 */
.card-cover__tag {
    display: inline-block;
    font-weight: 600;
    font-size: 18px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--accent-color);
    margin-bottom: 20px;
    padding: 6px 16px;
    border: 1px solid var(--accent-color);
    border-radius: 100px;
}
```

```html
<!-- 커버 카드 HTML 구조 -->
<div class="card">
    <div class="card-cover">
        <!-- 배경 이미지 -->
        <img class="card-cover__bg" src="IMAGE_PATH" alt="">

        <!-- 그라데이션 -->
        <div class="card-cover__gradient"></div>

        <!-- 코너 앵커 -->
        <div class="anchor-tl" style="color: rgba(255,255,255,0.6);">BrandName</div>
        <div class="anchor-tr" style="color: rgba(255,255,255,0.6);">01</div>

        <!-- 텍스트 -->
        <div class="card-cover__content">
            <div class="card-cover__tag">CATEGORY</div>
            <h1 class="card-cover__title">카드뉴스의<br>핵심 제목을 여기에</h1>
            <p class="card-cover__subtitle">부제목이나 요약문을 여기에 작성</p>
        </div>
    </div>
</div>
```

### 5-2. 콘텐츠 카드 (본문 카드)

정보를 전달하는 중간 카드들. 깔끔한 여백과 타이포그래피 위계가 핵심.

```css
/* 콘텐츠 카드 레이아웃 */
.card-content {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: var(--pad);
    background: var(--bg-color);
}

/* 콘텐츠 카드 상단 영역 (카테고리 + 페이지 번호) */
.card-content__header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 48px;
}

.card-content__category {
    font-weight: 600;
    font-size: 18px;
    letter-spacing: 0.03em;
    color: var(--accent-color);
}

.card-content__page {
    font-weight: 300;
    font-size: 18px;
    color: var(--dim-gray);
}

/* 콘텐츠 카드 본문 영역 */
.card-content__body {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* 콘텐츠 카드 제목 */
.card-content__title {
    font-weight: 800;
    font-size: 48px;
    line-height: 1.25;
    letter-spacing: -0.04em;
    color: var(--text-color);
    margin-bottom: 32px;
    word-break: keep-all;
}

/* 콘텐츠 카드 본문 텍스트 */
.card-content__text {
    font-weight: 400;
    font-size: 26px;
    line-height: 1.7;
    color: var(--secondary-color);
    word-break: keep-all;
}

/* 콘텐츠 카드 구분선 */
.card-content__divider {
    width: 60px;
    height: 3px;
    background: var(--accent-color);
    margin-bottom: 32px;
    border: none;
}

/* 콘텐츠 카드 하단 (출처, 부가정보) */
.card-content__footer {
    margin-top: auto;
    padding-top: 32px;
    font-weight: 300;
    font-size: 18px;
    color: var(--dim-gray);
}
```

```html
<!-- 콘텐츠 카드 HTML 구조 -->
<div class="card">
    <div class="card-content">
        <div class="card-content__header">
            <span class="card-content__category">TOPIC</span>
            <span class="card-content__page">03</span>
        </div>
        <div class="card-content__body">
            <hr class="card-content__divider">
            <h2 class="card-content__title">결론을 제목으로 쓴다</h2>
            <p class="card-content__text">
                <span class="dim">주제를 나열하지 말고</span>
                <span class="highlight">핵심 결론</span>
                <span class="dim">을 한 문장으로 전달한다.</span>
                프로는 청중이 해석하도록 내버려두지 않는다.
            </p>
        </div>
        <div class="card-content__footer">출처: 페이퍼로지 디자인 가이드</div>
    </div>
</div>
```

### 5-3. 엔딩 카드 (마지막 카드)

"감사합니다" 대신 감성적인 마무리. 커버 카드의 배경을 재사용하여 수미상관 효과를 낸다.

```css
/* 엔딩 카드 레이아웃 */
.card-ending {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: var(--pad);
}

/* 엔딩 카드 - 어두운 배경 (시네마틱 엔딩) */
.card-ending--dark {
    background: #0A0A0A;
    color: #FFFFFF;
}

/* 엔딩 메인 메시지 (명언이나 비전 담긴 한 문장) */
.card-ending__message {
    font-weight: 300;
    font-size: 40px;
    line-height: 1.6;
    letter-spacing: -0.02em;
    color: rgba(255, 255, 255, 0.9);
    max-width: 800px;
    word-break: keep-all;
}

/* 엔딩 메시지 내 강조 */
.card-ending__message strong {
    font-weight: 700;
    color: #FFFFFF;
}

/* 인용 부호 장식 */
.card-ending__quote-mark {
    font-size: 120px;
    font-weight: 100;
    line-height: 1;
    color: rgba(255, 255, 255, 0.15);
    margin-bottom: -20px;
}

/* 인용 출처 (인물명 등) */
.card-ending__author {
    font-weight: 400;
    font-size: 22px;
    color: rgba(255, 255, 255, 0.5);
    margin-top: 40px;
    letter-spacing: 0.02em;
}

/* 엔딩 하단 브랜드 정보 */
.card-ending__brand {
    position: absolute;
    bottom: var(--pad-sm);
    left: 50%;
    transform: translateX(-50%);
    font-weight: 300;
    font-size: 18px;
    color: rgba(255, 255, 255, 0.3);
    letter-spacing: 0.1em;
}

/* 이미지 배경 재사용 엔딩 (수미상관) */
.card-ending--with-bg {
    position: relative;
}

.card-ending--with-bg::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);    /* 커버 이미지 위에 어둡게 덮음 */
    z-index: 1;
}

.card-ending--with-bg > * {
    position: relative;
    z-index: 2;
}
```

```html
<!-- 엔딩 카드 HTML 구조 (시네마틱 엔딩) -->
<div class="card">
    <div class="card-ending card-ending--dark">
        <div class="card-ending__quote-mark">"</div>
        <p class="card-ending__message">
            좋은 디자인은 가능한 한<br>
            <strong>최소한으로 디자인</strong>하는 것이다
        </p>
        <p class="card-ending__author">-- Dieter Rams</p>
        <div class="card-ending__brand">BRAND NAME</div>
    </div>
</div>

<!-- 엔딩 카드 HTML 구조 (커버 배경 재사용 - 수미상관) -->
<div class="card">
    <div class="card-ending card-ending--with-bg" style="background: url('COVER_IMAGE_PATH') center/cover no-repeat;">
        <div class="card-ending__quote-mark">"</div>
        <p class="card-ending__message">마무리 메시지</p>
        <div class="card-ending__brand">BRAND NAME</div>
    </div>
</div>
```

### 5-4. 페이지 번호 인디케이터

세련된 페이지 표시. 슬래시와 전체 페이지 수는 회색으로 처리하여 현재 번호만 부각.

```css
/* 페이지 번호 인디케이터 - 기본 */
.page-indicator {
    font-family: 'Paperlogy', sans-serif;
    font-size: 18px;
    letter-spacing: 0.05em;
}

/* 현재 페이지 번호 */
.page-indicator__current {
    font-weight: 600;
    color: var(--text-color);
}

/* 구분자와 전체 페이지 수 (회색으로 톤다운) */
.page-indicator__total {
    font-weight: 300;
    color: var(--dim-gray);
}

/* 페이지 인디케이터 - 프로그레스 바 변형 */
.page-progress {
    position: absolute;
    top: 0;
    left: 0;
    height: 4px;
    background: var(--accent-color);
    z-index: 10;
    /* width는 인라인으로 퍼센트 지정: 예) width: 30% (3/10장) */
}

/* 페이지 인디케이터 - 도트 변형 */
.page-dots {
    display: flex;
    gap: 8px;
    align-items: center;
}

.page-dots__dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--light-gray);
}

/* 현재 페이지 도트 */
.page-dots__dot--active {
    width: 24px;
    border-radius: 4px;
    background: var(--accent-color);
}
```

```html
<!-- 페이지 번호 - 숫자 방식 -->
<div class="anchor-tr page-indicator">
    <span class="page-indicator__current">03</span>
    <span class="page-indicator__total"> / 10</span>
</div>

<!-- 페이지 번호 - 프로그레스 바 방식 (3/10장 = 30%) -->
<div class="page-progress" style="width: 30%;"></div>

<!-- 페이지 번호 - 도트 방식 -->
<div class="anchor-tr page-dots">
    <div class="page-dots__dot"></div>
    <div class="page-dots__dot"></div>
    <div class="page-dots__dot--active page-dots__dot"></div>
    <div class="page-dots__dot"></div>
    <div class="page-dots__dot"></div>
</div>
```

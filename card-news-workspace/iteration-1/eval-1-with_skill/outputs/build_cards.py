#!/usr/bin/env python3
"""Build all 5 card news HTML files with embedded base64 illustrations."""

import base64
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent
FONTS_DIR = "/Users/seongjin/Documents/Seongjin_Claude/Design/.claude/skills/card-news/assets/fonts"


def read_b64(card_num):
    """Read base64-encoded image for a card."""
    b64_path = OUTPUT_DIR / f"card{card_num}_b64.txt"
    return b64_path.read_text().strip()


def font_faces():
    """Generate @font-face declarations for Paperlogy."""
    weights = [
        (100, "1Thin"),
        (200, "2ExtraLight"),
        (300, "3Light"),
        (400, "4Regular"),
        (500, "5Medium"),
        (600, "6SemiBold"),
        (700, "7Bold"),
        (800, "8ExtraBold"),
        (900, "9Black"),
    ]
    declarations = []
    for weight, name in weights:
        declarations.append(
            f"@font-face {{ font-family: 'Paperlogy'; "
            f"src: url('{FONTS_DIR}/Paperlogy-{name}.ttf') format('truetype'); "
            f"font-weight: {weight}; font-style: normal; }}"
        )
    return "\n".join(declarations)


COMMON_CSS = """
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

:root {
    --primary: #00D4AA;
    --accent: #7B61FF;
    --neutral: #0A0A0F;
    --surface: #141420;
    --text: #FFFFFF;
    --text-dim: #888888;
    --text-muted: #555555;
    --bg: #0A0A0F;
    --radius-sm: 8px;
    --radius-md: 16px;
    --radius-lg: 24px;
    --pad: 72px;
    --pad-sm: 40px;
}

.card {
    position: relative;
    width: 1080px;
    height: 1350px;
    overflow: hidden;
    background: var(--bg);
    color: var(--text);
    font-family: 'Paperlogy', sans-serif;
    word-break: keep-all;
    line-height: 1.5;
}
"""


def build_card1(b64):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Card 01 - Cover</title>
<style>
{font_faces()}
{COMMON_CSS}

.card {{
    background: var(--bg);
    background-image:
        radial-gradient(ellipse at 30% 70%, rgba(0, 212, 170, 0.12) 0%, transparent 55%),
        radial-gradient(ellipse at 75% 25%, rgba(123, 97, 255, 0.10) 0%, transparent 50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}}

/* Corner anchors */
.anchor-tl {{
    position: absolute;
    top: var(--pad-sm);
    left: var(--pad-sm);
    font-weight: 500;
    font-size: 18px;
    color: var(--text-dim);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    z-index: 10;
}}

.anchor-tr {{
    position: absolute;
    top: var(--pad-sm);
    right: var(--pad-sm);
    font-weight: 300;
    font-size: 18px;
    color: var(--text-dim);
    z-index: 10;
}}

.anchor-bl {{
    position: absolute;
    bottom: var(--pad-sm);
    left: var(--pad-sm);
    font-weight: 300;
    font-size: 16px;
    color: var(--text-muted);
    z-index: 10;
}}

.anchor-br {{
    position: absolute;
    bottom: var(--pad-sm);
    right: var(--pad-sm);
    font-weight: 200;
    font-size: 20px;
    color: var(--text-muted);
    z-index: 10;
}}

/* Watermark */
.bg-watermark {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: 'Paperlogy', sans-serif;
    font-weight: 900;
    font-size: 200px;
    color: rgba(255, 255, 255, 0.03);
    white-space: nowrap;
    z-index: 0;
    pointer-events: none;
    user-select: none;
    letter-spacing: -0.03em;
    line-height: 1;
    text-transform: uppercase;
}}

/* Tag */
.tag {{
    display: inline-block;
    font-weight: 600;
    font-size: 20px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--primary);
    padding: 8px 24px;
    border: 1.5px solid rgba(0, 212, 170, 0.4);
    border-radius: 100px;
    margin-bottom: 36px;
    z-index: 2;
}}

/* Illustration */
.illust-container {{
    width: 380px;
    height: 380px;
    margin-bottom: 48px;
    z-index: 2;
    filter: drop-shadow(0 0 40px rgba(0, 212, 170, 0.25));
}}

.illust-container img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
}}

/* Title */
.cover-title {{
    font-weight: 900;
    font-size: 58px;
    line-height: 1.25;
    letter-spacing: -0.04em;
    text-align: center;
    color: var(--text);
    z-index: 2;
    max-width: 860px;
    padding: 0 40px;
}}

.cover-title .highlight {{
    color: var(--primary);
}}

/* Subtitle */
.cover-subtitle {{
    font-weight: 400;
    font-size: 26px;
    line-height: 1.5;
    color: var(--text-dim);
    text-align: center;
    margin-top: 24px;
    z-index: 2;
    max-width: 700px;
}}

/* Progress bar */
.progress-bar {{
    position: absolute;
    top: 0;
    left: 0;
    height: 4px;
    background: linear-gradient(to right, var(--primary), var(--accent));
    z-index: 10;
}}
</style>
</head>
<body>
<div class="card">
    <!-- Background watermark -->
    <div class="bg-watermark">AI</div>

    <!-- Progress bar -->
    <div class="progress-bar" style="width: 20%;"></div>

    <!-- Corner anchors -->
    <div class="anchor-tl">AI Guide</div>
    <div class="anchor-tr"><span style="font-weight:600; color: var(--text);">01</span><span style="color: var(--text-dim);"> / 05</span></div>
    <div class="anchor-bl">2026</div>
    <div class="anchor-br" style="font-size: 16px; color: var(--text-muted);">+</div>

    <!-- Tag -->
    <div class="tag">Artificial Intelligence</div>

    <!-- Illustration -->
    <div class="illust-container">
        <img src="data:image/png;base64,{b64}" alt="AI Robot">
    </div>

    <!-- Title -->
    <h1 class="cover-title">
        AI는 <span class="highlight">생각보다 단순한 원리</span>로<br>작동한다
    </h1>

    <!-- Subtitle -->
    <p class="cover-subtitle">어려운 용어 없이 알아보는 인공지능의 핵심</p>
</div>
</body>
</html>"""


def build_card2(b64):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Card 02 - Learning</title>
<style>
{font_faces()}
{COMMON_CSS}

.card {{
    background: var(--bg);
    background-image:
        radial-gradient(ellipse at 70% 80%, rgba(0, 212, 170, 0.08) 0%, transparent 50%);
    display: flex;
    flex-direction: column;
    padding: var(--pad);
}}

/* Corner anchors */
.anchor-tl {{
    position: absolute;
    top: var(--pad-sm);
    left: var(--pad-sm);
    font-weight: 500;
    font-size: 18px;
    color: var(--text-dim);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    z-index: 10;
}}

.anchor-tr {{
    position: absolute;
    top: var(--pad-sm);
    right: var(--pad-sm);
    font-weight: 300;
    font-size: 18px;
    color: var(--text-dim);
    z-index: 10;
}}

/* Progress bar */
.progress-bar {{
    position: absolute;
    top: 0;
    left: 0;
    height: 4px;
    background: linear-gradient(to right, var(--primary), var(--accent));
    z-index: 10;
}}

/* Header section */
.header {{
    margin-top: 48px;
    margin-bottom: 20px;
}}

.step-label {{
    font-weight: 600;
    font-size: 18px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 16px;
}}

.card-title {{
    font-weight: 800;
    font-size: 46px;
    line-height: 1.25;
    letter-spacing: -0.04em;
    color: var(--text);
}}

.card-title .dim {{
    color: var(--text-dim);
}}

/* Illustration */
.illust-area {{
    display: flex;
    justify-content: center;
    align-items: center;
    flex: 0 0 auto;
    margin: 24px 0;
}}

.illust-area img {{
    width: 380px;
    height: 380px;
    object-fit: contain;
    filter: drop-shadow(0 0 30px rgba(0, 212, 170, 0.2));
}}

/* Content area */
.content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding-bottom: 20px;
}}

.explanation {{
    font-weight: 400;
    font-size: 28px;
    line-height: 1.7;
    color: var(--text-dim);
}}

.explanation .key {{
    color: var(--text);
    font-weight: 700;
}}

.explanation .accent {{
    color: var(--primary);
    font-weight: 700;
}}

/* Divider */
.divider {{
    width: 60px;
    height: 3px;
    background: var(--primary);
    border: none;
    margin-bottom: 28px;
}}

/* Analogy box */
.analogy-box {{
    background: rgba(0, 212, 170, 0.06);
    border: 1px solid rgba(0, 212, 170, 0.15);
    border-radius: var(--radius-md);
    padding: 28px 32px;
    margin-top: 28px;
}}

.analogy-label {{
    font-weight: 600;
    font-size: 16px;
    color: var(--primary);
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 10px;
}}

.analogy-text {{
    font-weight: 400;
    font-size: 24px;
    line-height: 1.6;
    color: rgba(255, 255, 255, 0.8);
}}

.analogy-text .key {{
    color: var(--primary);
    font-weight: 600;
}}
</style>
</head>
<body>
<div class="card">
    <!-- Progress bar -->
    <div class="progress-bar" style="width: 40%;"></div>

    <!-- Corner anchors -->
    <div class="anchor-tl">AI Guide</div>
    <div class="anchor-tr"><span style="font-weight:600; color: var(--text);">02</span><span style="color: var(--text-dim);"> / 05</span></div>

    <!-- Header -->
    <div class="header">
        <div class="step-label">Step 1 -- How AI Learns</div>
        <h2 class="card-title">
            AI는 <span class="dim">수많은 예시를 보고</span><br>
            <span style="color: var(--primary);">패턴을 찾아</span> 배운다
        </h2>
    </div>

    <!-- Illustration -->
    <div class="illust-area">
        <img src="data:image/png;base64,{b64}" alt="Robot learning">
    </div>

    <!-- Content -->
    <div class="content">
        <div class="divider"></div>
        <p class="explanation">
            사람이 <span class="key">고양이 사진을 수백 장</span> 보면 처음 보는 고양이도 알아보듯,
            AI도 <span class="accent">엄청나게 많은 데이터</span>를 보면서 스스로 규칙을 찾아냅니다.
        </p>

        <div class="analogy-box">
            <div class="analogy-label">쉽게 말하면</div>
            <div class="analogy-text">
                AI의 학습 = <span class="key">문제집을 수만 번 푸는 것</span><br>
                틀릴 때마다 조금씩 고쳐서, 점점 정답률을 높여갑니다.
            </div>
        </div>
    </div>
</div>
</body>
</html>"""


def build_card3(b64):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Card 03 - Prediction</title>
<style>
{font_faces()}
{COMMON_CSS}

.card {{
    background: var(--bg);
    background-image:
        radial-gradient(ellipse at 25% 30%, rgba(123, 97, 255, 0.08) 0%, transparent 50%);
    display: flex;
    flex-direction: column;
    padding: var(--pad);
}}

/* Corner anchors */
.anchor-tl {{
    position: absolute;
    top: var(--pad-sm);
    left: var(--pad-sm);
    font-weight: 500;
    font-size: 18px;
    color: var(--text-dim);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    z-index: 10;
}}

.anchor-tr {{
    position: absolute;
    top: var(--pad-sm);
    right: var(--pad-sm);
    font-weight: 300;
    font-size: 18px;
    color: var(--text-dim);
    z-index: 10;
}}

/* Progress bar */
.progress-bar {{
    position: absolute;
    top: 0;
    left: 0;
    height: 4px;
    background: linear-gradient(to right, var(--primary), var(--accent));
    z-index: 10;
}}

/* Header */
.header {{
    margin-top: 48px;
    margin-bottom: 20px;
}}

.step-label {{
    font-weight: 600;
    font-size: 18px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 16px;
}}

.card-title {{
    font-weight: 800;
    font-size: 46px;
    line-height: 1.25;
    letter-spacing: -0.04em;
    color: var(--text);
}}

/* Layout - LR split */
.content-area {{
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 40px;
    margin-top: 10px;
}}

.illust-side {{
    flex: 0 0 380px;
}}

.illust-side img {{
    width: 380px;
    height: 380px;
    object-fit: contain;
    filter: drop-shadow(0 0 30px rgba(123, 97, 255, 0.2));
}}

.text-side {{
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 24px;
}}

/* Process steps */
.process-step {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: var(--radius-md);
    padding: 24px 28px;
    position: relative;
}}

.process-step.active {{
    background: rgba(123, 97, 255, 0.08);
    border-color: rgba(123, 97, 255, 0.25);
}}

.step-num {{
    font-weight: 900;
    font-size: 16px;
    color: var(--accent);
    letter-spacing: 0.05em;
    margin-bottom: 8px;
}}

.step-text {{
    font-weight: 400;
    font-size: 24px;
    line-height: 1.5;
    color: rgba(255, 255, 255, 0.7);
}}

.step-text .key {{
    color: var(--text);
    font-weight: 700;
}}

.step-text .accent {{
    color: var(--accent);
    font-weight: 700;
}}

/* Bottom note */
.bottom-note {{
    margin-top: auto;
    padding: 28px 0 20px 0;
    font-weight: 400;
    font-size: 24px;
    line-height: 1.6;
    color: var(--text-dim);
    border-top: 1px solid rgba(255, 255, 255, 0.08);
}}

.bottom-note .key {{
    color: var(--primary);
    font-weight: 600;
}}
</style>
</head>
<body>
<div class="card">
    <!-- Progress bar -->
    <div class="progress-bar" style="width: 60%;"></div>

    <!-- Corner anchors -->
    <div class="anchor-tl">AI Guide</div>
    <div class="anchor-tr"><span style="font-weight:600; color: var(--text);">03</span><span style="color: var(--text-dim);"> / 05</span></div>

    <!-- Header -->
    <div class="header">
        <div class="step-label">Step 2 -- How AI Answers</div>
        <h2 class="card-title">
            AI는 <span style="color: var(--accent);">스스로 생각하지 않고</span><br>
            가장 그럴듯한 답을 고른다
        </h2>
    </div>

    <!-- Content area: LR layout -->
    <div class="content-area">
        <div class="illust-side">
            <img src="data:image/png;base64,{b64}" alt="Robot thinking">
        </div>
        <div class="text-side">
            <div class="process-step">
                <div class="step-num">01</div>
                <div class="step-text"><span class="key">질문</span>이 들어오면</div>
            </div>
            <div class="process-step">
                <div class="step-num">02</div>
                <div class="step-text">배운 <span class="key">패턴</span>을 훑어보고</div>
            </div>
            <div class="process-step active">
                <div class="step-num">03</div>
                <div class="step-text"><span class="accent">확률이 가장 높은 답</span>을<br>내놓습니다</div>
            </div>
        </div>
    </div>

    <!-- Bottom note -->
    <div class="bottom-note">
        즉, AI는 "이해"하는 게 아니라<br>
        <span class="key">"이런 질문엔 이런 답이 나올 확률이 높다"</span>고 예측하는 것입니다.
    </div>
</div>
</body>
</html>"""


def build_card4(b64):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Card 04 - Daily Life</title>
<style>
{font_faces()}
{COMMON_CSS}

.card {{
    background: var(--bg);
    background-image:
        radial-gradient(ellipse at 50% 90%, rgba(0, 212, 170, 0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(123, 97, 255, 0.06) 0%, transparent 50%);
    display: flex;
    flex-direction: column;
    padding: var(--pad);
}}

/* Corner anchors */
.anchor-tl {{
    position: absolute;
    top: var(--pad-sm);
    left: var(--pad-sm);
    font-weight: 500;
    font-size: 18px;
    color: var(--text-dim);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    z-index: 10;
}}

.anchor-tr {{
    position: absolute;
    top: var(--pad-sm);
    right: var(--pad-sm);
    font-weight: 300;
    font-size: 18px;
    color: var(--text-dim);
    z-index: 10;
}}

/* Progress bar */
.progress-bar {{
    position: absolute;
    top: 0;
    left: 0;
    height: 4px;
    background: linear-gradient(to right, var(--primary), var(--accent));
    z-index: 10;
}}

/* Header */
.header {{
    margin-top: 48px;
    margin-bottom: 24px;
}}

.step-label {{
    font-weight: 600;
    font-size: 18px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--primary);
    margin-bottom: 16px;
}}

.card-title {{
    font-weight: 800;
    font-size: 44px;
    line-height: 1.25;
    letter-spacing: -0.04em;
    color: var(--text);
}}

/* Illustration */
.illust-center {{
    display: flex;
    justify-content: center;
    margin: 16px 0 28px 0;
}}

.illust-center img {{
    width: 320px;
    height: 320px;
    object-fit: contain;
    filter: drop-shadow(0 0 25px rgba(0, 212, 170, 0.2));
}}

/* Grid of examples */
.examples-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    flex: 1;
    align-content: center;
}}

.example-card {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: var(--radius-md);
    padding: 28px 24px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}}

.example-icon {{
    font-size: 36px;
    line-height: 1;
}}

.example-title {{
    font-weight: 700;
    font-size: 22px;
    color: var(--text);
}}

.example-desc {{
    font-weight: 400;
    font-size: 20px;
    line-height: 1.5;
    color: var(--text-dim);
}}

.example-desc .key {{
    color: var(--primary);
    font-weight: 600;
}}
</style>
</head>
<body>
<div class="card">
    <!-- Progress bar -->
    <div class="progress-bar" style="width: 80%;"></div>

    <!-- Corner anchors -->
    <div class="anchor-tl">AI Guide</div>
    <div class="anchor-tr"><span style="font-weight:600; color: var(--text);">04</span><span style="color: var(--text-dim);"> / 05</span></div>

    <!-- Header -->
    <div class="header">
        <div class="step-label">In Your Daily Life</div>
        <h2 class="card-title">
            <span style="color: var(--text-dim);">사실</span> AI는 이미<br>
            <span style="color: var(--primary);">우리 일상 곳곳</span>에 있다
        </h2>
    </div>

    <!-- Illustration -->
    <div class="illust-center">
        <img src="data:image/png;base64,{b64}" alt="Robot with daily items">
    </div>

    <!-- Examples grid -->
    <div class="examples-grid">
        <div class="example-card">
            <div class="example-icon">
                <svg width="36" height="36" viewBox="0 0 36 36" fill="none"><rect x="4" y="8" width="28" height="20" rx="4" stroke="#00D4AA" stroke-width="2"/><path d="M12 18L16 22L24 14" stroke="#00D4AA" stroke-width="2" stroke-linecap="round"/></svg>
            </div>
            <div class="example-title">유튜브 추천</div>
            <div class="example-desc"><span class="key">취향을 분석</span>해서 좋아할 영상을 골라줍니다</div>
        </div>
        <div class="example-card">
            <div class="example-icon">
                <svg width="36" height="36" viewBox="0 0 36 36" fill="none"><circle cx="18" cy="14" r="6" stroke="#7B61FF" stroke-width="2"/><path d="M8 30c0-5.5 4.5-10 10-10s10 4.5 10 10" stroke="#7B61FF" stroke-width="2" stroke-linecap="round"/></svg>
            </div>
            <div class="example-title">얼굴 인식</div>
            <div class="example-desc">스마트폰 잠금 해제, <span class="key">얼굴 패턴</span>을 기억합니다</div>
        </div>
        <div class="example-card">
            <div class="example-icon">
                <svg width="36" height="36" viewBox="0 0 36 36" fill="none"><path d="M18 4L18 32M4 18L32 18" stroke="#00D4AA" stroke-width="2" stroke-linecap="round"/><circle cx="18" cy="18" r="12" stroke="#00D4AA" stroke-width="2"/></svg>
            </div>
            <div class="example-title">내비게이션</div>
            <div class="example-desc"><span class="key">실시간 교통</span>을 분석해 빠른 길을 안내합니다</div>
        </div>
        <div class="example-card">
            <div class="example-icon">
                <svg width="36" height="36" viewBox="0 0 36 36" fill="none"><path d="M6 28L14 20L20 24L30 10" stroke="#7B61FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="30" cy="10" r="3" fill="#7B61FF"/></svg>
            </div>
            <div class="example-title">번역 앱</div>
            <div class="example-desc"><span class="key">언어의 규칙</span>을 학습해 자연스러운 번역을 합니다</div>
        </div>
    </div>
</div>
</body>
</html>"""


def build_card5(b64):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Card 05 - Ending</title>
<style>
{font_faces()}
{COMMON_CSS}

.card {{
    background: var(--bg);
    background-image:
        radial-gradient(ellipse at 50% 60%, rgba(0, 212, 170, 0.10) 0%, transparent 55%),
        radial-gradient(ellipse at 30% 80%, rgba(123, 97, 255, 0.08) 0%, transparent 50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: var(--pad);
}}

/* Corner anchors */
.anchor-tl {{
    position: absolute;
    top: var(--pad-sm);
    left: var(--pad-sm);
    font-weight: 500;
    font-size: 18px;
    color: var(--text-dim);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    z-index: 10;
}}

.anchor-tr {{
    position: absolute;
    top: var(--pad-sm);
    right: var(--pad-sm);
    font-weight: 300;
    font-size: 18px;
    color: var(--text-dim);
    z-index: 10;
}}

.anchor-bl {{
    position: absolute;
    bottom: var(--pad-sm);
    left: 50%;
    transform: translateX(-50%);
    font-weight: 300;
    font-size: 18px;
    color: var(--text-muted);
    z-index: 10;
    letter-spacing: 0.1em;
}}

/* Progress bar */
.progress-bar {{
    position: absolute;
    top: 0;
    left: 0;
    height: 4px;
    background: linear-gradient(to right, var(--primary), var(--accent));
    z-index: 10;
}}

/* Watermark */
.bg-watermark {{
    position: absolute;
    bottom: -30px;
    right: -20px;
    font-family: 'Paperlogy', sans-serif;
    font-weight: 900;
    font-size: 220px;
    color: rgba(255, 255, 255, 0.025);
    line-height: 1;
    pointer-events: none;
    user-select: none;
    z-index: 0;
}}

/* Illustration */
.illust-container {{
    width: 360px;
    height: 360px;
    margin-bottom: 48px;
    z-index: 2;
    filter: drop-shadow(0 0 40px rgba(0, 212, 170, 0.2)) drop-shadow(0 0 80px rgba(123, 97, 255, 0.15));
}}

.illust-container img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
}}

/* Quote mark */
.quote-mark {{
    font-family: 'Paperlogy', sans-serif;
    font-weight: 100;
    font-size: 120px;
    line-height: 1;
    color: rgba(255, 255, 255, 0.12);
    margin-bottom: -20px;
    z-index: 2;
}}

/* Ending message */
.ending-message {{
    font-weight: 300;
    font-size: 38px;
    line-height: 1.65;
    letter-spacing: -0.02em;
    color: rgba(255, 255, 255, 0.9);
    max-width: 800px;
    z-index: 2;
}}

.ending-message .strong {{
    font-weight: 700;
    color: var(--text);
}}

.ending-message .highlight {{
    color: var(--primary);
    font-weight: 700;
}}

/* Attribution */
.attribution {{
    margin-top: 32px;
    font-weight: 400;
    font-size: 22px;
    color: rgba(255, 255, 255, 0.4);
    z-index: 2;
}}
</style>
</head>
<body>
<div class="card">
    <!-- Background watermark -->
    <div class="bg-watermark">FUTURE</div>

    <!-- Progress bar -->
    <div class="progress-bar" style="width: 100%;"></div>

    <!-- Corner anchors -->
    <div class="anchor-tl">AI Guide</div>
    <div class="anchor-tr"><span style="font-weight:600; color: var(--text);">05</span><span style="color: var(--text-dim);"> / 05</span></div>
    <div class="anchor-bl">AI GUIDE 2026</div>

    <!-- Illustration -->
    <div class="illust-container">
        <img src="data:image/png;base64,{b64}" alt="Robot looking to future">
    </div>

    <!-- Quote mark -->
    <div class="quote-mark">"</div>

    <!-- Ending message -->
    <p class="ending-message">
        AI를 두려워할 필요는 없습니다<br>
        <span class="strong">원리를 이해하면</span>,<br>
        AI는 가장 <span class="highlight">든든한 도구</span>가 됩니다
    </p>

    <!-- Attribution -->
    <p class="attribution">-- 이해에서 활용으로, 당신의 AI 여정이 시작됩니다</p>
</div>
</body>
</html>"""


def main():
    print("Building card news HTML files...")

    builders = [
        (1, build_card1),
        (2, build_card2),
        (3, build_card3),
        (4, build_card4),
        (5, build_card5),
    ]

    for card_num, builder in builders:
        b64 = read_b64(card_num)
        html = builder(b64)
        output_path = OUTPUT_DIR / f"card_{card_num:02d}.html"
        output_path.write_text(html, encoding="utf-8")
        print(f"  Created: {output_path.name} ({len(html):,} bytes)")

    print("\nAll 5 HTML files created successfully.")


if __name__ == "__main__":
    main()

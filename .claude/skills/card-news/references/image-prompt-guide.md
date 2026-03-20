# Nano Banana Image Prompt Guide for Card News

카드뉴스 일러스트레이션 생성에 특화된 Nano Banana 프롬프트 가이드.
메타프롬프트 원칙과 공식 API 문서를 기반으로 카드뉴스 작업 흐름에 맞게 재구성했다.

---

## 1. 핵심 원칙

### 서술형 장면 묘사, 키워드 나열 금지

Nano Banana의 최대 강점은 깊이 있는 자연어 이해다. 키워드를 쉼표로 나열하지 말고, 장면을 설명하는 서술형 문장으로 프롬프트를 작성한다.

나쁜 예: `icon, money, growth, green, 3D, clay style`
좋은 예: `A cheerful 3D clay-style icon of a small green plant sprouting from a golden coin, rendered with soft rounded edges and a matte tactile texture. The background is pure white. No text.`

### Layout > Style

레이아웃(공간 구조, 배치, 여백)이 예술적 스타일보다 우선한다. 카드뉴스에서는 텍스트가 올라갈 영역을 먼저 확보한 뒤, 스타일을 결정한다.

### Edit, Don't Re-roll

생성된 이미지가 80% 만족스러우면 처음부터 재생성하지 않는다. 대화형 수정(multi-turn editing)으로 원하는 부분만 조정한다. 성공적인 요소를 유지하면서 필요한 부분만 바꾸는 것이 훨씬 효율적이다.

### 모든 프롬프트는 영문으로 작성

Nano Banana는 영문 프롬프트에서 최적 성능을 발휘한다. 한국어 컨셉이더라도 최종 프롬프트는 반드시 영어로 작성한다.

### 부정형 대신 긍정형으로

"~가 없는"이라고 쓰지 말고, 원하는 상태를 긍정형으로 묘사한다.

나쁜 예: `no clutter, no text, no complex background`
좋은 예: `a clean, uncluttered composition with a solid white background and ample negative space`

### 지원 비율 참고

API에서 설정 가능한 aspect_ratio 값: `1:1`, `1:4`, `1:8`, `2:3`, `3:2`, `3:4`, `4:1`, `4:3`, `4:5`, `5:4`, `8:1`, `9:16`, `16:9`, `21:9`

해상도 옵션 (Gemini 3 이상): `512`, `1K`, `2K`, `4K`

---

## 2. 카드뉴스 일러스트레이션 카테고리

### 아이콘 및 심볼 (1:1)

카드뉴스 본문에서 핵심 개념을 시각적으로 전달하는 아이콘. 배경 제거(rembg) 후 사용하거나, 흰 배경 상태로 직접 배치한다.

**3D 클레이 스타일 아이콘**

```
A colorful 3D clay-style icon of a glowing light bulb with a small gear inside, rendered with soft rounded edges, matte tactile texture, and gentle ambient occlusion shadows. The design is playful and slightly oversized with chibi-like proportions. The background must be pure white. No text.
```

```
A 3D clay-style icon of a shield with a checkmark in the center, rendered in soothing teal and white tones with soft rounded geometry and a subtle contact shadow beneath. The surface has a smooth matte finish like hand-molded clay. The background must be pure white. No text.
```

**플랫 디자인 아이콘**

```
A flat design icon of a megaphone emitting colorful sound waves, using a limited palette of coral, navy, and warm yellow. The shapes are geometric and clean with bold outlines and absolutely no gradients. Centered on a pure white background. No text.
```

```
A minimal flat design icon of a calendar page with a star marking today's date, using a two-tone palette of soft blue and bright orange. Clean geometric shapes with uniform line weight. The background must be pure white. No text.
```

**카와이 스타일**

```
A kawaii-style sticker of a happy coffee cup character with blushing cheeks and tiny arms giving a thumbs-up. The design features bold clean outlines, simple cel-shading, and a vibrant pastel color palette. The background must be pure white. No text.
```

---

### 컨셉 일러스트레이션 (1:1 또는 4:5)

추상적 개념이나 복잡한 아이디어를 시각적으로 설명하는 일러스트레이션.

**아이소메트릭 장면**

```
A clean isometric illustration of a small workspace scene showing a desk with a laptop, a potted plant, a coffee mug, and floating notification icons above the screen. The style is modern vector art with soft pastel colors, gentle shadows, and clean edges. The composition is centered with generous white space around the scene. No text.
```

```
A 45-degree isometric miniature 3D illustration of a tiny factory processing raw data into gold bars, with conveyor belts, gears, and glowing screens. The style uses soft refined textures with subtle PBR materials and gentle lighting. Clean solid-colored background in light gray. No text.
```

**은유적 시각화**

```
A conceptual illustration showing a person standing at a crossroads where one path is paved with golden bricks leading to a bright sunrise, and the other path fades into fog. The style is modern editorial illustration with clean lines, a limited color palette of warm gold and cool blue-gray, and significant negative space on the upper portion for text overlay. No text in the image.
```

```
A metaphorical illustration of a small seedling growing through a crack in a concrete floor, with warm sunlight streaming down from above. The style is clean vector illustration with soft gradients, using a palette of fresh green, warm yellow, and neutral gray. The upper two-thirds of the image is intentionally left as open space with a soft gradient. No text.
```

**인포그래픽 요소**

```
A clean, modern illustration of three ascending platforms like a podium, each holding a different icon: a book on the lowest, a brain on the middle, and a rocket on the highest. The style is flat design with subtle depth through layered shadows, using a cohesive palette of indigo, teal, and warm coral. White background with clean composition. No text.
```

---

### 배경 이미지 (4:5)

카드뉴스 슬라이드의 전체 배경으로 사용. 텍스트가 올라갈 공간을 충분히 확보하는 것이 핵심이다.

**미니멀 + 네거티브 스페이스**

```
A minimalist composition with a single small succulent plant positioned in the bottom-right corner of the frame. The background is a vast, seamless gradient from warm off-white to very pale peach, creating significant negative space covering at least 70 percent of the canvas for text overlay. Soft, diffused lighting from the top left. The image should be in 4:5 portrait format.
```

```
A minimalist composition featuring delicate abstract geometric lines in thin gold strokes, clustered in the bottom-left corner of the frame. The rest of the canvas is clean off-white with a subtle paper texture, providing ample negative space for text placement. Soft even lighting throughout. Portrait orientation 4:5.
```

**그라데이션 및 추상 배경**

```
An abstract background with soft flowing gradients transitioning from deep navy blue at the bottom to warm coral at the top, with subtle organic wave shapes creating gentle depth. The texture is smooth and digital with a slight grain. The composition leaves the central area relatively clear and uniform for text readability. Portrait format 4:5.
```

```
A soft abstract background with large overlapping translucent circles in muted pastel tones of lavender, mint, and pale rose against a clean white base. The shapes are concentrated toward the edges, leaving the center open and clear. Gentle diffused lighting with a calm, modern aesthetic. 4:5 portrait format.
```

**테마 장면 배경**

```
A dreamy, slightly out-of-focus photograph of a cozy library interior with warm ambient lighting from table lamps. Bookshelves line the background in soft bokeh. The foreground is intentionally empty with a smooth gradient into the blurred scene, creating a natural text overlay zone in the upper half. Shot with a 50mm lens at f/1.8 for maximum background blur. Warm, inviting color tones. 4:5 portrait format.
```

---

### 헤더 및 배너 이미지 (16:9 또는 3:2)

카드뉴스 시리즈의 표지나 상단 배너로 사용하는 와이드 포맷 이미지.

**와이드 장면**

```
A panoramic illustration of a vibrant cityscape at golden hour, with warm sunlight reflecting off modern glass buildings. The left third of the composition features the detailed city scene, while the right two-thirds transitions into a soft gradient of warm amber tones, providing clean space for a title and subtitle. Modern editorial illustration style with clean lines and rich color. 16:9 landscape format.
```

```
A wide establishing shot of a peaceful mountain landscape at dawn, with layers of misty blue mountains receding into the distance. The scene is composed with the mountain peaks on the left side and an expansive gradient sky on the right, creating natural text placement area. Soft pastel tones of blue, lavender, and warm pink. Photorealistic style with dreamy atmosphere. 3:2 landscape format.
```

**파노라믹 일러스트레이션**

```
A wide panoramic flat illustration of a connected digital ecosystem, showing tiny isometric buildings, data streams, and people interacting with floating screens, all arranged along a gentle horizontal S-curve. The style uses a cohesive palette of teal, white, and soft coral with clean vector shapes. Generous white space above and below the central band of activity. 16:9 format.
```

---

## 3. 스타일 일관성 전략

카드뉴스는 여러 장의 슬라이드로 구성되므로, 시리즈 전체에서 시각적 일관성을 유지하는 것이 중요하다.

### 첫 번째 카드에서 스타일 확립

시리즈의 첫 이미지를 생성할 때, 스타일을 최대한 구체적으로 정의한다. 이 정의를 "스타일 앵커"로 삼아 이후 모든 이미지에 동일하게 적용한다.

스타일 앵커에 포함해야 할 요소:
- 아트 스타일: flat vector, 3D clay, watercolor, editorial illustration 등
- 색상 팔레트: 구체적인 색상 2-4개 지정
- 외곽선 스타일: bold outlines, thin lines, no outlines
- 조명 방향과 품질: soft diffused, warm directional 등
- 전체적인 분위기: playful, professional, serene 등

### 레퍼런스 이미지 활용

Nano Banana는 최대 14개의 레퍼런스 이미지를 동시에 처리할 수 있다. 첫 번째 카드에서 만족스러운 이미지가 나오면, 해당 이미지를 레퍼런스로 첨부하고 역할을 명시한다.

```
Apply the exact same visual style, color palette, and illustration technique from the provided reference image. Create a new scene showing [새로운 장면 설명] while maintaining identical line weight, shading approach, and overall aesthetic.
```

레퍼런스 이미지에 역할을 할당하는 패턴:
- **Style/Aesthetic**: `Apply the color palette and illustration style from Image A`
- **Lighting/Atmosphere**: `Match the lighting and color temperature from Image B`
- **Identity/Character**: `Use Image C for the character's facial features and identity`

### "Maintain the same visual style" 패턴

후속 카드를 생성할 때 매번 사용하는 기본 패턴:

```
Maintain the exact same visual style as the reference image -- same line weight, same color palette, same shading technique, same level of detail. Only change the subject matter to [새로운 주제]. Keep the background treatment and overall composition approach consistent.
```

---

## 4. 배경 처리

### 흰색 배경 패턴 (rembg 또는 직접 사용)

아이콘이나 오브젝트를 생성한 뒤 배경을 제거(rembg)하여 사용하는 경우, 순수 흰색 배경에서 생성하면 배경 제거 품질이 가장 높다.

```
[오브젝트 설명]. The background must be pure white with no shadows, gradients, or textures. The object should be cleanly separated from the background with crisp edges. No text.
```

그림자가 필요한 경우(배경 제거 없이 사용):

```
[오브젝트 설명]. The background is pure white. A soft, subtle contact shadow sits directly beneath the object to give it grounding. No other shadows or elements in the background. No text.
```

### 솔리드 컬러 배경 (카드 팔레트 매칭)

카드뉴스의 브랜드 색상에 맞춰 배경 색상을 지정하는 패턴:

```
[오브젝트 설명]. The background is a solid, flat, uniform [색상명 + hex 코드 설명] color with no gradients, patterns, or textures. The object is centered with generous padding around it. No text.
```

예시:

```
A 3D clay-style icon of a rising bar chart with an upward arrow. The background is a solid, flat, uniform soft blue color matching a calm sky tone. The icon is centered with generous spacing. Soft ambient lighting. No text.
```

### 전체 배경 vs 투명 배경 선택 기준

**전체 배경(풀 배경) 사용**: 카드 슬라이드 전체를 차지하는 배경 이미지, 또는 특정 분위기를 전달해야 하는 일러스트레이션. 텍스트 영역을 프롬프트에서 미리 확보한다.

**흰색/솔리드 배경 (rembg 후 투명 처리) 사용**: 아이콘, 스티커, 개별 오브젝트 등 HTML/CSS 레이아웃 위에 자유롭게 배치해야 하는 요소. 순수 흰색 배경에서 생성 후 rembg로 배경을 제거한다.

---

## 5. 프롬프트 템플릿

아래 템플릿에서 `[PLACEHOLDER]` 부분을 실제 값으로 교체하여 사용한다.

### 아이콘 생성 템플릿

```
A [STYLE: 3D clay-style / flat design / kawaii-style] icon of [SUBJECT: 아이콘 주제와 구체적 설명], rendered with [RENDERING: soft rounded edges and matte texture / clean geometric shapes and bold outlines / bold clean outlines and simple cel-shading]. The color palette uses [COLORS: 구체적 색상 2-3개]. The background must be pure white. No text.
```

사용 예시:

```
A 3D clay-style icon of a padlock with a glowing keyhole, rendered with soft rounded edges and matte texture. The color palette uses deep navy blue and bright gold accents. The background must be pure white. No text.
```

### 컨셉 일러스트레이션 템플릿

```
A [STYLE: isometric / editorial / conceptual] illustration depicting [SCENE: 장면의 서술형 묘사]. The visual metaphor conveys the idea of [CONCEPT: 전달하려는 개념]. The style is [ART_STYLE: modern vector art with soft gradients / clean flat design with subtle depth / hand-drawn illustration with watercolor textures], using a cohesive palette of [COLORS: 색상 팔레트]. The composition leaves [SPACE: the upper third / the right half / generous margins] open as negative space for text overlay. No text in the image. [ASPECT: 1:1 square format / 4:5 portrait format].
```

사용 예시:

```
A conceptual illustration depicting a person climbing a staircase made of open books, each step revealing a different skill icon. The visual metaphor conveys the idea of continuous learning and professional growth. The style is modern vector art with soft gradients, using a cohesive palette of warm coral, deep teal, and cream. The composition leaves the upper third open as negative space for text overlay. No text in the image. 4:5 portrait format.
```

### 배경 이미지 템플릿

```
A [MOOD: minimalist / dreamy / vibrant / serene] background composition featuring [ELEMENT: 배경의 시각적 요소 설명], positioned in the [POSITION: bottom-right / edges / lower portion] of the frame. The [BACKGROUND: remaining area / upper two-thirds / center] is [TREATMENT: a vast empty off-white canvas / a smooth gradient from X to Y / clean and clear], creating significant negative space for text overlay covering at least [PERCENT: 60-70] percent of the canvas. [LIGHTING: Soft diffused lighting from the top left / Warm ambient glow / Even gentle illumination]. [ASPECT: 4:5 portrait format / 9:16 vertical format].
```

사용 예시:

```
A serene background composition featuring soft watercolor cherry blossom petals scattered in the bottom-right corner of the frame. The upper two-thirds is a smooth gradient from pale rose to clean white, creating significant negative space for text overlay covering at least 65 percent of the canvas. Soft diffused lighting from the top left. 4:5 portrait format.
```

### 스타일 레퍼런스 템플릿 (시리즈 일관성)

첫 번째 이미지 생성 후, 후속 이미지에 레퍼런스를 첨부하며 사용:

```
Using the provided reference image as the definitive style guide, create a new illustration showing [NEW_SCENE: 새로운 장면 설명]. Match exactly the following from the reference: the illustration technique, line weight, shading style, color palette, level of detail, and background treatment. The only change should be the subject matter. [ASPECT: 동일 비율 유지].
```

사용 예시:

```
Using the provided reference image as the definitive style guide, create a new illustration showing a team of three people collaborating around a holographic dashboard with floating data charts. Match exactly the following from the reference: the illustration technique, line weight, shading style, color palette, level of detail, and background treatment. The only change should be the subject matter. 1:1 square format.
```

### 이미지 수정 템플릿 (정교화)

생성된 이미지가 대체로 만족스럽지만 일부 조정이 필요할 때:

**색상 변경**:
```
Keep everything identical but change the color of [TARGET: 대상 요소] from [CURRENT: 현재 색상] to [NEW: 새 색상]. Preserve all other elements exactly as they are, including the lighting, composition, and style.
```

**배경 교체**:
```
Maintain the subject perfectly but replace the background with [NEW_BG: 새로운 배경 설명]. Ensure the subject's edges, lighting, and shadows integrate naturally with the new background.
```

**요소 추가**:
```
Add [ELEMENT: 추가할 요소의 상세 설명] to the [POSITION: 위치]. Ensure the new element matches the existing lighting, perspective, and visual style. Keep everything else exactly the same.
```

**요소 제거**:
```
Remove the [TARGET: 제거할 요소] from the scene and fill the area naturally with the surrounding background. Keep everything else exactly the same, preserving the original style, lighting, and composition.
```

**분위기 조정**:
```
Keep everything identical but adjust the overall mood to be [MOOD: warmer / cooler / more dramatic / brighter]. [SPECIFIC: Add warm golden hour lighting from the right / Shift the color temperature toward cool blue tones / Increase the contrast and deepen the shadows]. Preserve the composition and all objects exactly as they are.
```

---

## 6. 흔한 문제와 해결법

### 텍스트가 정확하지 않음

이미지에 텍스트를 포함해야 하는 경우(카드뉴스에서는 거의 없지만 표지 등에서 필요할 수 있다):
- 텍스트를 큰따옴표로 감싼다: `with the text "Hello" in the center`
- 3-5단어 이내로 제한한다
- 폰트를 설명적으로 기술한다: `clean bold sans-serif` (특정 폰트명 사용 금지)
- Nano Banana Pro (Gemini 3 Pro Image)를 사용하면 텍스트 렌더링 품질이 더 높다

### 구도가 의도와 다름

- 명시적 샷 타입을 포함한다: close-up, medium shot, wide shot
- 카메라 앵글을 지정한다: eye level, slightly elevated 45-degree angle, top-down
- 오브젝트의 프레임 내 위치를 구체적으로 기술한다: `positioned in the bottom-right corner of the frame`
- 공간 관계를 서술한다: `the icon is centered with generous padding on all sides`

### 조명이 기대와 다름

- 빛의 방향을 명시한다: `soft lighting from the top-left`
- 빛의 품질을 지정한다: `soft diffused light`, `hard directional light`
- 구체적 시간대를 활용한다: `golden hour warmth`, `cool overcast daylight`
- 조명 셋업을 설명한다: `three-point softbox setup`, `rim lighting from behind`

### 반복 생성 시 일관성 부족

- 재생성 대신 대화형 수정(multi-turn editing)을 사용한다
- 성공한 결과물을 레퍼런스 이미지로 첨부한다
- 스타일 정의를 가능한 한 기술적이고 구체적으로 작성한다
- 동일한 스타일 앵커 문구를 모든 후속 프롬프트에 포함한다

### 배경이 깔끔하지 않음 (rembg용)

- `The background must be pure white`를 반드시 포함한다
- `with no shadows, gradients, or textures on the background`를 추가한다
- `cleanly separated from the background with crisp edges`를 명시한다
- 그래도 해결되지 않으면: `isolated object on a seamless pure white studio backdrop, product photography lighting`

### 일러스트가 너무 복잡하거나 혼잡함

- 구조화 프롬프트 형식을 사용하여 컴포넌트를 명시한다
- 화이트 스페이스를 명시적으로 확보한다: `allocate at least 30 percent of the canvas to white space`
- 제약조건을 추가한다: `clean composition with minimal elements`, `no overlapping objects`
- 단, 제약조건은 2-3개 이내로 유지한다 (너무 많으면 모델의 창의성을 제한함)

### 수정 시 의도치 않은 변경 발생

- `Keep everything else exactly the same`을 반드시 포함한다
- 변경 대상을 구체적으로 지목한다: `change only the background color`, `modify only the icon in the center`
- 보존할 요소를 명시한다: `preserving the original style, lighting, and composition`
- 한 번에 하나의 변경만 요청한다 (여러 변경을 동시에 요청하면 의도치 않은 결과 발생 가능)

---

## 부록: 카드뉴스 작업에서 자주 쓰는 품질 키워드 모음

아래 키워드들은 반복적으로 좋은 결과를 만드는 것으로 검증된 것들이다. 프롬프트의 적절한 위치에 삽입한다.

**일러스트레이션 품질**: `clean composition`, `crisp edges`, `cohesive color palette`, `soft ambient occlusion`, `gentle shadows`

**배경 관련**: `clean background`, `pure white background`, `seamless gradient`, `significant negative space`, `ample space for text overlay`

**스타일 관련**: `flat design`, `vector art`, `3D clay style`, `soft matte texture`, `bold clean outlines`, `simple cel-shading`, `modern editorial illustration`

**분위기 관련**: `soft natural light`, `warm inviting tones`, `calm and professional`, `playful and approachable`, `serene and minimal`

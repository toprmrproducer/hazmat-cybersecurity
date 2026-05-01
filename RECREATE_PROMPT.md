# HAZMAT CYBERSECURITY — Complete Recreate Prompt

Build a complete, single-file (`index.html`) dark-mode cybersecurity SaaS landing page called **HazMat Cybersecurity** with an interactive 3D hero model, liquid glass UI, premium typography, and animated sections. Everything — HTML, CSS, and JavaScript — lives in one file. No build tools, no frameworks, no npm.

---

## TECH STACK

- **Pure HTML + CSS + vanilla JS** — single `index.html` file, no build tools
- **Three.js `0.162.0`** via importmap from `cdn.jsdelivr.net`
- **Three.js add-ons**: `GLTFLoader`, `EffectComposer`, `RenderPass`, `UnrealBloomPass`, `ShaderPass`, `VignetteShader`
- **Two separate Three.js renderers**: one for the hero fullscreen canvas, one for a second smaller canvas inside the "Threat Intel" section
- **No React, no Tailwind, no bundler** — everything inline

```html
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.162.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.162.0/examples/jsm/"
  }
}
</script>
```

---

## FONTS

Load via `<link>` in `<head>`:

```html
<link href="https://api.fontshare.com/v2/css?f[]=clash-display@200,300,400,500,600,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
```

CSS variables:
```css
--font-display: 'Clash Display', sans-serif;   /* headings, numbers, logo */
--font-ui:      'Inter', sans-serif;            /* body, buttons, nav */
--font-mono:    'JetBrains Mono', monospace;    /* labels, eyebrows, tags */
```

Apply globally:
```css
html, body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}
```

---

## COLOR PALETTE

- **Background**: `#000000` pure black
- **Primary accent**: `#ffcc00` gold
- **Secondary accent**: `#ff4444` red (danger/critical)
- **Tertiary**: `#ff8800` orange (high severity)
- **Success**: `#5dff8c` green (live status)
- **Text primary**: `#ffffff`
- **Text muted**: `rgba(255,255,255,0.5)`
- **Text dimmer**: `rgba(255,255,255,0.35)`
- **Borders**: `rgba(255,255,255,0.08)` default, `rgba(255,204,0,0.35)` on hover
- **Custom scrollbar**: 5px width, `#ffcc00` thumb, `#000` track
- **Selection highlight**: `rgba(255,204,0,0.3)` background

---

## GLOBAL DESIGN SYSTEM: LIQUID GLASS CARDS

The `.glass` class is the core UI primitive. Apply it to any card-like element:

```css
.glass {
  position: relative;
  isolation: isolate;
  background:
    radial-gradient(circle at top left, rgba(255,255,255,0.055) 0%, transparent 55%),
    linear-gradient(145deg, rgba(255,255,255,0.045) 0%, rgba(255,255,255,0.015) 100%);
  border: 1px solid rgba(255,255,255,0.09);
  backdrop-filter: blur(22px) saturate(185%);
  -webkit-backdrop-filter: blur(22px) saturate(185%);
  border-radius: 10px;
  box-shadow:
    inset 1px 1px 1px 0 rgba(255,255,255,0.14),
    inset -1px -1px 1px 0 rgba(255,255,255,0.04),
    inset 0 0 24px rgba(255,255,255,0.015),
    0 4px 10px rgba(0,0,0,0.35),
    0 0 30px rgba(255,255,255,0.03);
  transition: background 0.4s ease, border-color 0.4s ease,
              transform 0.4s cubic-bezier(.3,1.2,.4,1), box-shadow 0.4s ease;
}
/* Top refraction edge highlight */
.glass::before {
  content: '';
  position: absolute;
  top: 0; left: 14%; right: 14%; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.55), transparent);
  pointer-events: none; z-index: 1; opacity: 0.9;
}
/* Diagonal sheen on hover */
.glass::after {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(125deg, transparent 40%, rgba(255,255,255,0.035) 50%, transparent 60%);
  border-radius: inherit; pointer-events: none; z-index: 1;
  opacity: 0; transition: opacity 0.5s ease;
}
.glass:hover {
  background:
    radial-gradient(circle at top left, rgba(255,204,0,0.06) 0%, transparent 55%),
    linear-gradient(145deg, rgba(255,204,0,0.035) 0%, rgba(255,255,255,0.02) 100%);
  border-color: rgba(255,204,0,0.35);
  transform: translateY(-4px);
  box-shadow:
    inset 1px 1px 1px 0 rgba(255,255,255,0.18),
    inset -1px -1px 1px 0 rgba(255,255,255,0.06),
    inset 0 0 30px rgba(255,204,0,0.04),
    0 24px 50px rgba(0,0,0,0.55),
    0 0 42px rgba(255,204,0,0.18);
}
.glass:hover::after { opacity: 1; }
.glass > * { position: relative; z-index: 2; }
```

Also add `.feat-framed` to cards that should show corner bracket highlights on hover:
```css
.feat-framed { position: relative; }
.feat-framed::before, .feat-framed::after {
  content: ''; position: absolute;
  width: 13px; height: 13px;
  border-color: rgba(255,204,0,0.55); border-style: solid;
  transition: opacity 0.3s ease; opacity: 0;
}
.feat-framed::before { top: -1px; left: -1px;  border-width: 2px 0 0 2px; }
.feat-framed::after  { top: -1px; right: -1px; border-width: 2px 2px 0 0; }
.feat-framed:hover::before, .feat-framed:hover::after { opacity: 1; }
```

---

## FILM GRAIN OVERLAY

Add this fixed div as the very first child of `<body>` for a premium tactile feel:

```html
<div class="grain"></div>
```

```css
.grain {
  pointer-events: none;
  position: fixed; inset: 0;
  z-index: 300;
  opacity: 0.06;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml;utf8,<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='0.9'/></svg>");
}
```

---

## LOADING SCREEN

Full-screen black overlay with spinning ring and mono text. Fades out with `opacity: 0` and then `display: none` once the 3D model finishes loading:

```html
<div id="loading-screen">
  <div class="spinner"></div>
  <p class="loader-text">Initializing</p>
</div>
```

Spinner: 36px circle, 1.5px gold border, top transparent, `spin` keyframe animation.

---

## SECTION 1: HERO (fullscreen 3D)

### Layout
`#hero` is `100vh`, `overflow: hidden`, `position: relative`, `background: #000`.

A Three.js `<canvas>` fills it absolutely (`position: absolute; inset: 0; z-index: 1`).

A `#ui-overlay` sits on top at `z-index: 10`.

### Left content block (`#hero-content`)
- Positioned `left: 36px`, `top: 50%`, `transform: translateY(-50%)`, `max-width: 420px`
- **Eyebrow**: JetBrains Mono, 10px, 5px letter-spacing, gold, uppercase. Text: "Est. 2025 — Cyber Division"
- **H1**: Clash Display, `clamp(36px, 4.2vw, 64px)`, weight 500, line-height 1.04, letter-spacing -2px. Text: "Stop the Breach / Before It / Even Starts." — wrap the last line in `<em>` with a gold gradient:
  ```css
  .hero-heading em {
    font-style: normal;
    background: linear-gradient(90deg, #ffcc00 0%, #ffe566 45%, #ffcc00 100%);
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 32px rgba(255,204,0,0.4));
  }
  ```
- **Sub-paragraph**: Inter, 16px, weight 400, line-height 1.75, `rgba(255,255,255,0.62)`. Text: "AI-powered containment that operates at machine speed. Real-time threat neutralisation. Zero tolerance for breach."
- **Two CTA buttons** side by side:
  - Primary: gold background (`#ffcc00`), black text, no border-radius, uppercase Inter 11px weight 500, 3.5px letter-spacing, `padding: 15px 34px`. Hover: white background, lifts 2px.
  - Ghost: `backdrop-filter: blur(14px)`, `rgba(255,255,255,0.06)` background, `rgba(255,255,255,0.22)` border, white text. Same size as primary. Hover: brighter border.
- **Tags row**: pill badges in JetBrains Mono 9px, 3px letter-spacing, `rgba(255,255,255,0.35)`, `border: 1px solid rgba(255,255,255,0.1)`, `border-radius: 100px`, blurred. Badges: "SOC Teams", "Enterprise", "Zero-day", "MSSP"

### Right HUD cards (`#hero-cards`)
- Positioned `right: 36px`, `top: 50%`, `transform: translateY(-50%)`, `width: 260px`, `flex-direction: column`, `gap: 14px`
- Three `.hcard.glass` cards. Hide on `max-width: 960px`.
- Card 1: Label "Active Threat Level", Value "CRITICAL" (Clash Display 32px w500), animated bar (red, pulses between 86%↔78%), note "85% severity index"
- Card 2: Label "Containments Today", Value "2,847", note with green blinking dot + "+12 neutralised now"
- Card 3: Label "Avg Response Time", Value "0.003s", note "Machine-speed containment"

### Bottom bar (`#bottom-bar`)
- Positioned `bottom: 32px`, spanning full width
- Left: circular play button (42px, glass border) + "Play Trailer" label
- Center: three tab labels — "Training 01" (gold), "Gallery 02" (red), "Collections 03" (white muted)

---

## 3D HERO SCENE (Three.js)

This is the main Three.js scene rendered onto the hero's fullscreen canvas.

### Setup
```js
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(w, h);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.3;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.shadowMap.enabled = true;
```

Camera: `PerspectiveCamera(32, aspect, 0.1, 100)`, positioned at `(0.5, 0.5, 5.5)`, looking at `(0.8, 0.6, 0)`.

### Post-processing
Chain: `RenderPass → UnrealBloomPass → ShaderPass(VignetteShader)`.
- Bloom: `strength: 0.55`, `radius: 0.42`, `threshold: 0.38`
- Vignette: `offset: 1.0`, `darkness: 1.35`

### Lighting
```js
const ambient = new THREE.AmbientLight(0x0a0a14, 0.5);
const key = new THREE.DirectionalLight(0xfff0cc, 2.8); // top-left
const rim = new THREE.DirectionalLight(0xffcc00, 1.5); // back-right
const fill = new THREE.DirectionalLight(0x334466, 0.8); // front-right
const underlight = new THREE.PointLight(0xffcc00, 1.2, 6); // below
```

### Model loading
Load GLB from URL:
```
https://raw.githubusercontent.com/toprmrproducer/3dasset/main/Hazmat_Suit_Character.glb
```

After loading:
1. Call `geometry.computeBoundingBox()` and `computeBoundingSphere()` on all SkinnedMesh children
2. Compute bounding box and scale model so height = `TARGET_H = 5.5` units
3. Place feet at `FEET_Y = -4.0` using `model.position.y += (FEET_Y - bbox.min.y)`
4. Center X/Z using `model.position.x -= center.x`, `model.position.z -= center.z`
5. Set `CHAR_ROT = 0.3`, `model.rotation.y = CHAR_ROT`
6. Store `modelRestY = model.position.y`

After load, find bones by name:
```js
model.traverse(obj => {
  if (obj.isBone) {
    const n = obj.name.toLowerCase();
    if (obj.name === 'Head') headBone = obj;
    if (obj.name === 'neck') neckBone = obj;
    if (!headBone && n.includes('head')) headBone = obj;
    if (!neckBone && n.includes('neck')) neckBone = obj;
  }
});
// Reset to chin-down default pose
if (headBone) headBone.rotation.set(0.38, 0, 0, 'YXZ');
if (neckBone) neckBone.rotation.set(0.16, 0, 0, 'YXZ');
```

Set environment map using `THREE.RGBELoader` or a PMREMGenerator with a neutral warm environment.

### Mouse tracking
```js
let mouseX = 0, mouseY = 0, mouseLastMove = performance.now();
window.addEventListener('mousemove', e => {
  mouseX = (e.clientX / window.innerWidth)  * 2 - 1;  // -1 to +1
  mouseY = (e.clientY / window.innerHeight) * 2 - 1;  // -1 to +1
  mouseLastMove = performance.now();
});
```

### Animate loop
```js
let trackingStrength = 0;
let idleTargetY = 0, idleTargetX = 0, idleChangeTimer = 0;

function animate() {
  requestAnimationFrame(animate);

  // Gentle body float and yaw
  model.position.y = modelRestY + Math.sin(t * 0.6) * 0.006;
  const bodyTarget = CHAR_ROT + mouseX * 0.04 * trackingStrength + Math.sin(t * 0.4) * 0.020;
  model.rotation.y = THREE.MathUtils.lerp(model.rotation.y, bodyTarget, 0.025);

  // Idle head drift (random slow wander)
  idleChangeTimer -= 0.016;
  if (idleChangeTimer <= 0) {
    idleTargetY = (Math.random() - 0.5) * 0.12;
    idleTargetX = (Math.random() - 0.5) * 0.05;
    idleChangeTimer = 4.0 + Math.random() * 3.0;
  }
  const idleY = THREE.MathUtils.lerp(headBone.rotation.y, idleTargetY, 0.008);
  const idleX = THREE.MathUtils.lerp(headBone.rotation.x, idleTargetX, 0.008);

  // Zone-based tracking fade
  const inZone = mouseX > -0.55 && mouseX < 0.78;
  const recentMove = (performance.now() - mouseLastMove) < 3000;
  trackingStrength = THREE.MathUtils.lerp(trackingStrength,
    (inZone && recentMove) ? 1.0 : 0.0, 0.08);

  // Head tracking with lateral z-tilt (key to organic feel)
  headBone.rotation.order = 'YXZ';
  neckBone.rotation.order = 'YXZ';

  const tY = mouseX * 0.62 * trackingStrength;
  const tX = 0.34 + mouseY * -0.45 * trackingStrength;  // 0.34 = chin-down default
  const tZ = mouseX * -0.12 * trackingStrength;          // lateral tilt

  const blendedTY = THREE.MathUtils.clamp(tY * 0.85 + idleY * 0.15, -0.62, 0.62);
  const blendedTX = THREE.MathUtils.clamp(tX * 0.85 + idleX * 0.15, -0.14, 0.68);
  const blendedTZ = THREE.MathUtils.clamp(tZ * 0.85, -0.12, 0.12);

  headBone.rotation.y = THREE.MathUtils.lerp(headBone.rotation.y, blendedTY, 0.13);
  headBone.rotation.x = THREE.MathUtils.lerp(headBone.rotation.x, blendedTX, 0.13);
  headBone.rotation.z = THREE.MathUtils.lerp(headBone.rotation.z, blendedTZ, 0.10);
  neckBone.rotation.y = THREE.MathUtils.lerp(neckBone.rotation.y, blendedTY * 0.42, 0.13);
  neckBone.rotation.x = THREE.MathUtils.lerp(neckBone.rotation.x, blendedTX * 0.42, 0.13);
  neckBone.rotation.z = THREE.MathUtils.lerp(neckBone.rotation.z, blendedTZ * 0.50, 0.10);

  // Camera drift with mouse
  camera.position.x = THREE.MathUtils.lerp(camera.position.x, 0.5 + mouseX * 0.15, 0.018);
  camera.position.y = THREE.MathUtils.lerp(camera.position.y, 0.5 + mouseY * -0.08, 0.018);
  camera.lookAt(0.8, 0.6, 0);

  composer.render();
}
```

**CRITICAL NOTE on SkinnedMesh bounding box**: Always call `geometry.computeBoundingBox()` on SkinnedMesh children before using `Box3.setFromObject()`. Without it, the bounding box returns zero and model positioning breaks.

---

## SECTION 2: THREAT STATS (Live Intelligence)

`#threat-stats` section with dot-grid background (`radial-gradient` 1px dots every 38px).

Eyebrow: "Live Intelligence"
Heading: "Numbers that define our containment protocol."

4-column grid of `.glass.stat-card.feat-framed` cards. Each card has:
- **Header row**: left = animated "LIVE" pulse indicator (6px gold dot with expanding ring-shadow animation + "LIVE" text in JetBrains Mono 9px), right = themed SVG icon (16px, gold stroke, rotates on hover)
- **Giant number**: Clash Display 64px, weight 300, letter-spacing -3px, `font-variant-numeric: tabular-nums`, gradient text `(#ffffff → rgba(255,255,255,0.65))` via background-clip. Animated count-up on scroll via IntersectionObserver.
- **Label**: 13.5px, weight 500, white
- **Desc**: JetBrains Mono 11px, muted
- **Progress bar** (`--progress: XX%`): 2px tall, `rgba(255,255,255,0.07)` track, gold→orange gradient fill with glow, animated grow from 0 on load, periodic shine sweep

Stats: `99.7% Threat Detection Rate`, `0.3ms Response Time`, `4.2M+ Threats Contained`, `247 Nations Protected`

Count-up animation (JS): observe each `.stat-number` with IntersectionObserver, then animate from 0 to `data-count` over ~1.4s with `requestAnimationFrame`. Respect `data-int="1"` for integer display, `data-suffix` for appending units.

---

## SECTION 3: HOW IT WORKS (Protocol)

`#how-it-works` section.

Two-column grid: left `hiw-intro` (sticky), right `hiw-steps`.

Left: eyebrow "Protocol", heading "Three steps. / Zero breach.", body paragraph, 60px gold divider line.

Right: 3 steps vertically, each with:
- Circular icon (42px, gold border, `border-radius: 50%`, black background, glow on hover)
- Vertical connecting line between icons (1px `rgba(255,255,255,0.1)` on `.hiw-steps::before`)
- Step tag: JetBrains Mono 11px uppercase "STEP 01 — DETECT"
- H3: Clash Display 26px weight 500 letter-spacing -0.5px
- Paragraph: Inter 15px line-height 1.75

Steps: "AI scans every vector simultaneously" / "Classify. Prioritize. Understand intent." / "Neutralize before propagation."

---

## SECTION 4: THREAT INTEL (Live Feed) — SECOND 3D SCENE

`#threat-intel` has `overflow: hidden`, animated colored orbs in background (blurred radial circles: gold top-left, red bottom-right, blue mid-right), a grid overlay (`60px × 60px` 1px lines at 3% opacity).

Two-column split: left = text + intel cards, right = 3D sentinel canvas.

### Intel Cards (2×2 grid)
Each `.glass.intel-card` has: icon + title + region + severity badge + animated progress bar.

4 threats: APT Group Activity (CRITICAL, red), DDoS Surge Detected (HIGH, orange), Phishing Campaign (MEDIUM, gold), Zero-Day Signature (CRITICAL, red).

Severity badges: JetBrains Mono 9.5px, 3px letter-spacing, bordered, colored matching severity.

### Sentinel 3D Column
A 380×560px glass panel on the right with canvas `id="sentinel-canvas"`, an inset glow overlay, and a bottom badge "☢ SENTINEL UNIT ACTIVE".

The sentinel uses a SECOND completely independent Three.js scene:

**Model URL:**
```
https://raw.githubusercontent.com/toprmrproducer/3dasset/main/Meshy_AI_Containment_Sentinel_biped_Animation_Walking_withSkin.glb
```

**Setup:**
```js
function initSentinelScene() {
  const sentCanvas = document.getElementById('sentinel-canvas');
  const sentScene = new THREE.Scene();
  const sentCamera = new THREE.PerspectiveCamera(50, 1, 0.1, 50);
  sentCamera.position.set(0, 1.2, 5.5);
  sentCamera.lookAt(0, 1.2, 0);

  const sentRenderer = new THREE.WebGLRenderer({ canvas: sentCanvas, antialias: true, alpha: true });
  sentRenderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  sentRenderer.toneMapping = THREE.ACESFilmicToneMapping;
  sentRenderer.toneMappingExposure = 1.1;
  sentRenderer.outputColorSpace = THREE.SRGBColorSpace;

  // Resize function
  function resizeSentinel() {
    const w = sentCanvas.offsetWidth || 380;
    const h = sentCanvas.offsetHeight || 560;
    sentCamera.aspect = w / h;
    sentCamera.updateProjectionMatrix();
    sentRenderer.setSize(w, h, false);
  }
  setTimeout(resizeSentinel, 0);
  new ResizeObserver(resizeSentinel).observe(sentCanvas);

  // Lights
  const sk = new THREE.DirectionalLight(0xfff4e0, 1.8);
  sk.position.set(-2, 3, 3);
  sentScene.add(sk);
  // + fill light from right, ambient, spot from front

  // Model load — CRITICAL: call computeBoundingBox on SkinnedMesh FIRST
  const loader = new GLTFLoader();
  loader.load(MODEL_URL, gltf => {
    const sentModel = gltf.scene;
    sentScene.add(sentModel);

    // Compute geometry bounding boxes (required for SkinnedMesh setFromObject accuracy)
    sentModel.traverse(obj => {
      if (obj.isSkinnedMesh && obj.geometry) {
        obj.geometry.computeBoundingBox();
        obj.geometry.computeBoundingSphere();
      }
    });
    sentModel.updateMatrixWorld(true);

    const rb = new THREE.Box3().setFromObject(sentModel);
    const SENT_TARGET_H = 2.4;
    const sc = SENT_TARGET_H / rb.getSize(new THREE.Vector3()).y;
    sentModel.scale.setScalar(sc);
    sentModel.updateMatrixWorld(true);

    const sb = new THREE.Box3().setFromObject(sentModel);
    const sbC = sb.getCenter(new THREE.Vector3());
    sentModel.position.x -= sbC.x;
    sentModel.position.y -= sb.min.y;  // feet at y=0
    sentModel.position.z -= sbC.z;

    const sentMidY = SENT_TARGET_H / 2; // 1.2
    sentCamera.position.set(0, sentMidY, 5.5);
    sentCamera.lookAt(0, sentMidY, 0);
    sentRestY = sentModel.position.y;
  });

  // Animate — only render when visible (IntersectionObserver)
  function sentAnimate() {
    requestAnimationFrame(sentAnimate);
    if (!sentVisible || !sentModel) return;
    const t = sentClock.getElapsedTime();
    sentModel.position.y = sentRestY + Math.sin(t * 0.55) * 0.007;
    sentModel.rotation.y = 0.3 + Math.sin(t * 0.38) * 0.025;
    // Head bone: gentle idle looking down toward viewer
    if (sentHead) {
      sentHead.rotation.order = 'YXZ';
      sentHead.rotation.y = lerp(sentHead.rotation.y, Math.sin(t * 0.43) * 0.18, 0.03);
      sentHead.rotation.x = lerp(sentHead.rotation.x, 0.22 + Math.sin(t * 0.27) * 0.05, 0.03);
    }
    sentCamera.lookAt(0, sentModel.position.y + sentMidY, 0);
    sentRenderer.render(sentScene, sentCamera);
  }
}
```

---

## SECTION 5: CAPABILITIES (Features)

`#features` section.

3-column masonry-style grid of `.glass.feature-card.feat-framed` cards. Some cards `span-2` (`grid-column: span 2`).

Each card: gold SVG icon (24px, stroke-only), H3 in Clash Display 20px weight 400, paragraph in 13.5px.

Feature cards:
1. (span-2) Omniscient Visibility — eye icon
2. Neural Threat Engine — lightning icon
3. Autonomous Response — shield + check icon
4. Identity Fabric — fingerprint icon
5. (span-2) Mesh Deception Grid — network nodes icon
6. Breach Guarantee — microphone/voice icon

---

## SECTION 6: TESTIMONIALS (Field Reports)

3-column grid of `.glass.testimonial-card`. Each card:
- Large opening quote `"` in Clash Display 56px gold
- Quote text 14px line-height 1.7
- Author row: 40px avatar circle (gold border, initials in JetBrains Mono), name + role
- Min-height 320px

3 testimonials from fake customers (CISO, VP Security, Director of Infrastructure).

---

## TRUSTED BY MARQUEE

Full-width scrolling marquee. Duplicate items for seamless loop:

```css
.marquee-track {
  display: flex; gap: 80px; width: max-content;
  animation: marquee-scroll 35s linear infinite;
}
@keyframes marquee-scroll {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
```

Fade edges with `mask-image: linear-gradient(90deg, transparent, #000 10%, #000 90%, transparent)`.

Items in Clash Display 24px weight 400, hover turns gold. Companies: APEX FINANCIAL, NOVATECH, VAULT CORP, HELIOS DEFENSE, KRONOS LABS, ORBITAL SYSTEMS, MERIDIAN BANK, NEXUS BIOTECH.

---

## SECTION 7: PRICING (Deploy)

3-column grid of `.glass.price-card`. Middle card (`.highlight`) has:
- `background: rgba(255,204,0,0.06)`, `border-color: rgba(255,204,0,0.4)`, `transform: scale(1.03)`
- Highlighted SVG check icons in gold

Tiers:
- **Sentinel** — $2,400/mo (500 endpoints, detection, containment, SOC dashboard, API)
- **Containment** — $8,900/mo (unlimited, neural engine, zero-day, breach guarantee, dedicated analyst) — HIGHLIGHTED
- **Classified** — Custom (air-gapped, nation-state, source code, 99.999% SLA)

---

## SECTION 8: FINAL CTA

`#final-cta` — centered text, `padding: 180px 36px`, radial gold glow in center background.

Eyebrow: JetBrains Mono "Ready to contain"
H1: Clash Display `clamp(48px, 6vw, 88px)` weight 600, letter-spacing -3px. "Stop the next breach / before it starts." — `<em>starts.</em>` in gold.
Sub: Inter 16px
Two buttons: primary (gold, black text) + secondary (ghost border)

---

## SECTION 9: FOOTER

4-column grid: brand column (2fr) + 3 link columns (1fr each).

Brand: HAZMAT logo in JetBrains Mono 14px 8px tracking, description paragraph.
Columns: Product, Company, Legal — links in 13px.
Footer bottom bar: copyright left, "SYSTEM STATUS: OPERATIONAL" (green) right.

---

## NAVIGATION (Liquid Glass Nav)

Fixed at `top: 16px`, centered, pill shape (`border-radius: 100px`), `width: calc(100% - 32px)`, `max-width: 1200px`, height 62px.

```css
#liquid-nav {
  background: rgba(10,10,12,0.55);
  backdrop-filter: blur(30px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 10px 40px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.06);
  transition: background 0.4s ease, border-color 0.4s ease;
}
#liquid-nav.scrolled {
  background: rgba(10,10,12,0.85);
  border-color: rgba(255,204,0,0.18);
}
```

Logo: ☢ nuclear emoji (gold, drop-shadow glow) + "HAZMAT" in Clash Display 16px weight 600, 7px letter-spacing.

Nav links: Inter 11px, 2.5px letter-spacing, uppercase. Active link is gold with a 4px gold dot below it (`::after`).

Scrollspy: `window.addEventListener('scroll', ...)` + `IntersectionObserver` on each section to update `.active` class.

Right side: Login / Register text buttons. Register is gold.

---

## SECTION DOT-GRID BACKGROUND

Every `.section` has a dot-grid overlay:

```css
.section::before {
  content: '';
  position: absolute; inset: 0; z-index: 0; pointer-events: none;
  background-image: radial-gradient(rgba(255,255,255,0.035) 1px, transparent 1px);
  background-size: 38px 38px;
}
```

---

## SCROLL REVEAL ANIMATION

```css
.reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.9s ease, transform 0.9s ease; }
.reveal.visible { opacity: 1; transform: translateY(0); }
```

```js
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObserver.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
```

---

## COUNT-UP ANIMATION (Stat Numbers)

Triggers when stat cards scroll into view:

```js
const countObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const el = entry.target;
    const target = parseFloat(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const isInt = el.dataset.int === '1';
    const duration = 1400;
    const start = performance.now();
    function tick(now) {
      const t = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - t, 3);
      const val = target * eased;
      el.textContent = (isInt ? Math.round(val) : val.toFixed(1)) + suffix;
      if (t < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
    countObserver.unobserve(el);
  });
}, { threshold: 0.5 });
document.querySelectorAll('.stat-number[data-count]').forEach(el => countObserver.observe(el));
```

---

## SCAN LINE ANIMATION

`#threat-stats` section has a 1px horizontal line that travels from top to bottom of the section:

```css
#threat-stats .scan-line {
  position: absolute; left: 0; right: 0; top: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,204,0,0.45), transparent);
  animation: scan 6s linear infinite;
  pointer-events: none;
}
@keyframes scan {
  0%   { transform: translateY(0); }
  100% { transform: translateY(100vh); }
}
```

---

## STAT CARD LIVE PULSE DOT

```css
.stat-pulse-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: #ffcc00;
  animation: stat-pulse 2s ease-in-out infinite;
}
@keyframes stat-pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(255,204,0,0.6); }
  50%       { box-shadow: 0 0 0 8px rgba(255,204,0,0); }
}
```

---

## STAT PROGRESS BAR ANIMATION

```css
.stat-progress::before {
  content: ''; position: absolute; left: 0; top: 0; bottom: 0;
  width: var(--progress, 85%);
  background: linear-gradient(90deg, #ffcc00, #ff9500);
  box-shadow: 0 0 12px rgba(255,204,0,0.6);
  animation: progress-grow 1.8s cubic-bezier(.2,.8,.2,1) both;
}
.stat-progress::after {
  /* periodic shine sweep */
  content: ''; position: absolute; top: 0; bottom: 0;
  left: var(--progress, 85%); width: 40px;
  background: linear-gradient(90deg, rgba(255,204,0,0.5), transparent);
  transform: translateX(-100%);
  animation: progress-shine 2.8s ease-in-out infinite 2s;
}
@keyframes progress-grow { from { width: 0; } }
@keyframes progress-shine {
  0%   { opacity: 0; transform: translateX(-100%); }
  50%  { opacity: 1; }
  100% { opacity: 0; transform: translateX(40px); }
}
```

---

## INTEL ORB BACKGROUND ANIMATION

```css
@keyframes orb-float {
  0%, 100% { transform: translate(0, 0) scale(1); }
  50%       { transform: translate(100px, 80px) scale(1.1); }
}
```

3 orbs with different sizes, colors (gold, red, blue), positions, durations (18s, 22s, 25s), and `animation-direction: reverse` on the second one.

---

## COMPLETE FILE STRUCTURE

Everything in a single `index.html`:

```
index.html
  <head>
    - meta tags (charset, viewport, cache-control no-cache)
    - title
    - font links (Fontshare + Google Fonts)
    - importmap for Three.js
    - <style> block (all CSS, ~950 lines)
  </head>
  <body>
    .grain (film overlay)
    #loading-screen
    #liquid-nav
    #hero (Three.js canvas + UI overlay)
    #threat-stats
    #how-it-works
    #threat-intel (with #sentinel-canvas)
    #features
    #testimonials
    #trusted-by
    #pricing
    #final-cta
    #site-footer
    <script type="module"> (all JS, ~400 lines)
      - Three.js hero scene
      - Head tracking + bone animation
      - Post-processing (bloom + vignette)
      - initSentinelScene() function
      - Nav scroll/spy
      - Scroll reveal observer
      - Count-up observer
  </body>
```

---

## KEY IMPLEMENTATION NOTES

1. **SkinnedMesh bounding box bug**: ALWAYS call `geometry.computeBoundingBox()` on all SkinnedMesh children before computing `Box3.setFromObject()`. Without this, Three.js returns zero-size bounds for skinned characters and your model won't be positioned correctly.

2. **Head tracking realism**: Add a lateral Z-tilt (`headBone.rotation.z = mouseX * -0.12 * trackingStrength`) — this makes the head cock slightly sideways as it turns, which is the single biggest factor in making tracking feel organic vs robotic.

3. **Tracking zone**: Only track when mouse is near the character. Define a zone (`mouseX > -0.55 && mouseX < 0.78`) and smoothly fade `trackingStrength` in/out via lerp (rate 0.08) so tracking starts/stops gracefully instead of snapping.

4. **Chin-down default**: In the walking animation's rest/bind pose, the head faces forward. Apply `headBone.rotation.set(0.38, 0, 0, 'YXZ')` immediately after finding the bone to force a chin-down default that reads naturally on screen.

5. **Sentinel visibility optimization**: Use IntersectionObserver to set a `sentVisible` flag, and gate the sentinel's `requestAnimationFrame` loop with `if (!sentVisible) return`. This prevents wasting GPU time when the section is off-screen.

6. **Sentinel camera**: After positioning the model with feet at y=0, set `sentMidY = SENT_TARGET_H / 2 = 1.2`. Place camera at `(0, sentMidY, 5.5)` and call `lookAt(0, sentMidY, 0)`. Update `lookAt` every frame to track the model's idle float.

7. **Glass on dark backgrounds**: The glass effect only reads as glass when there's content or texture behind it. In all-black sections, add the dot-grid (`::before` radial-gradient pattern) or use the intel orb colored glows in the background to give the blur something to work with.

8. **Single-file, no HMR**: Add `?v=XXXXX` query string when testing to bust browser cache during development.

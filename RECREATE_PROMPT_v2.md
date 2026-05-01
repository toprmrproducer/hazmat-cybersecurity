# HAZMAT CYBERSECURITY — MASTER RECREATE PROMPT (v2, 100% accurate)

Build a complete, single-file `index.html` dark-mode cybersecurity SaaS landing page called **HazMat Cybersecurity**.
Everything — HTML, CSS, JavaScript — lives in one file. No build tools, no npm, no frameworks.

---

## 1. FILE STRUCTURE

```
index.html
  <head>
    meta tags, font links, Three.js importmap, <style> (~970 lines)
  <body>
    .grain               ← fixed film-grain overlay
    #loading-screen      ← fullscreen black loader
    #liquid-nav          ← fixed pill navbar
    #hero                ← fullscreen Three.js canvas + UI overlay
    .section#threat-stats
    .section#how-it-works
    .section#threat-intel  ← contains #sentinel-canvas (2nd Three.js scene)
    .section#features
    .section#testimonials
    #trusted-by          ← infinite marquee
    .section#pricing
    #final-cta
    #site-footer
    <script type="module"> (~510 lines of JS)
```

---

## 2. HEAD / IMPORTS

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />
  <title>HazMat Cybersecurity — Neutralizing Cyber Threats Before They Spread</title>

  <!-- Clash Display (geometric, premium) via Fontshare -->
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@200,300,400,500,600,700&display=swap" rel="stylesheet">
  <!-- Inter (UI) + JetBrains Mono (technical labels) via Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">

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

## 3. CSS — ROOT VARIABLES & GLOBAL RESET

```css
:root {
  --font-display: 'Clash Display', sans-serif;
  --font-ui:      'Inter', sans-serif;
  --font-mono:    'JetBrains Mono', monospace;
}

*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

html, body {
  width: 100%; min-height: 100%;
  overflow-x: hidden; overflow-y: auto;
  background: #000000; font-family: var(--font-ui);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}
html { scroll-behavior: smooth; }
::selection { background: rgba(255,204,0,0.3); color: #fff; }
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #000; }
::-webkit-scrollbar-thumb { background: #ffcc00; border-radius: 3px; }
```

---

## 4. CSS — HERO SECTION

```css
#hero {
  position: relative; width: 100%; height: 100vh;
  overflow: hidden; background: #000;
}
#hero canvas {
  position: absolute; top: 0; left: 0;
  width: 100%; height: 100%;
  display: block; z-index: 1;
}
```

---

## 5. CSS — LOADING SCREEN

```css
#loading-screen {
  position: fixed; inset: 0; z-index: 100;
  background: #000000;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  transition: opacity 1.2s ease;
}
.spinner {
  width: 36px; height: 36px;
  border: 1.5px solid #ffcc00;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
.loader-text {
  font-family: var(--font-mono);
  font-size: 10px; font-weight: 400;
  letter-spacing: 6px; color: rgba(255,255,255,0.7);
  text-transform: uppercase; margin-top: 18px;
}
```

---

## 6. CSS — HERO OVERLAY & CONTENT

```css
#ui-overlay {
  position: absolute; inset: 0; z-index: 10;
  pointer-events: none;
}

/* ── TOP BAR (inside hero) ── */
#top-bar {
  position: absolute; top: 28px; left: 0; right: 0;
  padding: 0 36px;
  display: flex; align-items: center; justify-content: space-between;
}
.logo {
  font-family: var(--font-mono); font-size: 15px;
  font-weight: 500; letter-spacing: 8px;
  color: #ffffff; text-transform: uppercase;
}

/* ── HERO CONTENT BLOCK (left) ── */
#hero-content {
  position: absolute; left: 36px; top: 50%;
  transform: translateY(-50%);
  pointer-events: auto; z-index: 10;
  max-width: 420px; text-align: left;
}
.hero-eyebrow {
  font-family: var(--font-mono); font-size: 10px; font-weight: 400;
  letter-spacing: 5px; color: #ffcc00;
  text-transform: uppercase; margin-bottom: 20px; opacity: 0.85;
}
.hero-heading {
  font-family: var(--font-display);
  font-size: clamp(36px, 4.2vw, 64px);
  font-weight: 500; line-height: 1.04; letter-spacing: -2px;
  color: #ffffff; margin-bottom: 28px; text-transform: none;
}
/* Gold gradient on <em> inside heading — no font-style */
.hero-heading em {
  font-style: normal;
  background: linear-gradient(90deg, #ffcc00 0%, #ffe566 45%, #ffcc00 100%);
  -webkit-background-clip: text; background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 32px rgba(255,204,0,0.4));
}
.hero-sub {
  font-family: var(--font-ui); font-size: 16px; font-weight: 400;
  line-height: 1.75; color: rgba(255,255,255,0.62);
  letter-spacing: 0.1px; margin-bottom: 40px; max-width: 480px;
}

/* ── HERO CTA BUTTONS ── */
.hero-cta-row {
  display: flex; align-items: center; gap: 18px; flex-wrap: wrap;
}
.hero-cta {
  font-family: var(--font-ui); font-size: 11px; font-weight: 500;
  letter-spacing: 3.5px; text-transform: uppercase;
  color: #000; background: #ffcc00; border: 1px solid rgba(255,204,0,0.8);
  padding: 15px 34px; cursor: pointer; position: relative; overflow: hidden;
  box-shadow: 0 0 22px rgba(255,204,0,0.35), inset 0 1px 1px rgba(255,255,255,0.5);
  transition: all 0.3s ease;
}
.hero-cta::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.28) 0%, transparent 55%);
  pointer-events: none;
}
.hero-cta:hover {
  background: #fff; transform: translateY(-2px);
  box-shadow: 0 0 40px rgba(255,204,0,0.55), inset 0 1px 1px rgba(255,255,255,0.6);
}
.hero-cta-ghost {
  font-family: var(--font-ui); font-size: 11px; font-weight: 400;
  letter-spacing: 3.5px; text-transform: uppercase;
  color: rgba(255,255,255,0.75); position: relative; overflow: hidden;
  background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.22);
  padding: 15px 28px; cursor: pointer;
  backdrop-filter: blur(14px) saturate(160%);
  -webkit-backdrop-filter: blur(14px) saturate(160%);
  box-shadow: inset 1px 1px 1px rgba(255,255,255,0.1),
              inset -1px -1px 1px rgba(255,255,255,0.04),
              0 0 18px rgba(255,255,255,0.03);
  transition: all 0.3s ease;
}
.hero-cta-ghost::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, transparent 55%);
  pointer-events: none;
}
.hero-cta-ghost:hover {
  color: #fff; border-color: rgba(255,255,255,0.55);
  background: rgba(255,255,255,0.1);
  box-shadow: inset 1px 1px 1px rgba(255,255,255,0.18), 0 0 28px rgba(255,255,255,0.07);
  transform: translateY(-2px);
}

/* ── HERO TAGS (pill badges) ── */
.hero-tags { display: flex; gap: 10px; margin-top: 26px; flex-wrap: wrap; }
.hero-tags span {
  font-family: var(--font-mono); font-size: 9px; letter-spacing: 3px;
  color: rgba(255,255,255,0.35); text-transform: uppercase;
  padding: 6px 14px; border: 1px solid rgba(255,255,255,0.1);
  border-radius: 100px; backdrop-filter: blur(8px);
}

/* ── RIGHT-SIDE GLASS HUD CARDS ── */
#hero-cards {
  position: absolute; right: 36px; top: 50%;
  transform: translateY(-50%);
  z-index: 10; pointer-events: none;
  display: flex; flex-direction: column; gap: 14px; width: 260px;
}
.hcard { padding: 20px 24px; border-radius: 16px; }
.hcard-label {
  font-family: var(--font-mono); font-size: 9px; letter-spacing: 4px;
  color: rgba(255,255,255,0.38); text-transform: uppercase; margin-bottom: 9px;
}
.hcard-val {
  font-family: var(--font-display); font-size: 32px; font-weight: 500;
  letter-spacing: -1px; color: #fff; line-height: 1;
}
.hcard-note {
  font-family: var(--font-ui); font-size: 12px;
  color: rgba(255,255,255,0.42); margin-top: 9px;
  display: flex; align-items: center; gap: 6px;
}
.hcard-bar {
  height: 2px; background: rgba(255,255,255,0.08);
  border-radius: 2px; margin-top: 10px; overflow: hidden;
}
.hcard-fill {
  height: 100%; border-radius: 2px;
  background: linear-gradient(90deg, #ff4040, #ff6a00);
  animation: pulse-fill 2.2s ease-in-out infinite;
}
@keyframes pulse-fill { 0%,100%{opacity:1;width:86%} 50%{opacity:0.6;width:78%} }
.hcard-dot {
  display: inline-block; width: 7px; height: 7px; border-radius: 50%;
  background: #5dff8c; flex-shrink: 0;
  animation: dot-blink 1.6s ease-in-out infinite;
}
@keyframes dot-blink { 0%,100%{opacity:1} 50%{opacity:0.1} }
@media (max-width: 960px) { #hero-cards { display: none; } }

/* ── BOTTOM BAR ── */
#bottom-bar {
  position: absolute; bottom: 32px; left: 0; right: 0;
  padding: 0 36px;
  display: flex; align-items: center; justify-content: space-between;
}
.play-group { display: flex; align-items: center; gap: 14px; pointer-events: auto; cursor: pointer; }
.play-btn {
  width: 42px; height: 42px; border-radius: 50%;
  border: 1px solid rgba(255,255,255,0.4);
  background: rgba(255,255,255,0.04);
  display: flex; align-items: center; justify-content: center;
  transition: background 0.3s ease; flex-shrink: 0;
}
.play-btn:hover { background: rgba(255,255,255,0.1); }
.play-label {
  font-family: var(--font-ui); font-size: 10px; font-weight: 400;
  letter-spacing: 4px; color: rgba(255,255,255,0.75); text-transform: uppercase;
}
.tabs-group { display: flex; align-items: center; gap: 40px; }
.tab { display: flex; flex-direction: column; align-items: center; gap: 5px; pointer-events: auto; cursor: pointer; }
.tab-label { font-family: var(--font-ui); font-size: 10px; font-weight: 500; letter-spacing: 4px; text-transform: uppercase; }
.tab-num { font-family: var(--font-mono); font-size: 9px; font-weight: 300; color: rgba(255,255,255,0.4); letter-spacing: 2px; }
.tab.training .tab-label { color: #ffcc00; }
.tab.gallery .tab-label { color: #ff4444; }
.tab.collections .tab-label { color: rgba(255,255,255,0.8); }
```

---

## 7. CSS — LIQUID GLASS NAV

```css
#liquid-nav {
  position: fixed; top: 16px; left: 50%;
  transform: translateX(-50%);
  z-index: 200;
  width: calc(100% - 32px); max-width: 1200px; height: 62px;
  border-radius: 100px;
  background: rgba(10,10,12,0.55);
  backdrop-filter: blur(30px) saturate(180%);
  -webkit-backdrop-filter: blur(30px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 10px 40px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.06);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 28px; font-family: var(--font-ui);
  transition: background 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
}
#liquid-nav.scrolled {
  background: rgba(10,10,12,0.85);
  border-color: rgba(255,204,0,0.18);
  box-shadow: 0 14px 50px rgba(0,0,0,0.7), inset 0 1px 0 rgba(255,255,255,0.08);
}
.nav-logo { display: flex; align-items: center; gap: 11px; text-decoration: none; cursor: pointer; }
.nav-nuclear-icon {
  font-size: 22px; line-height: 1; color: #ffcc00;
  filter: drop-shadow(0 0 8px rgba(255,204,0,0.8)) drop-shadow(0 0 16px rgba(255,204,0,0.4));
}
.nav-logo-text {
  font-family: var(--font-display); font-size: 16px; font-weight: 600;
  letter-spacing: 7px; color: #fff; text-transform: uppercase;
}
.nav-links { display: flex; gap: 32px; list-style: none; }
.nav-links a {
  color: rgba(255,255,255,0.65); text-decoration: none;
  font-size: 11px; font-weight: 500; letter-spacing: 2.5px; text-transform: uppercase;
  transition: color 0.3s ease; position: relative;
}
.nav-links a:hover { color: #fff; }
.nav-links a.active { color: #ffcc00; }
.nav-links a.active::after {
  content: ''; position: absolute;
  bottom: -9px; left: 50%; transform: translateX(-50%);
  width: 4px; height: 4px; border-radius: 50%;
  background: #ffcc00; box-shadow: 0 0 8px #ffcc00;
}
.nav-actions { display: flex; align-items: center; gap: 14px; }
.nav-actions .login, .nav-actions .register {
  font-size: 11px; font-weight: 500; letter-spacing: 3px;
  text-transform: uppercase; cursor: pointer; transition: color 0.3s ease;
}
.nav-actions .login { color: rgba(255,255,255,0.6); }
.nav-actions .login:hover { color: #fff; }
.nav-actions .divider { color: rgba(255,255,255,0.2); font-size: 10px; }
.nav-actions .register { color: #ffcc00; }
.nav-actions .register:hover { color: #fff; }
@media (max-width: 900px) { .nav-links { display: none; } }
```

---

## 8. CSS — SECTION SHARED STYLES

```css
.section {
  position: relative; background: #000;
  padding: 140px 36px;
  border-top: 1px solid rgba(255,255,255,0.06);
}
/* Dot-grid background — gives glass cards something to blur */
.section::before {
  content: ''; position: absolute; inset: 0; z-index: 0; pointer-events: none;
  background-image: radial-gradient(rgba(255,255,255,0.035) 1px, transparent 1px);
  background-size: 38px 38px;
}
.section-inner { max-width: 1200px; margin: 0 auto; position: relative; z-index: 1; }
.section-eyebrow {
  font-family: var(--font-mono); font-size: 10px; font-weight: 500;
  letter-spacing: 7px; color: #ffcc00; text-transform: uppercase;
  margin-bottom: 18px; opacity: 1;
  display: flex; align-items: center; gap: 12px;
}
/* Gold line before eyebrow */
.section-eyebrow::before {
  content: ''; display: inline-block; width: 24px; height: 1px;
  background: #ffcc00; flex-shrink: 0;
}
.section-heading {
  font-family: var(--font-display);
  font-size: clamp(42px, 4.8vw, 68px); font-weight: 500;
  line-height: 1.04; letter-spacing: -2px; color: #fff;
  margin-bottom: 60px; max-width: 720px;
}
/* Scroll reveal */
.reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.9s ease, transform 0.9s ease; }
.reveal.visible { opacity: 1; transform: translateY(0); }
```

---

## 9. CSS — LIQUID GLASS CARD (`.glass`)

This is the core design primitive. Apply to any card element.

```css
.glass {
  position: relative; isolation: isolate;
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
/* Top refraction edge */
.glass::before {
  content: ''; position: absolute;
  top: 0; left: 14%; right: 14%; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.55), transparent);
  pointer-events: none; z-index: 1; opacity: 0.9;
}
/* Diagonal sheen on hover */
.glass::after {
  content: ''; position: absolute; inset: 0;
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

---

## 10. CSS — CORNER-BRACKET HOVER EFFECT (`.feat-framed`)

Add alongside `.glass` on interactive cards:

```css
.feat-framed { position: relative; }
.feat-framed::before, .feat-framed::after {
  content: ''; position: absolute;
  width: 13px; height: 13px;
  border-color: rgba(255,204,0,0.55); border-style: solid;
  transition: opacity 0.3s ease, border-color 0.3s ease; opacity: 0;
}
.feat-framed::before { top: -1px; left: -1px;  border-width: 2px 0 0 2px; }
.feat-framed::after  { top: -1px; right: -1px; border-width: 2px 2px 0 0; }
.feat-framed:hover::before, .feat-framed:hover::after { opacity: 1; }
.feat-framed:hover { border-color: rgba(255,204,0,0.22) !important; }
```

---

## 11. CSS — FILM GRAIN OVERLAY

```css
.grain {
  pointer-events: none; position: fixed; inset: 0;
  z-index: 300; opacity: 0.06; mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml;utf8,<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='0.9'/></svg>");
}
```

---

## 12. CSS — THREAT STATS SECTION

```css
#threat-stats .scan-line {
  position: absolute; left: 0; right: 0; top: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,204,0,0.45), transparent);
  animation: scan 6s linear infinite; pointer-events: none;
}
@keyframes scan { 0% { transform: translateY(0); } 100% { transform: translateY(100vh); } }

.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
@media (max-width: 900px) { .stats-grid { grid-template-columns: repeat(2, 1fr); } }

.stat-card { padding: 32px 28px 36px; overflow: hidden; cursor: default; }
.stat-card-head {
  display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;
}
.stat-pulse {
  display: flex; align-items: center; gap: 7px;
  font-family: var(--font-mono); font-size: 9px;
  letter-spacing: 3px; color: rgba(255,204,0,0.75); text-transform: uppercase;
}
.stat-pulse-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: #ffcc00; box-shadow: 0 0 0 0 rgba(255,204,0,0.8);
  animation: stat-pulse 2s ease-in-out infinite;
}
@keyframes stat-pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(255,204,0,0.6); }
  50%       { box-shadow: 0 0 0 8px rgba(255,204,0,0); }
}
.stat-icon {
  width: 16px; height: 16px; stroke: rgba(255,204,0,0.55);
  stroke-width: 1.6; fill: none; stroke-linecap: round; stroke-linejoin: round;
  transition: stroke 0.3s ease, transform 0.3s ease;
}
.stat-card:hover .stat-icon { stroke: #ffcc00; transform: rotate(12deg) scale(1.1); }

.stat-number {
  font-family: var(--font-display); font-size: 64px; font-weight: 300;
  line-height: 1; color: #fff; letter-spacing: -3px;
  font-variant-numeric: tabular-nums;
  background: linear-gradient(170deg, #ffffff 20%, rgba(255,255,255,0.65) 100%);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
.stat-card:hover .stat-number { text-shadow: 0 0 40px rgba(255,204,0,0.35); }
.stat-label { margin-top: 18px; font-size: 13.5px; font-weight: 500; color: rgba(255,255,255,0.92); letter-spacing: 0.3px; }
.stat-desc { margin-top: 6px; font-family: var(--font-mono); font-size: 11px; color: rgba(255,255,255,0.42); }

.stat-progress {
  margin-top: 28px; position: relative; height: 2px; border-radius: 2px;
  background: rgba(255,255,255,0.07); overflow: hidden;
}
.stat-progress::before {
  content: ''; position: absolute; left: 0; top: 0; bottom: 0;
  width: var(--progress, 85%);
  background: linear-gradient(90deg, #ffcc00, #ff9500);
  border-radius: 2px; box-shadow: 0 0 12px rgba(255,204,0,0.6);
  animation: progress-grow 1.8s cubic-bezier(.2,.8,.2,1) both;
}
.stat-progress::after {
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

## 13. CSS — HOW IT WORKS SECTION

```css
.hiw-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: start; }
.hiw-intro { position: sticky; top: 140px; }
.hiw-intro p { margin-top: 24px; font-size: 14px; line-height: 1.7; color: rgba(255,255,255,0.5); max-width: 380px; }
.hiw-intro .hiw-divider { margin-top: 36px; width: 60px; height: 1px; background: #ffcc00; }
.hiw-steps { position: relative; }
/* Vertical connector line */
.hiw-steps::before {
  content: ''; position: absolute; left: 20px; top: 20px; bottom: 20px;
  width: 1px; background: rgba(255,255,255,0.1);
}
.hiw-step { position: relative; display: flex; gap: 32px; padding-bottom: 60px; }
.hiw-step-icon {
  flex-shrink: 0; width: 42px; height: 42px; border-radius: 50%;
  border: 1px solid rgba(255,204,0,0.4); background: #000;
  display: flex; align-items: center; justify-content: center; z-index: 2;
  transition: box-shadow 0.3s ease, border-color 0.3s ease;
}
.hiw-step:hover .hiw-step-icon { box-shadow: 0 0 20px rgba(255,204,0,0.3); border-color: #ffcc00; }
.hiw-step-icon svg { width: 16px; height: 16px; stroke: #ffcc00; fill: none; stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; }
.hiw-step-tag { font-family: var(--font-mono); font-size: 11px; letter-spacing: 4px; color: rgba(255,255,255,0.3); text-transform: uppercase; margin-bottom: 8px; }
.hiw-step h3 { font-family: var(--font-display); font-size: 26px; font-weight: 500; letter-spacing: -0.5px; color: #fff; margin-bottom: 12px; }
.hiw-step p { font-family: var(--font-ui); font-size: 15px; line-height: 1.75; color: rgba(255,255,255,0.48); }
@media (max-width: 900px) { .hiw-grid { grid-template-columns: 1fr; gap: 40px; } .hiw-intro { position: static; } }
```

---

## 14. CSS — THREAT INTEL SECTION (second 3D scene)

```css
#threat-intel { padding: 160px 36px; overflow: hidden; position: relative; }

/* Animated background orbs */
.intel-orbs { position: absolute; inset: 0; pointer-events: none; overflow: hidden; z-index: 0; }
.intel-orb { position: absolute; width: 380px; height: 380px; border-radius: 50%; filter: blur(90px); opacity: 0.28; }
.intel-orb.o1 { background: rgba(255,204,0,0.55); top: -120px; left: -80px;   animation: orb-float 18s ease-in-out infinite; }
.intel-orb.o2 { background: rgba(255,80,80,0.4);  bottom: -140px; right: -60px; animation: orb-float 22s ease-in-out infinite reverse; }
.intel-orb.o3 { background: rgba(80,120,255,0.35); top: 45%; right: 30%;       animation: orb-float 25s ease-in-out infinite; }
@keyframes orb-float {
  0%, 100% { transform: translate(0,0) scale(1); }
  50%       { transform: translate(100px, 80px) scale(1.1); }
}
/* Fine grid overlay */
.intel-grid-bg {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 60px 60px; pointer-events: none; z-index: 1;
}
#threat-intel .section-inner { z-index: 2; }

/* Split layout */
.intel-split { display: grid; grid-template-columns: 1fr 380px; gap: 64px; align-items: center; }
@media (max-width: 1000px) { .intel-split { grid-template-columns: 1fr; } .intel-3d-col { display: none; } }

/* 2×2 intel cards grid */
.intel-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; max-width: 820px; }
@media (max-width: 700px) { .intel-grid { grid-template-columns: 1fr; } }

/* Intel cards override glass defaults for darker background */
.intel-card {
  padding: 24px 26px;
  background: rgba(8,8,10,0.7) !important;
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.08) !important;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}
.intel-card:hover {
  border-color: rgba(255,204,0,0.2) !important;
  box-shadow: 0 0 30px rgba(255,204,0,0.06) !important;
}
.intel-card-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 16px; }
.intel-card-left { display: flex; align-items: flex-start; gap: 12px; }
.intel-icon { width: 22px; height: 22px; flex-shrink: 0; stroke-width: 1.6; fill: none; stroke-linecap: round; stroke-linejoin: round; }
.intel-title { font-size: 13.5px; font-weight: 500; color: #fff; }
.intel-region { font-family: var(--font-mono); font-size: 11px; color: rgba(255,255,255,0.5); margin-top: 3px; }
.intel-severity {
  font-family: var(--font-mono); font-size: 9.5px; letter-spacing: 3px;
  padding: 4px 8px; border: 1px solid; border-radius: 3px; white-space: nowrap;
}
.intel-bar { margin-top: 16px; height: 3px; background: rgba(255,255,255,0.08); border-radius: 99px; overflow: hidden; }
.intel-bar-fill { height: 100%; border-radius: 99px; animation: pulse-slow 4s ease-in-out infinite; }
@keyframes pulse-slow { 0%,100% { opacity: 0.7; } 50% { opacity: 1; } }

/* 3D Sentinel column */
.intel-3d-col { position: relative; height: 560px; border-radius: 20px; overflow: hidden; }
#sentinel-canvas { width: 100%; height: 100%; display: block; border-radius: 20px; }
.sentinel-glow {
  position: absolute; inset: 0; border-radius: 20px; pointer-events: none;
  box-shadow: inset 0 0 60px rgba(255,204,0,0.08), inset 0 0 120px rgba(255,204,0,0.04);
}
.sentinel-badge {
  position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%);
  font-family: var(--font-mono); font-size: 9px; letter-spacing: 5px;
  color: rgba(255,204,0,0.7); text-transform: uppercase;
  padding: 7px 18px; background: rgba(0,0,0,0.5);
  border: 1px solid rgba(255,204,0,0.25); border-radius: 100px;
  backdrop-filter: blur(12px); white-space: nowrap;
}
```

---

## 15. CSS — FEATURES, TESTIMONIALS, PRICING, FOOTER, FINAL CTA, MARQUEE

```css
/* FEATURES */
.features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
.feature-card { padding: 36px; min-height: 240px; display: flex; flex-direction: column; }
.feature-card.span-2 { grid-column: span 2; }
.feature-card svg { width: 24px; height: 24px; stroke: #ffcc00; fill: none; stroke-width: 1.4; stroke-linecap: round; stroke-linejoin: round; margin-bottom: 28px; }
.feature-card h3 { font-family: var(--font-display); font-size: 20px; font-weight: 400; color: #fff; margin-bottom: 12px; }
.feature-card p { font-size: 13.5px; line-height: 1.7; color: rgba(255,255,255,0.5); }
@media (max-width: 900px) { .features-grid { grid-template-columns: 1fr; } .feature-card.span-2 { grid-column: auto; } }

/* TESTIMONIALS */
.testimonials-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.testimonial-card { padding: 36px; display: flex; flex-direction: column; justify-content: space-between; min-height: 320px; }
.testimonial-quote-mark { font-family: var(--font-display); font-size: 56px; line-height: 0.6; color: #ffcc00; margin-bottom: 20px; }
.testimonial-quote { font-size: 14px; line-height: 1.7; color: rgba(255,255,255,0.75); }
.testimonial-author { margin-top: 30px; display: flex; align-items: center; gap: 14px; }
.testimonial-avatar {
  width: 40px; height: 40px; border-radius: 50%;
  background: rgba(255,204,0,0.1); border: 1px solid rgba(255,204,0,0.3);
  display: flex; align-items: center; justify-content: center;
  font-family: var(--font-mono); font-size: 11px; color: #ffcc00;
}
.testimonial-name { font-size: 13px; font-weight: 500; color: #fff; }
.testimonial-role { font-family: var(--font-mono); font-size: 11px; color: rgba(255,255,255,0.4); margin-top: 2px; }
@media (max-width: 900px) { .testimonials-grid { grid-template-columns: 1fr; } }

/* TRUSTED BY MARQUEE */
#trusted-by { background: #000; padding: 60px 36px; border-top: 1px solid rgba(255,255,255,0.06); overflow: hidden; }
.trusted-label { font-family: var(--font-mono); font-size: 10px; letter-spacing: 6px; color: rgba(255,255,255,0.4); text-transform: uppercase; text-align: center; margin-bottom: 32px; }
.marquee {
  position: relative; overflow: hidden;
  mask-image: linear-gradient(90deg, transparent, #000 10%, #000 90%, transparent);
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 10%, #000 90%, transparent);
}
.marquee-track { display: flex; gap: 80px; width: max-content; animation: marquee-scroll 35s linear infinite; }
@keyframes marquee-scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
.marquee-item { font-family: var(--font-display); font-size: 24px; font-weight: 400; letter-spacing: 2px; color: rgba(255,255,255,0.35); white-space: nowrap; transition: color 0.3s ease; }
.marquee-item:hover { color: #ffcc00; }

/* PRICING */
.pricing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; align-items: stretch; }
.price-card { padding: 36px; display: flex; flex-direction: column; min-height: 520px; }
.price-card.highlight { background: rgba(255,204,0,0.06) !important; border-color: rgba(255,204,0,0.4) !important; transform: scale(1.03); box-shadow: 0 20px 50px rgba(255,204,0,0.08); }
.price-card.highlight:hover { transform: scale(1.03) translateY(-3px); }
.price-tier { font-family: var(--font-mono); font-size: 11px; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 22px; color: rgba(255,255,255,0.4); }
.price-card.highlight .price-tier { color: #ffcc00; }
.price-amount { font-family: var(--font-display); font-size: 48px; font-weight: 300; color: #fff; letter-spacing: -1px; }
.price-period { font-size: 13px; color: rgba(255,255,255,0.4); margin-top: 2px; margin-bottom: 28px; }
.price-features { list-style: none; margin-bottom: 30px; flex: 1; }
.price-features li { font-size: 13px; color: rgba(255,255,255,0.72); padding: 8px 0; display: flex; align-items: center; gap: 10px; }
.price-features svg { width: 14px; height: 14px; stroke-width: 2; fill: none; stroke: rgba(255,255,255,0.4); stroke-linecap: round; stroke-linejoin: round; flex-shrink: 0; }
.price-card.highlight .price-features svg { stroke: #ffcc00; }
.price-cta { width: 100%; padding: 14px; background: transparent; border: 1px solid rgba(255,255,255,0.2); color: #fff; font-family: var(--font-ui); font-size: 11px; font-weight: 500; letter-spacing: 4px; text-transform: uppercase; cursor: pointer; transition: all 0.3s ease; }
.price-cta:hover { border-color: #ffcc00; color: #ffcc00; }
.price-card.highlight .price-cta { background: #ffcc00; border-color: #ffcc00; color: #000; }
.price-card.highlight .price-cta:hover { background: #fff; border-color: #fff; color: #000; }
@media (max-width: 900px) { .pricing-grid { grid-template-columns: 1fr; } .price-card.highlight { transform: none; } }

/* FINAL CTA */
#final-cta { position: relative; padding: 180px 36px; background: #000; border-top: 1px solid rgba(255,255,255,0.06); overflow: hidden; text-align: center; }
#final-cta::before { content: ''; position: absolute; top: 50%; left: 50%; width: 800px; height: 800px; transform: translate(-50%, -50%); background: radial-gradient(circle, rgba(255,204,0,0.12) 0%, transparent 60%); pointer-events: none; z-index: 0; }
.final-cta-inner { position: relative; z-index: 1; max-width: 860px; margin: 0 auto; }
.final-cta-eyebrow { font-family: var(--font-mono); font-size: 10px; letter-spacing: 6px; color: #ffcc00; text-transform: uppercase; margin-bottom: 24px; }
.final-cta-heading { font-family: var(--font-display); font-size: clamp(48px, 6vw, 88px); font-weight: 600; line-height: 1.00; letter-spacing: -3px; color: #fff; margin-bottom: 32px; }
.final-cta-heading em { font-style: normal; color: #ffcc00; }
.final-cta-sub { font-family: var(--font-ui); font-size: 16px; font-weight: 400; line-height: 1.75; color: rgba(255,255,255,0.48); max-width: 520px; margin: 0 auto 48px; }
.final-cta-actions { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }
.cta-primary { padding: 16px 38px; background: #ffcc00; color: #000; border: none; font-family: var(--font-ui); font-size: 12px; font-weight: 500; letter-spacing: 4px; text-transform: uppercase; cursor: pointer; transition: all 0.3s ease; }
.cta-primary:hover { background: #fff; transform: translateY(-2px); box-shadow: 0 12px 30px rgba(255,204,0,0.3); }
.cta-secondary { padding: 16px 38px; background: transparent; color: #fff; border: 1px solid rgba(255,255,255,0.25); font-family: var(--font-ui); font-size: 12px; font-weight: 500; letter-spacing: 4px; text-transform: uppercase; cursor: pointer; transition: all 0.3s ease; }
.cta-secondary:hover { border-color: #ffcc00; color: #ffcc00; }

/* FOOTER */
#site-footer { background: #000; padding: 100px 36px 40px; border-top: 1px solid rgba(255,255,255,0.06); }
.footer-inner { max-width: 1200px; margin: 0 auto; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 60px; }
.footer-brand .brand-logo { font-family: var(--font-mono); font-size: 14px; letter-spacing: 8px; color: #fff; margin-bottom: 20px; text-transform: uppercase; }
.footer-brand p { font-size: 13px; line-height: 1.7; color: rgba(255,255,255,0.4); max-width: 320px; }
.footer-col .footer-title { font-family: var(--font-mono); font-size: 11px; letter-spacing: 4px; color: #ffcc00; text-transform: uppercase; margin-bottom: 22px; }
.footer-col a { display: block; font-size: 13px; color: rgba(255,255,255,0.4); text-decoration: none; padding: 7px 0; transition: color 0.25s ease; }
.footer-col a:hover { color: #fff; }
.footer-bottom { padding-top: 30px; border-top: 1px solid rgba(255,255,255,0.06); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }
.footer-bottom span { font-family: var(--font-mono); font-size: 11px; color: rgba(255,255,255,0.25); }
.status-ok { color: #5dff8c; }
@media (max-width: 800px) { .footer-grid { grid-template-columns: 1fr 1fr; } .footer-brand { grid-column: span 2; } }
```

---

## 16. HTML BODY STRUCTURE

```html
<body>
  <div class="grain"></div>

  <div id="loading-screen">
    <div class="spinner"></div>
    <p class="loader-text">Initializing</p>
  </div>

  <!-- LIQUID GLASS NAV -->
  <nav id="liquid-nav">
    <a href="#hero" class="nav-logo">
      <span class="nav-nuclear-icon">&#9762;</span>
      <span class="nav-logo-text">HAZMAT</span>
    </a>
    <ul class="nav-links">
      <li><a href="#hero"         class="active" data-nav="hero">Home</a></li>
      <li><a href="#threat-stats"  data-nav="threat-stats">Intel</a></li>
      <li><a href="#how-it-works"  data-nav="how-it-works">Protocol</a></li>
      <li><a href="#features"      data-nav="features">Capabilities</a></li>
      <li><a href="#pricing"       data-nav="pricing">Deploy</a></li>
    </ul>
    <div class="nav-actions">
      <span class="login">Login</span>
      <span class="divider">/</span>
      <span class="register">Register</span>
    </div>
  </nav>

  <!-- HERO SECTION (Three.js canvas injected by JS) -->
  <section id="hero">
    <div id="ui-overlay">
      <div id="hero-content">
        <p class="hero-eyebrow">Est. 2025 &mdash; Cyber Division</p>
        <h1 class="hero-heading">Stop the Breach<br>Before It<br><em>Even Starts.</em></h1>
        <p class="hero-sub">AI-powered containment that operates at machine speed.<br>Real-time threat neutralisation. Zero tolerance for breach.</p>
        <div class="hero-cta-row">
          <button class="hero-cta">Deploy Now</button>
          <button class="hero-cta-ghost">See Demo</button>
        </div>
        <div class="hero-tags">
          <span>SOC Teams</span><span>Enterprise</span><span>Zero-day</span><span>MSSP</span>
        </div>
      </div>

      <!-- RIGHT HUD CARDS -->
      <div id="hero-cards">
        <div class="hcard glass">
          <div class="hcard-label">Active Threat Level</div>
          <div class="hcard-val">CRITICAL</div>
          <div class="hcard-bar"><div class="hcard-fill"></div></div>
          <div class="hcard-note">85% severity index</div>
        </div>
        <div class="hcard glass">
          <div class="hcard-label">Containments Today</div>
          <div class="hcard-val">2,847</div>
          <div class="hcard-note"><span class="hcard-dot"></span>+12 neutralised now</div>
        </div>
        <div class="hcard glass">
          <div class="hcard-label">Avg Response Time</div>
          <div class="hcard-val">0.003s</div>
          <div class="hcard-note">Machine-speed containment</div>
        </div>
      </div>

      <div id="bottom-bar">
        <div class="play-group">
          <div class="play-btn">
            <svg width="10" height="12" viewBox="0 0 10 12" fill="none">
              <path d="M0 0L10 6L0 12V0Z" fill="white"/>
            </svg>
          </div>
          <span class="play-label">Play Trailer</span>
        </div>
        <div class="tabs-group">
          <div class="tab training"><span class="tab-label">Training</span><span class="tab-num">01</span></div>
          <div class="tab gallery"><span class="tab-label">Gallery</span><span class="tab-num">02</span></div>
          <div class="tab collections"><span class="tab-label">Collections</span><span class="tab-num">03</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- THREAT STATS -->
  <section class="section" id="threat-stats">
    <div class="scan-line"></div>
    <div class="section-inner reveal">
      <p class="section-eyebrow">Live Intelligence</p>
      <h2 class="section-heading">Numbers that define our containment protocol.</h2>
      <div class="stats-grid">

        <div class="glass stat-card feat-framed">
          <div class="stat-card-head">
            <div class="stat-pulse"><span class="stat-pulse-dot"></span>LIVE</div>
            <svg class="stat-icon" viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
          </div>
          <div class="stat-number" data-count="99.7" data-suffix="%">0%</div>
          <div class="stat-label">Threat Detection Rate</div>
          <div class="stat-desc">Across all vector classes</div>
          <div class="stat-progress" style="--progress: 99.7%;"></div>
        </div>

        <div class="glass stat-card feat-framed">
          <div class="stat-card-head">
            <div class="stat-pulse"><span class="stat-pulse-dot"></span>LIVE</div>
            <svg class="stat-icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/></svg>
          </div>
          <div class="stat-number" data-count="0.3" data-suffix="ms">0ms</div>
          <div class="stat-label">Response Time</div>
          <div class="stat-desc">Average neutralization speed</div>
          <div class="stat-progress" style="--progress: 96%;"></div>
        </div>

        <div class="glass stat-card feat-framed">
          <div class="stat-card-head">
            <div class="stat-pulse"><span class="stat-pulse-dot"></span>LIVE</div>
            <svg class="stat-icon" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <div class="stat-number" data-count="4.2" data-suffix="M+">0M+</div>
          <div class="stat-label">Threats Contained</div>
          <div class="stat-desc">In the last 30 days</div>
          <div class="stat-progress" style="--progress: 84%;"></div>
        </div>

        <div class="glass stat-card feat-framed">
          <div class="stat-card-head">
            <div class="stat-pulse"><span class="stat-pulse-dot"></span>LIVE</div>
            <svg class="stat-icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>
          </div>
          <div class="stat-number" data-count="247" data-suffix="" data-int="1">0</div>
          <div class="stat-label">Nations Protected</div>
          <div class="stat-desc">Global deployment coverage</div>
          <div class="stat-progress" style="--progress: 62%;"></div>
        </div>

      </div>
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section class="section" id="how-it-works">
    <div class="section-inner">
      <div class="hiw-grid">
        <div class="hiw-intro reveal">
          <p class="section-eyebrow">Protocol</p>
          <h2 class="section-heading" style="margin-bottom:0;">Three steps.<br>Zero breach.</h2>
          <p>The HazMat containment protocol operates at machine speed. By the time a human analyst reviews the report, the threat is already neutralized.</p>
          <div class="hiw-divider"></div>
        </div>
        <div class="hiw-steps">
          <div class="hiw-step reveal">
            <div class="hiw-step-icon"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
            <div>
              <div class="hiw-step-tag">Step 01 &mdash; Detect</div>
              <h3>AI scans every vector simultaneously.</h3>
              <p>Our neural containment engine monitors 847 threat vectors in real time — network ingress, endpoint behavior, zero-day signatures, social engineering patterns, and supply chain anomalies.</p>
            </div>
          </div>
          <div class="hiw-step reveal">
            <div class="hiw-step-icon"><svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>
            <div>
              <div class="hiw-step-tag">Step 02 &mdash; Analyze</div>
              <h3>Classify. Prioritize. Understand intent.</h3>
              <p>Every detected anomaly is classified in 0.3ms using a multi-layered threat taxonomy. Severity scoring, blast radius projection, and attacker intent modeling give your team context.</p>
            </div>
          </div>
          <div class="hiw-step reveal">
            <div class="hiw-step-icon"><svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></div>
            <div>
              <div class="hiw-step-tag">Step 03 &mdash; Contain</div>
              <h3>Neutralize before propagation.</h3>
              <p>Automated containment protocols execute microsecond-level isolation. Infected nodes are quarantined, lateral movement is severed, and rollback snapshots are deployed.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- THREAT INTEL + SENTINEL 3D -->
  <section class="section" id="threat-intel">
    <div class="intel-orbs">
      <div class="intel-orb o1"></div><div class="intel-orb o2"></div><div class="intel-orb o3"></div>
    </div>
    <div class="intel-grid-bg"></div>
    <div class="section-inner reveal">
      <div class="intel-split">
        <div class="intel-col-text">
          <p class="section-eyebrow">Live Feed</p>
          <h2 class="section-heading">Global threat<br>intelligence, live.</h2>
          <div class="intel-grid">
            <div class="glass intel-card">
              <div class="intel-card-head">
                <div class="intel-card-left">
                  <svg class="intel-icon" style="stroke:#ff4444;" viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2z"/><line x1="12" y1="9" x2="12" y2="14"/><line x1="12" y1="17" x2="12" y2="17.5"/></svg>
                  <div><div class="intel-title">APT Group Activity</div><div class="intel-region">Eastern Europe</div></div>
                </div>
                <span class="intel-severity" style="color:#ff4444;border-color:rgba(255,68,68,0.4);">CRITICAL</span>
              </div>
              <div class="intel-bar"><div class="intel-bar-fill" style="width:92%;background:#ff4444;"></div></div>
            </div>
            <div class="glass intel-card">
              <div class="intel-card-head">
                <div class="intel-card-left">
                  <svg class="intel-icon" style="stroke:#ff8800;" viewBox="0 0 24 24"><polyline points="3 12 7 12 10 3 14 21 17 12 21 12"/></svg>
                  <div><div class="intel-title">DDoS Surge Detected</div><div class="intel-region">Asia Pacific</div></div>
                </div>
                <span class="intel-severity" style="color:#ff8800;border-color:rgba(255,136,0,0.4);">HIGH</span>
              </div>
              <div class="intel-bar"><div class="intel-bar-fill" style="width:68%;background:#ff8800;"></div></div>
            </div>
            <div class="glass intel-card">
              <div class="intel-card-head">
                <div class="intel-card-left">
                  <svg class="intel-icon" style="stroke:#ffcc00;" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                  <div><div class="intel-title">Phishing Campaign</div><div class="intel-region">North America</div></div>
                </div>
                <span class="intel-severity" style="color:#ffcc00;border-color:rgba(255,204,0,0.4);">MEDIUM</span>
              </div>
              <div class="intel-bar"><div class="intel-bar-fill" style="width:42%;background:#ffcc00;"></div></div>
            </div>
            <div class="glass intel-card">
              <div class="intel-card-head">
                <div class="intel-card-left">
                  <svg class="intel-icon" style="stroke:#ff4444;" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 15h3M1 9h3M1 15h3"/></svg>
                  <div><div class="intel-title">Zero-Day Signature</div><div class="intel-region">Global</div></div>
                </div>
                <span class="intel-severity" style="color:#ff4444;border-color:rgba(255,68,68,0.4);">CRITICAL</span>
              </div>
              <div class="intel-bar"><div class="intel-bar-fill" style="width:95%;background:#ff4444;"></div></div>
            </div>
          </div>
        </div>
        <div class="intel-3d-col">
          <canvas id="sentinel-canvas"></canvas>
          <div class="sentinel-glow"></div>
          <div class="sentinel-badge">&#9762;&nbsp; Sentinel Unit Active</div>
        </div>
      </div>
    </div>
  </section>

  <!-- [FEATURES, TESTIMONIALS, TRUSTED BY, PRICING, FINAL CTA, FOOTER — follow same pattern] -->
</body>
```

---

## 17. JAVASCRIPT — HERO THREE.JS SCENE (COMPLETE, VERBATIM)

```js
<script type="module">
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js';
import { VignetteShader } from 'three/addons/shaders/VignetteShader.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

/* ── CONSTANTS ── */
const MODEL_URL = 'https://raw.githubusercontent.com/toprmrproducer/3dasset/main/Meshy_AI_Containment_Sentinel_biped_Animation_Walking_withSkin.glb';
const CHAR_X   = 0.8;    // model X offset in world space
const CHAR_ROT = -0.65;  // ~-37° — shows face, still angled toward left-side text
const FEET_Y   = -4.0;   // push feet below viewport, crop sits at waist/chest
const TARGET_H = 5.5;    // target model height in world units

/* ── STATE ── */
let model = null, headBone = null, neckBone = null;
let mouseX = 0, mouseY = 0, mouseLastMove = 0;
let idleTargetY = 0, idleTargetX = 0, idleChangeTimer = 0;
let modelRestY = 0, trackingStrength = 0;
const clock = new THREE.Clock();

/* ── SCENE ── */
const scene = new THREE.Scene();

/* ── CAMERA ── */
const camera = new THREE.PerspectiveCamera(32, window.innerWidth / window.innerHeight, 0.1, 100);
camera.position.set(0.5, 0.5, 5.5);
camera.lookAt(0.8, 0.6, 0);

/* ── RENDERER ── */
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0x000000, 0);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.physicallyCorrectLights = true;
document.getElementById('hero').appendChild(renderer.domElement);

/* ── ENVIRONMENT MAP (RoomEnvironment PMREM) ── */
const pmrem = new THREE.PMREMGenerator(renderer);
pmrem.compileEquirectangularShader();
const envTexture = pmrem.fromScene(new RoomEnvironment(0.5), 0.04).texture;
scene.environment = envTexture;
scene.environmentIntensity = 1.0;
scene.background = null;

/* ── LIGHTING (8 lights) ── */
// 1. Key: warm, camera-left/front/above
const keyLight = new THREE.DirectionalLight(0xfff4e0, 1.6);
keyLight.position.set(-3, 3, 4); keyLight.target.position.set(0.8, 1.2, 0);
keyLight.castShadow = true; keyLight.shadow.mapSize.set(2048, 2048);
keyLight.shadow.camera.near = 0.1; keyLight.shadow.camera.far = 20;
keyLight.shadow.bias = -0.0005;
scene.add(keyLight, keyLight.target);

// 2. Left fill: warm, lights the face-side that looks toward text
const leftFill = new THREE.DirectionalLight(0xffe8b0, 1.1);
leftFill.position.set(-5, 1.2, 2); leftFill.target.position.set(0.8, 1.2, 0);
scene.add(leftFill, leftFill.target);

// 3. Face spotlight: focused on head/mask area
const faceFill = new THREE.SpotLight(0xffffff, 2.2, 12, Math.PI / 7, 0.55, 1.0);
faceFill.position.set(0.2, 2.8, 3.8); faceFill.target.position.set(0.8, 2.0, 0.2);
scene.add(faceFill, faceFill.target);

// 4. Back rim: warm gold silhouette separation from behind+right
const backRim = new THREE.DirectionalLight(0xffcc66, 1.4);
backRim.position.set(5, 2.2, -3); backRim.target.position.set(0.8, 1.2, 0);
scene.add(backRim, backRim.target);

// 5. Cool blue rim: from behind+left, subtle complement to warm backRim
const rimLight = new THREE.DirectionalLight(0x5566ff, 0.6);
rimLight.position.set(0.5, 2.0, -2.5);
scene.add(rimLight);

// 6. Fill: gold from front-right
const fillLight = new THREE.DirectionalLight(0xffd700, 0.3);
fillLight.position.set(2, 1, 3);
scene.add(fillLight);

// 7. Ambient: very dark purple-ish base
const ambientLight = new THREE.AmbientLight(0x1a1520, 0.7);
scene.add(ambientLight);

// 8. Soft top spot: casts clean shadows
const spotLight = new THREE.SpotLight(0xffffff, 0.2);
spotLight.position.set(0, 4, 3); spotLight.target.position.set(0.8, 1.2, 0);
spotLight.penumbra = 0.5; spotLight.angle = Math.PI / 7; spotLight.castShadow = true;
spotLight.shadow.mapSize.set(2048, 2048); spotLight.shadow.bias = -0.0005;
scene.add(spotLight, spotLight.target);

/* ── VIDEO BACKGROUND ──
   Use a looping MP4 as scene.background via THREE.VideoTexture.
   Provide your own video file. Autoplay/muted required by browsers.  */
const bgVideo = document.createElement('video');
bgVideo.src = 'YOUR_BACKGROUND_VIDEO.mp4'; // ← replace with your file
bgVideo.loop = true; bgVideo.muted = true; bgVideo.playsInline = true;
bgVideo.autoplay = true; bgVideo.crossOrigin = 'anonymous'; bgVideo.preload = 'auto';
bgVideo.style.display = 'none';
document.body.appendChild(bgVideo);
const tryPlay = () => bgVideo.play().catch(e => console.warn('bg video play blocked:', e));
bgVideo.addEventListener('canplay', tryPlay); tryPlay();
window.addEventListener('pointerdown', () => tryPlay(), { once: true });
const bgTexture = new THREE.VideoTexture(bgVideo);
bgTexture.colorSpace = THREE.SRGBColorSpace;
bgTexture.minFilter = THREE.LinearFilter;
bgTexture.magFilter = THREE.LinearFilter;
scene.background = bgTexture;

/* ── POST-PROCESSING ── */
const composer = new EffectComposer(renderer);
composer.setSize(window.innerWidth, window.innerHeight);
composer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
composer.addPass(new RenderPass(scene, camera));
// Bloom: subtle, not overdone
const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  0.3,   // strength
  0.9,   // radius
  0.85   // threshold
);
composer.addPass(bloomPass);
// Vignette: strong corners
const vignettePass = new ShaderPass(VignetteShader);
vignettePass.uniforms['offset'].value   = 0.92;
vignettePass.uniforms['darkness'].value = 1.6;
composer.addPass(vignettePass);

/* ── MOUSE ── */
window.addEventListener('mousemove', (e) => {
  mouseX = (e.clientX / window.innerWidth) * 2 - 1;           // -1 (left) to +1 (right)
  mouseY = -((e.clientY / window.innerHeight) * 2 - 1);       // +1 (top) to -1 (bottom) — NEGATED
  mouseLastMove = performance.now();
});

/* ── MODEL LOAD ── */
const loader = new GLTFLoader();
loader.load(MODEL_URL, (gltf) => {
  model = gltf.scene;
  scene.add(model);
  model.rotation.y = 0;

  // CRITICAL: compute SkinnedMesh geometry bounds BEFORE setFromObject
  model.updateMatrixWorld(true);
  model.traverse((o) => {
    if (o.isSkinnedMesh && o.geometry) {
      o.geometry.computeBoundingBox();
      o.geometry.computeBoundingSphere();
    } else if (o.isMesh && o.geometry) {
      o.geometry.computeBoundingBox();
    }
  });

  // Scale to TARGET_H (5.5 world units)
  const rawBox  = new THREE.Box3().setFromObject(model);
  const rawSize = rawBox.getSize(new THREE.Vector3());
  const s = THREE.MathUtils.clamp(TARGET_H / Math.max(rawSize.y, 0.0001), 0.001, 6.0);
  model.scale.setScalar(s);
  model.updateMatrixWorld(true);

  // Position: center X/Z, feet at FEET_Y (-4.0)
  const scaledBox    = new THREE.Box3().setFromObject(model);
  const scaledCenter = scaledBox.getCenter(new THREE.Vector3());
  model.position.x += (CHAR_X - scaledCenter.x);
  model.position.y += (FEET_Y - scaledBox.min.y);
  model.position.z += (0 - scaledCenter.z);
  model.rotation.y  = CHAR_ROT;
  modelRestY = model.position.y;

  // Material overrides — more metallic/glossy look
  model.traverse((obj) => {
    if (obj.isMesh) {
      obj.castShadow = true; obj.receiveShadow = true;
      obj.material.side = THREE.FrontSide;
      obj.material.needsUpdate = true;
      if (obj.material.envMapIntensity !== undefined) obj.material.envMapIntensity = 1.2;
      if (obj.material.roughness  !== undefined) obj.material.roughness  = Math.min(obj.material.roughness,  0.35);
      if (obj.material.metalness  !== undefined) obj.material.metalness  = Math.max(obj.material.metalness,  0.15);
    }
  });

  // Find head/neck bones
  model.traverse((obj) => {
    if (obj.isBone || obj.type === 'Bone') {
      const n = obj.name.toLowerCase();
      if (obj.name === 'Head')  headBone = obj;
      if (obj.name === 'neck')  neckBone = obj;
      if (!headBone && n.includes('head')) headBone = obj;
      if (!neckBone && n.includes('neck')) neckBone = obj;
    }
  });

  // Override walking-animation frame-0 pose with chin-down default
  if (headBone) headBone.rotation.set(0.38, 0, 0, 'YXZ'); // chin down, eyes toward viewer
  if (neckBone) neckBone.rotation.set(0.16, 0, 0, 'YXZ');

  // After load: boost env intensity
  scene.environmentIntensity = 1.8;

  // Hide loading screen
  const ls = document.getElementById('loading-screen');
  ls.style.opacity = '0';
  setTimeout(() => { ls.style.display = 'none'; }, 1200);
});

/* ── ANIMATE LOOP ── */
function animate() {
  requestAnimationFrame(animate);
  const t = clock.getElapsedTime();

  if (model) {
    // Idle float
    model.position.y = modelRestY + Math.sin(t * 0.6) * 0.006;
    // Subtle body yaw follows mouse (multiplied by trackingStrength so it only activates in zone)
    const bodyTarget = CHAR_ROT + mouseX * 0.04 * trackingStrength + Math.sin(t * 0.4) * 0.020;
    model.rotation.y = THREE.MathUtils.lerp(model.rotation.y, bodyTarget, 0.025);
  }

  // Random idle head drift (updates every 4–7 seconds)
  idleChangeTimer -= 0.016;
  if (idleChangeTimer <= 0) {
    idleTargetY = (Math.random() - 0.5) * 0.12;
    idleTargetX = (Math.random() - 0.5) * 0.05;
    idleChangeTimer = 4.0 + Math.random() * 3.0;
  }
  const idleY = THREE.MathUtils.lerp(headBone ? headBone.rotation.y : 0, idleTargetY, 0.008);
  const idleX = THREE.MathUtils.lerp(headBone ? headBone.rotation.x : 0, idleTargetX, 0.008);

  if (headBone && neckBone) {
    headBone.rotation.order = 'YXZ';
    neckBone.rotation.order = 'YXZ';

    // Zone: don't track when mouse is over far-left text area or beyond right edge
    const inZone    = mouseX > -0.55 && mouseX < 0.78;
    const recentMove = (performance.now() - mouseLastMove) < 3000;
    trackingStrength = THREE.MathUtils.lerp(
      trackingStrength, (inZone && recentMove) ? 1.0 : 0.0, 0.08
    );

    const tY = mouseX *  0.62 * trackingStrength;          // yaw  ±0.62 rad
    const tX = 0.34 + mouseY * -0.45 * trackingStrength;   // pitch 0.34 default (chin-down), ±0.45
    const tZ = mouseX * -0.12 * trackingStrength;           // lateral z-tilt — key to organic feel

    const blendedTY = THREE.MathUtils.clamp(tY * 0.85 + idleY * 0.15, -0.62,  0.62);
    const blendedTX = THREE.MathUtils.clamp(tX * 0.85 + idleX * 0.15, -0.14,  0.68);
    const blendedTZ = THREE.MathUtils.clamp(tZ * 0.85,                 -0.12,  0.12);

    headBone.rotation.y = THREE.MathUtils.lerp(headBone.rotation.y, blendedTY,        0.13);
    headBone.rotation.x = THREE.MathUtils.lerp(headBone.rotation.x, blendedTX,        0.13);
    headBone.rotation.z = THREE.MathUtils.lerp(headBone.rotation.z, blendedTZ,        0.10);
    neckBone.rotation.y = THREE.MathUtils.lerp(neckBone.rotation.y, blendedTY * 0.42, 0.13);
    neckBone.rotation.x = THREE.MathUtils.lerp(neckBone.rotation.x, blendedTX * 0.42, 0.13);
    neckBone.rotation.z = THREE.MathUtils.lerp(neckBone.rotation.z, blendedTZ * 0.50, 0.10);
  }

  // Camera drift
  camera.position.x = THREE.MathUtils.lerp(camera.position.x,  0.5 + mouseX *  0.15, 0.018);
  camera.position.y = THREE.MathUtils.lerp(camera.position.y,  0.5 + mouseY * -0.08, 0.018);
  camera.lookAt(0.8, 0.6, 0);

  composer.render();
}
animate();

/* ── RESIZE ── */
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
  composer.setSize(window.innerWidth, window.innerHeight);
});
```

---

## 18. JAVASCRIPT — SENTINEL 3D SCENE (COMPLETE, VERBATIM)

```js
function initSentinelScene() {
  const sentCanvas = document.getElementById('sentinel-canvas');
  if (!sentCanvas) return;

  const sentRenderer = new THREE.WebGLRenderer({ canvas: sentCanvas, antialias: true, alpha: true });
  sentRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
  sentRenderer.outputColorSpace = THREE.SRGBColorSpace;
  sentRenderer.toneMapping = THREE.ACESFilmicToneMapping;
  sentRenderer.toneMappingExposure = 1.15;
  sentRenderer.shadowMap.enabled = true;
  sentRenderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const sentScene  = new THREE.Scene();
  const sentCamera = new THREE.PerspectiveCamera(50, 1, 0.1, 50);
  sentCamera.position.set(0, 0, 5.5);
  sentCamera.lookAt(0, 0, 0);

  function resizeSentinel() {
    const w = sentCanvas.offsetWidth  || 380;
    const h = sentCanvas.offsetHeight || 560;
    sentRenderer.setSize(w, h, false);
    sentCamera.aspect = w / h;
    sentCamera.updateProjectionMatrix();
  }
  setTimeout(resizeSentinel, 0);
  new ResizeObserver(resizeSentinel).observe(sentCanvas);

  // Environment map
  const sp = new THREE.PMREMGenerator(sentRenderer);
  sp.compileEquirectangularShader();
  sentScene.environment = sp.fromScene(new RoomEnvironment(0.5), 0.04).texture;
  sentScene.environmentIntensity = 1.3;

  // Lights
  const sk = new THREE.DirectionalLight(0xfff4e0, 1.8); sk.position.set(-2, 3, 3); sk.target.position.set(0, 1, 0); sentScene.add(sk, sk.target);
  const sb2 = new THREE.DirectionalLight(0xffcc66, 1.3); sb2.position.set(3, 1.5, -2); sb2.target.position.set(0, 1, 0); sentScene.add(sb2, sb2.target);
  const sa = new THREE.AmbientLight(0x1a1520, 0.9); sentScene.add(sa);
  const sfill = new THREE.SpotLight(0xffffff, 2.0, 12, Math.PI / 6, 0.6, 1.0);
  sfill.position.set(0.2, 3, 3.5); sfill.target.position.set(0, 1.6, 0); sentScene.add(sfill, sfill.target);

  let sentModel = null, sentHead = null, sentNeck = null, sentRestY = 0, sentMidY = 1.2;
  const SENT_ROT = 0.3;
  const sentClock = new THREE.Clock();
  let sentVisible = false;

  // Only render when visible
  new IntersectionObserver(([e]) => { sentVisible = e.isIntersecting; }, { threshold: 0.05 }).observe(sentCanvas);

  const sentLoader = new GLTFLoader();
  sentLoader.load(
    'https://raw.githubusercontent.com/toprmrproducer/3dasset/main/Meshy_AI_Containment_Sentinel_biped_Animation_Walking_withSkin.glb',
    (gltf) => {
      sentModel = gltf.scene;
      sentScene.add(sentModel);

      // CRITICAL: compute SkinnedMesh bounds first
      sentModel.traverse(obj => {
        if (obj.isSkinnedMesh && obj.geometry) {
          obj.geometry.computeBoundingBox();
          obj.geometry.computeBoundingSphere();
        } else if (obj.isMesh && obj.geometry) {
          obj.geometry.computeBoundingBox();
        }
      });
      sentModel.updateMatrixWorld(true);

      // Scale to 2.4 world units tall
      const rb = new THREE.Box3().setFromObject(sentModel);
      const rs = rb.getSize(new THREE.Vector3());
      const SENT_TARGET_H = 2.4;
      const sc = THREE.MathUtils.clamp(SENT_TARGET_H / Math.max(rs.y, 0.001), 0.001, 5);
      sentModel.scale.setScalar(sc);
      sentModel.updateMatrixWorld(true);

      // Feet exactly at y=0, center X/Z
      const sb3 = new THREE.Box3().setFromObject(sentModel);
      const sbC = sb3.getCenter(new THREE.Vector3());
      sentModel.position.x -= sbC.x;
      sentModel.position.y -= sb3.min.y;
      sentModel.position.z -= sbC.z;
      sentModel.rotation.y  = SENT_ROT;
      sentRestY = sentModel.position.y;

      // Camera looks at model mid-body
      sentMidY = SENT_TARGET_H / 2; // 1.2
      sentCamera.position.set(0, sentMidY, 5.5);
      sentCamera.lookAt(0, sentMidY, 0);

      sentModel.traverse((obj) => {
        if (obj.isMesh) {
          obj.castShadow = true; obj.material.side = THREE.FrontSide; obj.material.needsUpdate = true;
          if (obj.material.envMapIntensity !== undefined) obj.material.envMapIntensity = 1.4;
          if (obj.material.roughness !== undefined) obj.material.roughness = Math.min(obj.material.roughness, 0.3);
          if (obj.material.metalness !== undefined) obj.material.metalness = Math.max(obj.material.metalness, 0.2);
        }
        if (obj.isBone) {
          const n = obj.name.toLowerCase();
          if ((n.includes('head') || n.includes('skull')) && !sentHead) sentHead = obj;
          if (n.includes('neck') && !sentNeck) sentNeck = obj;
        }
      });
      resizeSentinel();
    }
  );

  function sentAnimate() {
    requestAnimationFrame(sentAnimate);
    if (!sentVisible || !sentModel) return;
    const t = sentClock.getElapsedTime();

    sentModel.position.y = sentRestY + Math.sin(t * 0.55) * 0.007;
    sentModel.rotation.y = SENT_ROT + Math.sin(t * 0.38) * 0.025;

    if (sentHead && sentNeck) {
      sentHead.rotation.order = 'YXZ'; sentNeck.rotation.order = 'YXZ';
      // Gentle idle: look slightly down, subtle yaw drift
      sentHead.rotation.y = THREE.MathUtils.lerp(sentHead.rotation.y, Math.sin(t * 0.43) * 0.18,            0.03);
      sentHead.rotation.x = THREE.MathUtils.lerp(sentHead.rotation.x, 0.22 + Math.sin(t * 0.27) * 0.05,    0.03);
      sentHead.rotation.z = THREE.MathUtils.lerp(sentHead.rotation.z, 0,                                    0.03);
      sentNeck.rotation.y = THREE.MathUtils.lerp(sentNeck.rotation.y, Math.sin(t * 0.43) * 0.07,            0.03);
      sentNeck.rotation.x = THREE.MathUtils.lerp(sentNeck.rotation.x, 0.09 + Math.sin(t * 0.27) * 0.02,    0.03);
      sentNeck.rotation.z = THREE.MathUtils.lerp(sentNeck.rotation.z, 0,                                    0.03);
      sentCamera.lookAt(0, sentModel.position.y + sentMidY, 0);
    }
    sentRenderer.render(sentScene, sentCamera);
  }
  sentAnimate();
}
initSentinelScene();
```

---

## 19. JAVASCRIPT — PAGE INTERACTIONS (COMPLETE, VERBATIM)

```js
/* ── SCROLL REVEAL ── */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
document.querySelectorAll('.reveal').forEach((el) => revealObserver.observe(el));

/* ── COUNT-UP ANIMATION ── */
const countObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    const el     = entry.target;
    const target = parseFloat(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const isInt  = el.dataset.int === '1';
    const duration = 1600;
    const start = performance.now();
    const tick = (now) => {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 3);        // ease-out cubic
      const val = target * eased;
      el.textContent = (isInt ? Math.round(val) : val.toFixed(1)) + suffix;
      if (p < 1) requestAnimationFrame(tick);
      else el.textContent = (isInt ? Math.round(target) : target.toFixed(1)) + suffix;
    };
    requestAnimationFrame(tick);
    countObserver.unobserve(el);
  });
}, { threshold: 0.6 });
document.querySelectorAll('.stat-number').forEach((el) => countObserver.observe(el));

/* ── LIQUID NAV: SCROLLED STATE + SCROLLSPY ── */
const navEl    = document.getElementById('liquid-nav');
const navLinks = document.querySelectorAll('.nav-links a[data-nav]');
const sections = ['hero','threat-stats','how-it-works','features','pricing']
  .map((id) => document.getElementById(id)).filter(Boolean);

window.addEventListener('scroll', () => {
  // Scrolled state
  if (window.scrollY > 40) navEl.classList.add('scrolled');
  else navEl.classList.remove('scrolled');
  // Scrollspy: section at 35% from top of viewport
  const y = window.scrollY + window.innerHeight * 0.35;
  let activeId = 'hero';
  for (const s of sections) { if (s.offsetTop <= y) activeId = s.id; }
  navLinks.forEach((a) => a.classList.toggle('active', a.dataset.nav === activeId));
}, { passive: true });

/* ── SMOOTH SCROLL ── */
document.querySelectorAll('a[href^="#"]').forEach((a) => {
  a.addEventListener('click', (e) => {
    const id     = a.getAttribute('href').slice(1);
    const target = document.getElementById(id);
    if (target) {
      e.preventDefault();
      window.scrollTo({ top: target.offsetTop - 20, behavior: 'smooth' });
    }
  });
});
```

---

## 20. CRITICAL IMPLEMENTATION NOTES

1. **SkinnedMesh bounding box bug** — ALWAYS call `geometry.computeBoundingBox()` and `geometry.computeBoundingSphere()` on every SkinnedMesh child **before** calling `new THREE.Box3().setFromObject(model)`. Without this, Three.js returns zero-size bounds for skinned models and all positioning is wrong.

2. **Chin-down head pose** — The walking animation's bind pose leaves the head tilted upward at frame 0. Override it immediately after finding the bone: `headBone.rotation.set(0.38, 0, 0, 'YXZ')`. This is what makes the character appear to look toward the camera rather than at the sky.

3. **mouseY negation** — `mouseY = -((e.clientY / window.innerHeight) * 2 - 1)`. The minus sign is essential. Without it, looking up/down is inverted.

4. **CHAR_ROT is negative** (`-0.65`). This rotates the character ~37° clockwise so the face is visible while the body is angled away from the text content. Positive rotation would point the back at the camera.

5. **Lateral z-tilt is the key to organic tracking** — `headBone.rotation.z = mouseX * -0.12 * trackingStrength`. When the head turns left, it cocks slightly to the left (negative Z). Without this, head tracking looks robotic.

6. **Zone-based tracking fade** — `trackingStrength` lerps between 0 and 1 at rate 0.08. `inZone = mouseX > -0.55 && mouseX < 0.78`. The zone intentionally excludes far-left (over the text content) so reading doesn't cause erratic head movement.

7. **Sentinel visibility gate** — The sentinel's `requestAnimationFrame` loop checks `if (!sentVisible || !sentModel) return`. This prevents GPU drain while scrolled away. Use IntersectionObserver with threshold 0.05.

8. **Video background** — `scene.background = new THREE.VideoTexture(bgVideo)`. The video must be `muted + loop + playsInline`. Add a `pointerdown` gesture fallback because some browsers block autoplay even with `muted`.

9. **`renderer.physicallyCorrectLights = true`** — Required for PBR materials to look correct. Without it, light intensity values are not in physical units and everything looks flat.

10. **Both 3D scenes use the same model URL** — `https://raw.githubusercontent.com/toprmrproducer/3dasset/main/Meshy_AI_Containment_Sentinel_biped_Animation_Walking_withSkin.glb`. The hero scene and the sentinel panel both load this exact URL.

11. **Glass needs background content** — The `backdrop-filter` blur only looks like glass if there's content behind the element. The dot-grid (`::before` radial-gradient) and the orb glows in `#threat-intel` exist specifically to give the glass cards something to refract.

12. **`isolation: isolate` on `.glass`** — Required so `::before`/`::after` pseudo-elements stay clipped to the card's stacking context and don't bleed into parent compositing layers.

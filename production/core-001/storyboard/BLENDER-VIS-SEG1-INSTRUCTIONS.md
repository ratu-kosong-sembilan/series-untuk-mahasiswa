# Blender Execution Guide — Segment 1 (Explainer, Phasor Intro)

Target: Deliver animation renders for Segment 1 shots (S1–S17) with clean, educational style.

## Global Setup
- Resolution: 1920×1080, 30 fps, sRGB/Rec.709
- Render: PNG sequence (alpha) for finals; MP4 (H.264) for review
- Camera: Orthographic, static, head-on
- World: Flat white or flat dark; no gradients; no depth of field
- Color code: Real=blue (#1E88E5), Imag=orange (#F57C00), Magnitude=green (#43A047), Angle=purple (#8E24AA)
- Font: Simple sans (e.g., Inter/Roboto substitute). Ensure legibility.
- Naming: CORE001_SEG1_SCN_SXX_vNN.ext (e.g., CORE001_SEG1_SCN_S01_v01.png)

## Reusable Assets (make once, reuse)
- Axes: X/Y thin lines (white/gray); grid optional at low opacity
- Phasor arrow: arrow mesh/curve with head; material per color code
- Timeline bar: thin rect + circular markers
- Icons: book, factory, hard-hat, eye, bulb, sigma, slider, factory; build as simple flat curves/planes
- Clock: circle + hour/minute hands (separate objects)
- Check/X: green check, red X (flat)

## Shot Instructions

### S1 (00:00–00:10) Split trig vs complex
- Objects: Two planes (L/R), text blocks, equation text (left), phasor arrow (right), X/✓.
- Anim: Keyframe opacity/scale-in for text; quick pop on X/✓.
- Camera: Static ortho.
- Duration: 240 frames.

### S2 (00:10–00:22) Stopwatch contrast
- Objects: Two dials (circle + needle), text labels.
- Anim: Needle rotation (keyframes), text fade-in; optional time text driver.
- Camera: Static ortho.
- Duration: 360 frames.

### S3 (00:22–00:34) Question card
- Objects: Single text; dark bg plane.
- Anim: Scale-in with ease; hold.
- Duration: 360 frames.

### S4 (00:34–00:45) Answer emphasis
- Objects: Text.
- Anim: Pop scale-in + slight Y slide.
- Duration: 330 frames.

### S5 (00:45–01:10) Icons relevance
- Objects: Book/factory/hard-hat icons, text labels, small checkmarks.
- Anim: Sequential L→R opacity/scale-in; check pop.
- Duration: 750 frames.

### S6 (01:10–01:30) Course list
- Objects: Bullet list text.
- Anim: Line-by-line fade/wipe.
- Duration: 600 frames.

### S7 (01:30–01:45) Industry list
- Objects: Bullet list text.
- Anim: Line-by-line fade/wipe.
- Duration: 450 frames.

### S8 (01:45–02:00) Metric statement
- Objects: Large stacked text; percent numbers.
- Anim: Staggered scale-in; light pulse on percentages.
- Duration: 450 frames.

### S9 (02:00–02:15) Hafal vs Mengerti
- Objects: Split cards; main text + subtext.
- Anim: Slide-in from sides; subtle bounce.
- Duration: 450 frames.

### S10 (02:15–02:30) Resolution cue
- Objects: Single text.
- Anim: Fade-in; hold.
- Duration: 450 frames.

### S11 (02:30–02:50) 6-step timeline
- Objects: Timeline bar; six icons; labels.
- Anim: L→R reveal; icon pops.
- Duration: 600 frames.

### S12 (02:50–03:05) Depth emphasis
- Objects: Timeline ghosted; overlay text.
- Anim: Fade overlay; slight scale.
- Duration: 450 frames.

### S13 (03:05–03:20) Clock reassurance
- Objects: Clock (circle + hands); text.
- Anim: Hand rotation; gentle pulse.
- Duration: 450 frames.

### S14 (03:20–03:40) Questions list
- Objects: Centered list; bold highlight on POWER FACTOR.
- Anim: Staggered fade/slide; color change on highlight.
- Duration: 600 frames.

### S15 (03:40–04:00) Answer anchor
- Objects: Text with bold segment.
- Anim: Fade + slight Y slide.
- Duration: 600 frames.

### S16 (04:00–04:20) Promise
- Objects: Three-line stack; small check icons.
- Anim: Sequential pop-in; small bounce.
- Duration: 600 frames.

### S17 (04:20–04:30) Call to start
- Objects: Text.
- Anim: Fade-in; fade-to-black last 10–15f.
- Duration: 300 frames.

## Export Steps
1) Render review: MP4 H.264, 1080p30, naming *_review_vNN.mp4
2) Render final: PNG sequence (RGBA) or ProRes4444 with alpha
3) Include: first-frame thumbnail + README (colors, speeds, angles)

## Delivery
- Place in production/core-001/animation/exports/
- Send alongside .blend file with packed resources or relative paths.

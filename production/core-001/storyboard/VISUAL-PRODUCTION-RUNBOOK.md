# Visual Production Runbook — CORE-001

Goal: Get animations + edits produced with zero ambiguity. Use this as the day-one handoff to animator & editor.

## Assets to hand off today
- Script cues: ../../01-MASTER-PLAN/05-CORE-001-PRODUCTION-PLAN.md (segment references)
- Teleprompter cue sheet: ../script/cue-sheet-teleprompter.md
- Shot list with durations: ../storyboard/shot-list-core-001.csv
- Animator brief: ../storyboard/brief-animator.md
- Editor brief: ../video/brief-editor.md
- Naming conventions: ../README-naming-conventions.md
- Pilot lines (for tone): ../script/pilot-pre-module-script.md

## Animation production (Phase 1 focus)
- Priority scenes (custom): VIS-01 (270s), VIS-02 (240s), MOD-02 (120s), SIM-02 (120s)
- Deliverables per scene:
  - MP4 review + ProRes4444/PNG sequence with alpha
  - First-frame thumbnail
  - Source file (AE/Blender) with organized layers
  - Parameter readme: colors, speeds, angles
- Approval path:
  - Step 1: Animatics for timing (no polish)
  - Step 2: Style pass
  - Step 3: Final render + alpha
- Rounds: Max 2 revisions per scene; turnaround 48–72h per batch

## Editing production
- Inputs: VO WAV per segment, slides, animations (alpha), screen captures
- Output: 6 segment videos, 1080p30, -14 LUFS, Rec.709
- Order of assembly:
  1) Segment 1–2 (use slides + light motion)
  2) Insert Animation 1 & 2 into Segment 3
  3) Segment 4 diagrams (slides/text callouts)
  4) Segment 5 derivation overlays
  5) Segment 6 simulator screen + case study b-roll
- Review: 2 rounds per segment; naming CORE001_SEG{1-6}_final_vNN.mp4

## File exchange & structure
- Project root: production/core-001/
- Place renders:
  - animation/exports/
  - audio/
  - video/
- Use naming: CORE001_SEG{#}_SCN{ID}_vNN.ext (animations), CORE001_SEG{#}_VO_vNN.wav (audio)

## Daily check-in (15 minutes)
- Animator: progress per scene, blockers, next upload
- Editor: segments assembled, missing assets, loudness check
- You: approvals, quick notes only

## Definition of Ready
- Script lines frozen for the scene
- Timing target agreed (from shot list)
- Visual references provided (colors, axes, labels)

## Definition of Done
- Review MP4 approved
- Alpha render + source file delivered
- Editor integrated and segment render passes QC
- Naming + folders correct

## QC checklist (spot-check per delivery)
- Labels legible at 1080p
- Color coding consistent (Real=blue, Imag=orange, Magnitude=green, Angle=purple)
- Motion smooth; no jitter
- Audio sync tight; loudness near -14 LUFS; peaks < -1 dBTP
- No spelling errors on text/axes

## Immediate next actions
- Send animator brief + shot list + cue sheet
- Request animatics for VIS-01 and VIS-02 first
- Prep VO WAVs for SEG-1/SEG-2 and share with editor
- Schedule first review in 48–72h

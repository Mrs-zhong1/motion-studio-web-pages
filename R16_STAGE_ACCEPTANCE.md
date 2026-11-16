# Motion Studio Web — R16 full-phase acceptance

**Channel:** public browser review (not production or commercially cleared)
**Pinned source:** `f9fdcdb23f0948308c97de3ceed74efebd898c14`
**CI:** https://github.com/Mrs-zhong1/motion-studio-web/actions/runs/43786444513
**Live:** https://mrs-zhong1.github.io/motion-studio-web-pages/review-preview.html
**Live proof:** [R14_LIVE_VERIFIED.json](./R14_LIVE_VERIFIED.json) (historical filename, current build verified)
**Media proof:** [R13_REVIEW_BUILD.json](./R13_REVIEW_BUILD.json)
**Actual browser screenshots:** https://github.com/Mrs-zhong1/motion-studio-web/blob/fix/u1-u2-template-first-20261114/stage9/visual-evidence/README.md

## Implemented during the R16 phase

| Node | Actual result | Browser evidence |
|---|---|---|
| R16-01 | Eight template-specific scroll-driven photographic reveals | `test_r16_story_transitions.py` |
| R16-02 | Separate photograph, heading and atmosphere depth/camera movement | `test_r16_multiplane_camera.py`, paired scroll frames |
| R16-03 | Adjacent chapter background color bridges and coordinated entrance/exit | `test_r16_cross_chapter.py`, paired seam frames |
| R16-04 | Real iframe/Three.js presentation handoff through exposure; existing camera transforms unchanged | Browser-computed filter and reduced-motion assertions |
| R16-05 | Scroll event rendering coalesced by requestAnimationFrame | Test dispatches 80 scroll events and requires <=3 redraws; this is **not** an FPS benchmark |
| R16-06 | Desktop/mobile checks, keyboard-accessible chapter nav, reduced-motion disable, photo/source inventory, screenshots and online SHA-256 | Chromium / Firefox / WebKit green, browser screenshots, GitHub Pages live verification |

## Verified

- 3/3 automated browser engine jobs passed.
- 8 templates × desktop/mobile geometry audit passed.
- 39/39 photographic chapter images embedded; zero generated fallback images at build time.
- Browser test exercised actual exported page scroll progress, overlay opacity, interactive iframe exposure, reduced-motion CSS and mobile overflow.
- Live HTTPS asset matched build SHA-256.

## NOT verified or not approved

- **Visual art direction:** reference-site equivalence and native design quality are not proven by automated tests.
- **Human review:** no final approval of the 8 complete visual narratives.
- **Actual device performance:** no real iPhone/Android/Safari GPU, sustained 60fps, memory or battery measurement. Software Chromium WebGL2 does not replace real-device testing.
- **Commercial images:** license, releases and depiction rights remain HOLD. Imported user images are not independently rights-cleared.
- **Production readiness:** this is a review build; do not claim commercial signoff.

## Next phase

R17 should work from the actual screenshot evidence: art-direct each template end to end, test native phones, remove or license unapproved imagery, then conduct explicit production acceptance. R16 engineering batch is complete on the review branch; these external acceptance gates remain open.

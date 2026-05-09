# Unified Diff

## Stage

Landing page scrollable analyst-problem hero pass.

## Files Changed

- `index.html`
- `docs/unified_diff.md`

## What Changed

- Added a compact scrollable hero right-rail card for spreadsheet users with the full conversational "Ever..." problem list.
- Split the scrollable list into `for spreadsheet people` and `for developers` chunks.
- Moved the existing `main.png` hero screenshot below the hero card as a wide proof image.
- Removed the separate Problems section so the first view carries the list directly.
- Kept the existing dark mono visual style, compact typography, borders, and card language.
- Kept the page static: no framework and no new JavaScript.

## Validation

- Parsed `index.html` with Python `HTMLParser`; no unclosed or mismatched tags found.
- Confirmed all in-page nav anchors point to existing IDs.
- Confirmed local image references exist, including `./main.png`.
- Confirmed mobile media query includes `.hero-shot-wide` and `.analyst-hook-card`.
- Confirmed no new JavaScript was added.
- `node --check script.js`
- `git diff --check`
- Confirmed the requested forbidden platform/governance phrases were not introduced in the page.
- Local browser layout smoke:
  - desktop nav stayed on one row at `1280px`
  - hero hook title rendered at `17px`
  - right-rail card rendered all 26 items and scrolls
  - no separate Problems section remained
  - mobile `.hero-grid` collapsed to one column and the card still scrolls

## Risks / Follow-Up

- The hero card is intentionally scrollable. Verify the right rail height feels right on the deployed desktop and mobile viewports.

---

## Stage

Landing page Model Memory copy pass.

## Files Changed

- `index.html`
- `docs/unified_diff.md`

## What Changed

- Added a hero proof line for Model Memory after the approved Methods proof line.
- Replaced the old spreadsheet memory desk-note item with Model Memory copy focused on institutional judgment and auditable execution context.
- Added a short Model Memory paragraph to the AI formulas section.
- Updated How It Works step 05 so Audit includes Model Memory context.
- Kept the page static: no new section, no new assets, no CSS changes, and no JavaScript changes.

## Validation

- Parsed `index.html` with Python `HTMLParser`; no unclosed or mismatched tags found.
- Confirmed the requested Model Memory copy appears in the hero proof list, desk-notes sidebar, AI formulas section, and Audit step.
- Confirmed forbidden visible copy is absent: AI learned, AI remembers you, chatbot memory, agent memory, brain, autonomous learning, self-improving, RAG, vector, prompt memory, personalization, hidden context.
- `node --check script.js`
- `git diff --check`

## Risks / Follow-Up

- The copy now names a newer capability. Keep future changes disciplined so Model Memory reads as approved institutional context, not hidden AI learning.

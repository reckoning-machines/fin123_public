# Unified Diff

## Stage

Homepage governed AI workflow copy pass.

## Files Changed

- `index.html`
- `docs/unified_diff.md`

## What Changed

- Layered in that `=AI()` can execute reviewed, chained Methods through the governed runtime.
- Updated hero, AI formulas, How It Works, DECISION_RECORD, and Reckoning Machines runtime copy.
- Added a compact `reckoning-machines` runtime section above `prompt123` and kept the company background section separate.
- Kept the existing page structure, screenshots, anchors, and static HTML implementation.

## Validation

- `python3 -m html.parser index.html`
- `git diff --check -- index.html docs/unified_diff.md`
- `tidy -qe index.html` was available but not usable as a pass/fail check because the installed parser rejects HTML5 sectioning tags already present on the page.

## Risks / Follow-Up

- None.

---

## Stage

Homepage PM copy completed-roadmap implementation.

## Files Changed

- `index.html`
- `docs/reports/homepage_pm_copy_completed_roadmap_implementation_report.md`
- `docs/unified_diff.md`

## What Changed

- Re-centered the homepage around the PM-facing story that the spreadsheet became a governed decision system.
- Rewrote the hero around build, branch, run, explain, and replay.
- Added the compact narrative bridge between the hero and institutional-decision section.
- Rewrote the institutional-decision section around Build, Branch, Run, Explain, and Replay.
- Pruned the hero hook rail while preserving the strongest PM pain points.
- Rewrote the product-surface Audit card to remove id/hash-heavy visible labels.
- Revised the Features section around lineage, one model across many companies, approved DATA, replay, and Audit.
- Tightened AI, Run Later, How It Works, YAP/Model Memory, asof123, and footer copy.
- Preserved screenshots, image assets, app links, walkthrough mailto, nav shape, and static HTML implementation.

## Validation

- Forbidden homepage jargon check.
- Anchor extraction and nav anchor resolution check.
- Link preservation checks for `app.fin123.dev`, `app.yap123.dev`, and walkthrough mailto.
- `git diff --check`

## Risks / Follow-Up

- Review the compact narrative bridge and pruned hook rail visually on desktop and mobile.
- Some completed-roadmap capabilities are described in copy but may not be visible in current screenshots.

---

## Stage

Homepage completed-roadmap PM copy plan final tightening.

## Files Changed

- `docs/plans/homepage_pm_copy_completed_roadmap_plan.md`
- `docs/unified_diff.md`

## What Changed

- Added visual-treatment guidance for the narrative bridge: compact paragraph, optionally slightly larger or in a restrained standalone panel, not a manifesto section.
- Added implementation priority order: hero, narrative bridge, Audit card rewrite, Features section, YAP/asof123 tightening, hook rail pruning, footer.
- Marked the hero line `Build in the grid. Branch the work. Run the model. Explain what changed. Replay the decision.` as tagline-quality compression that should not be diluted.
- Recommended placing the bridge between the hero and institutional-decision section as a transition.

## Validation

- `git diff --check`

## Risks / Follow-Up

- None.

---

## Stage

Homepage completed-roadmap PM copy plan narrative bridge.

## Files Changed

- `docs/plans/homepage_pm_copy_completed_roadmap_plan.md`
- `docs/unified_diff.md`

## What Changed

- Added a recommended one-paragraph narrative bridge explaining that spreadsheets moved from publishing artifacts to live institutional decision systems.
- Recommended placing the bridge between the hero and the governed institutional decisions section, or as the opening paragraph inside that section.
- Kept the guidance PM-facing and finance-native.
- Added explicit constraints not to expand the bridge into a manifesto and not to add Global Research Analyst Settlement or Spitzer history to homepage copy.

## Validation

- `git diff --check`

## Risks / Follow-Up

- None.

---

## Stage

asof123 homepage positioning pass.

## Files Changed

- `index.html`
- `docs/asof123_homepage_positioning_report.md`
- `docs/unified_diff.md`

## What Changed

- Added a lower homepage section titled `Every bug in finance software is secretly an "as of" bug.`
- Introduced asof123 as the temporal semantics layer for the Reckoning Machines stack.
- Positioned YAP as institutional memory, fin123 as governed execution, and asof123 as temporal truth.
- Clarified that asof123 governs temporal interpretation, not scheduling or workflow.
- Used only existing static HTML and existing visual styles.

## Validation

- No package manifest, frontend static test runner, pytest config, or test files were present.
- `pytest -q` found no tests to run.
- `git diff --check`
- ASCII markdown check on touched docs.

## Risks / Follow-Up

- None.

---

## Stage

YAP fin123 positioning copy pass.

## Files Changed

- `index.html`
- `docs/yap_fin123_positioning_copy_report.md`
- `docs/unified_diff.md`

## What Changed

- Updated the YAP frame headline to: `YAP remembers how the pod thinks. fin123 governs what the firm executes.`
- Reframed YAP as the conversational evidence layer for a pod.
- Clarified that selected YAP State can become a candidate fin123 Model Memory draft subject to approval.
- Clarified that YAP can retrieve read-only fin123 model state with provenance.
- Preserved the boundary that YAP does not mutate Runs, Results, or active Model Memory.
- Kept the existing demo image/frame structure and made no UI machinery or integration-behavior changes.

## Validation

- No package manifest, static frontend test runner, pytest config, or test files were present.
- `git diff --check`
- ASCII markdown check on touched docs.

## Risks / Follow-Up

- None.

---

## Stage

Homepage institutional decision graph pass.

## Files Changed

- `index.html`
- `docs/homepage_institutional_decision_graph_update_report.md`
- `docs/unified_diff.md`

## What Changed

- Updated the `How it works` flow copy to support the governed institutional decision operating-system framing.
- Preserved the `Model -> Version -> Scenario -> Run -> Results -> Audit` product contract.
- Added the supporting line that every institutional decision becomes an immutable, replayable execution artifact.
- Replaced the lower data-evidence terminal label with `INSTITUTIONAL_DECISION_GRAPH`.
- Replaced the lower terminal body with a broader institutional decision graph covering Fund, Pod, Model, Version, Scenario, Run, Results, Audit, Replay, Run Diff, Data Evidence, and AI / DATA Formula Evidence.
- Kept the page static: no React, no new JavaScript, and no new dependencies.

## Validation

- Confirmed the previous data-only terminal label is not used in `index.html`.
- Confirmed `INSTITUTIONAL_DECISION_GRAPH` appears in `index.html`.
- `git diff --check`
- ASCII scan on touched files.

## Risks / Follow-Up

- None.

---

## Stage

Landing page control-plane panel copy pass.

## Files Changed

- `index.html`
- `docs/unified_diff.md`

## What Changed

- Rewrote only the `.panel` contents under `A control plane for spreadsheet models`.
- Kept `Model -> Version -> Scenario -> Run -> Results -> Audit` as the first line in the panel.
- Removed the OS/governance thesis line from this section so it remains only in the hero.
- Removed the `reconstructable discretionary decision-making` phrase from homepage copy.
- Shortened the panel copy around Versions, Scenarios, Runs, Results, Audit, and `=DATA()`.

## Validation

- `git diff --check`
- Confirmed only the target panel copy changed in `index.html`.

## Risks / Follow-Up

- None.

---

## Stage

Landing page OS/governance thesis placement pass.

## Files Changed

- `index.html`
- `docs/unified_diff.md`

## What Changed

- Moved the OS/governance thesis line in the hero so it appears after the value paragraph and before the technical proof line.
- Kept the hero H1, value paragraph, and technical Rust/Run artifacts proof line unchanged.
- Added the same thesis line as the first paragraph in the control-plane panel.
- Added a lightweight `.thesis-line` class for the control-plane thesis paragraph while preserving the existing `contract-line` styling for `Model -> Version -> Scenario -> Run -> Results -> Audit`.

## Validation

- Parsed `index.html` with Python `HTMLParser`; no unclosed or mismatched tags found.
- `git diff --check`
- Confirmed the thesis line appears in both intended places.

## Risks / Follow-Up

- None.

---

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

---

## Stage

Landing page Medium read-more link pass.

## Files Changed

- `index.html`
- `docs/unified_diff.md`

## What Changed

- Added a quiet `Read more` row under the hero CTA buttons.
- Linked the two Reckoning Machines Medium articles:
  - `Spreadsheets were never meant to be production systems`
  - `Stripe removed payment logic from application code. fin123 removes spreadsheet logic.`
- Added small inline hero link styling that matches the existing dark mono visual system.
- Kept the page static: no new section, no new assets, no JavaScript, and no layout architecture change.

## Validation

- Parsed `index.html` with Python `HTMLParser`; no unclosed or mismatched tags found.
- Confirmed `hero-read-more`, both Medium URLs, and `Read more` copy are present.
- `node --check script.js`
- `git diff --check`

## Risks / Follow-Up

- Medium links are external dependencies. If the canonical articles move, update the hrefs here.

---

## Stage

Landing page Medium read-more placement adjustment.

## Files Changed

- `index.html`
- `docs/unified_diff.md`

## What Changed

- Moved the `Read more` Medium article row from under the hero CTA buttons to the bottom of the desk-notes card.
- Added a small top divider for the desk-notes read-more row.
- Kept the same two Medium links and did not add JavaScript, assets, or a new section.

## Validation

- Parsed `index.html` with Python `HTMLParser`; no unclosed or mismatched tags found.
- Confirmed the `Read more` row is inside `.analyst-hook-card` and no longer under `.hero-actions`.
- `node --check script.js`
- `git diff --check`

## Risks / Follow-Up

- The links now live inside the scrollable desk-notes card, so they appear after the full problem list rather than next to the primary CTA.

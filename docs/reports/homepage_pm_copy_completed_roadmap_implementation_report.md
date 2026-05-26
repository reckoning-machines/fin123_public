# Homepage PM Copy Completed Roadmap Implementation Report

## Files Changed

- `index.html`
- `docs/reports/homepage_pm_copy_completed_roadmap_implementation_report.md`
- `docs/unified_diff.md`

## Copy Strategy

The homepage copy now centers on one PM-facing operator story:

```text
The spreadsheet became a governed decision system.
```

The page collapses the product into the working loop:

```text
build -> branch -> run -> explain -> replay
```

The update keeps the existing static page structure, screenshots, app links, nav, and visual style. It reduces implementation-heavy visible copy and uses product language such as approved, replayable, explainable, reviewable, versioned, historical, and institutional.

## Major Sections Updated

- Refreshed metadata for lineage, replay, Audit, DATA, and AI.
- Rewrote the hero value copy and proof lines around build, branch, run, explain, and replay.
- Pruned the hook rail and preserved the strongest PM pain points.
- Added the compact narrative bridge between the hero and institutional-decision section.
- Rewrote the institutional-decision section around Build, Branch, Run, Explain, and Replay.
- Updated the hero screenshot caption.
- Rewrote the product-surface Audit card to remove id/hash-heavy visible labels.
- Revised the Features section around lineage, one model across many companies, approved DATA, replay, and Audit.
- Tightened AI, Run Later, How It Works, YAP/Model Memory, asof123, and footer copy.

## Validation Run

- Forbidden homepage jargon check:
  - `rg -n "replay identity|admissibility|Provider authority|Data Snapshot authority|TemporalContext|sidecars|mapping hashes|provider policy records|substrate internals|ontology|projection bridge|authority substrate" index.html`
  - Result: no matches.
- Anchor extraction:
  - `rg -n "href=\"#([^\"]+)\"" index.html`
- Link preservation checks for `app.fin123.dev`, `app.yap123.dev`, and walkthrough mailto.
- Nav anchor resolution check.
  - Result: no missing anchors.
- `git diff --check`
  - Result: passed.

## Remaining Risks

- The narrative bridge is intentionally compact, but it should be reviewed visually after deploy to make sure spacing does not make it feel like a separate manifesto section.
- The hook rail remains scrollable by design; the pruned list should still be checked on mobile.
- Some lower-page copy now references completed capabilities that may not be visible in current screenshots.

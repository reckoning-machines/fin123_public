# AAPL Proof Model Memory Feedback Loop Report

## Objective

Refine the AAPL proof section so it preserves `Same output. Three views.` while showing that approved YAP discussion can become Model Memory and inform future governed work.

## Files Changed

- `index.html`
- `docs/reports/aapl_proof_model_memory_feedback_loop_report.md`

## Visual Hierarchy Rationale

The AAPL proof still uses three primary cards:

- Spreadsheet
- Document
- YAP

Model Memory is rendered beneath the YAP card as a smaller subordinate card. It is visually separated from the primary flow so it does not read as a fourth Workbook view.

The loop is shown with:

- a downward arrow from YAP to Model Memory
- a small `MODEL MEMORY` card with `Approved discussion`
- a leftward feedback label: `Informs future governed work`

This keeps the section readable in a few seconds and avoids adding explanatory paragraph weight to the primary proof.

## Doctrine Validation

- `Same output. Three views.` remains unchanged.
- Spreadsheet, Document, and YAP remain the only primary cards.
- Model Memory is visually subordinate.
- Model Memory appears as substrate support, not a Workbook view.
- The loop communicates approved discussion -> Model Memory -> future governed work.
- The loop does not imply YAP automatically mutates the model.
- The loop does not imply chat mutates outputs.
- No new product concepts were added.
- No stale Document language was introduced.

## Validation Commands / Results

- `git diff --check -- index.html docs/reports/aapl_proof_model_memory_feedback_loop_report.md` passed.

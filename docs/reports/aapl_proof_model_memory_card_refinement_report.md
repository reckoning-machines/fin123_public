# AAPL Proof Model Memory Card Refinement Report

## Objective

Refine the AAPL proof Model Memory loop so the subordinate card explains both:

- what Model Memory contains
- what it does

The three primary Workbook view cards remain unchanged: Spreadsheet, Document, and YAP.

## Visual Rationale

The Model Memory element remains below the YAP card and smaller than the three primary AAPL cards.

The card now carries the semantic work:

> MODEL MEMORY
>
> Approved discussion
>
> ↓
>
> Informs future
> governed work

The external left arrow remains as a visual direction cue. It no longer carries explanatory text, so the loop reads as:

YAP -> approved discussion -> Model Memory -> future governed work -> feedback into later model work.

## Copy Changes

Before:

> MODEL MEMORY
>
> Approved discussion

External caption:

> Informs future governed work

After:

> MODEL MEMORY
>
> Approved discussion
>
> Informs future
> governed work

The external caption text was removed.

## Doctrine Validation

- `Same output. Three views.` remains unchanged.
- Spreadsheet, Document, and YAP remain the only primary cards.
- Model Memory remains subordinate and visually smaller.
- Model Memory is presented as substrate support, not a Workbook view.
- The loop communicates YAP discussion can be approved into Model Memory and inform future governed work.
- The loop does not imply YAP automatically edits the model.
- The loop does not imply Model Memory is a fourth Workbook view.
- No stale Document language was introduced.

## Validation Results

- `git diff --check -- index.html docs/reports/aapl_proof_model_memory_card_refinement_report.md` passed.

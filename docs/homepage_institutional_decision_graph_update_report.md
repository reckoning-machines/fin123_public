# Homepage Institutional Decision Graph Update Report

## Verdict

PASS

## Summary

- Updated the homepage `How it works` section to support the broader fin123 positioning as an operating system for governed institutional decisions.
- Kept the existing static HTML/CSS structure, terminal-style code panel, flow cards, typography, borders, and spacing.
- Replaced the narrow data-evidence terminal label and data-only hierarchy with `INSTITUTIONAL_DECISION_GRAPH`.
- Reframed the terminal body around Fund, Pod, Model, Version, Scenario, Run, Results, Audit, Replay, Run Diff, Data Evidence, and AI / DATA Formula Evidence.

## Validation

- Confirmed the previous data-only terminal label is not used in `index.html`.
- Confirmed `INSTITUTIONAL_DECISION_GRAPH` appears in `index.html`.
- Confirmed no React or new dependency was introduced.
- `git diff --check` passed.
- ASCII scan passed for touched files.

## Tests

- No package manifest or frontend/static test runner was present in this static site repo.

## Risk

- Low. The change is limited to homepage copy in the existing `How it works` section and documentation.

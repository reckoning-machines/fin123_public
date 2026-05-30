# Homepage Removed Architecture Sections

This file preserves detailed homepage material moved out of the landing page during the focused reduction pass. The homepage now leads with workflow positioning and keeps architecture as proof, not the main story.

## Run Later

Scheduled execution is the same Run model, just delayed. It references a saved model state, selected Scenarios, and selected company contexts. It never runs the mutable grid.

Run later means: run this saved model state with these Scenarios at this time. Use it for one name, a scenario pack, or a whole coverage universe. When it triggers, fin123 leaves the same Results and Audit trail as an interactive Run.

Headless running is not unattended Office automation. Microsoft's official guidance says it does not recommend or support automating Microsoft Office applications from unattended, non-interactive client applications or components because Office can become unstable or deadlock in that environment. By contrast, fin123 model Runs are executed from the saved model record and approved formula/data/AI definitions, not by opening Excel on a server.

- References the saved model state.
- Uses selected Scenarios and company contexts.
- Executes approved AI-assisted Formula definitions only.
- Produces reviewable Results, replay, and Audit.

## How It Works

The product contract is:

```text
Model -> Version -> Scenario -> Run -> Results -> Replay -> Audit
```

Every institutional decision becomes a replayable, explainable model record.

```text
Model
  -> Branch / Version
      -> Company + Scenario
          -> Run
              -> Approved DATA + AI Workflow Execution
              -> Results + Diff
              -> Replay + Audit
                  -> Data + Provider Evidence
                  -> AI Method + Approved Memory
                  -> YAP Chronology + Time Rules
```

## YAP Detailed Example

```text
@yap why did we lower $AAPL gross margin in Q3?

Response:

Gross margin was reduced from 46.2% to 44.8% in Scenario Base on 2026-05-12.

Primary drivers:
- Management commentary suggesting elevated NAND costs
- China mix deterioration concerns
- Temporary services mix normalization

Approved memory:
- Source: earnings reaction thread
- Approved by: JG
- Confidence: medium

Affected formulas:
- gross_margin_q3
- product_margin_assumption
```

## asof123

asof123 governs what time meant for the decision. It records market state, holidays, publication windows, effective dates, stale status, and replay-valid time context.

- YAP preserves the investment discussion and decision chronology.
- fin123 runs approved models, scenarios, estimates, and outputs.
- asof123 supplies the market clock, publication windows, and as-of rules.

Replay uses those same time rules instead of judging the past with today's information. A PM, analyst, risk team, or compliance reviewer can reconstruct what the desk could actually know at the time.

YAP preserves the thesis record. fin123 runs the model record. asof123 preserves the market clock. Together they make institutional decisions replayable and explainable.

## Reckoning Machines Runtime

Reckoning Machines is the runtime layer behind chained AI execution: methods, evidence, validation, typed outputs, replay, and audit.

```text
ReviewedMethod
  -> Evidence
      -> Validation
          -> TypedOutput
              -> Replay
                  -> Audit
```

## prompt123

prompt123 is a product in development and is not yet deployed to fin123.

prompt123 is optional prompt improvement before running. Reviewable, approved, audited, and nothing done silently.

It flags ambiguity, missing schema, hidden assumptions, nondeterministic wording, and unsafe external dependencies. If the prompt is unclear, prompt123 records findings instead of silently deciding what the user meant.

- Prompts are intent.
- Proofed prompts are drafts.
- Approved prompts are execution artifacts.
- Execution systems own approval and execution.
- prompt123 must never silently rewrite and execute prompts.

LLM-assisted proofing may propose clarifications or normalized draft language, but every suggestion remains advisory. Approval and execution stay with the analyst.

```text
PromptIntent
  -> PromptDraft
      -> ApprovedPrompt
          -> ExecutionArtifact
              -> Audit
```

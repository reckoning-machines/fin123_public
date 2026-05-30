# Homepage Landing Page Reduction Plan

## 1. Current Problem

The homepage now has the right core positioning:

```text
The spreadsheet for AI workflows in the model.
```

The first part of the page explains the product well: AI workflows live inside spreadsheet models, one workflow can serve multiple stakeholders, one workflow can run across coverage, and Bring Your Model answers the adoption objection.

The problem is length and density. The current homepage contains three pages in one:

1. Product positioning
   - Hero
   - AI Workflow Inside The Model
   - One Workflow. Four Stakeholders.
   - Build Once. Run Everywhere.
   - Bring Your Model.

2. Product tour
   - Product Surface
   - AI That Participates In The Model
   - Run Later
   - How It Works.

3. Architecture / manifesto
   - YAP
   - asof123
   - Reckoning Machines
   - prompt123
   - deeper replay/audit doctrine.

The landing page should make a qualified user want a walkthrough. It should not try to teach the full ontology, runtime philosophy, and product suite in one pass.

The reduction should preserve the core distinction:

```text
fin123 is not a generic workflow engine.
The model is the unit of work.
AI workflows participate inside the model.
```

## 2. Proposed Homepage Structure

Target homepage order:

1. Hero
2. AI Workflow Inside The Model
3. One Workflow. Four Stakeholders.
4. Build Once. Run Everywhere.
5. Bring Your Model
6. Product Surface, shortened
7. AI That Participates In The Model, shortened
8. Short Replay / Audit proof block
9. Short YAP / Model Memory proof block
10. Get Started

Recommended flow:

```text
Workflow value
→ coverage scale
→ existing model adoption
→ product proof
→ institutional proof
→ walkthrough CTA
```

The homepage should be understandable in under 60 seconds. Deeper doctrine should move to separate pages or linked docs.

## 3. Sections To Keep

### Hero

Keep the hero. It is the right positioning:

```text
The spreadsheet for AI workflows in the model.

ChatGPT and Claude gave analysts AI assistants.
fin123 lets them build reusable AI workflows directly inside the models that drive investment decisions.
Build once. Reuse everywhere.
```

Plan:

- Keep the headline and core supporting copy.
- Reduce the hero proof list. It is currently doing too much.
- Keep only the strongest proof lines:
  - Build in the grid.
  - Bring your model.
  - Run one model/workflow across the coverage universe.
  - AI workflows run inside the model.
  - Replay / Audit proof.
  - Sheet Warnings.
- Consider removing the long right-side hook rail or reducing it to 5-7 best items. It is strong but pushes the page toward exhaustive problem cataloging.

### AI Workflow Inside The Model

Keep this section as-is or nearly as-is. It explains what a workflow is.

Preserve:

```text
Management Commentary
        ↓
Credit Card Data
        ↓
Historical Seasonality
        ↓
Consensus Estimates
        ↓
AI Validation
        ↓
Forecast
        ↓
Spreadsheet Output
```

Preserve:

```text
A workflow is more than a prompt. It can retrieve evidence, compare history, apply approved context, validate assumptions, and return a typed result directly to the model.
```

### One Workflow. Four Stakeholders.

Keep this section. It is compact and effective.

Preserve the exact card language:

```text
Analyst
Build AI workflows directly inside the model.

PM
Run the same workflow across every company in coverage.

Head of Research
Institutionalize methodology.

Compliance / FINRA
Prove what happened.
```

Preserve the supporting sentence unless the page still feels long after other cuts.

### Build Once. Run Everywhere.

Keep this section. It explains the PM / coverage universe story.

Preserve:

```text
Retail Guidance Workflow
        ↓
TGT   WMT   COST   HD
        ↓
Result   Result   Result   Result
        ↓
Coverage Results
```

Preserve:

```text
Build a workflow once. Run it across a coverage universe while preserving assumptions, scenarios, audit history, replay context, and results for every company.
```

### Bring Your Model

Keep BYM. It answers the adoption objection.

Preserve the core idea:

- Analysts should not have to rebuild working Excel models to enter the fin123 ecosystem.
- Existing Excel models can bring formulas, Bloomberg links, Visible Alpha links, comments, and workbook structure.
- Once uploaded, the model gains versioning, Sheet Warnings, YAP context, Audit, replay, and `=AI()`.
- Comments can import into YAP for later promotion to Model Memory if approved.

The section can be tightened, but it should not be removed.

## 4. Sections To Compress

### Product Surface

Current issue: four screenshot cards create a product tour inside the homepage.

Plan:

- Keep one main product screenshot, preferably `main.png`.
- Replace the four screenshot-card tour with one concise panel:
  - spreadsheet remains the primary surface;
  - assumptions, outputs, scenarios, Runs, Results, replay, and Audit live around the model;
  - the product is build, branch, run, explain, replay.
- If screenshots remain, use one main screenshot plus 3-5 pills. Do not keep all four card-level explanations on the landing page.

Suggested copy:

```text
The grid stays primary. Analysts mark assumptions and outputs, add `=DATA()` and `=AI()` steps, save versions, run scenarios, and inspect Results without leaving the model surface.
```

### AI That Participates In The Model

Current issue: the section repeats the workflow argument and expands into FINRA/governance detail.

Plan:

- Shorten to one panel and one compact code example.
- Keep:
  - `=AI()` sits in a normal worksheet cell;
  - the approved definition lives behind the cell;
  - methods can retrieve evidence, compare history, validate assumptions, and return typed output;
  - Audit records method, inputs, validation, memory, chronology, and Run identity.
- Remove or move the long FINRA paragraph from this section. FINRA should appear only as short Compliance proof on the homepage.

### Workflow Behind The Number

Current issue: overlaps with Product Surface, How It Works, and Replay/Audit.

Plan:

- Replace the full four-card grid with a short Replay / Audit proof block.
- Keep the core proof:
  - versions preserve model states;
  - runs preserve company/scenario context;
  - replay reconstructs model state, data, AI method, memory, chronology, and time rules;
  - Audit shows what ran, what changed, evidence, and approval.

Suggested block title:

```text
Replay and Audit prove the workflow.
```

Suggested copy:

```text
Every workflow run leaves a reviewable record: model state, company, scenario, data evidence, AI method, approved memory, results, diff, replay context, and Audit.
```

### YAP

Current issue: YAP has become a second product tour with a screenshot, long doctrine, a knowledge-flow graphic, and a long AAPL example.

Plan:

- Keep YAP as workflow/memory proof, not a separate product narrative.
- Keep the "How Desk Knowledge Enters The Model" diagram.
- Remove the long AAPL example from the homepage.
- Remove most of the long explanatory prose.
- Keep only:
  - YAP captures discussion;
  - Model Memory captures approved knowledge;
  - AI workflows can use approved memory;
  - YAP is non-mutating and does not silently change Runs, Results, assumptions, or active Model Memory.

Suggested title:

```text
YAP and Model Memory: how desk knowledge enters future workflows.
```

Suggested supporting copy:

```text
Desk knowledge should not disappear into chat logs, email threads, or analyst notebooks. YAP captures discussion. Model Memory captures approved knowledge. AI workflows can use that approved knowledge inside the model.
```

### Hero Hook Rail

Current issue: the hook rail is compelling but long. It makes the first screen feel like a full objection-handling document.

Plan:

- Keep the strongest analyst hooks and remove developer hooks from the homepage.
- Keep hooks that map to the landing-page story:
  - filename sprawl;
  - model already works / BYM;
  - same model across coverage;
  - AI output belongs in the model;
  - compliance asks where a number came from;
  - fragile workbook / Sheet Warnings.
- Move developer-oriented jokes and longer doctrine into a separate article or docs page.

## 5. Sections To Move Off Homepage

### asof123

Move off the homepage or reduce to a one-line link inside Replay / Audit.

Reason: asof123 is important architecture, but it turns the landing page into a time/replay manifesto.

Homepage treatment:

```text
Replay uses the model state, data, provider evidence, AI method, memory, chronology, and time rules that applied then.
```

Optional link:

```text
Learn how asof123 handles market time and publication windows.
```

### Reckoning Machines Runtime

Move off the homepage.

Reason: runtime architecture is useful proof after interest exists, but it is too internal for a landing page.

Homepage treatment:

- Mention only indirectly through `=AI()` methods, evidence, validation, typed outputs, replay, and Audit.
- Move the full `ReviewedMethod -> Evidence -> Validation -> TypedOutput -> Replay -> Audit` ontology to a product/architecture page.

### prompt123

Move off the homepage.

Reason: it is in development and not deployed to fin123. It distracts from the core landing-page story.

Homepage treatment:

- Remove from the homepage.
- Preserve in a separate product roadmap or docs page if needed.

### Run Later

Compress heavily or move off homepage.

Reason: useful feature, but it is not core to the first sales story.

Homepage treatment options:

1. Remove from homepage and mention scheduled runs in the shortened product proof.
2. Keep one bullet in Product Surface:
   - schedule saved model states for later execution.

### How It Works

Compress or merge into Replay / Audit proof.

Reason: the six-step product contract is useful, but the landing page already shows workflow, stakeholders, coverage, BYM, and product surface.

Homepage treatment:

```text
Model -> Version -> Scenario -> Run -> Results -> Replay -> Audit
```

Use this as one compact line, not a whole section with flow cards and code.

### Reckoning Machines Company

Move or merge into Get Started.

Reason: company background belongs at the end, but it should not add another full section after the CTA.

Homepage treatment:

```text
Reckoning Machines builds finance-focused software for replayable, explainable model workflows.
```

Keep this as one sentence in Get Started if needed.

## 6. Exact Copy Blocks To Preserve

Preserve the hero:

```text
The spreadsheet for AI workflows in the model.

ChatGPT and Claude gave analysts AI assistants.
fin123 lets them build reusable AI workflows directly inside the models that drive investment decisions.
Build once. Reuse everywhere.
```

Preserve the workflow definition:

```text
A workflow is more than a prompt. It can retrieve evidence, compare history, apply approved context, validate assumptions, and return a typed result directly to the model.
```

Preserve the AI Workflow Inside The Model diagram:

```text
Management Commentary
        ↓
Credit Card Data
        ↓
Historical Seasonality
        ↓
Consensus Estimates
        ↓
AI Validation
        ↓
Forecast
        ↓
Spreadsheet Output
```

Preserve the stakeholder cards:

```text
Analyst
Build AI workflows directly inside the model.

PM
Run the same workflow across every company in coverage.

Head of Research
Institutionalize methodology.

Compliance / FINRA
Prove what happened.
```

Preserve the coverage diagram:

```text
Retail Guidance Workflow
        ↓
TGT   WMT   COST   HD
        ↓
Result   Result   Result   Result
        ↓
Coverage Results
```

Preserve the BYM lede:

```text
Analysts should not have to rebuild working Excel models to enter the fin123 ecosystem.
```

Preserve the core YAP / Model Memory diagram:

```text
Trader Observation

"Traffic looks weaker than expected."
        ↓

YAP Discussion

Analyst + PM + Trader debate it.
        ↓

Promote

Analyst approves observation.
        ↓

Model Memory

Weak traffic signal gets stored.
        ↓

Workflow

Future retail workflows can use it.
        ↓

Forecast

Estimate changes.
```

Preserve one compact product contract line:

```text
Model -> Version -> Scenario -> Run -> Results -> Replay -> Audit
```

## 7. Risks

- Cutting too much replay/audit copy could make fin123 sound like a generic AI workflow spreadsheet. Mitigation: keep a concise Replay / Audit proof block.
- Cutting too much YAP copy could make Model Memory feel unexplained. Mitigation: keep the desk-knowledge diagram and one paragraph.
- Keeping too many screenshots could preserve the current page bloat. Mitigation: keep one primary screenshot on the homepage and move deeper screenshots to a walkthrough/product page.
- Removing asof123, Reckoning Machines, and prompt123 entirely from public navigation could lose important product narrative. Mitigation: move them to linked docs/product pages or defer them behind "Read more" links.
- The hero proof rail may still dominate the first screen. Mitigation: reduce the hook rail and proof list during implementation if the first viewport still feels dense.
- Over-compressing BYM could weaken the adoption story. Mitigation: keep the BYM lede and concrete import details.

## 8. Acceptance Criteria

- Homepage can be understood in under 60 seconds.
- First few sections still communicate:
  - AI workflows inside the model.
  - One workflow serves four stakeholders.
  - Build once, run across coverage.
  - Bring existing models.
- The homepage no longer feels like a full architecture manifesto.
- YAP remains present, but as workflow/memory proof, not a second product tour.
- Replay/Audit remain present as institutional proof layers.
- asof123, Reckoning Machines, and prompt123 are not deleted from the product narrative; they are moved, linked, or deferred.
- The model remains the unit of work; fin123 does not read like a generic workflow engine.
- Existing screenshots are not replaced.
- No backend work, new assets, React, or external libraries are required.
- No implementation changes are made in this planning step.

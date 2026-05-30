# Homepage AI Workflow Repositioning Plan

## Objective

Reposition the homepage around a workflow-first story:

```text
The spreadsheet for AI workflows in the model.
```

Lead with analyst workflow value. Do not lead with governance. Replay, Audit, FINRA, YAP, Model Memory, asof123, and Bring Your Model are proof/support layers that show why the workflow is institutional-grade after the user understands the workflow.

This is a copy and information-architecture update with four focused homepage graphics. Do not turn this into a full visual redesign. Use the existing visual language, spacing, panels, and code/diagram treatments unless a small local style is necessary for readability.

## Core Positioning

The top-of-page story should say:

```text
ChatGPT and Claude gave analysts AI assistants.
fin123 lets them build reusable AI workflows directly inside the models that drive investment decisions.
Build once. Reuse everywhere.
```

The page should then show what that means:

1. What an AI workflow is.
2. How one workflow serves four stakeholders.
3. How one workflow scales across a coverage universe.
4. How desk knowledge enters the workflow architecture through YAP and Model Memory.

The four graphics should collectively explain the full fin123 architecture:

1. AI Workflow Inside The Model
   - What a workflow is.

2. One Workflow. Four Stakeholders.
   - Why different institutional users care.

3. Build Once. Run Everywhere.
   - How workflows scale across coverage.

4. How Desk Knowledge Enters The Model.
   - How institutional knowledge becomes part of future workflows.

Graphics 1-3 explain how workflows are built and scaled. Graphic 4 explains how workflows improve over time.

The page should communicate:

```text
Workflow
→ Coverage
→ Institutional Knowledge
→ Replay / Audit
```

Replay, Audit, FINRA, asof123, and governance remain proof layers after the workflow story is understood.

## Required Page Order

1. Hero
2. AI Workflow Inside The Model graphic
3. One Workflow. Four Stakeholders graphic
4. Build Once. Run Everywhere graphic
5. Why fin123?
6. Bring Your Model
7. Product Surface
8. Workflow Behind The Number
9. AI That Participates In The Model
10. Run Later
11. How It Works
12. YAP, including "How Desk Knowledge Enters The Model" graphic
13. asof123
14. Reckoning Machines
15. prompt123
16. Get Started / Company

## Four Required Graphics

### 1. AI Workflow Inside The Model

Purpose: explain what an AI workflow is.

Place this immediately after the hero. The graphic should make the abstract claim concrete before the page introduces stakeholders or governance proof.

Diagram text:

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

Supporting copy:

```text
A workflow is more than a prompt. It can retrieve evidence, compare history, apply approved context, validate assumptions, and return a typed result directly to the model.
```

Implementation guidance:

- Use a compact visual section, not a large product diagram.
- A `code-panel` can work if it feels native to the existing page.
- A simple stacked `.panel` with arrow dividers can also work.
- Keep the diagram readable on mobile.
- Do not add a new illustration system or external asset dependency.

### 2. One Workflow. Four Stakeholders.

Purpose: show that the same workflow has different value for different institutional users.

Place this immediately after "AI Workflow Inside The Model."

Keep the exact compressed card language:

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

Add one short sentence below the cards:

```text
The same workflow that helps an analyst move faster helps a PM scale analysis, a Head of Research standardize methodology, and Compliance explain how a decision was made.
```

Do not add chat language to the top stakeholder cards. YAP belongs later in the workflow architecture, not in this compressed stakeholder section.

### 3. Build Once. Run Everywhere.

Purpose: explain the PM / coverage universe story.

Place this immediately after "One Workflow. Four Stakeholders."

Diagram text:

```text
Retail Guidance Workflow
        ↓
TGT   WMT   COST   HD
        ↓
Result   Result   Result   Result
        ↓
Coverage Results
```

Supporting copy:

```text
Build a workflow once. Run it across a coverage universe while preserving assumptions, scenarios, audit history, replay context, and results for every company.
```

Implementation guidance:

- Keep this as a simple workflow/coverage diagram.
- Do not over-explain coverage mechanics in this section.
- The point is scale: one workflow, many companies, preserved execution context.
- This graphic should support the PM card without repeating the stakeholder copy verbatim.

### 4. How Desk Knowledge Enters The Model

Purpose: explain YAP as the institutional knowledge intake layer, not generic chat.

Place this inside the YAP section, not near the top stakeholder cards.

Use this exact diagram text:

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

Supporting copy:

```text
Desk knowledge should not disappear into chat logs, email threads, or analyst notebooks.

YAP captures discussion.
Model Memory captures approved knowledge.
AI workflows operationalize that knowledge inside the model.
Over time, workflows improve as the institution learns.
```

Why This Graphic Matters:

```text
Most systems stop at discussion.

fin123 provides a path from:

Observation
→ Discussion
→ Approval
→ Memory
→ Workflow
→ Forecast

This graphic explains how institutional knowledge becomes part of the investment process.
```

YAP framing requirements:

- YAP should not be positioned as generic chat.
- YAP is how desk observations and institutional discussion can become approved Model Memory.
- Model Memory can then inform future AI workflows inside the model.
- YAP remains non-mutating: it does not silently change Runs, Results, assumptions, or active Model Memory.
- YAP belongs in the workflow architecture, not as a standalone chat feature.

## Section-by-Section Plan

### 1. Hero

Use the existing headline:

```text
The spreadsheet for AI workflows in the model.
```

Use this supporting copy:

```text
ChatGPT and Claude gave analysts AI assistants.
fin123 lets them build reusable AI workflows directly inside the models that drive investment decisions.
Build once. Reuse everywhere.
```

Keep any additional proof line short. If "Versioned, replayable, auditable, and built for institutional use" remains, it should support the workflow claim rather than compete with it.

### 2. AI Workflow Inside The Model

Add the first required graphic immediately after the hero. This section should define "AI workflow" before the page introduces BYM, Audit, Replay, or governance concepts.

### 3. One Workflow. Four Stakeholders.

Use the second required graphic/card section. Keep the PM card only:

```text
Run the same workflow across every company in coverage.
```

Do not add chat language to the top stakeholder cards.

Optional copy test: consider changing the Head of Research card from "Institutionalize methodology." to "Institutionalize what the desk learns." only if implementation needs a stronger tie to "How Desk Knowledge Enters The Model." Do not make that change by default; preserve the compressed card language unless testing shows it reads better.

### 4. Build Once. Run Everywhere.

Use the third required graphic to make the coverage-universe story visual. This is the PM scaling proof immediately after the stakeholder section.

### 5. Why fin123?

Keep the existing narrative bridge, but make sure it now follows the workflow graphics. It should explain why spreadsheets became living institutional decision systems without becoming the lead message.

### 6. Bring Your Model

Keep BYM after the workflow-first story. BYM answers the adoption objection: analysts already have working Excel models.

Retain these BYM ideas:

- Analysts should not have to rebuild working Excel models to enter the fin123 ecosystem.
- Preserve formulas, Bloomberg links, Visible Alpha links, comments, and workbook structure.
- Once uploaded, the model gains fin123 versioning, Sheet Warnings, YAP context, Audit, replay, and governed `=AI()`.
- Comments import into YAP chat for later promotion to Model Memory if approved.

### 7. Product Surface

Keep the product surface section after BYM. It should show where the workflow lives: the spreadsheet remains the primary surface, with lineage, Results, Audit, and replay around it.

### 8. Workflow Behind The Number

Keep the existing proof section but align the language with the workflow-first message:

- Lineage and Branches preserve workflow/model state.
- One Model, Many Companies supports Build Once / Run Everywhere.
- Approved DATA supplies governed inputs.
- Replay and Audit explain the output.

### 9. AI That Participates In The Model

This section should deepen the workflow claim. It can explain that `=AI()` is not side chat or copy/paste; it executes reviewed methods as model steps with evidence, validation, typed output, Model Memory, YAP chronology, replay, and Audit.

### 10. Run Later

Keep this as execution proof. It should show that scheduled execution runs a saved model/workflow state, not a mutable open workbook.

### 11. How It Works

Keep the product contract, but ensure it reads as workflow architecture:

```text
Model -> Version -> Scenario -> Run -> Results -> Replay -> Audit
```

Do not let this section become the top-level positioning. It is proof after the workflow story.

### 12. YAP

Add the fourth required graphic, "How Desk Knowledge Enters The Model," inside this section.

The YAP copy should explain:

- YAP is not generic chat.
- YAP is the layer where desk observations and institutional discussion can become approved Model Memory.
- Model Memory can inform future AI workflows inside the model.
- YAP remains non-mutating and does not silently change Runs, Results, assumptions, or active Model Memory.

### 13. asof123

Keep asof123 as time/context proof. It should support replay and Audit by explaining how time rules, publication windows, market state, and stale status are preserved.

### 14. Reckoning Machines

Keep this as runtime proof for governed AI execution: methods, evidence, validation, typed outputs, replay, and Audit.

### 15. prompt123

Keep prompt123 clearly secondary and in development. Do not let it distract from the homepage's workflow-first story.

### 16. Get Started / Company

Keep calls to action and company context at the end.

## Navigation Guidance

Do not add multiple new nav links for the four graphics. The nav is already tight.

If one link is needed, use a single `Workflow` link to the first workflow graphic. Avoid separate nav entries for stakeholders, coverage, or YAP learning.

## Acceptance Criteria

- The plan explicitly includes all four graphics.
- "AI Workflow Inside The Model" explains what an AI workflow is.
- "One Workflow. Four Stakeholders." uses the exact compressed card language.
- The PM stakeholder card is only: "Run the same workflow across every company in coverage."
- The plan says not to add chat language to the top stakeholder cards.
- "Build Once. Run Everywhere." explains the PM / coverage universe story.
- "How Desk Knowledge Enters The Model" is added as the YAP-specific graphic.
- The plan preserves the Trader Observation -> YAP Discussion -> Promote -> Model Memory -> Workflow -> Forecast sequence exactly in the diagram text.
- A reader should understand how a trader observation can eventually influence a forecast through YAP, Model Memory, and workflows without reading the lower-page technical sections.
- The plan says YAP belongs in the workflow architecture, not as a standalone chat feature.
- The plan says YAP is non-mutating and does not silently change Runs, Results, assumptions, or active Model Memory.
- Replay, Audit, FINRA, YAP, Model Memory, asof123, and BYM are treated as proof/support layers.
- The plan leads with analyst workflow value, not governance.
- No broad page redesign is proposed.
- No implementation code changes are included in this plan update.

## Suggested Commit

```text
Update AI workflow homepage plan
```

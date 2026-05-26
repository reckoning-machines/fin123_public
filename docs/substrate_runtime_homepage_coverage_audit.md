# Substrate Runtime Homepage Coverage Audit

## Verdict

PARTIAL PASS

Under the assumption that the roadmap's deferred work is now implemented, `index.html` covers the core PM-facing story but does not yet communicate the full built product. The homepage is strong on spreadsheet-native execution, AI, Audit, Results, Run Diff, YAP, and the "spreadsheet time machine" idea. It is weaker on lineage, Branch workflows, one-model-many-entities execution, governed data mapping, durable replay, provider-backed replay, and asof123 as an active runtime capability.

The page is mostly PM-facing today. The risk is not that it is too engineering-heavy; the risk is that it under-sells important capabilities and uses some technical nouns without turning them into clear PM outcomes.

## Audit Scope

- Source roadmap: `/Users/jedgore/dev/fin123-pod/docs/top_plans/substrate_runtime_implementation_roadmap.md`
- Public page audited: `index.html`
- Assumption for this audit: previously deferred roadmap items should be treated as built.
- Constraint: the public page should remain PM-facing, not engineering-heavy.

## What The Homepage Already Includes

### Strongly Covered

- Spreadsheet-first product surface.
- "GitHub for spreadsheets" positioning.
- Model state as the unit of work.
- Immutable Versions.
- Scenarios and scenario comparison.
- Governed Runs.
- Run Sets and scheduled Runs.
- Results and Audit.
- Run Diff.
- Replay and "spreadsheet time machine" positioning.
- `=AI()` as a governed formula step.
- Approved Methods behind AI-assisted formulas.
- Model Memory as governed institutional context.
- `=DATA()` as the spreadsheet-facing data formula.
- YAP as the conversation and chronology layer.
- fin123 as governed execution authority.
- hosted app entry point.
- asof123 as temporal semantics positioning.
- Reckoning Machines as authority/substrate-first company positioning.

### Present But Too Thin

- One model across many companies/entities.
- Lineage as a daily PM workflow.
- Branches as collaboration and model-state organization.
- Durable replay identity as the reason old decisions can be reconstructed.
- Provider-backed replay as a practical "what did we know then?" capability.
- Data Binding mapping as an analyst-maintainable data governance workflow.
- Branch reset/promote as controlled reconciliation workflows.
- asof123 as active runtime time authority, not just positioning.

## Missing Or Underrepresented PM-Facing Capabilities

### Lineage And Branch Workflows

The homepage says Versions, Runs, Replay, and Diff, but it does not clearly explain the built lineage workflow:

- organize model work by Branch;
- see where a model state came from;
- compare the path from Version to Scenario to Run;
- promote reviewed work into a protected path;
- reset a working path when a team needs to reconcile back to a known-good state.

PM-facing wording should avoid implementation detail:

- "Keep investment work organized by model lineage, not filename sprawl."
- "Review the path from draft to approved model state."
- "Promote reviewed work without rewriting history."
- "Reset a working path back to a governed state when the analysis needs to be cleaned up."

### One Model, Many Companies

The hero mentions "one model, many companies," but this deserves its own product statement. PMs should immediately understand that one approved model can run across a coverage universe while preserving company-specific context.

Recommended PM framing:

- "Run the same approved model across a whole coverage universe."
- "Each company keeps its own data, assumptions, Run history, Audit, and replay context."
- "Compare companies without losing the execution context behind each number."

### Governed Data Mapping

The page shows `=DATA("bank.net_interest_income")`, but it does not explain the built mapping workflow in PM terms.

Recommended PM framing:

- "Analysts use one formula shape for approved internal and external data."
- "The platform maps business concepts to the right provider fields, calendars, and entity identifiers."
- "When a mapping changes, Runs still know which mapping version they used."

Avoid homepage terms like mapping hashes, provider authority records, and sidecars. The PM outcome is that data is easier to use and safer to audit.

### Provider-Backed Replay

If provider-backed replay is now implemented, the homepage should say this more clearly. Today it implies historical reconstruction, but it does not explain why a PM should trust it.

Recommended PM framing:

- "Replay a decision using the data, mappings, provider evidence, AI context, and model state admitted for that point in time."
- "See when a value came from a stored Run artifact, an approved data snapshot, or provider-backed replay."
- "No silent fallback to the latest file or today's provider value."

### Durable Replay

The homepage uses "replay" heavily, but it does not explain the business value of durable replay identity.

Recommended PM framing:

- "Every replayable decision has a stable reconstruction record."
- "Compliance can return to the same replay package later and get the same explanation."
- "Replay is a governed object, not a best-effort rerun."

### Memory And YAP As Admitted Decision Context

The YAP section is vivid, but it still reads mostly as linked conversation plus memory proposal. If Memory and YAP admissibility are now done, the page should make the upgraded value clear:

- YAP preserves the decision chronology;
- selected YAP evidence can become admitted decision context;
- approved Model Memory can participate in replayable AI execution;
- Audit shows what memory and chronology were admitted.

PM-facing wording:

- "The model can remember approved institutional judgment, and Audit shows exactly which memory was used."
- "YAP preserves the discussion trail and can attach admitted decision context to the model record."

### asof123 Runtime Capability

The asof123 section is good conceptually, but it should read as an active runtime capability if that work is now complete.

Recommended PM framing:

- "asof123 records what time meant for the decision: market state, publication windows, holidays, effective dates, and stale/admissible status."
- "Replay uses the same as-of rules instead of judging the past with today's information."
- "PMs can separate a bad decision from a decision made with information that was valid at the time."

### Authority Evidence In Audit

The homepage says Audit proves the Run, but it can say more about the review experience without exposing backend nouns:

- "Audit shows the model state, scenario, data evidence, provider evidence, AI method, memory, chronology, and replay package behind the result."
- "Reviewers can see what was used, what changed, who approved it, and whether the evidence was valid for that time."

## PM-Facing Coverage Map

| Roadmap capability | Homepage status | PM-facing action |
| --- | --- | --- |
| Model / Version / Scenario / Run / Results / Audit | Strong | Keep as the core contract. |
| Run Diff | Strong | Keep tied to "why did the number move?" |
| Scheduled Runs | Strong | Keep as delayed governed execution. |
| `=AI()` and Methods | Strong | Add memory/replay participation if built. |
| `=DATA()` | Partial | Add governed mapping and provider-backed replay value. |
| Entity Context / Universe | Partial | Add one-model-many-companies explanation. |
| Branch / lineage | Weak | Add PM-facing lineage, promote, reset, and protected path copy. |
| Durable replay identity | Weak | Explain replay as stable reconstruction, not just rerun. |
| Provider-backed replay | Weak | Explain historical provider evidence without provider jargon. |
| Memory/YAP admissibility | Partial | Explain admitted memory and chronology. |
| asof123 runtime | Partial | Reframe from concept to active time authority. |
| Hosted distribution | Partial | Explain governed delivery and access, not just app link. |

## Recommended Homepage Story

The PM-facing homepage should compress the full built system into six promises:

1. Build models in the spreadsheet.
2. Save, branch, run, and promote model states without filename sprawl.
3. Run one model across many companies and scenarios.
4. Use governed data and governed AI inside execution.
5. Replay decisions with the model state, data, AI context, memory, chronology, and time rules that applied then.
6. Show Audit, Results, Diff, and lineage when a PM, risk team, or compliance reviewer asks why a number changed.

Recommended product vocabulary:

- workbook;
- Version;
- Branch;
- Scenario;
- Run;
- Results;
- Audit;
- Diff;
- Replay;
- lineage;
- governed data;
- governed AI;
- institutional memory;
- chronology;
- time context;
- coverage universe.

Avoid homepage vocabulary unless it appears in a deeper technical page:

- replay identity;
- admissibility;
- Provider authority;
- Data Snapshot authority;
- TemporalContext;
- sidecars;
- mapping hashes;
- provider policy records.

## Priority Fix List

1. Add a PM-facing lineage/Branch section that covers protected paths, promote, reset, and model history without using Git internals.
2. Add a "one model, many companies" section or card that explains entity/context execution across a universe.
3. Strengthen `=DATA()` copy around governed mappings, provider evidence, and historical replay.
4. Strengthen replay copy so it says stable governed reconstruction, not only "time machine."
5. Upgrade YAP and Model Memory copy to include admitted decision context and replayable AI context.
6. Reframe asof123 as active runtime time authority.
7. Add a compact Audit value statement that includes data evidence, provider evidence, AI method, memory, chronology, replay, and as-of time.
8. Keep implementation nouns out of the main page; move them to technical docs or walkthrough material.

## Suggested Homepage Copy Blocks

### Lineage

"Keep every model state on a governed path. Analysts can branch work, compare changes, promote reviewed versions, and reset a working path without rewriting the history behind prior decisions."

### One Model, Many Companies

"Run one approved model across a whole coverage universe. Each company keeps its own assumptions, data bindings, Runs, Results, Audit, and replay context."

### Governed Replay

"Replay a decision with the model version, scenario, data evidence, provider context, AI method, memory, conversation chronology, and market-time rules that applied then."

### Audit

"Audit shows what ran, what changed, which evidence was used, who approved it, and why the result was valid at that point in time."

## Final Assessment

`index.html` includes much of the built product and is appropriately PM-facing. Under the assumption that deferred roadmap work is now complete, the homepage should be expanded: it needs clearer coverage of lineage/Branch workflows, entity-context execution, governed data mapping, durable/provider-backed replay, admitted Memory/YAP context, and asof123 runtime time authority. The page should keep the current simple language, but it should claim the full PM value of the system now that those capabilities are assumed to exist.

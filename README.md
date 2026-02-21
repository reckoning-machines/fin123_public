# fin123

Deterministic financial model infrastructure.

Author spreadsheet models. Run them headlessly, versioned, and reproducibly.

Built on Polars for high-performance execution. Model, data, and formatting are strictly separated. No drift. No surprises.

---

## What fin123 is

fin123 is infrastructure for financial model execution.

It applies software engineering discipline to spreadsheet-based modeling:

- Explicit lifecycle: Commit → Build → Verify → Release  
- Deterministic builds from versioned model logic  
- Offline evaluation with reproducible inputs  
- Immutable artifacts with traceable provenance  

fin123 is not a spreadsheet clone. It focuses on the model-building core — not replicating Excel’s entire UI surface area.

---

## Core Principles

### Determinism

Given the same committed model and the same local inputs, fin123 will produce identical outputs.

Build artifacts are versioned and fingerprinted. Verification confirms integrity and guards against drift.

---

### Separation of Concerns

fin123 separates:

- Model logic  
- Input data  
- Formatting and presentation  

The model is versioned independently from vendor or market data. Data is synchronized into local caches ahead of execution. Builds never depend on live database calls.

Formatting is not treated as the system of record.

---

### Headless First

Models are executed via CLI. A GUI is optional.

The lifecycle is enforced regardless of interface.

---

### No PRINT Button — By Design

fin123 is not optimized for slide decks.

It produces build artifacts intended for verification, review, and downstream consumption.

If you need presentation output, generate it from released data — not from live model state.

---

## Key Features

### Two-Graph Computation Model

Scalar computation and table computation are evaluated separately.

Scalars resolve as explicit dependency graphs.  
Tables execute as optimized query plans before materialization.

This separation keeps evaluation predictable and auditable.

---

### Offline Builds with Controlled Sync

External data access is isolated to a sync step.

Sync writes local caches.  
Build reads only local files.  
No live queries during evaluation.

This enforces reproducibility.

---

### Guardrails for Financial Integrity

- Schema expectations can be enforced  
- Lookup cardinality can be validated  
- Ambiguous joins fail fast  
- Missing required data fails explicitly  

Silent row multiplication is unacceptable in financial models.

---

### Versioned Artifacts and Provenance

Every build produces immutable outputs and records the lineage required to reproduce them.

Models are snapshotted.  
Inputs are fingerprinted.  
Artifacts are versioned.  

Releases are explicit promotions of verified builds.

---

### Scenario and Parameter Sweeps

Running the same model across many entities or parameter sets is a first-class workflow.

Each build remains independently identifiable, while still supporting batch grouping for reporting and release management.

---

### Bounded Storage

Retention policies prevent unbounded disk growth.

Recent and pinned artifacts are protected.  
Old, unpinned history can be safely removed according to policy.

---

### Extensible Connectors and Workflows

Data acquisition and auxiliary workflows are pluggable.

Connectors produce cached datasheets.  
Workflows produce versioned artifacts.  

AI may be used to produce artifacts — but it is never embedded in live cell evaluation.

---

### Database Optional

fin123 runs fully standalone on the filesystem.

A database-backed registry and headless runner can be enabled for centralized execution and team visibility, but they are not required for deterministic builds.

---

## Intended Audience

fin123 is built for:

- Financial analysts who care about reproducibility  
- Research teams running large parameter sweeps  
- Engineering teams supporting financial model workflows  
- Firms that require auditability and release discipline  

---

## Status

fin123 is under active development.

A compiled release will be available soon.

---

Questions?  
jedgore1@gmail.com
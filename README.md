# fin123 — The operating standard for financial models

Faster than Excel. Built like software. Designed for finance.

**Website:** [fin123.reckoningmachines.com](https://fin123.reckoningmachines.com) *(or open `index.html` locally)*

---

## One system. Three products.

Financial models should behave like software. fin123 starts as a standalone spreadsheet system, extends into applications as a worksheet runtime, and scales into a hosted platform for governed delivery.

### 1. Standalone spreadsheet runtime

Use fin123 as a finance-grade spreadsheet and modeling system on your own machine. Build models, run scenarios, verify outputs, and ship deterministic artifacts — no server required. Fast grid UX, explicit parameters, deterministic builds, auditability, and headless execution.

### 2. Embeddable worksheet runtime

Internal tools and trading desk applications repeatedly rebuild spreadsheet logic in application code. fin123 moves that logic into a worksheet specification that compiles into a deterministic artifact. The calculations live in the worksheet — not your application code.

```
WorksheetView → CompiledWorksheet → Viewer embedded in app
```

### 3. Hosted worksheet platform (Pod)

Teams can publish, approve, release, and serve compiled worksheets from a central system. Applications request released worksheet artifacts over an API instead of re-implementing spreadsheet logic locally. Worksheets become governed, versioned infrastructure — not one-off UI code.

---

## Repositories

| Repository | Description | License |
|---|---|---|
| [**fin123-core**](https://github.com/reckoning-machines/fin123-core) | Deterministic financial modeling engine. Polars-backed workbook engine, Excel-like formula language, local browser UI, deterministic build/verify lifecycle, XLSX import, scenario sweeps, and headless execution. Runs entirely locally. | Apache-2.0 |
| [**fin123-pod**](https://github.com/reckoning-machines/fin123-pod) | Enterprise platform layer. Adds database-backed registries, headless runner, data connectors (Bloomberg, SQL), plugin system, workflow automation, release governance, and hosted worksheet delivery. Depends on fin123-core. | Proprietary |

---

## Why teams switch

- **Faster than Excel** — columnar compute engine designed for financial workloads
- **Built like software** — commit, build, verify, release lifecycle with native versioning and audit
- **Parameters and scenarios are first-class** — explicit system inputs and structured overlays, not hidden cell edits
- **Headless at scale** — run committed models across tickers, scenarios, and parameter sets without a UI
- **Bloomberg-connected** — vendor data synchronized into governed local caches for offline, reproducible builds
- **AI as a controlled tool** — AI can generate artifacts and assist workflows but does not run inside deterministic computation
- **Embeddable worksheets** — compile calculation logic into portable artifacts that applications render directly

---

## Quick start

**Core** (open source):

```bash
pip install "fin123-core @ git+https://github.com/reckoning-machines/fin123-core.git@main"
fin123 doctor
fin123 init my-model
fin123 build my-model
```

Or download a binary from [releases](https://github.com/reckoning-machines/fin123-core/releases).

**Pod** (proprietary — [contact us](mailto:jed@reckoningmachines.com?subject=fin123-pod%20access%20request) for access):

```bash
pip install "fin123-pod @ git+https://github.com/reckoning-machines/fin123-pod.git@main"
```

---

## Contact

- **Walkthrough request:** [jed@reckoningmachines.com](mailto:jed@reckoningmachines.com?subject=fin123%20walkthrough%20request)
- **General:** [reckoningmachines@gmail.com](mailto:reckoningmachines@gmail.com)

# Homepage Visual Language Rewrite Report

## What changed

Reworked the public homepage from a capability-heavy marketing page into a product-forward page centered on:

- Work the way you think.
- Research velocity.
- Institutional memory.
- The Model.
- The investment research operating system.

The hero now leads with the emotional hook, a quiet category line, a concise thesis, one primary CTA, and a search-style product entry metaphor.

The post-hero body was restored away from the sparse essay version and back toward a product walkthrough organized around the analyst's day:

- Start with the thought.
- Open a Model.
- Explore an idea.
- Understand what changed.
- Preserve how your team thinks.
- Wake up to what's changed.
- Everything else follows.

The `search.png` product screenshot was added directly after the hero as the "Start with the thought" surface. `product.png`, `surface.png`, `aimethod.png`, and the audit screenshot are used as concrete product moments instead of turning the body into doctrine.

## Moving Away From Standard SaaS Formatting

The page no longer relies on a bordered hero card, dense hero pills, comparison-table energy, or a long feature grid tour.

The browser page is treated as the canvas. Whitespace, typography, and a single search focal point now carry the first screen.

Feature-card density was reduced without turning the body into abstract doctrine. Sections now use strong product surfaces, screenshots, and concrete analyst actions to explain what fin123 does.

## Hero Priority

The hero prioritizes:

- Emotion: `Work the way you think.`
- Outcome: `Built for research velocity.`
- Long-term value: `Designed for institutional memory.`
- Category: `The investment research operating system.`

The hero search bar is used as the metaphor for starting with the thought. Its placeholder now rotates through a small analyst story: `AAPL`, `What changed?`, `Why did EPS move?`, `Lower Services growth 2%`, `Compare to last quarter`, `Retail guidance method`, and `Promote to Model`.

The full search screenshot appears immediately after the hero as product evidence, not as a second hero.

## Colors And Gradients

The design moved to a warm white / pale aqua system:

- Canvas near `#FCFEFE`
- Surface near `#F8FBFB`
- Elevated white
- Deep charcoal text
- Restrained teal accent
- Soft borders using `rgba(18, 40, 55, 0.08)`

Gradients were softened and enlarged so they read as ambient daylight rather than decorative blobs or AI glow.

## Typography

The page now uses a modern sans-serif stack for primary display and body copy, with Inter loaded as the preferred web font.

JetBrains Mono remains as an accent for:

- the fin123 logo
- navigation
- search prompt
- formula references such as `=DATA()` and `=AI()`

The hero headline is large and emotionally dominant. The page avoids letting many tiny type sizes compete above the fold.

## Product Concepts

The Model is presented through the "Open a Model" product moment, with research velocity and institutional memory as outcomes of keeping reasoning attached to Model work.

Explore is represented as the analyst's canvas: try an idea, see what changed, compare alternatives, keep what matters, and walk away from the rest. The product sequence mirrors the rotating search story.

The new "Understand what changed" section uses the audit/proof surface to show Results, evidence, run diffs, and proof attached to Model work.

Methods are positioned as reusable firm judgment: how the firm thinks, not prompt storage. AI Method and AI Formula remain present, but Method is bigger than AI.

Analytical language is represented through analyst-native commands. The public copy says fin123 turns analyst intent into governed Model operations and shows the proof.

Headless overnight work is represented as preparation: refreshed evidence, prepared Model updates, changed assumptions, and attention items. The authority boundary is explicit: overnight preparation is not hidden canonical mutation, and the analyst still decides what to keep.

## Governance

Governance is demoted to exhaust and proof-on-demand.

The page says: `Governance is exhaust, not the product.`

Timeline, Memory, Report, Audit, Replay, Provenance, and Governance are framed as emitted representations of the same reasoning because the reasoning happened in fin123.

## Reservations / TODOs

- The page still uses existing screenshots. A future screenshot pass should capture the calmer search/product entry experience directly.
- The CSS still contains some legacy component styles used by previous sections. They do not dominate the current rendered page, but a later cleanup could remove unused selectors.
- Browser-level visual QA was limited by local Chromium sandbox restrictions during this pass; static HTML validation was completed.

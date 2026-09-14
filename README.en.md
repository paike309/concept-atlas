# Concept Atlas

A bilingual knowledge base for **AI, agent, and software engineering** concepts.

The organizing principle is **dependency, not alphabet**. Every card must state what you need to understand before reading it. That single rule turns the collection into a directed graph, so the reading order comes from the graph instead of from a table of contents.

The primary language of this repository is Chinese (the author's working language for study notes). English is preserved for every term, and each card carries a one-sentence English definition so the concepts stay aligned with the field's standard vocabulary.

---

## Structure

| Layer | Location | Question it answers |
|---|---|---|
| Maps | [`maps/`](maps/) | In what order should I read? Where am I stuck? |
| Cards | [`concepts/`](concepts/) | What is this concept? |
| Inventory | [`roadmap.md`](roadmap.md) | What is still missing in this domain? |

A map is not a table of contents. It records dependencies and, more usefully, a diagnostic table: **if you are stuck on card *n*, the gap is usually in card *n−1*.**

---

## Card format

Every card has eight fixed sections. Five are conventional; three exist to prevent the illusion of understanding:

| Section | Purpose |
|---|---|
| One-sentence definition | One sentence in Chinese, one in English |
| **My understanding** | In the author's own words. This section cannot be delegated to AI |
| Core mechanism | How it works internally. Orders of magnitude, never "it's big" or "it's fast" |
| **Boundary: what it is not** | Where the most confusable neighbouring concepts differ |
| Common misconceptions | Written as "misconception → what actually happens" |
| When to use it | Decision criteria, not a feature list |
| **Self-test** | Asks "why" and "how would you tell", not "define X" |
| Source mapping | Which source supports which section above |

The bolded three are what separate this repository from a collection of excerpts.

Full spec: [`docs/schema.md`](docs/schema.md). Template: [`docs/template.md`](docs/template.md).

---

## Bilingual convention

There is **no `zh/` and `en/` directory pair**. Parallel trees diverge the moment one side is revised, and after that you cannot tell which side is current.

Instead:

- Card titles are `中文名 · English Term`
- Attribute tables carry dedicated `英文` (English) and `别名` (aliases) rows
- The one-sentence definition appears in both languages
- The body is written in Chinese, with the English term preserved at first occurrence — e.g. 注意力机制 Attention, 控制反转 IoC — and Chinese thereafter
- File names and paths are ASCII slugs; Chinese appears only in titles and prose, because paths end up in URLs

---

## Diagrams

Diagrams are **Mermaid** in fenced code blocks. GitHub renders them natively — no tooling, no build step, no deployment.

Start at [`maps/overview.md`](maps/overview.md).

---

## Status and provenance

**Card status**: `stub` (skeleton only) · `stable` (self-consistent, reliable) · `stale` (possibly outdated)

**Provenance level**, recorded in each card's attribute table:

| Level | Meaning |
|---|---|
| `unverified` | AI-generated or quickly excerpted, not checked item by item |
| `machine-confirmed` | Every source link opened and confirmed reachable; prose not yet rewritten by hand |
| `human-reviewed` | Prose read sentence by sentence; "My understanding" is in the author's own words |

A card whose "last checked" date is over a year old is treated as `stale`.

This field is not ceremony. Months later it is the only reliable way to distinguish "I understand this" from "I once saved this".

---

## Provenance of the structure itself

- [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — bundle/concept definitions, and the provenance and trust fields
- [iwe](https://github.com/iwe-org/iwe) — separating inclusion links from cross-references; one document under multiple parents
- [ai-llm-glossary](https://github.com/JingHao-Leon/ai-llm-glossary) — the bilingual term + one-sentence definition + short explanation format
- [ai-concept-learner](https://github.com/178-com/ai-skill-mawenwen-) — fixed-section generation followed by human verification

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
| `link-checked` | Links machine-verified: reachable, and pointing at the resource the card claims. Does **not** mean the source supports the prose |
| `machine-confirmed` | Every source checked against the specific paragraph it is cited for |
| `human-reviewed` | Prose read sentence by sentence; "My understanding" is in the author's own words |

The four levels are progressive. **Skipping a level is the usual way this field degrades** — treating "the link opens" as "the claim is supported", and then "the claim is supported" as "I understand this".

A card whose "last checked" date is over a year old is treated as `stale`.

This field is not ceremony. Months later it is the only reliable way to distinguish "I understand this" from "I once saved this".

**Current status: 76 of 77 cards are `link-checked`, one is `unverified`.**

A first machine pass has been done: all 35 arXiv identifiers were matched against their actual paper titles (zero mismatches) and all other source links were checked for reachability. That pass found and fixed 10 problems — including one case of **mislabeling**, where the first five cards claimed `human-reviewed` without that review ever having happened.

What `link-checked` does **not** mean: the prose has not been compared sentence by sentence against the sources, and no order-of-magnitude figures have been measured. So the guarantees are "the right paper is cited", not "the paper supports this sentence".

Full record, including what was *not* done, is in [`docs/verification-log.md`](docs/verification-log.md).

The correct way to use this repository right now is therefore still as an **index and a question list** — to see which concepts exist and how they depend on each other — not as a source of facts.

---

## License and round 2

- Knowledge content (the prose under `concepts/`, `maps/`, and `docs/`) is licensed **CC BY-SA 4.0** — see [LICENSE](LICENSE). Code and build scripts (`scripts/`) are **MIT** — see [LICENSE-CODE](LICENSE-CODE).
- Round 1 only machine-checked the source links (`link-checked`). The round-2 checklist and its discipline are in [docs/round2-verification-checklist.md](docs/round2-verification-checklist.md); per-card conclusions accumulate in [docs/verification-log.md](docs/verification-log.md).

---

## Provenance of the structure itself

- [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — bundle/concept definitions, and the provenance and trust fields
- [iwe](https://github.com/iwe-org/iwe) — separating inclusion links from cross-references; one document under multiple parents
- [ai-llm-glossary](https://github.com/JingHao-Leon/ai-llm-glossary) — the bilingual term + one-sentence definition + short explanation format
- [ai-concept-learner](https://github.com/178-com/ai-skill-mawenwen-) — fixed-section generation followed by human verification

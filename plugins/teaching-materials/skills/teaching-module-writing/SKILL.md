---
name: teaching-module-writing
description: How to write a per-meeting teaching module (modul ajar / bahan ajar pertemuan) section by section — measurable learning outcomes, concept map, content, common-mistakes table, practicum timeline, graded exercises (◆ / ◆◆ / ◆◆◆), slide outline, references, figure/table register, and notes for the future textbook chapter — with constructive alignment between outcomes, content, practicum, exercises, and assessment. Works with rps-alignment, which decides what material is allowed. Use when writing a new module, rewriting or expanding a section, designing exercises or a practicum, or drafting learning outcomes. Triggers in English and Indonesian — teaching module, lesson, handout, learning outcomes, exercises, lab session, modul, bahan ajar, pertemuan, praktikum, latihan soal, capaian pembelajaran, peta konsep.
---

# Teaching Module Writing

Respond in the user's language; write the module in the course's language. The skeleton is in
`references/templat-modul.md`, pedagogy tables in `references/pedagogi.md`.

## Step zero

Use `rps-alignment` alongside this skill; it wins where they differ. It decides *what* may be
in the module (the RPS material for that meeting, locked items, the traceability matrix). This
skill decides *how* to write it.

Before writing a sentence:

1. Read the meeting's row in the traceability matrix — RPS material, module number, chapter,
   slide count.
2. Read the modules before and after (prerequisites; what is deferred).
3. If a linked course must lead or follow, read its matching module.

## Principles

**Constructive alignment.** Outcomes (A) → content (C) → practicum (E) → exercises (G) →
assessment must point at the same things. Quick test: every outcome has at least one content
subsection, one practicum step, and one exercise testing exactly it. An outcome tested nowhere
is removed or tested; an exercise testing no outcome is removed.

**Explain why.** Every rule comes with the consequence of breaking it, so the reader knows it is
not taste.

**Real, local examples.** Campus administration, cooperatives, small businesses, public data from
the region — not `foo`, `bar`, `data_dummy`.

**A module is for the lecturer in class, not for reading alone.** It may be brief where the
lecturer explains aloud — but section K records what the textbook chapter must write out in full.

## Section by section

| Section | Good content | Avoid |
|---|---|---|
| **Metadata** | Course, meeting "N of 16", time allocation matching SKS, CPMK/Sub-CPMK, prerequisites, pre-reading, self-practice exercise numbers | Values that contradict the RPS |
| **A. Outcomes** | 4–6 items; observable verbs (*menuliskan, menelusuri, membandingkan, merancang, menjelaskan penyebab*); cognitive level rising | "Memahami", "mengetahui", "mengenal" — untestable |
| **B. Concept map** | ASCII map in a code block, ≤ 20 lines, links to previous/next modules | A vertical topic list called a map |
| **C. Content** | Subsections C.1…C.n per RPS material: problem → concept → example code **actually run** → real output → its limits | Material outside the RPS row; output written from expectation |
| **D. Common mistakes** | Table: mistake · symptom the student sees (exact error message) · cause · fix; from real student mistakes | Invented mistakes |
| **E. Practicum** | Minute-by-minute timeline summing to the session length; clear deliverable and submission channel | A practicum that only repeats C |
| **F. Summary** | 5–8 sentences of prose tying back to A | Bullets copying C headings |
| **G. Exercises** | Mix ◆ / ◆◆ / ◆◆◆; if answer keys cover only odd numbers, even ones are reserved for graded work and equally difficult | All ◆; answers copyable from C |
| **H. Slide outline** | Table per slide: number · title · content · figure/table; **row count = the matrix slide count**; delivery notes | Paragraph slides; count off the matrix |
| **I. References** | Core references from the RPS, with chapter/page | Citations from memory |
| **J. Figures/tables** | `Gambar N.M` / `Tabel N.M` (N = module), section and slide where used, a status line | Codes numbered for another module |
| **K. Book notes** | What the chapter adds: steps explained aloud in class, deeper material, a chapter project replacing E | Empty — the chapter then starts from zero |

Sections used once per course (e.g. the practicum rubric and academic-integrity policy in
Module 1, exam coverage in the last module before UTS) are **referenced** by other modules, not
copied — copies drift when the original is corrected.

## Order of work

| Stage | Output | Gate |
|---|---|---|
| 1. Check RPS | Matrix row + list of C subsections | Lecturer approves the list |
| 2. A and G first | Outcomes and exercises | Every outcome tested by ≥ 1 exercise |
| 3. C, D | One subsection per turn; all code run | |
| 4. E, F | Practicum and summary | Minutes sum to the session length |
| 5. H, J | Slide outline and figure register | Slide count = matrix; every figure used in C or H |
| 6. I, K, metadata | | |
| 7. Check | Traceability check, style check (`academic-writing:manuscript-proofreading` if installed) | No heavy findings |
| 8. Derived | Answer key, figure specs, slides (`lecture-slides`) | |

**Why A and G before C:** writing exercises first forces measurable outcomes, and the content is
then written to answer them — not a long text followed by exercises fished out of it.

## Hard rules

- Material exactly as the RPS row; adding or dropping means stop (`rps-alignment`).
- All code in C, D, E is run in the course's locked language version; printed output is real.
- Deliberately broken teaching files stay broken — the defect is the lesson.
- Never invent blank administrative values (lecturer titles, NUPTK, document codes).

## References

- `references/templat-modul.md` — module skeleton
- `references/pedagogi.md` — observable verbs by Bloom level, exercise tiers, practicum template

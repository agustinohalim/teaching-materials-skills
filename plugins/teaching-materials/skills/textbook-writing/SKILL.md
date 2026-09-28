---
name: textbook-writing
description: Writing a university textbook (buku ajar) chapter by chapter from existing teaching modules and a book outline (kerangka buku ajar) — chapter N follows module N, a readiness check and an approved sub-chapter-to-source map before any prose, one sub-chapter per turn, every printed code example actually run, figure numbers kept from the module, visible markers instead of guesses, Markdown as the manuscript with Word/PDF as exports, and Indonesian publication requirements (RPS-aligned, ISBN, institutional endorsement, angka kredit). Use when writing or revising a chapter, mapping sub-chapters to module sections, deciding what a chapter adds beyond its module, building exercises and answer keys for the book, or preparing a manuscript for a publisher. Triggers in English and Indonesian — textbook, book chapter, manuscript for publisher, buku ajar, bab, naskah buku, kerangka buku, ISBN, penerbit, angka kredit.
---

# Textbook Writing

Respond in the user's language; write the book in its language. Indonesian register and
publication rules are in `references/id/`.

## Why this skill exists

When modules, figures, and an outline already exist, the danger in writing a chapter is not a
lack of material but **too much freedom**. A chapter "improved" bit by bit beyond its module
produces a book that no longer matches the course it came from — and a textbook that does not
match its RPS loses its reason to exist (and its eligibility as a *buku ajar*).

This skill keeps chapters tied to modules and outline, and keeps the prose sounding like a
lecturer, not a machine.

## Step zero: two documents that win over this skill

1. The course's control document (see `rps-alignment`).
2. The book outline — the content contract: sub-chapters, page estimates, required figures,
   number of exercises.

## Derivation

```
RPS → Module N ──────┐
                     ├──→ Chapter N
RPS → Outline ch. N ─┘
```

If writing a chapter shows the module is wrong, **stop and say so**. A correct chapter on a
wrong module yields two contradicting documents, and the one used in class is the module. If
the outline demands something the module lacks, check the module's book notes (section K)
first; if it is not there either, stop and ask — it is not licence to invent.

## Sources for one chapter

| Source | Taken for |
|---|---|
| Outline, chapter N | Sub-chapters, page estimate, required figures, exercise count |
| Module A | Chapter outcomes (opening) |
| Module B | Concept map, redrawn as Figure N.0 |
| Module C | Main content, expanded into flowing prose |
| Module D | A "Common mistakes" box |
| Module F | Chapter summary |
| Module G | Chapter exercises |
| Module I | Chapter references |
| Module J | Figures and tables, with their numbers |
| Module K | **What the chapter adds beyond the module** |
| Answer keys | Answers for the back matter (only those not reserved for grading) |

The practicum (E) becomes a chapter project; the slide outline (H) does not enter the book.

**Module vs chapter.** A module is used by a lecturer in class; a chapter is read alone. Every
place where the module relies on spoken explanation must be written out — installation steps
done in the first lab, transitions between sub-chapters, a sentence introducing and closing each
figure. Find these places before writing, not after.

## Stages and gates

| Stage | Output | Gate |
|---|---|---|
| 1. Readiness | Outline sub-chapters vs module content; figures present vs missing; discrepancies | Author approves the discrepancy list |
| 2. Chapter map | Table: sub-chapter → source (module §C.x, section K addition, figure) | **Author approves the map before a single sentence is written** |
| 3. Write | One sub-chapter per turn | Sub-chapter finished before the next |
| 4. Check | Style checker clean of heavy findings; traceability still clean | Both pass |
| 5. Tidy | Terms consistent, cross-references correct, exercise count matches outline, no markers left | Author reads the whole chapter |
| 6. Merge | Book-level checks, then export to `.docx` | TOC and lists populate in Word |

Stage 2 is the gate most tempting to skip and most expensive to skip: 20 pages written on a
wrong map are 20 pages rewritten. **One sub-chapter per turn**: a whole chapter generated in one
pass has a uniform rhythm, the clearest sign of machine prose.

## Hard rules

- **No invented** citations, authors, titles, years, pages, DOIs, measurements, or place names.
  Chapter references come from the module's section I.
- **Run every printed code example.** Printed output is real output. Deliberately broken
  teaching files stay broken; show a fix as a separate snippet.
- **Figures come from the project's figure pipeline**, not redrawn another way. A figure the
  outline needs but no module registers: register it in the module first, then specify, render,
  and only then use it.
- **Chapter figure numbers equal module figure numbers.** Chapter 2 uses Figures 2.1–2.5 exactly
  as Module 2. No renumbering by order of appearance.
- **Markers, not guesses**: `[PERLU KEPUTUSAN PENULIS: …]`, `[PERLU SITASI: …]`,
  `[GAMBAR BELUM ADA: …]`. None may remain when a chapter is declared finished.
- **Prose lives in the manuscript files**, never inside strings of a build script, where it
  escapes checking.
- **Markdown is the manuscript; `.docx`/PDF are exports.** Never edit the export and carry it
  back. Merge at the end, not after every chapter.
- **Answer keys stay out of the shareable build** by default; a keyed build goes to a separately
  named file so it can never overwrite the student copy.

## When to stop and ask

- The outline demands a sub-chapter the module does not cover and section K does not record.
- Writing reveals an error in the module or RPS.
- A figure is needed that no module registers.
- The requested page count clearly does not fit the available content, up or down.
- An administrative value is blank (author titles, NUPTK, document codes) — leave it blank.

Report in one or two sentences, then work on parts that do not depend on the answer.

## References

- `references/anatomi-bab.md` — chapter anatomy, numbering, code and figures, answer keys
- `references/id/gaya-bahasa.md` — Indonesian register and machine-prose tics
- `references/id/syarat-terbit.md` — what makes a *buku ajar* count, and publisher checklist

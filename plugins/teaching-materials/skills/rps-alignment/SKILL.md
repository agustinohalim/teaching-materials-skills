---
name: rps-alignment
description: Keeps a course's teaching documents aligned to its RPS (Rencana Pembelajaran Semester) under Indonesian outcome-based education — one-way derivation Kurikulum → RPS → {kontrak kuliah, lembar tugas, modul, kerangka buku ajar} → {slide, kunci jawaban}, a control document (daftar kendali) with locked items and a traceability matrix, numbered RPS revisions, and what may change mid-semester. Use whenever work touches an RPS, CPL, CPMK, Sub-CPMK, assessment weights, meeting sequence, lecture contract, assignment sheet, module, answer key, textbook outline, or slides; or when someone asks "can I change…" about a course document. Triggers in English and Indonesian — RPS, course plan, syllabus, learning outcomes, CPMK, Sub-CPMK, CPL, bobot penilaian, kontrak kuliah, lembar tugas, pertemuan, revisi RPS, OBE, daftar kendali, keterlacakan.
---

# RPS Alignment

Respond in the user's language. Indonesian templates are in `references/id/`.

## Why this skill exists

Teaching documents are tightly coupled. One assessment weight appears in the RPS, the lecture
contract, an assignment sheet, and a module at once. Changing it in one place produces documents
that contradict each other — found only at audit (akreditasi, LPM) or when students object that
the contract they signed differs from how they were graded.

So a change here is not a question of technically right or wrong, but of **direction**. This
skill keeps the direction.

## Step zero: the control document

Each course set should have one control document (`Daftar_Kendali_*.md`) that is the source of
truth for this procedure — the skill is only the procedure. If the project has none, offer to
create one from `references/id/templat-daftar-kendali.md` before editing anything else. If the
control document and this skill disagree, **the control document wins**; say so.

## The one rule: derivation flows one way

```
KURIKULUM / BORANG  →  RPS  →  Kontrak Kuliah, Lembar Tugas, Modul, Kerangka Buku Ajar
                                              ↓
                                   Slide, Kunci Jawaban
```

A module follows the RPS. Never the reverse.

The consequence most often forgotten: **if writing a module shows the RPS is wrong, do not patch
the module to fit.** Stop, report the finding, and let the lecturer decide whether it justifies a
numbered RPS revision. Patching feels productive, but yields a module that can no longer be
traced to its RPS — exactly the damage the control document exists to prevent.

## Three situations

### 1. Editing an existing document

| Category | Examples | Action |
|---|---|---|
| Free to change | Case examples, exercise data, illustrations, minute allocation inside one practicum session, slide design | Do it |
| Needs a numbered revision | A typo that changes meaning; a campus policy change | Stop, propose the revision, wait |
| Locked during the semester | CPL, CPMK, assessment weights, meeting sequence, number and type of assignments, core references | Refuse and explain |

The third category is not bureaucracy: students signed the lecture contract on those numbers.
Moving them mid-semester harms them. One exception that favours students — extending a
deadline, never bringing it forward — is recorded as a contract addendum, not an RPS revision.

The typical locked items and what silently breaks each are listed in
`references/id/butir-terkunci-umum.md`. Read it before approving any change that touches a
number, weight, code, or sequence.

### 2. Creating a new document

The order matters because each step feeds the next:

1. **Check the RPS first.** Match the meeting's material against the traceability matrix.
2. **Write the document to exactly that material.** Add no topics, drop none.
3. **Update the textbook outline** — sub-chapters, pages, figure list only.
4. **Build slides** from the module's slide outline.
5. **Do not touch the RPS or the lecture contract.**

If step 2 tempts you to add material, ask first: is it required to reach a CPMK, or merely
interesting? Only the former justifies an RPS revision.

### 3. Checking consistency

The traceability matrix (meeting → RPS material → module → book chapter → slide count) must be
consistent left to right. Touch one cell, verify the whole row. What a machine can check —
meeting numbers, section order, slide counts, figure-code prefixes, file existence — deserves a
small script; what it cannot — content matching the RPS, weights summing correctly, one course
leading another, answer-key coverage — is checked by hand.

Two traps to know:

- **Exam offset.** When meeting 8 is UTS and 16 is UAS, modules 1–7 map to meetings 1–7 but
  modules 8–14 map to meetings **9–15**. Book chapter N always equals module N.
- **Weights sum per component, not only overall.** A split task (Tugas 3A + 3B) must still sum
  to the RPS weight of Tugas 3, and the CPMK matrix must not move.

## When to stop and ask

- The work requires changing a locked item.
- A module and the RPS conflict, and the RPS looks wrong.
- New material seems needed but supports no clear CPMK.
- A change shifts the synchronisation between two linked courses.
- A value the control document leaves blank (lecturer titles, NUPTK, schedule, document codes)
  is needed now. **Leave it blank; never invent it.** Those come from staff, the academic
  office, and the quality unit.

Say it in one or two sentences, then finish the parts that do not depend on the answer.

## References

- `references/id/templat-daftar-kendali.md` — control document template (Indonesian)
- `references/id/butir-terkunci-umum.md` — typical locked items and how each is silently broken

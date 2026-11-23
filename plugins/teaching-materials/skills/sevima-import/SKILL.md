---
name: sevima-import
description: Preparing import files for SEVIMA's campus platforms without breaking them — Edlink quiz questions (Import Soal, import-quiz-questions.xlsx) and the Siakad RPS and per-meeting RPS detail (Template RPS.xlsx, Template Rincian RPS.xlsx) — by filling a copy of the platform's own template (never a workbook rebuilt from scratch), validating every row first, checking the item count after import, and keeping answer keys out of student material. Use when the user wants to import a quiz, pretest, or question bank into Edlink, fill or import an RPS or Rincian RPS into Siakad, asks what can be imported into Edlink or Siakad, or reports an import that shows a wrong number of items or an unreadable first row. Triggers in English and Indonesian — Edlink, SEVIMA, Siakad, Siakadcloud, SEMIVA, import soal, impor kuis, kuis Edlink, pretest, bank soal, template RPS, rincian RPS, impor RPS, isi template excel.
---

# SEVIMA Import (Edlink and Siakad)

Respond in the user's language. Column lists and example data are in `references/formats.md`.
Scripts are in `scripts/` next to this file. They need Python 3.10+ and nothing else.

## What can be imported, and into which platform

Edlink is the LMS and Siakad is the academic information system. Both are SEVIMA products and
they are easy to mix up, so name the platform every time.

| Platform | What | Template (download it from the platform) | Sheet filled |
|---|---|---|---|
| Edlink | Quiz questions: one correct answer and four wrong ones per row | `import-quiz-questions.xlsx`, from **Import Soal** on a quiz | first sheet |
| Siakad | RPS identity: curriculum, course code, description, objectives, topics, references, media | `Template RPS.xlsx` | `Format Isian` |
| Siakad | RPS detail per meeting: CPMK, meeting type, topic, indicators, methods, weight | `Template Rincian RPS.xlsx` | `Format Isian` |

What SEVIMA's own Edlink FAQ says is **not** imported: Edlink grades do not flow into Siakad (Edlink
gives a raw Excel recap and grades are entered in Siakad by hand), and material uploaded in Siakad
does not appear in Edlink. Anything outside this table is unverified. Before promising an import,
ask the user to check the platform's menu or send a screenshot of it.

## The one rule: fill a copy of the template

The platforms parse the template they hand out. One workbook rebuilt from scratch with a spreadsheet
library imported as 11 questions instead of 10, with question 1 unreadable. The suspected cause, not
isolated in a separate test, is that the library stored text as inline strings while the template
uses a shared-strings table. Staying as close to the template as possible removes the question. So:

- Never build the file from scratch, and never "save as" through a library that rewrites the package.
- Fill a copy of the template with `scripts/fill_template.py` or `scripts/make_quiz.py`. They put every
  value into the template's shared-strings table, rewrite only the target sheet's rows, and copy
  every other part of the package byte for byte. Other sheets, such as the example sheet and the
  meeting-type list in `Template Rincian RPS.xlsx`, stay intact.
- Do not bundle or redistribute the templates. Ask the user to download them from their own
  platform, because the campus's version is the one its importer reads.

## Quiz workflow (Edlink)

1. Write the questions as a JSON spec (shape in `references/formats.md`). Draw them from what was
   actually taught: compare the course plan with what the class covered, and flag a question whose
   topic may have been skipped.
2. Validate and build:

   ```
   python scripts/make_quiz.py --template path/to/import-quiz-questions.xlsx --check quiz.json
   python scripts/make_quiz.py --template path/to/import-quiz-questions.xlsx quiz.json
   ```

   A spec is refused when a question does not have exactly four wrong answers, has an empty field,
   has two identical choices, or has a field over 3000 characters (Edlink's editor limit per field).
3. After import, check that **Daftar Soal (N)** in Edlink equals the number of questions in the
   spec, and spot-check that the correct answer is marked. Edlink shuffles the choices itself, so
   the correct one always goes in the `correct` field.

Quiz files carry the answer key. Keep the spec and the `.xlsx` with the lecturer's documents, never
in a folder uploaded as course material.

## RPS workflow (Siakad)

The RPS document is the source and the import file is derived from it, never the reverse. If the
project has an RPS-alignment procedure (`rps-alignment`), follow it: when filling the template
exposes an error in the RPS, stop and report it rather than fixing it in the import file only.

```
python scripts/fill_template.py "path/to/Template RPS.xlsx" --header
python scripts/fill_template.py "path/to/Template Rincian RPS.xlsx" rincian.json -o Rincian_RPS_<code>.xlsx
```

`--header` prints the template's columns. Data rows are JSON objects keyed by exact header text, or
lists in column order. An unknown column name is refused with the valid names listed. In the
detail template, meeting type uses the IDs from its `Daftar Jenis Pertemuan` sheet (`K` lecture, `P`
practicum, `T` midterm, `A` final), and the weights across meetings should add up to the RPS total.

## Where the files live

Keep templates, specs, and generated files in the project, for example `Edlink/` and `Siakad/` folders
under version control, not in Downloads. Files left in Downloads get overwritten, duplicated with
`(1)` suffixes, and lose the link to the spec they came from. A generated file can always be rebuilt
from its spec, so the spec is the thing to keep.

## When to stop and ask

- The user asks to import something not in the table above.
- The template's header differs from `references/formats.md`. The platform may have changed it, so
  show the new header and confirm before filling.
- An import shows a different item count than the file. Do not re-import on top of it. Have the user
  delete the imported items first, then compare the file against a fresh template.

# Import formats

Headers as they appear in the templates downloaded in September–November 2026. If a freshly
downloaded template differs, trust the template and run `fill_template.py --header` to see it.

## Edlink quiz — `import-quiz-questions.xlsx`

| Column | Content |
|---|---|
| `Question` | Question text |
| `Correct Answer` | The one correct answer |
| `Incorrect Answer 01` … `Incorrect Answer 04` | Four wrong answers |

The template ships with three example rows. They are replaced, not appended to.

Spec for `make_quiz.py`:

```json
{
  "title": "Quiz 4, after meeting 11",
  "coverage": "Modules 8–10",
  "questions": [
    {
      "question": "What does print(7 // 2) display?",
      "correct": "3",
      "wrong": ["3.5", "4", "3.0", "An error message"]
    }
  ]
}
```

Only `questions` is read. `title` and `coverage` are for the lecturer.

## Siakad RPS — `Template RPS.xlsx`, sheet `Format Isian`

One row per course.

| Column | Content |
|---|---|
| `Kurikulum` | Curriculum year, e.g. `2024` |
| `Kode MK` | Course code |
| `Tanggal Penyusunan` | Date written, `YYYY-MM-DD` |
| `Deskripsi Mata Kuliah (IND)` | Course description in Indonesian |
| `Deskripsi Mata Kuliah (ENG)` | Course description in English |
| `Tujuan Mata Kuliah` | Objectives, numbered `1. …;` one per line |
| `Materi Pembelajaran` | Topics, numbered, one per line |
| `Pustaka Utama` | Main references, one per line |
| `Pustaka Pendukung` | Supporting references |
| `Media Perangkat Lunak` | Software media |
| `Media Perangkat Keras` | Hardware media |

## Siakad RPS detail — `Template Rincian RPS.xlsx`, sheet `Format Isian`

One row per meeting, midterm and final included.

| Column | Content |
|---|---|
| `Pertemuan Ke-` | Meeting number |
| `CPMK & Sub-CPMK` | e.g. `CPMK-1` or `CPMK-2,CPMK-3` |
| `ID Jenis Pertemuan (Lihat Daftar Jenis Pertemuan)` | `K` lecture, `P` practicum, `T` midterm (UTS), `A` final (UAS) |
| `Materi Pembelajaran (IND)` | Topic in Indonesian |
| `Materi Pembelajaran (EN)` | Topic in English |
| `Indikator Penilaian` | Assessment indicators |
| `Bentuk & Kriteria Penilaian` | Assessment form and criteria |
| `Metode Pembelajaran Luring` | Face-to-face methods |
| `Metode Pembelajaran Daring` | Online methods |
| `Bobot Penilaian (%)` | Weight of this meeting's assessment |

The workbook also holds `Contoh Isian` (a filled example) and `Daftar Jenis Pertemuan` (the ID list).
Both are left untouched.

Data for `fill_template.py`:

```json
[
  {"Pertemuan Ke-": 1, "CPMK & Sub-CPMK": "CPMK-1", "ID Jenis Pertemuan (Lihat Daftar Jenis Pertemuan)": "K",
   "Materi Pembelajaran (IND)": "Pengantar pemrograman", "Materi Pembelajaran (EN)": "Introduction to programming",
   "Bobot Penilaian (%)": 0},
  {"Pertemuan Ke-": 8, "ID Jenis Pertemuan (Lihat Daftar Jenis Pertemuan)": "T",
   "Materi Pembelajaran (IND)": "Ujian Tengah Semester", "Bobot Penilaian (%)": 20}
]
```

Numbers are written as text, the way the templates' own example rows store them. A line break
inside a cell is written as `\n` in JSON.

# teaching-materials-skills

**English** · [Bahasa Indonesia](#bahasa-indonesia)

Agent skills for preparing university teaching materials under Indonesian outcome-based
education: keeping every document aligned to the RPS, writing per-meeting teaching modules, turning
modules into a textbook (*buku ajar*), building lecture slides, and preparing import files for
SEVIMA's Edlink and Siakad. Packaged as a Claude Code plugin; the skills are plain Agent Skills
folders, so Codex, Gemini CLI, OpenCode, and other agents can use them too. Companion to
[academic-writing-skills](https://github.com/agustinohalim/academic-writing-skills) (research
integrity and bilingual proofreading); install both for the full workflow.

## Skills

| Skill | What it does |
|---|---|
| `rps-alignment` | RPS as single source of truth; one-way derivation to contract, assignments, modules, book outline, slides, answer keys; a control document (*daftar kendali*) with locked items and a traceability matrix; what may change mid-semester. Includes a control-document template. |
| `teaching-module-writing` | Section-by-section guidance for a per-meeting module: measurable outcomes, content, common mistakes, practicum timeline, tiered exercises (◆/◆◆/◆◆◆), slide outline, figure register, notes for the book. Module template and pedagogy tables included. |
| `textbook-writing` | Chapter N from module N and the outline, with a readiness check and an approved chapter map before prose, one sub-chapter per turn, run-every-snippet, figure numbering, and *buku ajar* publication requirements. |
| `lecture-slides` | Decks derived from the module's slide outline; generated-deck practices (one style module, locked footer, checker); Mayer's multimedia principles; research talks. |
| `sevima-import` | Import files for Edlink quizzes and the Siakad RPS and per-meeting RPS detail, filled into a copy of the platform's own template so the importer reads them; validation before import, item-count check after. Python scripts, standard library only. |

Skills activate automatically in English or Indonesian, or directly, e.g.
`/teaching-materials:teaching-module-writing`.

## Install

### Claude Code

```
/plugin marketplace add agustinohalim/teaching-materials-skills
/plugin install teaching-materials@teaching-materials-skills
```

### Other agents (Codex, Gemini CLI, OpenCode, and others)

Copy the skill folders into your agent's skills folder. `~/.agents/skills` is read by Codex, Gemini
CLI, and OpenCode. Install into one folder only, or each skill shows up twice.

```bash
git clone https://github.com/agustinohalim/teaching-materials-skills.git
mkdir -p ~/.agents/skills
cp -r teaching-materials-skills/plugins/teaching-materials/skills/* ~/.agents/skills/
```

```powershell
git clone https://github.com/agustinohalim/teaching-materials-skills.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force teaching-materials-skills\plugins\teaching-materials\skills\* "$HOME\.agents\skills\"
```

To update, pull the clone and copy again.

## License

CC BY 4.0. See `LICENSE`.

---

## Bahasa Indonesia

Skill agen untuk menyusun perangkat ajar perguruan tinggi berbasis OBE: menjaga semua dokumen
selaras dengan RPS, menulis modul per pertemuan, menurunkan modul menjadi buku ajar, menyusun slide
kuliah, dan menyiapkan berkas impor untuk Edlink dan Siakad SEVIMA. Dikemas sebagai plugin Claude
Code. Skill-nya berupa folder Agent Skills biasa, sehingga Codex, Gemini CLI, OpenCode, dan agen
lain juga bisa memakainya. Pasangan dari
[academic-writing-skills](https://github.com/agustinohalim/academic-writing-skills) (integritas
riset dan proofreading dwibahasa); pasang keduanya untuk alur kerja lengkap.

| Skill | Isinya |
|---|---|
| `rps-alignment` | RPS sebagai acuan tunggal, arah penurunan satu arah, daftar kendali dengan butir terkunci dan matriks keterlacakan, apa yang boleh diubah di tengah semester. Termasuk templat daftar kendali. |
| `teaching-module-writing` | Panduan per bagian modul pertemuan: capaian terukur, uraian, kesalahan umum, praktikum, latihan bertingkat, kerangka slide, daftar gambar, catatan buku. Termasuk templat modul. |
| `textbook-writing` | Bab N dari modul N dan kerangka, dengan pemeriksaan kesiapan dan peta bab yang disetujui sebelum menulis, satu sub-bab per giliran, dan syarat terbit buku ajar. |
| `lecture-slides` | Slide diturunkan dari kerangka slide modul; praktik deck yang dibangkitkan skrip; prinsip multimedia Mayer; presentasi riset. |
| `sevima-import` | Berkas impor kuis Edlink serta RPS dan Rincian RPS Siakad, diisikan ke salinan templat resmi platform agar terbaca importer-nya; pemeriksaan sebelum impor dan pencocokan jumlah butir sesudahnya. Skrip Python tanpa paket tambahan. |

**Claude Code:**

```
/plugin marketplace add agustinohalim/teaching-materials-skills
/plugin install teaching-materials@teaching-materials-skills
```

**Agen lain (Codex, Gemini CLI, OpenCode, dan lainnya):** salin folder skill ke
`~/.agents/skills` dengan perintah di bagian Install di atas. Pasang di satu folder saja agar skill
tidak muncul dua kali.

Lisensi CC BY 4.0.

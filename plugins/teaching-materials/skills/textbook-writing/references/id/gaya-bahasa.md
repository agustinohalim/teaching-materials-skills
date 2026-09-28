# Gaya Bahasa Naskah Buku Ajar

<!-- gaya:abaikan-berkas — berkas ini mengutip polanya sebagai contoh, jadi pemeriksa akan menandai kutipannya sendiri. -->

Register sebuah buku ajar sudah ditentukan oleh modul-modul yang mendahuluinya. Berkas ini
merumuskannya supaya bab yang ditulis belakangan tidak terdengar seperti orang
lain — atau seperti mesin.

Pemeriksa otomatisnya `periksa_gaya.py` (ada di skill `academic-writing:manuscript-proofreading`
bila plugin itu terpasang); aturannya di `pola/claudish_id.json`. Berkas ini menjelaskan yang tidak bisa diperiksa
mesin.

## Register

**Sapaan "Anda".** Konsisten di seluruh modul dan buku. Bukan "kamu", bukan
"kalian", bukan kalimat pasif yang menghindari sapaan sama sekali.

**Jelaskan mengapa, bukan hanya apa.** Ini ciri yang paling membedakan buku ajar
yang baik dari buku kebanyakan. Bandingkan:

> Variabel harus dinamai dengan huruf kecil dan garis bawah.

dengan versi yang menyebut akibatnya:

> Kode yang tidak dapat dijelaskan sendiri oleh penyusunnya saat responsi
> dinilai nol pada kriteria kebenaran hasil, berapa pun kualitas kodenya.

Yang kedua menyebutkan akibatnya, jadi pembaca tahu aturannya bukan selera.

**Prosa, bukan butir bertumpuk.** Butir dipakai bila isinya benar-benar sejajar
dan tidak berurut. Dua kalimat yang saling menyebabkan ditulis sebagai dua
kalimat, bukan dua butir — hubungan sebab-akibatnya hilang begitu dipecah jadi
butir.

**Contoh berlatar nyata.** Studi kasus berlatar data administrasi kampus,
koperasi, atau usaha kecil di daerah pembacanya. Bukan `foo`, `bar`, dan `data_dummy`.

**Istilah teknis tetap dalam bentuk aslinya.** `commit`, `push`, `array`,
`hash`, `stack`. Yang diindonesiakan hanya istilah yang padanannya sudah mapan
dan dipakai modul: senarai berantai, tumpukan, antrean, penelusuran. Glosarium
di bagian belakang buku yang menjembatani keduanya — itu sebabnya ia ada.

## Panjang dan irama

Kalimat panjang tidak dilarang, kalimat seragam yang dilarang. Yang membuat
prosa terbaca mesin bukan satu kalimat 50 kata, melainkan dua puluh kalimat
yang semuanya 18 kata dengan bentuk yang sama.

Pemeriksa menandai kalimat di atas 45 kata sebagai temuan ringan, dan tiga
paragraf berturut-turut yang dibuka kata yang sama. Keduanya petunjuk, bukan
larangan.

Satu sebab teknis yang menghasilkan keseragaman itu: menulis satu bab utuh
dalam satu giliran. Karena itu skill ini menuntut satu sub-bab per giliran.

## Pola yang ditandai berat

Pola yang praktis tidak pernah benar dalam prosa ajar. Selengkapnya di
`claudish_id.json`; yang paling sering muncul:

| Pola | Contoh | Perbaikannya |
|---|---|---|
| Pembuka bergaya esai | "Di era digital ini, pemrograman …" | Mulai dari persoalan yang dihadapi pembaca |
| Pengantar tanpa isi | "Perlu dicatat bahwa …" | Buang frasanya |
| Ajakan basa-basi | "Mari kita bahas lebih dalam." | Langsung bahas |
| Pertanyaan retoris | "Pernahkah Anda bertanya-tanya …" | Sampaikan jawabannya saja |
| Klaim kepentingan | "Struktur data memegang peranan penting." | Sebutkan akibat nyatanya |
| Emoji pada judul | "## Pengantar 🚀" | Hapus |
| Menyuruh memperhatikan | "Perhatikan bahwa kelima ciri ini menguji bentuknya." | Buang frasanya: "Kelima ciri ini menguji bentuknya." |
| Rujukan tanpa isi | "yang baru terasa di Bab 12" | "Bab 12 membahasnya sebagai operasi berkas" |
| Rujukan lintas bab | "seperti disebutkan di §1.5" dari dalam Bab 2 | "seperti disebutkan di Bab 1 §1.5" |

Tiga baris terakhir berasal dari pengalaman nyata: empat bab lulus pemeriksaan,
tetapi pembacanya menilai bahasanya masih terbaca sebagai tulisan mesin.
Hitungannya membenarkan penilaian itu — 15 "Perhatikan", 16 "justru", 11 "Itulah"
dalam 14.000 kata. Tic seperti itu tidak ada di daftar Inggris mana pun karena ia
tic penulisnya sendiri.

Pelajarannya untuk bab berikutnya: pemeriksa yang bersih bukan bukti bahasanya
sudah baik. Ia hanya bukti bahwa pola yang sudah dikenali tidak muncul. Baca
ulang naskah sendiri dan hitung kata yang terasa berulang; bila ada yang lewat
tiga kali per seribu kata tanpa alasan, tambahkan ke `kepadatan_kata`.

## Yang ditandai ringan, dan sering justru benar

Aturan ringan ada karena pola yang sama bisa benar atau salah tergantung apa
yang dikerjakannya. Tiga contoh nyata dari modul, ketiganya
**tidak perlu diubah**:

- **"Memilih yang paling canggih."** — tabel kesalahan umum. Ini *nama sebuah
  kesalahan mahasiswa* di tabel bagian D, bukan pujian penulis pada teknologi.
- **"Pertanyaannya bukan 'data saya berbentuk apa' melainkan 'operasi apa yang
  akan dilakukan terhadapnya'."** — modul struktur data. Kontras biner yang
  membawa seluruh pelajaran tentang ADT. Membuangnya membuang pelajarannya.
- **"Bayangkan Anda diminta menghitung rata-rata nilai 40 mahasiswa."** —
  modul perulangan. Alat peraga, bukan retorika. Yang retorika adalah
  "Bayangkan jika semua data Anda hilang" — pemeriksa membedakan keduanya.

Karena itu: baca setiap temuan ringan, jangan menurutinya otomatis. Untuk yang
memang benar, tersedia `<!-- gaya:abaikan -->` di baris sebelumnya.

## Perbedaan bab dari modul, dalam hal bahasa

Modul boleh berhenti di tengah dan menunggu dosen melanjutkan secara lisan. Bab
tidak. Tiga akibat praktisnya:

1. **Tidak ada rujukan ke kegiatan kelas.** "Seperti yang sudah Anda kerjakan
   di praktikum pertemuan 1" tidak berlaku bagi pembaca buku. Tulis langkahnya.
2. **Peralihan antar sub-bab harus ditulis.** Di kelas, dosen yang
   menjembatani; di buku, kalimat terakhir sebuah sub-bab yang menyiapkan
   sub-bab berikutnya.
3. **Tabel dan gambar perlu kalimat pengantar dan kalimat penutup.** Gambar
   yang berdiri sendiri tanpa dibicarakan di prosa akan dilewati pembaca.

Yang tidak berubah: tetap plain, tetap langsung, tetap menjelaskan sebabnya.
Bab yang lebih resmi bahasanya daripada modulnya sudah salah arah.

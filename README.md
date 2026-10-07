# UMKM Design Director

**Panduan desain AI untuk pemilik UMKM: dari ngobrol sederhana sampai prompt gambar siap pakai yang tidak terlihat seperti "AI slop".**
*A design-director conversation for small-business owners that ends in ready-to-use, standalone image prompts.*

---

## Mulai di sini: pakai lewat ChatGPT, Claude, atau Gemini

Tidak perlu instal apa pun, tidak perlu paham teknologi atau desain. Kakak hanya butuh akun salah satu AI chat (ChatGPT, Claude, atau Gemini) dan satu file dari folder [`siap-pakai/`](siap-pakai/).

> **Catatan penting:** alur ini punya dua bagian. (1) **Wawancara dan penyusunan prompt**, bisa di ChatGPT, Claude, atau Gemini. (2) **Membuat gambar**, harus di AI yang bisa membuat gambar (misalnya ChatGPT atau Gemini). Beberapa AI chat, termasuk Claude, bisa membantu menyusun prompt tetapi belum tentu bisa membuat gambar; pilih alat gambar yang tersedia di akun Kakak. Fitur unggah file dan batasnya bisa berbeda di paket gratis dan berbayar.

### Cara 1 (paling mudah, tanpa setup)

1. **Unduh** file [`siap-pakai/umkm-design-director-lengkap.md`](siap-pakai/umkm-design-director-lengkap.md) (buka file, pilih Download atau Raw, lalu simpan).
2. **Buka chat baru** di ChatGPT, Claude, atau Gemini, lalu **unggah file itu** (ikon klip kertas atau tanda +).
3. **Kirim pesan pembuka ini** bersama file:

   > Halo! Saya pemilik usaha dan ingin membuat desain promosi. Tolong ikuti panduan di file terlampir sepenuhnya: mulai dari tahap awal, tanya saya sedikit demi sedikit (maksimal 3 pertanyaan sekali jalan) dengan bahasa Indonesia yang sederhana. Di akhir, berikan prompt gambar siap pakai beserta daftar gambar yang harus saya lampirkan untuk tiap prompt.
   >
   > *(English: Hi! I own a small business and want a promotional design. Please follow the attached guide fully, asking me at most 3 simple questions at a time. At the end, give me ready-to-use image prompts and the list of images I must attach to each one.)*

4. **Jawab pertanyaannya.** Siapkan foto produk asli, logo, atau desain lama (kalau ada); kirim kapan saja saat ditanya. Jawaban jujur dan konkret (angka, bahan, cerita) menghasilkan desain yang khas.
5. **Terima hasilnya:** rencana desain, lalu **Prompt 1, Prompt 2, ...** (satu per jenis gambar, misalnya feed dan story). Setiap prompt **berdiri sendiri** dan punya **daftar lampiran**.
6. **Buat gambarnya:** buka AI pembuat gambar (chat baru), **salin satu prompt, lampirkan gambar sesuai urutan di daftar lampiran, lalu kirim bersamaan.** Ulangi untuk prompt berikutnya.
7. **Cek tulisan huruf demi huruf** (nama, harga, tanggal, alamat), tempel logo halal resmi bila perlu, lalu posting. Boleh kembali ke chat awal untuk meminta tinjauan hasil.

*Jika AI menolak file, lupa instruksi di tengah jalan, atau paket gratis membatasi ukuran file (file ini cukup besar, sekitar 145 KB), pakai Cara 2 atau Cara 3 di bawah.*

### Cara 2 (setup sekali, dipakai berulang)

Buat asisten khusus supaya Kakak tidak perlu mengunggah file setiap kali. Nama menu bisa berubah dan sebagian fitur butuh paket berbayar.

| AI | Langkah |
|---|---|
| **ChatGPT** | Buat GPT atau Project baru. Isi kolom Instructions dengan isi [`umkm-design-director-ringkas.md`](siap-pakai/umkm-design-director-ringkas.md) (kurang dari 8.000 karakter), lalu unggah `umkm-design-director-lengkap.md` ke bagian Knowledge/Files. |
| **Gemini** | Buat Gem baru. Instruksi = isi `umkm-design-director-ringkas.md`; unggah `umkm-design-director-lengkap.md` sebagai file pendukung. |
| **Claude** | Buat Project: Instructions = isi `ringkas`, lalu tambahkan `lengkap` ke pengetahuan project. Atau unggah [`umkm-design-director.skill`](siap-pakai/umkm-design-director.skill) di Settings, Capabilities, Skills. |

### Cara 3 (jika tidak bisa mengunggah file)

Tempel seluruh isi `umkm-design-director-ringkas.md` sebagai pesan pertama, lalu tulis "Mulai". Kualitas sedikit di bawah Cara 1 karena panduannya lebih singkat.

### Tips agar hasilnya paling bagus

- **Siapkan bahan asli:** foto produk (cahaya jendela, latar polos), logo, foto gerobak/toko, desain lama. Foto asli membuat pembeli percaya dan hasilnya tidak terlihat seperti AI pasaran.
- **Jawab dengan fakta khas:** apa yang bikin beda, buktinya, kata-kata pelanggan. Jawaban generik ("enak dan murah") menghasilkan desain generik.
- **Satu pesan, satu aksi.** Lebih sedikit tulisan dan lebih banyak ruang kosong membuat desain lebih jelas.
- **Beberapa jenis gambar sekaligus** (maksimal sekitar 4) akan dibuat satu keluarga: warna, huruf, dan gayanya konsisten.
- **Jangan minta AI membuat logo halal, QR code, atau logo.** Tempel yang asli sendiri; skill menyisakan tempatnya.

---

## Apa yang membuat skill ini berbeda

Banyak UMKM memakai AI untuk poster lalu hasilnya terlihat sama: gradien neon, makanan mengilap seperti plastik, semua sudut penuh, tulisan salah ketik. Penyebabnya bukan malas, tetapi **tidak ada keputusan desain**: apa pun yang tidak ditentukan akan diisi AI dengan rata-rata internet. Skill ini bertindak seperti desainer yang duduk bersama pemilik usaha:

1. **Memahami keunggulan usaha:** keunggulan, bukti, pesaing, kesan yang diinginkan, sifat usaha, dan apa yang tidak boleh terlihat.
2. **Memakai bahan asli pemilik:** foto, logo, maskot, orang, desain lama. Setiap gambar diberi peran, perlakuan, posisi, dan ukuran di dalam prompt.
3. **Menanyakan gambar apa saja yang dibutuhkan,** satu atau beberapa, dan membuatnya sebagai satu keluarga visual dengan **prompt mandiri per gambar**.
4. **Mengutamakan ruang kosong yang disengaja** dan "secukupnya": ruang dialokasikan dulu, elemen yang tidak membantu pesan dibuang.
5. **Jujur dan aman:** foto produk asli dipertahankan; tanda resmi (halal, PIRT) tidak dikarang AI; budaya dan izin foto orang diperhatikan.

Contoh sesi lengkap: [`examples/01-warung-bakso-sesi-lengkap.md`](examples/01-warung-bakso-sesi-lengkap.md) (dua prompt mandiri dengan lampiran masing-masing). Contoh spanduk: [`examples/02-spanduk-laundry-ringkas.md`](examples/02-spanduk-laundry-ringkas.md).

## Isi folder `siap-pakai/`

| File | Untuk apa |
|---|---|
| `umkm-design-director-lengkap.md` | Panduan lengkap, diunggah ke chat atau disimpan sebagai pengetahuan (Cara 1 dan 2) |
| `umkm-design-director-ringkas.md` | Versi pendek untuk kolom instruksi GPT/Gem/Project atau ditempel langsung (Cara 2 dan 3) |
| `umkm-design-director.skill` | Untuk pengguna Claude yang ingin mengunggah sebagai skill |

---

## Untuk developer dan kontributor

Pengguna akhir tidak perlu bagian ini. Di bawah ini cara memasang skill ke agen yang mendukung format **Agent Skills**, struktur repositori, dan alat pengembangan.

| Alat | Cara |
|---|---|
| Claude Code | Salin `skills/umkm-design-director/` ke `~/.claude/skills/` (pribadi) atau `.claude/skills/` (proyek). |
| Agen lain berformat Agent Skills (mis. Codex, Cursor, Gemini CLI, Copilot) | Salin folder skill ke folder skills agen tersebut; lihat daftar klien di <https://agentskills.io>. Pemasang komunitas seperti `openskills` ada; cek kompatibilitas terbaru. |
| Bangun ulang file siap pakai | `python scripts/bundle.py` membuat ulang `siap-pakai/umkm-design-director-lengkap.md`. |
| Validasi | `python scripts/validate.py` memeriksa frontmatter, tautan, panjang versi ringkas, dan konsistensi contoh (prompt mandiri, sistem visual identik). |

```
umkm-design-director/
├── README.md
├── siap-pakai/                       # file untuk pengguna akhir (chat umum)
├── skills/umkm-design-director/
│   ├── SKILL.md                      # alur 11 tahap, aturan keputusan, format penyerahan
│   ├── references/
│   │   ├── 01-interview-guide.md         # bank pertanyaan, istilah awam, kasus sulit
│   │   ├── 02-business-distinction.md    # USP, bukti, pesaing, kesan, sifat, uji tukar
│   │   ├── 03-reference-images.md        # bahan gambar: minta, analisis, perlakuan, mode Perbaiki
│   │   ├── 04-design-principles.md       # persepsi, ruang kosong, hierarki, psikologi
│   │   ├── 05-color-and-culture.md       # warna, audiens, konteks budaya Indonesia
│   │   ├── 06-typography.md              # huruf, batas teks, harga, risiko salah ketik
│   │   ├── 07-business-archetypes.md     # arah awal dan bahan yang diminta per jenis usaha
│   │   ├── 08-formats-and-platforms.md   # ukuran, safe zone, cetak, kepadatan
│   │   ├── 09-output-sets.md             # beberapa output, sistem visual bersama, prompt mandiri
│   │   ├── 10-anti-slop.md               # tanda-tanda AI slop, perbaikan, audit
│   │   ├── 11-prompt-assembly.md         # template prompt, strategi teks, contoh
│   │   └── 12-review-and-iteration.md    # tinjauan hasil, uji kesetiaan, uji set, perbaikan
│   └── assets/                       # brief-template.md, prompt-template.md
├── examples/                         # sesi contoh
├── evals/evals.json                  # prompt uji dan kriteria penilaian
├── scripts/                          # validate.py, bundle.py
└── docs/RESEARCH-NOTES.md            # dasar keputusan struktur dan anti-slop
```

Struktur mengikuti konvensi Agent Skills: satu folder per skill, `SKILL.md` dengan frontmatter `name` dan `description`, dan `references/` dibaca hanya saat dibutuhkan (progressive disclosure).

**Status:** versi 1.2.0. Prompt uji ada di `evals/evals.json`; skill belum diuji secara terkontrol dengan pemilik UMKM sungguhan. Masukan sangat diharapkan (`CONTRIBUTING.md`). Lisensi MIT.

---

## English summary

**Use it in ChatGPT, Claude, or Gemini, no install needed.** Download `siap-pakai/umkm-design-director-lengkap.md`, start a new chat, upload it, and send the starter message above. The assistant interviews you (max 3 questions per turn) about your business, what makes it different, your reference images, which graphics you need, your audience, exact text, and taste. It then delivers a shared design plan and **one fully standalone image prompt per output**, each with its own list of images to attach. Copy a prompt, attach its images in the stated order, and send them together in an image-generating AI (for example ChatGPT or Gemini; some chat assistants cannot generate images). For a reusable assistant, put `umkm-design-director-ringkas.md` in the instructions of a custom GPT/Gem/Project and upload the full file as knowledge. Developers can install `skills/umkm-design-director/` in any Agent Skills-compatible agent and validate with `python scripts/validate.py`.

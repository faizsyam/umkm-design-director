# UMKM Design Director

**Panduan desain AI untuk pemilik UMKM: dari ngobrol santai hingga prompt gambar cetak siap pakai dengan art direction profesional tanpa "AI slop".**
*A professional art-direction framework and prompt system for small-business print marketing.*

---

## Mulai di sini: pakai lewat ChatGPT, Claude, atau Gemini

Tidak perlu instal apa pun, tidak perlu paham istilah teknis desain atau teknologi. Anda hanya butuh akun salah satu AI chat (ChatGPT, Claude, atau Gemini) dan file dari folder [`siap-pakai/`](siap-pakai/).

> **Catatan penting:** Alur ini terdiri dari dua bagian:
> 1. **Wawancara & penyusunan art direction:** Berlangsung di ChatGPT, Claude, atau Gemini untuk merumuskan konsep, hierarki pesan, dan prompt.
> 2. **Pembuatan gambar:** Dilakukan di AI yang memiliki fitur pembuat gambar (misalnya ChatGPT Plus/Team atau Gemini Advanced/Pro). Beberapa antarmuka chat (termasuk Claude standar) sangat cakap menyusun prompt tetapi belum terintegrasi pembuat gambar langsung; salin prompt hasil akhir ke model pembuat gambar pilihan Anda.

### Cara 1 (Paling mudah, tanpa instalasi)

1. **Unduh** file [`siap-pakai/umkm-design-director-lengkap.md`](siap-pakai/umkm-design-director-lengkap.md) (buka file, pilih tombol **Download** atau **Raw**, lalu simpan ke komputer/HP).
2. **Buka obrolan baru** di ChatGPT, Claude, atau Gemini, lalu **unggah file tersebut** (klik ikon klip kertas atau tanda `+`).
3. **Kirim pesan pembuka ini** bersama file:

   > Halo! Saya pemilik usaha dan ingin membuat materi desain promosi cetak. Tolong ikuti panduan di file terlampir sepenuhnya: mulai dari Tahap 0, ajukan pertanyaan sedikit demi sedikit (maksimal 3 pertanyaan per giliran) menggunakan bahasa Indonesia yang sederhana dan mudah dipahami. Di akhir, berikan rencana desain, ringkasan arah kreatif, dan prompt gambar siap pakai beserta daftar lampiran gambarnya.
   >
   > *(English: Hi! I own a small business and want to design physical promotional materials. Please follow the attached guide fully: start at Stage 0, ask me at most 3 simple questions at a time in plain language. At the end, deliver a shared design plan, creative direction summary, and ready-to-use standalone image prompts with attachment instructions.)*

4. **Jawab pertanyaan secara bertahap.** Siapkan foto produk asli, logo, foto tempat usaha, atau contoh desain lama (bila ada). Jawaban yang jujur, konkret (bahan, resep, ukuran porsi, cerita usaha) akan menghasilkan desain yang berkarakter dan unik.
5. **Terima hasil lengkap:** Rencana desain bersama, rumusan **Visual Thesis**, ringkasan arah kreatif, dan **Prompt 1, Prompt 2, ...** (satu prompt mandiri per materi fisik yang dibutuhkan). Setiap prompt berdiri sendiri dalam blok kode terpisah dan memiliki daftar lampiran lokal.
6. **Buat gambarnya:** Buka obrolan baru di AI pembuat gambar Anda, **salin satu prompt utuh, lampirkan gambar sesuai urutan lampiran, lalu kirim bersamaan.** Ulangi langkah ini secara terpisah untuk prompt materi lainnya.
7. **Periksa hasil:** Cek ejaan nama usaha, harga, tanggal, dan nomor kontak huruf demi huruf. Tempel logo sertifikasi resmi (Halal Indonesia/BPOM) dan QR code secara manual bila diwajibkan secara hukum.

*Jika AI menolak file atau paket gratis membatasi ukuran unggahan dokumen (file lengkap berukuran ~267 KB), gunakan Cara 2 atau Cara 3 di bawah.*

---

### Cara 2 (Setup sekali, dipakai berulang)

Buat asisten khusus di akun Anda agar panduan tersimpan permanen dan tidak perlu diunggah ulang setiap sesi:

| Layanan AI | Langkah Penyiapan |
|---|---|
| **ChatGPT** | Buat **Custom GPT** atau **Project** baru. Isi kolom **Instructions** dengan teks dari [`siap-pakai/umkm-design-director-ringkas.md`](siap-pakai/umkm-design-director-ringkas.md) (di bawah 8.000 karakter), lalu unggah [`siap-pakai/umkm-design-director-lengkap.md`](siap-pakai/umkm-design-director-lengkap.md) ke bagian **Knowledge / Files**. |
| **Gemini** | Buat **Gem** baru. Masukkan isi `umkm-design-director-ringkas.md` ke kolom **Instructions**, lalu unggah `umkm-design-director-lengkap.md` sebagai file pendukung pengetahuan. |
| **Claude** | Buat **Project**: Isi kolom **Project Instructions** dengan `umkm-design-director-ringkas.md`, dan tambahkan `umkm-design-director-lengkap.md` ke **Project Knowledge**. Untuk pengguna Claude dengan dukungan skill kustom, unggah langsung file [`siap-pakai/umkm-design-director.skill`](siap-pakai/umkm-design-director.skill) (~114 KB) di Settings $\to$ Capabilities $\to$ Skills. |

---

### Cara 3 (Jika tidak bisa mengunggah dokumen)

Salin seluruh isi [`siap-pakai/umkm-design-director-ringkas.md`](siap-pakai/umkm-design-director-ringkas.md) langsung ke dalam kotak obrolan sebagai pesan pertama Anda, lalu tambahkan tulisan *"Mulai"* di baris terakhir. AI akan langsung menyapa Anda dan memulai sesi wawancara.

---

## Tips Agar Desain Tampil Maksimal

- **Gunakan foto produk asli:** Foto dengan pencahayaan alami jendela dan latar belakang bersih selalu lebih dipercaya pembeli daripada gambar tiruan AI. Sistem akan menjaga foto produk Anda tanpa distorsi.
- **Berikan detail konkret (Anchors):** Ceritakan bahan baku asli (mis. "gula aren organik Cilacap", "daun pandan suji segar"), resep keluarga, atau alat khas (piring seng blirik, kuali tanah liat). Detail ini akan diubah sistem menjadi tekstur fisik nyata di gambar.
- **Satu pesan, satu hero visual:** Jangan penuhi materi promosi dengan puluhan teks kecil. Ruang tenang (35–50%) membuat pesan utama terbaca seketika (1–2 detik dari jalan raya).
- **Karya akhir langsung jadi (Final Integrated Artwork):** Seluruh tulisan, nama usaha, harga, dan penawaran dirender langsung ke dalam gambar secara utuh oleh AI. Anda tidak perlu menyisakan kotak kosong untuk repot mendesain ulang di Canva, kecuali jika secara khusus meminta template latar belakang.

---

## Mengapa Framework Ini Berbeda?

Banyak desain promosi UMKM berbasis AI terlihat generik dan murahan: efek kilau plastik 3D berlebihan, makanan tampak seperti lilin mainan, tata letak simetris kaku di tengah, dan gradien neon ungu/oranye. Masalah utamanya adalah **ketiadaan keputusan art direction**: model AI akan mengambil rata-rata internet jika tidak diarahkan dengan parameter visual yang presisi.

Skill ini dirancang layaknya seorang **Art Director & Visual Strategist Senior**:

1. **Uji Tukar Visual (Visual Swap Test):** Setiap konsep harus lolos pengujian: *"Jika nama usaha ini diganti dengan nama pesaing terdekatnya, apakah desainnya masih masuk akal?"* Jika ya, desain dianggap terlalu generik dan wajib diperkuat dengan jangkar khas usaha Anda.
2. **Spesifikasi Optik Positif vs Larangan Negatif:** Model AI tidak memahami adjektiva mood abstrak (*"terasa hangat"*, *"percaya diri"*). Framework ini mendiktekan parameter optik konkret: tradisi visual (Plakatstil Jerman, litografi komersial 1950-an, Swiss Modernism, vernakular warung Jawa/Sumatera), teknik medium (gouache tebal, woodcut, linocut, fotografi still life bernuansa studio), perlakuan tepi bentuk, dan material substrat cetak nyata (terpal vinyl flexi, kertas karton daur ulang berpori, kertas dluwang).
3. **Formulasi Visual Thesis:** Arah visual dibangun dari sintesis formal:
   $$\text{Visual Thesis} = \text{Tradisi Visual} + \text{Teknik Medium} + \text{Bahasa Bentuk \& Tepi} + \text{Substrat Material} + \text{Anatomi Tipografi}$$
   Menghindari pencocokan klise kategori (bakso tidak harus merah dan berasap; roti tidak harus krim pastel dan tulisan sambung).
4. **Perhitungan Konteks Fisik Cetak & Tipografi Anatomi:** Disesuaikan dengan jarak pandang fisik nyata (skala tinggi huruf 2,5 cm per 3 meter jarak pandang), kecepatan penonton (1–2 detik pengendara motor vs 15–30 detik menu meja), dan kontras nilai ekstrem di bawah terik matahari tropis.
5. **Prompt Bersih dan Mandiri (Zero Cross-Prompt Dependencies):** Prompts untuk beberapa materi sekaligus (mis. spanduk + poster) berbagi satu blok Sistem Visual yang identik demi konsistensi merek, namun masing-masing prompt 100% mandiri tanpa ketergantungan frasa rancu seperti *"same as previous prompt"*.

Contoh sesi lengkap: [`examples/01-warung-bakso-sesi-lengkap.md`](examples/01-warung-bakso-sesi-lengkap.md) (dua prompt mandiri terpadu).  
Contoh spanduk ringkas: [`examples/02-spanduk-laundry-ringkas.md`](examples/02-spanduk-laundry-ringkas.md).

---

## Isi Folder `siap-pakai/`

| File | Ukuran | Kegunaan |
|---|---|---|
| [`umkm-design-director-lengkap.md`](siap-pakai/umkm-design-director-lengkap.md) | ~267 KB | Panduan lengkap untuk diunggah ke ChatGPT, Claude, atau Gemini (Cara 1 & 2). |
| [`umkm-design-director-ringkas.md`](siap-pakai/umkm-design-director-ringkas.md) | 7.879 kar. | Versi ringkas padat instruksi untuk kolom Custom GPT / Gem / Claude Project (< 8.000 karakter). |
| [`umkm-design-director.skill`](siap-pakai/umkm-design-director.skill) | ~114 KB | Paket zip skill terstandar untuk diimpor ke Claude Skills atau runtime Agent Skills. |

---

## Untuk Pengembang dan Kontributor

Framework ini dibangun di atas spesifikasi terbuka [Agent Skills](https://agentskills.io) dengan prinsip *progressive disclosure* (instruksi inti di `SKILL.md` dimuat terlebih dahulu, sedangkan modul referensi di `references/` dibaca saat tahap terkait aktif).

### Pemasangan di Coding Agent & Lingkungan CLI

| Alat / Runtime | Cara Pemasangan |
|---|---|
| **Claude Code** | Salin folder `skills/umkm-design-director/` ke `~/.claude/skills/` (global) atau `.claude/skills/` (proyek). |
| **Antigravity / Gemini CLI / Cursor / Codex** | Pastikan folder `skills/umkm-design-director` berada di direktori skills agen Anda. |
| **Build & Bundling** | Jalankan `python scripts/bundle.py` untuk mengompilasi ulang `siap-pakai/umkm-design-director-lengkap.md` dan `siap-pakai/umkm-design-director.skill`. |
| **Validasi Otomatis** | Jalankan `python scripts/validate.py` untuk memastikan batas baris `SKILL.md` ($\le 500$), batas karakter versi ringkas ($< 8.000$), validitas tautan referensi, serta integritas Sistem Visual pada contoh. |

### Struktur Repositori

```
umkm-design-director/
├── README.md                                 # Panduan penggunaan dan dokumentasi proyek
├── CONTRIBUTING.md                           # Panduan kontribusi dan aturan pengujian
├── siap-pakai/                               # Distribusi siap pakai untuk pengguna umum
│   ├── umkm-design-director-lengkap.md       # Bundel markdown tunggal lengkap (~267 KB)
│   ├── umkm-design-director-ringkas.md       # Versi ringkas instruksi chat (7.879 karakter)
│   └── umkm-design-director.skill            # Arsip terkompresi zip Agent Skill (~114 KB)
├── skills/umkm-design-director/
│   ├── SKILL.md                              # Pipeline 8 tahap desain, aturan keputusan, dan self-check
│   ├── references/                           # Modul pengetahuan art direction mendalam
│   │   ├── 01-interview-guide.md             # Wawancara adaptif (maks 3 tanya), terjemahan istilah, Stage 5
│   │   ├── 02-business-distinction.md        # Peta distingsi usaha, jangkar fisik, wilayah pesaing, uji tukar
│   │   ├── 03-reference-images.md            # Audit aset asli, perlakuan foto napak, mode Build vs Enhance
│   │   ├── 04-design-principles.md           # Tata visual formal Gestalt, hierarki L1-L4, alokasi ruang tenang
│   │   ├── 05-color-and-culture.md           # Palet peran 60-30-10, psikologi warna, konteks budaya Nusantara
│   │   ├── 06-typography.md                  # Anatomi huruf (Grotesque, Slab, Didone), skala jarak pandang fisik
│   │   ├── 07-business-archetypes.md         # 10 arketipe UMKM, penggerak kepercayaan, jebakan slop, identitas
│   │   ├── 08-formats-and-platforms.md       # Spesifikasi cetak fisik (spanduk, poster, menu, flyer, label)
│   │   ├── 09-output-sets.md                 # Manajemen multi-output serangkai, Sistem Visual identik
│   │   ├── 10-anti-slop.md                   # Mekanika kegagalan AI slop, spesifikasi optik positif material
│   │   ├── 11-prompt-assembly.md             # Aturan art-direction-first, struktur 10 blok kanonik, 3 contoh
│   │   ├── 12-review-and-iteration.md        # Checklist 12 poin tinjauan, aturan satu perubahan per iterasi
│   │   ├── 13-design-thinking.md             # Penalaran desainer, simulasi 3 tahap pandang, ringkasan arah kreatif
│   │   ├── 14-visual-language.md             # Taksonomi visual, 11 tradisi cetak dunia, 5 vernakular Nusantara
│   │   └── 15-creative-direction-framework.md # 10 dimensi desain, sintesis Visual Thesis, uji wilayah visual
│   └── assets/
│       ├── brief-template.md                 # Lembar kerja pelacak keputusan desain tahap 1–6
│       └── prompt-template.md                # Kerangka kanonik prompt fisik print dan checklist pra-kirim
├── examples/                                 # Contoh sesi lengkap dan spanduk ringkas
├── evals/                                    # 14 skenario uji evaluasi (evals.json)
├── scripts/                                  # validate.py dan bundle.py
└── docs/RESEARCH-NOTES.md                    # Catatan riset arsitektur skill dan prinsip anti-slop
```

### Pengujian & Status Evaluasi

Suite evaluasi di [`evals/evals.json`](evals/evals.json) memverifikasi 14 skenario nyata:
- Respon bahasa Indonesia yang hangat tanpa jargon teknis (Eval 1)
- Ekstraksi informasi mandiri dan rencana ringkas (Eval 2)
- Penanganan cetak jarak jauh dalam bahasa Inggris (Eval 3)
- Penolakan pembuatan sertifikasi Halal / QR code ilegal oleh AI (Eval 4)
- Resolusi keinginan kontradiktif "mewah tapi murah" (Eval 5)
- Konsistensi multi-output mandiri dengan Sistem Visual identik (Eval 6)
- Penggalian diferensiasi mendalam toko kue (Eval 7)
- Disiplin ruang kosong dan pemangkasan dekorasi berlebih (Eval 8)
- Mode Enhance untuk diagnosis santun materi lama (Eval 9)
- Penanganan pembuka chat AI umum (Eval 10)
- Art direction spesifik toko roti Bu Tatik Surabaya (Eval 11)
- Diferensiasi dua kedai kopi: kaki lima Bekasi vs specialty roastery Jaksel (Eval 12)
- Seleksi bahasa visual kriya anyaman pandan Sukarara Lombok (Eval 13)
- Resolusi multidimensi salon warisan Jawa Malang menyambut Lebaran (Eval 14)

Semua skenario telah diaudit dan divalidasi dengan kode keluar 0 pada `scripts/validate.py`.

---

## English Summary

**UMKM Design Director is a professional art-direction framework and prompt system for small-business physical print marketing.**

Small businesses often end up with generic "AI-slop" graphics (plastic food renders, floating elements, neon gradients, and illegible text) because image models default to generic internet averages when prompts rely on vague literary mood descriptions (*"cozy vibes"*, *"domestic satisfaction"*).

This skill acts as an experienced Art Director:
1. **Guided Adaptive Interview:** Conducts a friendly, structured inquiry (max 3 questions per turn) in plain language, deriving distinction, physical viewing constraints (distance, speed, substrate), and message hierarchy.
2. **Visual Thesis Formulation:** Builds a concrete artistic thesis:
   $$\text{Visual Thesis} = \text{Visual Lineage} + \text{Image-Making Technique} + \text{Form Language/Edges} + \text{Material Substrate} + \text{Typographic Anatomy}$$
   drawing from 11 print traditions (Plakatstil, Mid-century lithography, Swiss Modernism, Linocut, Woodblock) and authentic Indonesian vernacular lineages.
3. **Physical Distance Scaling:** Calculates type sizes based on real-world optics (2.5 cm letter height per 3 meters distance) and ensures extreme value contrast for tropical outdoor sunlight.
4. **Final Integrated Artwork Default:** Renders all typography, headlines, prices, and branding directly in the image with anatomical classification directives, avoiding empty placeholder text boxes.
5. **Standalone Production-Ready Prompts:** Delivers completely self-contained prompts per format, each with its own local attachment instructions and a shared, word-for-word identical Visual System block.

**How to use:**
- **No install:** Download [`siap-pakai/umkm-design-director-lengkap.md`](siap-pakai/umkm-design-director-lengkap.md) (~267 KB), upload to ChatGPT, Claude, or Gemini, and start chatting.
- **Custom Assistant:** Paste [`siap-pakai/umkm-design-director-ringkas.md`](siap-pakai/umkm-design-director-ringkas.md) (7,879 chars) into custom GPT/Gem/Project instructions and upload the full file as knowledge.
- **Claude Skills / CLI Agents:** Upload [`siap-pakai/umkm-design-director.skill`](siap-pakai/umkm-design-director.skill) (~114 KB) or copy `skills/umkm-design-director/` into your Agent Skills directory. Run `python scripts/validate.py` to verify.

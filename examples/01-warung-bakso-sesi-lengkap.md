# Contoh sesi lengkap: Warung Bakso (dari permintaan samar sampai dua prompt mandiri)

Contoh ini menunjukkan alur skill: menggali keunggulan usaha, menanyakan gambar acuan, menentukan beberapa output, lalu menghasilkan **satu prompt mandiri per output** dengan **daftar lampiran per prompt**.
**U** = pemilik usaha, **S** = skill. Sesi dipadatkan; di sesi asli tiap giliran maksimal 3 pertanyaan.

---

**U:** buatin poster promo buat warung bakso saya dong, yang bagus biar ga keliatan AI

**S:** Siap, Kak! Saya tanya beberapa hal sederhana dulu supaya hasilnya benar-benar cocok untuk warung Kakak. Nggak perlu paham desain.
1. Nama warungnya apa, di daerah mana, dan harganya kira-kira?
2. Apa yang bikin bakso Kakak beda dari warung bakso lain? Kalau cuma boleh sebut satu.
3. Pelanggan biasanya bilang apa, kenapa beli di Kakak?

**U:** Bakso Pak Darto, Jl. Kemuning Klaten, 15rb. Bedanya bakso urat segede bola tenis. Pelanggan bilang "kenyang beneran, nggak pelit".

**S:** Mantap, "segede bola tenis" itu bukti yang bisa dilihat. Tiga hal lagi supaya tampilannya pas:
1. Apa buktinya selain ukuran? (kuah, bahan, cara bikin)
2. Pesaing terdekat tampilannya seperti apa? (supaya kita bisa beda)
3. Orang yang baru lihat, dalam 3 detik Kakak mau mereka merasa apa, dan jangan sampai dianggap apa?

**U:** Kuah kaldu sapi bening, direbus dari subuh. Pesaing banyak yang spanduk merah rame penuh tulisan. Mau kesannya jujur dan royal, jangan sampai kelihatan murahan.

**S:** Jelas. Ringkasan saya: *Bakso Pak Darto, Klaten, beda karena bakso urat segede bola tenis dengan kuah bening direbus dari subuh; pembeli bilang "kenyang beneran, nggak pelit"; kesan: jujur dan royal, bukan murahan; beda dari pesaing yang merah, ramai, dan penuh tulisan.* Betul? Lalu, ada gambar acuan? Boleh pilih lebih dari satu: A. Logo, B. Foto bakso asli, C. Foto gerobak, D. Desain lama, E. Contoh desain yang disuka, F. Belum ada.

**U:** Betul. Ada logo, foto bakso, foto gerobak (3 gambar).

**S:** Saya terima Gambar 1 (foto bakso), Gambar 2 (foto gerobak biru), Gambar 3 (logo). Fotonya bagus; latar foto bakso saya minta dibersihkan tanpa mengubah baksonya. Posternya mau dipasang di mana, dan tujuannya apa? Ada promo?

**U:** Promo beli 2 porsi gratis es teh sampai akhir bulan. Biar orang datang ke warung. Untuk Instagram, feed sama story.

**S:** Berarti dua gambar: feed 4:5 (menarik dan menawarkan) dan story 9:16 (menekankan batas waktu dan ajakan datang). Pembelinya siapa, dan nanti pakai AI yang mana untuk bikin gambar?

**U:** Keluarga dan pekerja pabrik siang. Pakai ChatGPT, bisa unggah banyak gambar.

**S:** Terakhir: alamat dan jam buka berapa? Logo halal harus yang resmi, jadi nanti Kakak tempel sendiri; saya sisakan kotaknya.

**U:** Jl. Kemuning, Klaten, buka 10.00-21.00.

---

## Rencana desain bersama

- **Pesan:** "Bakso segede bola tenis": ukuran jadi bukti, bukan kata "enak".
- **Kesan:** jujur dan royal, bukan murahan. Beda dari spanduk merah yang ramai: kita pakai ruang lega dan satu bintang.
- **Sistem visual (sama di semua gambar):** biru gerobak (#1F4E8C) sebagai warna utama, krem (#F3E6CE) untuk tulisan, merah cabai (#D6452F) hanya untuk penawaran; huruf cat tangan ala papan warung; foto asli tidak diubah; satu label krem hanya di balik penawaran; ruang kosong sekitar 40%.
- **Pemakaian gambar:** foto bakso = bintang (dibersihkan latarnya); foto gerobak = latar story; logo = ditempel apa adanya.
- **Teks:** sebagian di dalam gambar (judul, penawaran, alamat); logo halal ditempel sendiri.
- **Asumsi saya:** foto bakso cukup tajam untuk dipakai langsung.

## Daftar output

| Prompt | Output | Fungsi | Lampiran |
|---|---|---|---|
| 1 | Feed Instagram 4:5 | menarik dan menawarkan | foto bakso, logo |
| 2 | Story 9:16 | batas waktu dan ajakan datang | foto bakso, foto gerobak, logo |

## Prompt 1: Feed Instagram (4:5)

```
FORMAT: Instagram feed promo post, vertical 4:5 (1080x1350 px). Viewed on a phone during a fast scroll; must read in 3 seconds.

CONCEPT: "Bakso segede bola tenis." Warm, honest, proudly local. For families and factory workers in Klaten who want a filling lunch. This output's job: hook and offer.

ATTACHED IMAGES (attach in this order):
Image 1 = the owner's real photo of a bowl of bakso urat with a tennis-ball-sized meatball in clear beef broth. Role: hero. Treatment: keep exactly; clean the background. Placement: slightly right of center on a worn wooden cart counter. Size: about 50% of canvas height. Keep unchanged: bowl, broth, meatballs, colors. May change: background.
Image 2 = the business logo "Bakso Pak Darto". Role: brand mark. Treatment: place unaltered. Placement: top-right corner, about 14% of canvas width, with clear space. Keep unchanged: everything.
Priority: Image 1 wins on food appearance; never redraw Image 2.

HERO VISUAL: Image 1, gentle high angle, a little real steam, soft side window light.

COMPOSITION: Asymmetric, left-aligned spine. Headline in the top 27%. Offer label in the middle band left of the bowl. Narrow address strip across the bottom 10%. SPACE: about 40% of the canvas stays calm and empty (flat cart-blue), mainly the upper right and the lower left; nothing floats in it; no decorative elements. Margins about 6%. Reserve a small empty square in the bottom-right corner (about 12% of width) for an official halal logo added later; render nothing in it. Eye path: headline -> bowl -> offer -> address.

TEXT (render exactly as written, in Indonesian, no additional words):
1. Headline "BAKSO SEGEDE BOLA TENIS" - largest, three short lines, cream (#F3E6CE).
2. Offer "Beli 2 porsi, GRATIS es teh" - second largest, chili-red on the cream label; small beneath: "sampai akhir bulan".
3. Address strip "Jl. Kemuning, Klaten - buka 10.00-21.00" - small, cream on blue.
No other text, taglines, or logos.

VISUAL SYSTEM (identical in every prompt of this set):
Palette: cart-blue (#1F4E8C) dominant ~60%; warm cream (#F3E6CE) ~30%; chili-red (#D6452F) ~10%, used only for the offer. Type: hand-painted sign-painter capitals for headline and offer; sturdy humanist sans for support text. Style and material: real photos on a flat hand-painted blue wooden-cart wall with faint brush texture, matte, soft natural light. Image treatment: real product photos kept exactly, grounded on a surface, backgrounds cleaned or replaced only. Device: a plain cream painted label shape behind the offer only. Space level: calm.

KEEP / AVOID: Keep the bowl and logo exactly as provided. Avoid floating ingredients, glow, gradients, sparkles, extra text, stock-style people, crowded corners.
```

**Lampiran Prompt 1** (urutan harus sama):
1. Foto bakso (hero)
2. Logo Bakso Pak Darto (pojok kanan atas)

## Prompt 2: Story (9:16)

```
FORMAT: Instagram and WhatsApp story, vertical 9:16 (1080x1920 px), viewed full-screen for 2-5 seconds. Keep all text and the logo inside the central 70% of the height.

CONCEPT: "Bakso segede bola tenis." Warm, honest, proudly local. For families and factory workers in Klaten who want a filling lunch. This output's job: push the deadline and get people to come.

ATTACHED IMAGES (attach in this order):
Image 1 = the owner's real photo of a bowl of bakso urat with a tennis-ball-sized meatball in clear beef broth. Role: hero. Treatment: keep exactly; cut out and place. Placement: centered in the lower middle, resting on the counter of Image 2. Size: about 38% of canvas height. Keep unchanged: bowl, broth, meatballs, colors. May change: background.
Image 2 = the owner's photo of the blue wooden bakso cart. Role: setting. Treatment: clean up stray objects and other brands' signs; soften focus behind the bowl. Placement: upper two-thirds as a quiet backdrop, counter at the 62% height line. Keep unchanged: the cart's blue and wood.
Image 3 = the business logo "Bakso Pak Darto". Role: brand mark. Treatment: place unaltered. Placement: top-left inside the safe area, about 18% of canvas width.
Priority: Image 1 wins on food appearance; Image 2 is background only; never redraw Image 3.

HERO VISUAL: Image 1 on the cart counter from Image 2, soft side window light, a little real steam.

COMPOSITION: Vertical stack with a left-aligned spine. Headline in the upper third beside the logo, offer label under the bowl, address line near the lower safe limit. SPACE: about 40% of the canvas stays calm (the softened cart wall and flat blue), mainly the upper right; nothing floats in it; no decorative elements. Margins about 7%. Reserve a small empty square (about 12% of width) at the lower right inside the safe area for an official halal logo added later; render nothing in it. Eye path: headline -> bowl -> offer -> address.

TEXT (render exactly as written, in Indonesian, no additional words):
1. Headline "SEGEDE BOLA TENIS" - largest, two lines, cream (#F3E6CE).
2. Offer "Beli 2 porsi, GRATIS es teh" - second largest, chili-red on the cream label; small beneath: "sampai akhir bulan".
3. Address line "Mampir: Jl. Kemuning, Klaten" - small, cream on blue.
No other text, taglines, or logos.

VISUAL SYSTEM (identical in every prompt of this set):
Palette: cart-blue (#1F4E8C) dominant ~60%; warm cream (#F3E6CE) ~30%; chili-red (#D6452F) ~10%, used only for the offer. Type: hand-painted sign-painter capitals for headline and offer; sturdy humanist sans for support text. Style and material: real photos on a flat hand-painted blue wooden-cart wall with faint brush texture, matte, soft natural light. Image treatment: real product photos kept exactly, grounded on a surface, backgrounds cleaned or replaced only. Device: a plain cream painted label shape behind the offer only. Space level: calm.

KEEP / AVOID: Keep the bowl and logo exactly as provided. Avoid floating ingredients, glow, gradients, sparkles, extra text, stock-style people, crowded corners.
```

**Lampiran Prompt 2** (urutan harus sama):
1. Foto bakso (hero)
2. Foto gerobak biru (latar)
3. Logo Bakso Pak Darto (kiri atas)

## Cara pakai
1. Buka ChatGPT (chat baru untuk tiap prompt lebih rapi). **Salin Prompt 1, lampirkan gambar sesuai urutannya, lalu kirim bersamaan.** Ulangi untuk Prompt 2.
2. Cek tulisan huruf demi huruf: "BAKSO SEGEDE BOLA TENIS", "GRATIS", alamat, jam buka.
3. Tempel logo halal resmi di kotak kosong (Canva), lalu bandingkan kedua gambar berdampingan sebelum posting.

## Kenapa ini tidak terlihat seperti AI pasaran
- **Beda dari pesaing dengan sengaja:** pesaing ramai dan merah; ini lega dan biru dengan satu bintang.
- **Dua jangkar spesifik:** ukuran "segede bola tenis" dan gerobak biru asli.
- **Ruang dialokasikan:** 40% kosong dan datar, tanpa hiasan; hanya yang perlu yang tampil.
- **Foto asli dipertahankan:** bakso tidak dikarang AI.
- **Satu keluarga, dua prompt mandiri:** sistem visual ditulis persis sama di kedua prompt, dan tidak ada prompt yang merujuk prompt lain.

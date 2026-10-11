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

**S:** Terakhir: alamat dan jam buka berapa?

**U:** Jl. Kemuning, Klaten, buka 10.00-21.00.

---

## Rencana desain bersama

- **Konsep:** "Bakso segede bola tenis" — ukuran jadi bukti konkret, bukan klaim rasa abstrak.
- **Brief emosional:** Rasa jujur dan royal → mangkuk bakso nyata dan besar sebagai bintang tunggal → foto asli dipertahankan, latar biru gerobak yang tenang dan berwibawa, tanpa dekorasi artifisial.
- **Kesan:** Jujur dan royal, bukan murahan. Beda dari pesaing yang merah, ramai, dan penuh tulisan: kita pakai ruang lega, biru gerobak khas, dan satu bintang visual yang dominan.
- **Arah kreatif (Visual Thesis):** *German Plakatstil object-poster tradition dipadukan dengan seni reklame warung tenda tradisional Indonesia.* Mangkuk bakso asli berdiri kokoh di atas bidang biru cat kayu gerobak Pak Darto (#1F4E8C), dipadukan huruf tebal cat kuas berpotongan rata warna kuning kadmium (#FFD700) dan label krem polos (#FFFDD0).
- **Sistem visual (sama di semua gambar):** Huruf tebal cat tangan ala papan warung; foto asli tidak diubah; satu panel krem di balik penawaran; ruang tenang dan lega di sekitar bintang.
- **Pemakaian gambar:** foto bakso = bintang (latar diisolasi ke biru gerobak); foto gerobak = latar story; logo = ditempel apa adanya.
- **Teks:** Semua tulisan utama dirender langsung utuh di dalam gambar (karya akhir langsung jadi).
- **Asumsi saya:** foto bakso cukup tajam untuk dipakai langsung.

## Daftar output

| Prompt | Output | Fungsi | Lampiran |
|---|---|---|---|
| 1 | Feed Instagram 4:5 | Menarik dan menawarkan | Foto bakso, logo |
| 2 | Story 9:16 | Batas waktu dan ajakan datang | Foto bakso, foto gerobak, logo |

## Prompt 1: Feed Instagram (4:5)

```
FORMAT: Instagram feed promotional graphic, vertical 4:5 (1080×1350 px), digital display format.

OBJECTIVE: Catch the attention of passing workers and families mid-scroll, delivering instant recognition of the giant meatball offer so they decide to visit for lunch.

CONCEPT: "Bakso segede bola tenis." Warm, honest, proudly local. For families and factory workers in Klaten who want a filling, trustworthy lunch.

CONTENT:
- Headline: "BAKSO SEGEDE BOLA TENIS"
- Offer: "Beli 2 porsi, GRATIS es teh"
- Condition: "sampai akhir bulan"
- Address: "Jl. Kemuning, Klaten — buka 10.00–21.00"
- Hero: bowl of bakso urat with real giant meatball (Image 1)
- Brand: business logo (Image 2), upper placement
Render all copy exactly as written, in Indonesian, integrated directly into the final artwork. No blank reserved text zones.

CREATIVE DIRECTION: German Plakatstil object-poster tradition combined with Indonesian vernacular commercial sign-painting (seni reklame warung tenda). The composition is built around a singular dominant bowl silhouette commanding an unadorned, deep cart-blue field (#1F4E8C) — the specific weathered blue of Pak Darto's wooden gerobak. Flat matte enamel finish with zero digital gradients, zero artificial glows. Heavy condensed sign-painter casual capitals with flat-cut terminals in warm cadmium yellow (#FFD700) anchor the headline with bold graphic mass. A solid cream rectangular base panel (#FFFDD0) provides high-contrast grounding for the free tea offer. Generous unprinted negative space (approximately 45% of canvas) creates powerful visual focus and communicates honest neighborhood authority.

DESIGN CHARACTER: The undeniable visual identity of Pak Darto's 20-year-old wooden cart on Jl. Kemuning: the specific weathered cart-blue, the hand-painted enamel lettering with brush fringe, and the real tennis-ball-sized meatball. The dramatic scale contrast between the quiet grounded bowl and the bold headline proof ("SEGEDE BOLA TENIS") belongs exclusively to this warung and cannot be borrowed by a competitor.

HERO VISUAL: Image 1 — the owner's real photo of a bowl of bakso urat with a tennis-ball-sized meatball in clear bone broth. Keep the product exactly as photographed: bowl shape, broth color, meatball size, and visible urat texture unchanged. Place the bowl slightly right of center, resting solidly on a worn dark-teak wooden counter surface with satin finish. Directional raking morning window light from the left at 45°, casting a soft grounded contact shadow with penumbra falloff to the right. Seamless planar transition into the solid cart-blue background field (#1F4E8C). No reflections, no floating ingredients.

LOGO / IDENTITY: Image 2 — business logo "Bakso Pak Darto." Place unaltered in upper area. Keep unchanged: everything. Never redraw or recolor.

VISUAL SYSTEM (identical in every prompt of this set):
Type: heavy condensed sign-painter casual capitals with flat-cut terminals for headline; sturdy humanist sans for supporting copy; no scripts. Style and material: photographic real product on opaque painted wooden-cart surface, matte enamel finish, soft natural directional window light. Image treatment: real product photos preserved exactly, physically grounded with soft contact shadows, background isolated onto solid cart-blue. Device: solid cream rectangular label panel behind offer. Space level: calm.

ATTACHED IMAGES (attach in this order):
Image 1 = owner's real photo of a bowl of bakso urat with a tennis-ball-sized meatball in clear beef broth. Role: hero. Treatment: keep product exactly; isolate onto solid cart-blue background. Keep unchanged: bowl, broth, meatballs, colors. May change: background.
Image 2 = business logo "Bakso Pak Darto". Role: brand mark. Treatment: place unaltered, upper area. Keep unchanged: everything.
Priority if conflicts: Image 1 governs food appearance; Image 2 must never be redrawn or recolored.

EXCLUSIONS: Keep bowl, broth, meatballs, and logo exactly as provided. Avoid floating meatballs or splashing broth, glow effects, gradient backgrounds, decorative sparkles, extra invented text, stock smiling people, crowded corners, chili decorations scattered around the bowl.
```

**Lampiran Prompt 1** (urutan harus sama):
1. Foto bakso (hero)
2. Logo Bakso Pak Darto (area atas)

## Prompt 2: Story (9:16)

```
FORMAT: Instagram and WhatsApp story graphic, vertical 9:16 (1080×1920 px), mobile vertical format.

OBJECTIVE: Push the month-end deadline and make visiting immediate and frictionless for an interested patron — address and action clear at a glance.

CONCEPT: "Bakso segede bola tenis." Warm, honest, proudly local. For families and factory workers in Klaten who want a filling, trustworthy lunch.

CONTENT:
- Headline: "SEGEDE BOLA TENIS"
- Offer: "Beli 2 porsi, GRATIS es teh"
- Condition: "sampai akhir bulan"
- Address: "Mampir: Jl. Kemuning, Klaten"
- Hero: bowl of bakso urat with real meatball (Image 1), resting on the cart counter from Image 2
- Brand: business logo (Image 3), upper area inside safe zone
Render all copy exactly as written, in Indonesian, integrated directly into final artwork. Keep all text and logo inside the central safe zone (avoid top and bottom 15% of canvas).

CREATIVE DIRECTION: German Plakatstil object-poster tradition combined with Indonesian vernacular commercial sign-painting, adapted for a vertical story format. The composition uses vertical planar layering: the upper half is anchored by the softened, authentic blue wooden texture of Pak Darto's actual cart, while the lower half grounds the bowl and high-contrast typographic call to action. Flat matte finish, zero digital gradients, zero artificial sparkles. The headline in massive cadmium yellow sign-painter capitals (#FFD700) and the free iced tea offer in a crisp cream panel (#FFFDD0) command immediate attention in the central safe zone, designed for a 2-second vertical glance.

DESIGN CHARACTER: The authentic atmosphere of Pak Darto's actual cart on Jl. Kemuning: the real weathered blue wood backdrop, the sign-painter lettering, and the unmistakable tennis-ball-sized meatball resting on the cart counter. The design turns the owner's real physical stall and giant meatball proof into an un-swappable neighborhood brand that competitor warungs cannot copy.

HERO VISUAL: Image 1 — the owner's real bowl of bakso urat with a tennis-ball-sized meatball, resting directly on the wooden counter surface of Image 2. Keep the product exactly as photographed: bowl shape, broth color, meatball size, and urat texture unchanged. Soft directional side window light from the left, faint natural steam wisp above the broth, authentic grounded contact shadow. Image 2 as setting: soften focus slightly behind the bowl; clean up stray objects or foreign brand signage; preserve the cart's authentic blue paint and weathered wood grain.

LOGO / IDENTITY: Image 3 — business logo "Bakso Pak Darto." Place unaltered, upper area inside safe zone. Keep unchanged: everything. Never redraw or recolor.

VISUAL SYSTEM (identical in every prompt of this set):
Type: heavy condensed sign-painter casual capitals with flat-cut terminals for headline; sturdy humanist sans for supporting copy; no scripts. Style and material: photographic real product on opaque painted wooden-cart surface, matte enamel finish, soft natural directional window light. Image treatment: real product photos preserved exactly, physically grounded with soft contact shadows, background isolated onto solid cart-blue. Device: solid cream rectangular label panel behind offer. Space level: calm.

ATTACHED IMAGES (attach in this order):
Image 1 = owner's real photo of a bowl of bakso urat with a tennis-ball-sized meatball in clear beef broth. Role: hero. Treatment: keep product exactly; place on the cart counter from Image 2. Keep unchanged: bowl, broth, meatballs, colors. May change: background.
Image 2 = owner's photo of the blue wooden bakso cart. Role: setting. Treatment: clean up stray objects and other brands' signs; soften focus behind the bowl; preserve cart blue and wood character. Keep unchanged: the cart's color and structure.
Image 3 = business logo "Bakso Pak Darto". Role: brand mark. Treatment: place unaltered, upper area inside safe zone. Keep unchanged: everything.
Priority if conflicts: Image 1 governs food appearance; Image 2 is background setting; Image 3 must never be redrawn or recolored.

EXCLUSIONS: Keep bowl, meatballs, broth, cart character, and logo exactly as provided. Avoid floating meatballs or splashing broth, glow effects, gradient sky backgrounds, decorative sparkles, extra invented text, stock smiling people, crowded corners, any decoration in the calm upper-right area.
```

**Lampiran Prompt 2** (urutan harus sama):
1. Foto bakso (hero)
2. Foto gerobak biru (latar)
3. Logo Bakso Pak Darto (area atas, dalam safe zone)

## Cara pakai
1. Buka ChatGPT (chat baru untuk tiap prompt lebih rapi). **Salin Prompt 1, lampirkan gambar sesuai urutannya, lalu kirim bersamaan.** Ulangi untuk Prompt 2.
2. Cek tulisan huruf demi huruf: "BAKSO SEGEDE BOLA TENIS", "GRATIS", alamat, jam buka.
3. Bandingkan kedua gambar berdampingan sebelum posting; seluruh gambar sudah lengkap dan siap pakai tanpa perlu diedit ulang.

## Kenapa ini tidak terlihat seperti AI pasaran
- **Beda dari pesaing dengan sengaja:** Pesaing ramai dan merah; ini lega dan biru gerobak dengan satu bintang visual.
- **Dua jangkar spesifik:** Ukuran "segede bola tenis" dan gerobak biru asli Pak Darto.
- **Ruang lega karena konsep, bukan pengukuran:** Ruang tenang di sekitar mangkuk adalah bagian dari karakter desain — keyakinan bahwa bukti ukuran cukup kuat berdiri sendiri.
- **Foto asli dipertahankan:** Bakso asli tidak diganti dengan ilustrasi generik.
- **Satu keluarga, dua prompt mandiri:** Sistem Visual ditulis persis sama di kedua prompt, dan tidak ada prompt yang merujuk prompt lain.

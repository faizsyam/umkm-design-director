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

- **Konsep:** "Bakso segede bola tenis" — ukuran jadi bukti, bukan kata "enak".
- **Brief emosional:** Rasa jujur dan royal → mangkuk bakso nyata dan besar sebagai bintang → foto asli wajib, latar biru gerobak yang tenang, tidak ada dekorasi yang mengalihkan.
- **Kesan:** jujur dan royal, bukan murahan. Beda dari pesaing yang merah, ramai, dan penuh tulisan: kita pakai ruang lega, biru gerobak yang khas, dan satu bintang yang jelas.
- **Arah kreatif:** Biru gerobak Pak Darto yang khas — bukan biru generik laundry, tapi biru cat kayu yang sudah lama ada di Jl. Kemuning. Hangat dan langsung seperti warung yang sudah dipercaya bertahun-tahun.
- **Sistem visual (sama di semua gambar):** Huruf cat tangan ala papan warung; foto asli tidak diubah; satu label krem hanya di balik penawaran; ruang tenang dan lega di sekitar bintang.
- **Pemakaian gambar:** foto bakso = bintang (dibersihkan latarnya); foto gerobak = latar story; logo = ditempel apa adanya.
- **Teks:** Semua tulisan utama (judul, penawaran, alamat, jam buka) dirender langsung utuh di dalam gambar (karya akhir langsung jadi).
- **Asumsi saya:** foto bakso cukup tajam untuk dipakai langsung.

## Daftar output

| Prompt | Output | Fungsi | Lampiran |
|---|---|---|---|
| 1 | Feed Instagram 4:5 | menarik dan menawarkan | foto bakso, logo |
| 2 | Story 9:16 | batas waktu dan ajakan datang | foto bakso, foto gerobak, logo |

## Prompt 1: Feed Instagram (4:5)

```
FORMAT: Instagram feed promo post, vertical 4:5 (1080×1350 px).

OBJECTIVE: Hook a family or factory worker mid-scroll and communicate the daily offer clearly enough that they tap to visit or order.

CONCEPT: "Bakso segede bola tenis." Warm, honest, proudly local. For families and factory workers in Klaten who want a filling, trustworthy lunch.

CONTENT:
- Headline: "BAKSO SEGEDE BOLA TENIS"
- Offer: "Beli 2 porsi, GRATIS es teh"
- Condition: "sampai akhir bulan"
- Address: "Jl. Kemuning, Klaten — buka 10.00–21.00"
- Hero: bowl of bakso urat with real meatball (Image 1)
- Brand: business logo (Image 2), upper area
Render all text exactly as written, in Indonesian, no additional words.

CREATIVE DIRECTION: A warm, confident promo built around one honest product and one striking proof — the meatball the size of a tennis ball. The overall feeling is jujur dan royal: the design of a neighborhood warung that has served the same street for years, direct and unpretentious. Deep cart-blue fills the field — not generic blue, but the specific blue of Pak Darto's wooden gerobak, worn and familiar. The real bowl stands as the quiet hero; the sign-painter headline carries the proof; a single cream label frames the offer. Generous breathing room around the bowl signals confidence. The design looks like something made by a person who knows their food is good and does not need to shout.

DESIGN CHARACTER: The blue is Pak Darto's cart blue — the one thing on Jl. Kemuning that tells regulars "this is the bakso with the enormous meatball." The sign-painter headline, the cream label, and the real bowl together create a design that would look wrong for any other warung. The proof ("segede bola tenis") is the organizing idea — it cannot be borrowed by a competitor.

HERO VISUAL: Image 1 — the owner's real photo of a bowl of bakso urat with a tennis-ball-sized meatball in clear bone broth. Keep the product exactly as photographed: bowl shape, broth color, meatball size, and visible urat texture unchanged. Place the bowl slightly right of center on a worn wooden cart counter, soft side window light from the left, a faint wisp of real steam above the broth. Replace the background with flat cart-blue (#1F4E8C). No reflections on the bowl. Grounded contact shadow beneath.

LOGO / IDENTITY: Image 2 — business logo "Bakso Pak Darto." Place unaltered, upper area. Keep unchanged: everything. Never redraw or recolor.

VISUAL SYSTEM (identical in every prompt of this set):
Type: heavy hand-painted sign-painter capitals for headline and offer; sturdy humanist sans for support text; no scripts. Style and material: real product photos on flat hand-painted blue wooden-cart surface, matte finish, soft natural window light with warm cast. Image treatment: real product photos kept exactly, grounded on surface with soft contact shadow, backgrounds cleaned or replaced only. Device: plain cream painted label shape behind the offer only. Space level: calm.

ATTACHED IMAGES (attach in this order):
Image 1 = owner's real photo of a bowl of bakso urat with a tennis-ball-sized meatball in clear beef broth. Role: hero. Treatment: keep exactly; clean the background; replace with flat cart-blue. Keep unchanged: bowl, broth, meatballs, colors. May change: background.
Image 2 = business logo "Bakso Pak Darto". Role: brand mark. Treatment: place unaltered, upper area. Keep unchanged: everything.
Priority if conflicts: Image 1 wins on food appearance; Image 2 must never be redrawn or recolored.

EXCLUSIONS: Keep bowl, broth, meatballs, and logo exactly as provided. Avoid floating meatballs or splashing broth, glow effects, gradient backgrounds, decorative sparkles, extra invented text, stock smiling people, crowded corners, chili decorations scattered around the bowl.
```

**Lampiran Prompt 1** (urutan harus sama):
1. Foto bakso (hero)
2. Logo Bakso Pak Darto (area atas)

## Prompt 2: Story (9:16)

```
FORMAT: Instagram and WhatsApp story, vertical 9:16 (1080×1920 px).

OBJECTIVE: Push the deadline and make it easy for someone already interested to decide to visit — address and action clear at a glance.

CONCEPT: "Bakso segede bola tenis." Warm, honest, proudly local. For families and factory workers in Klaten who want a filling, trustworthy lunch.

CONTENT:
- Headline: "SEGEDE BOLA TENIS"
- Offer: "Beli 2 porsi, GRATIS es teh"
- Condition: "sampai akhir bulan"
- Address: "Mampir: Jl. Kemuning, Klaten"
- Hero: bowl of bakso urat with real meatball (Image 1), resting on the cart counter from Image 2
- Brand: business logo (Image 3), upper area inside safe zone
Render all text exactly as written, in Indonesian, no additional words. Keep all text and logo inside the central safe zone (avoid top and bottom 15% of the canvas).

CREATIVE DIRECTION: A warm, direct vertical composition built around the promise and the proof. The dominant feeling is the same honest confidence as the feed — this is the same warung, the same cart, the same bowl — but the story format pushes the deadline forward and gives the viewer one clear action. The softened gerobak biru fills the upper half as a quiet, familiar backdrop; the bowl sits grounded on the actual cart counter; the headline and offer are the things that must register in two seconds. Generous calm space in the upper right keeps the design from feeling crowded. The overall character is warm and local — the feeling of walking past a familiar cart and deciding today is the day.

DESIGN CHARACTER: The blue wooden cart in the background is Pak Darto's specific cart — not a generic backdrop, but the actual place where this bakso is sold. The bowl on the counter, the sign-painter headline, and the cart-blue together make this design look wrong for any other warung. The proof and the deadline share the frame without competing because the design gives each one room to breathe.

HERO VISUAL: Image 1 — the owner's real bowl of bakso urat with a tennis-ball-sized meatball, placed resting directly on the wooden counter surface of Image 2. Keep the product exactly as photographed: bowl shape, broth color, meatball size, urat texture unchanged. Soft side window light from the left, faint steam wisp above the broth, grounded contact shadow. Image 2 as setting: soften focus slightly behind the bowl; clean up any stray objects or other brands' signage; preserve the cart's blue paint and wood character.

LOGO / IDENTITY: Image 3 — business logo "Bakso Pak Darto." Place unaltered, upper area inside the safe zone. Keep unchanged: everything. Never redraw or recolor.

VISUAL SYSTEM (identical in every prompt of this set):
Type: heavy hand-painted sign-painter capitals for headline and offer; sturdy humanist sans for support text; no scripts. Style and material: real product photos on flat hand-painted blue wooden-cart surface, matte finish, soft natural window light with warm cast. Image treatment: real product photos kept exactly, grounded on surface with soft contact shadow, backgrounds cleaned or replaced only. Device: plain cream painted label shape behind the offer only. Space level: calm.

ATTACHED IMAGES (attach in this order):
Image 1 = owner's real photo of a bowl of bakso urat with a tennis-ball-sized meatball in clear beef broth. Role: hero. Treatment: keep exactly; place on the cart counter from Image 2. Keep unchanged: bowl, broth, meatballs, colors. May change: background.
Image 2 = owner's photo of the blue wooden bakso cart. Role: setting. Treatment: clean up stray objects and other brands' signs; soften focus behind the bowl; preserve cart blue and wood character. Keep unchanged: the cart's color and structure.
Image 3 = business logo "Bakso Pak Darto". Role: brand mark. Treatment: place unaltered, upper area inside safe zone. Keep unchanged: everything.
Priority if conflicts: Image 1 wins on food appearance; Image 2 is background only; Image 3 must never be redrawn or recolored.

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
- **Beda dari pesaing dengan sengaja:** pesaing ramai dan merah; ini lega dan biru dengan satu bintang.
- **Dua jangkar spesifik:** ukuran "segede bola tenis" dan gerobak biru asli Pak Darto.
- **Ruang lega karena konsep, bukan pengukuran:** ruang tenang di sekitar mangkuk adalah bagian dari karakter desain — keyakinan bahwa pesan ini cukup kuat berdiri sendiri.
- **Foto asli dipertahankan:** bakso tidak dikarang AI.
- **Satu keluarga, dua prompt mandiri:** sistem visual ditulis persis sama di kedua prompt, dan tidak ada prompt yang merujuk prompt lain.

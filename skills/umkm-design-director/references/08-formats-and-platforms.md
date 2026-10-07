# Formats, Platforms, and Viewing Context

Contents: why format comes first · quick-pick table · screen formats and safe zones · marketplace and delivery apps · physical and print · resolution and print readiness · density and text per medium · choosing aspect ratio · series and consistency

Platform sizes and interface layouts change. Treat the numbers below as sensible defaults and **ask the owner to check the platform's current requirements** when a platform enforces exact sizes (marketplace and delivery-app banners especially).

## 1. Why format comes first

The medium decides how long viewers look, how far away they are, how much text is acceptable, where platform buttons cover your design, and how exact the text must be. A good poster in the wrong format fails. Decide format *before* composition.

## 2. Quick-pick table

| Where it appears | Typical shape | Approx. pixels | Viewing time | Text budget | Text strategy |
|---|---|---|---|---|---|
| Instagram/Facebook feed post | Portrait 4:5 (best use of space) or square 1:1 | 1080x1350 / 1080x1080 | ~1-3 s while scrolling | 15-40 words | A or C |
| Instagram/Facebook Story, Reels cover, TikTok, WhatsApp Status | Vertical 9:16 | 1080x1920 | ~2-5 s per frame | 8-20 words | C |
| Marketplace/food-delivery banner (Shopee, Tokopedia, GoFood, GrabFood, ShopeeFood) | Wide banners vary (often ~16:9 or ~2:1, sometimes square product images) | Platform-specific | ~1-2 s | 6-12 words | B or C |
| Product photo on marketplace | Square 1:1 (commonly) | 1000x1000+ | ~1 s in a grid | Almost none (a badge at most) | B |
| Spanduk / banner depan toko | Wide (e.g. 3:1) | Vector or high-res in printer's software | ~2-3 s from distance | 3-7 words | B |
| X-banner / roll-up | Tall (~60x160 cm) | Printer spec | ~3-5 s | 8-15 words | B |
| Flyer/brosur A5/A4 | Portrait 148x210 / 210x297 mm | 300 dpi at final size | Held in hand; 5-20 s | 40-90 words grouped | B or C |
| Menu board / daftar menu | Portrait or wide | Printer spec | Reading to choose; 10-40 s | As needed, grouped | B |
| Label / stiker kemasan | Small; varies | 300 dpi at final size | Seconds | Name + 2-3 facts | B |
| WhatsApp broadcast image | 4:5 or 1:1 | 1080 wide | ~2 s | 10-30 words | C |
| Kartu nama | 90x55 mm | 300 dpi | Reference | Minimal | B |

## 3. Screen formats and safe zones

- **Feed posts:** Portrait 4:5 uses the most screen. Keep important content inside the central ~90% because feed grids and previews may crop edges to square or 3:4. Put the headline in the upper third; keep the CTA away from the extreme bottom.
- **Story/Reels/TikTok/WhatsApp Status (9:16):** The top and bottom portions are covered by interface elements (profile name, reply bar, captions, buttons). As a safe default keep essential text and the CTA inside roughly the middle 65-70% of the height: about 12-15% clear at the top and about 18-22% clear at the bottom. On TikTok the right edge also holds buttons: keep a margin on the right.
- **Mobile legibility:** test the design at about 360 px wide. If the smallest meaningful line is unreadable, enlarge or delete it.
- **Dark mode and brightness:** viewers use varied brightness; avoid designs that rely on subtle tonal differences.
- **Carousels:** each frame must work alone; frame 1 = hook, last frame = action. For a single AI prompt, create each frame as a separate prompt in a consistent style.

## 4. Marketplace and delivery apps

- Banners and product images are viewed as small thumbnails in grids, next to competitors: **simplicity and one clear promise** win. Large product, one offer, minimal text.
- Respect the platform's rules (restrictions on text coverage, watermarks, claims). Tell the owner to check the current guidelines of the platform.
- Use real product photos wherever the platform expects representation of the actual product.
- Keep important elements away from corners where badges or price overlays appear.

## 5. Physical and print

- **Distance sets size.** Rule of thumb: about 2.5 cm of letter height per 3 m of reading distance. A spanduk viewed from a road at motorbike speed needs far larger and fewer words than a flyer.
- **Light and context:** outdoor sun fades pale colors; use strong value contrast; matte vs glossy material changes glare.
- **Spanduk/banner:** one idea, one number, one contact. Reserve large clean text zones and add text in the printer's/Canva software (text strategy B), because text must be exact and big. Ask the printer for the final pixel/size requirements and file format.
- **Menus:** group into 3-6 categories, align prices in a right column, flag 1-3 best-sellers, leave margins for cropping or lamination.
- **Flyers:** one primary message at the top, offer in the middle, how to act at the bottom; leave margins.
- **Labels and stickers:** respect legal info zones (ingredients, net weight, halal, PIRT/BPOM) and keep the design secondary to the mandatory text.

## 6. Resolution and print readiness

- AI image outputs are typically a limited resolution (often around 1-2K px on the long side, some tools offer more). That is fine for screens; **large print needs upscaling or rebuilding** the text and graphic elements as vectors/high-res in a layout tool.
- For prints, aim for about 300 dpi at final size for flyers and labels; for large banners viewed from far, lower effective dpi is acceptable, but ask the printer.
- Printing may shift colors (RGB screen → CMYK ink). Avoid neon and very dark saturated colors in print; request a proof if color is critical.
- Add **bleed (about 3 mm)** and keep important content inside a safe margin (about 5-8 mm) for printed pieces.
- Tell the owner: for print, generate the *background/visual* with AI, then place exact text, logo, and legal marks in Canva or the printer's template.

## 7. Density, space, and text per medium

Calm space is part of the layout, not what is left over; budgets for each context are in `04-design-principles.md` section 2. The table below adds element and text limits.

| Medium | Max primary ideas | Max text elements | Calm space | Notes |
|---|---|---|---|---|
| Spanduk | 1 | 3 (name, offer, contact) | ~40-60% | Contact number huge and simple |
| Story/Status | 1 | 3-4 | ~35-45% | Big headline, one offer, one CTA |
| Feed promo | 1-2 | 4-6 | ~35-45% | Strong hero; price accent |
| Marketplace banner | 1 | 2-3 | ~40-50% | Product + promise |
| Flyer | 2-3 grouped | 6-10 | ~30-40% | Clear zones |
| Menu | n/a | grouped list | ~20-30%, strict grouping | Hierarchy via headings, alignment |

## 8. Choosing the aspect ratio

- Single post for scrolling → 4:5.
- Ephemeral and full-screen → 9:16.
- Thumbnail grids (marketplace, delivery) → follow the platform's spec; default 1:1.
- Roadside → wide; follow the printer's size.
- If the same message will run in multiple places, make one master and adapt: do not stretch; regenerate or recompose per ratio.

## 9. Series and consistency

For several outputs at once, follow `09-output-sets.md`: one shared Visual System, one standalone prompt per ratio.

If the owner will post repeatedly, define a small **system** that survives across posts: one palette with roles, two type characters, one layout skeleton (where headline, hero, price, CTA sit), one recurring graphic device (a stripe, a stamp, a border, a lettering style), and one photographic style. Recommend reusing the plan and prompt skeleton, changing only the content. Consistency builds recognition faster than variety.

#!/usr/bin/env python3
"""Generate the invented passport spread for the Republic of Valdoria.

Draws a 1024x1024 open passport spread with PIL only, deterministically.
Country: Republic of Valdoria (fictional). Capital: Aldermere.
Holder: Elena Maren Voss, born 14 JUN 1988, Aldermere.
Passport issued 12 MAR 2024, expires 12 MAR 2034.
All stamps are dated after the issue date and tell one coherent trip:
Aldermere -> Dravnia (03-17 Apr 2024) -> Selmere (02-21 May 2024) -> home.
"""
import math
import os
import random

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "entry.png")

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


INK = (38, 32, 26)
FAINT = (120, 110, 92)
GOLD = (150, 112, 40)
PAPER = (243, 236, 216)
PAPER2 = (238, 229, 205)


def draw_emblem(d, cx, cy, r, gold=GOLD, ink=INK):
    """Coat of arms: gold ring, three mountain peaks, a star, wheat ears."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=gold, width=3)
    d.ellipse([cx - r + 6, cy - r + 6, cx + r - 6, cy + r - 6], outline=gold, width=1)
    # mountains
    d.polygon([(cx - r + 10, cy + r - 12), (cx - 6, cy - 4), (cx + 2, cy + r - 12)],
              outline=ink, width=2)
    d.polygon([(cx - 2, cy + r - 12), (cx + 12, cy - 12), (cx + r - 10, cy + r - 12)],
              outline=ink, width=2)
    # star above peaks
    sx, sy, sr = cx, cy - r + 16, 7
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = sr if i % 2 == 0 else sr * 0.45
        pts.append((sx + rr * math.cos(a), sy + rr * math.sin(a)))
    d.polygon(pts, fill=gold)
    # base line + motto dots
    d.line([(cx - r + 12, cy + r - 12), (cx + r - 12, cy + r - 12)], fill=ink, width=2)


def draw_portrait(size=170):
    """Stylised passport photo: woman, dark bob hair, teal jacket."""
    img = Image.new("RGB", (size, size * 5 // 4), (168, 186, 196))
    d = ImageDraw.Draw(img)
    w, h = img.size
    # backdrop gradient bands
    for y in range(h):
        t = y / h
        c = tuple(int(168 + (148 - 168) * t) for _ in range(3))
        d.line([(0, y), (w, y)], fill=(c[0], 172, 190))
    # shoulders / jacket
    d.polygon([(w * 0.12, h), (w * 0.30, h * 0.74), (w * 0.70, h * 0.74),
               (w * 0.88, h)], fill=(38, 74, 84))
    d.polygon([(w * 0.38, h * 0.76), (w * 0.50, h * 0.98), (w * 0.62, h * 0.76)],
              fill=(240, 238, 230))  # shirt V
    # neck
    d.rectangle([w * 0.44, h * 0.62, w * 0.56, h * 0.78], fill=(214, 172, 138))
    # face
    d.ellipse([w * 0.30, h * 0.10, w * 0.70, h * 0.66], fill=(226, 186, 152))
    # ears
    d.ellipse([w * 0.27, h * 0.32, w * 0.32, h * 0.46], fill=(226, 186, 152))
    d.ellipse([w * 0.68, h * 0.32, w * 0.73, h * 0.46], fill=(226, 186, 152))
    # hair: dark bob framing the face
    d.pieslice([w * 0.24, h * 0.02, w * 0.76, h * 0.60], 180, 360, fill=(52, 38, 30))
    d.polygon([(w * 0.24, h * 0.30), (w * 0.30, h * 0.30), (w * 0.28, h * 0.62),
               (w * 0.22, h * 0.60)], fill=(52, 38, 30))
    d.polygon([(w * 0.76, h * 0.30), (w * 0.70, h * 0.30), (w * 0.72, h * 0.62),
               (w * 0.78, h * 0.60)], fill=(52, 38, 30))
    d.arc([w * 0.30, h * 0.06, w * 0.70, h * 0.40], 200, 340, fill=(52, 38, 30), width=6)
    # brows, eyes, nose, lips
    for ex in (0.39, 0.61):
        d.line([(w * (ex - 0.05), h * 0.36), (w * (ex + 0.05), h * 0.355)],
               fill=(52, 38, 30), width=3)
        d.ellipse([w * (ex - 0.032), h * 0.385, w * (ex + 0.032), h * 0.415],
                  fill=(255, 255, 255))
        d.ellipse([w * (ex - 0.014), h * 0.392, w * (ex + 0.014), h * 0.408],
                  fill=(46, 34, 26))
    d.line([(w * 0.50, h * 0.42), (w * 0.495, h * 0.50)], fill=(198, 152, 120), width=2)
    d.line([(w * 0.46, h * 0.55), (w * 0.54, h * 0.55)], fill=(158, 74, 66), width=3)
    d.arc([w * 0.455, h * 0.53, w * 0.545, h * 0.585], 0, 180, fill=(158, 74, 66), width=2)
    # soft cheek shading
    d.ellipse([w * 0.33, h * 0.47, w * 0.40, h * 0.52], fill=(228, 168, 138))
    d.ellipse([w * 0.60, h * 0.47, w * 0.67, h * 0.52], fill=(228, 168, 138))
    return img


def guilloche(d, x0, y0, x1, y1, color, step=14):
    """Faint wavy security lines across a page."""
    for k in range(0, (y1 - y0) // step):
        y = y0 + k * step
        pts = []
        for x in range(x0, x1 + 1, 8):
            pts.append((x, y + 3 * math.sin((x - x0) / 46.0 + k * 0.7)))
        d.line(pts, fill=color, width=1)


def stamp(d, cx, cy, w, h, angle, color, lines, fnt, sub=None):
    """A rotated rubber stamp: rounded border + centred lines."""
    layer = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    sd = ImageDraw.Draw(layer)
    sd.rounded_rectangle([6, 6, w + 34, h + 34], radius=10,
                         outline=color + (255,), width=3)
    sd.rounded_rectangle([11, 11, w + 29, h + 29], radius=8,
                         outline=color + (255,), width=1)
    y = 14
    for i, ln in enumerate(lines):
        f = fnt
        tw = sd.textlength(ln, font=f)
        sd.text(((w + 40 - tw) / 2, y), ln, font=f, fill=color + (255,))
        y += 17
    if sub:
        tw = sd.textlength(sub, font=fnt)
        sd.text(((w + 40 - tw) / 2, y + 2), sub, font=fnt, fill=color + (255,))
    layer = layer.rotate(angle, resample=Image.BICUBIC, expand=True)
    return layer, (cx - layer.width // 2, cy - layer.height // 2)


def main():
    rnd = random.Random(20261121)
    img = Image.new("RGB", (W, H), (74, 60, 46))
    d = ImageDraw.Draw(img, "RGBA")
    # table shading
    for y in range(H):
        d.line([(0, y), (W, y)], fill=(74 - y // 90, 60 - y // 110, 46 - y // 130))
    # pages
    L = (46, 58, 978, 966)   # left page box
    R = (524, 58, 978, 966)  # right page box
    # shadows
    for box in (L, R):
        d.rectangle([box[0] + 6, box[1] + 8, box[2] + 6, box[3] + 8], fill=(0, 0, 0, 90))
    d.rectangle(L, fill=PAPER)
    d.rectangle(R, fill=PAPER2)
    # centre gutter shadow
    for i in range(14):
        d.line([(510 - i, 58), (510 - i, 966)], fill=(0, 0, 0, 26 - i))
        d.line([(524 + i, 58), (524 + i, 966)], fill=(0, 0, 0, 26 - i))
    # gold double borders
    for box in (L, R):
        d.rectangle([box[0] + 10, box[1] + 10, box[2] - 10, box[3] - 10],
                    outline=GOLD, width=2)
        d.rectangle([box[0] + 16, box[1] + 16, box[2] - 16, box[3] - 16],
                    outline=GOLD, width=1)
    # faint guilloche on both pages
    guilloche(d, 70, 90, 490, 940, (208, 196, 166))
    guilloche(d, 548, 90, 954, 940, (208, 196, 166))

    # ---------------- LEFT PAGE: data page ----------------
    draw_emblem(d, 278, 118, 34)
    d.text((278, 158), "REPUBLIC OF VALDORIA", font=font(SERIF_B, 26),
           fill=INK, anchor="ma")
    d.text((278, 190), "PASSEPORT  •  PASSPORT",
           font=font(SANS, 13), fill=FAINT, anchor="ma")
    d.line([(90, 214), (466, 214)], fill=GOLD, width=2)

    # portrait
    photo = draw_portrait(150)
    img.paste(photo, (78, 232))
    d.rectangle([78, 232, 228, 232 + 187], outline=INK, width=2)
    # hologram circle overlapping photo corner
    d.ellipse([186, 376, 226, 416], outline=(120, 160, 190, 200), width=2)
    d.text((206, 392), "V", font=font(SERIF_B, 16), fill=(120, 160, 190, 220),
           anchor="mm")
    # round issue stamp overlapping photo
    d.ellipse([76, 351, 144, 419], outline=(150, 40, 40, 210), width=3)
    d.ellipse([84, 359, 136, 411], outline=(150, 40, 40, 210), width=1)
    d.text((110, 369), "ALDERMERE", font=font(SANS_B, 8), fill=(150, 40, 40, 220),
           anchor="ma")
    d.text((110, 385), "12 MAR 2024", font=font(SANS_B, 8), fill=(150, 40, 40, 220),
           anchor="ma")
    d.text((110, 401), "ISSUED", font=font(SANS_B, 8), fill=(150, 40, 40, 220),
           anchor="ma")

    # data fields
    fx, fy = 248, 232
    fields = [
        ("Surname / Nom", "VOSS"),
        ("Given names / Prénoms", "ELENA MAREN"),
        ("Nationality / Nationalité", "VALDORIAN"),
        ("Date of birth", "14 JUN 1988"),
        ("Place of birth", "ALDERMERE, VALDORIA"),
        ("Sex / Sexe", "F"),
        ("Passport No.", "VD 482 917"),
        ("Date of issue", "12 MAR 2024"),
        ("Date of expiry", "12 MAR 2034"),
        ("Authority", "MINISTRY OF THE INTERIOR"),
    ]
    y = fy
    for label, value in fields:
        d.text((fx, y), label, font=font(SANS, 11), fill=FAINT)
        d.text((fx, y + 12), value, font=font(SANS_B, 14), fill=INK)
        y += 32
    # signature
    d.text((78, 448), "Holder's signature", font=font(SANS, 11), fill=FAINT)
    d.text((78, 462), "Elena M. Voss", font=font(SERIF_I, 24), fill=(40, 40, 90))
    d.line([(78, 494), (240, 494)], fill=INK, width=1)
    # note box: telling detail on the data page
    d.rectangle([258, 560, 466, 640], outline=INK, width=1)
    d.text((268, 568), "ENDORSEMENT", font=font(SANS_B, 11), fill=INK)
    d.text((268, 584), "Holder is exempt from the\nmountain toll on the High\nPass of Aldermere.",
           font=font(SANS, 12), fill=INK)
    d.text((78, 560), "This passport is the property of\nthe Republic of Valdoria.\nIf found, return to the nearest\nValdorian consulate.",
           font=font(SANS, 12), fill=FAINT)
    # MRZ
    d.rectangle([66, 872, 490, 946], fill=(226, 218, 192))
    d.text((78, 884), "P<VALVOSS<<ELENA<MAREN<<<<<<<<<<<<<<<<<<<<",
           font=font(MONO, 15), fill=INK)
    d.text((78, 908), "VD482917<8VAL8806145F3403127<<<<<<<<<<<<<<04",
           font=font(MONO, 15), fill=INK)
    d.text((78, 848), "MACHINE READABLE ZONE", font=font(SANS, 10), fill=FAINT)

    # ---------------- RIGHT PAGE: visas & stamps ----------------
    d.text((751, 84), "VISAS", font=font(SERIF_B, 24), fill=INK, anchor="ma")
    d.text((940, 88), "p. 12", font=font(SANS, 12), fill=FAINT, anchor="ra")
    d.line([(568, 116), (934, 116)], fill=GOLD, width=2)

    # visa sticker
    d.rectangle([568, 132, 934, 268], fill=(214, 228, 200), outline=(90, 120, 70), width=2)
    d.rectangle([576, 140, 926, 260], outline=(90, 120, 70), width=1)
    d.text((751, 148), "GRAND DUCHY OF KESTREL  —  VISA", font=font(SANS_B, 14),
           fill=(60, 90, 50), anchor="ma")
    d.text((588, 172), "Type:  C  •  Single entry  •  Stay: up to 90 days",
           font=font(SANS, 13), fill=(50, 70, 45))
    d.text((588, 192), "Issued at the Kestrellian Consulate, Aldermere",
           font=font(SANS, 13), fill=(50, 70, 45))
    d.text((588, 212), "28 MAR 2024  —  Valid until 26 JUN 2024",
           font=font(SANS, 13), fill=(50, 70, 45))
    d.text((588, 232), "Fee: 40 crowns — PAID   •   No. K-77104",
           font=font(SANS_B, 13), fill=(50, 70, 45))
    # fee-paid stamp on the visa
    lay, pos = stamp(d, 905, 266, 76, 30, -12, (150, 40, 40),
                     ["FEE PAID"], font(SANS_B, 13))
    img.paste(lay, pos, lay)

    # arrival / departure stamps
    f_stamp = font(SANS_B, 12)
    stamps = [
        (650, 330, 200, 66, -8, (30, 70, 150),
         ["KINGDOM OF DRAVNIA", "PORT OF CALLUM — ENTRY", "03 APR 2024"]),
        (868, 362, 190, 66, 7, (150, 40, 40),
         ["KINGDOM OF DRAVNIA", "PORT OF CALLUM — EXIT", "17 APR 2024"]),
        (650, 472, 200, 66, 6, (40, 110, 60),
         ["REPUBLIC OF SELMERE", "OSTARA — ENTRY", "02 MAY 2024"]),
        (872, 496, 190, 66, -6, (90, 50, 140),
         ["REPUBLIC OF SELMERE", "OSTARA — EXIT", "21 MAY 2024"]),
        (660, 620, 210, 66, -4, (40, 40, 40),
         ["REPUBLIC OF VALDORIA", "ALDERMERE — ARRIVAL", "22 MAY 2024"]),
    ]
    for cx, cy, w, h, ang, col, lines in stamps:
        lay, pos = stamp(d, cx, cy, w, h, ang, col, lines, f_stamp)
        img.paste(lay, pos, lay)

    # small Kestrel visa entry stamp beside the sticker
    lay, pos = stamp(d, 862, 620, 150, 50, 10, (30, 70, 150),
                     ["KESTREL", "VISITED 30 MAR 2024"], font(SANS_B, 11))
    img.paste(lay, pos, lay)

    # condition of entry — the telling detail
    d.rectangle([568, 700, 934, 830], outline=INK, width=1)
    d.text((580, 710), "CONDITION OF ENTRY — GRAND DUCHY OF KESTREL",
           font=font(SANS_B, 12), fill=INK)
    d.text((580, 732),
           "This visa is valid for travel by the\n"
           "Northern Ferry only. No overland\n"
           "crossing at the Grey Marches.\n"
           "Luggage is searched at Callum Quay.\n"
           "Overstay fine: 5 crowns per day.",
           font=font(SANS, 13), fill=INK)
    # mountain toll exempt stamp
    lay, pos = stamp(d, 840, 885, 190, 44, -9, (40, 110, 60),
                     ["MOUNTAIN TOLL", "EXEMPT"], font(SANS_B, 12))
    img.paste(lay, pos, lay)
    d.text((580, 856), "High Pass toll office",
           font=font(SANS, 11), fill=FAINT)
    d.text((580, 872), "Stamped 12 MAR 2024", font=font(SANS, 11), fill=FAINT)

    # faint watermark emblem on right page
    wm = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wm)
    wd.ellipse([700, 330, 800, 430], outline=(150, 112, 40, 60), width=4)
    wd.text((750, 372), "V", font=font(SERIF_B, 60), fill=(150, 112, 40, 60),
            anchor="mm")
    img.paste(Image.alpha_composite(img.convert("RGBA"), wm).convert("RGB"), (0, 0))

    # outer cover hint at the very edges
    d.rectangle([0, 0, W - 1, H - 1], outline=(30, 24, 18), width=4)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()

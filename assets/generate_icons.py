"""Generator icons PWA pentru DASHBOARD.html.
Produce icon-192.png, icon-512.png, icon-maskable-512.png.
Design: cruce medicala alba pe fond albastru (#1e40af) = culoare theme dashboard.
Se ruleaza o singura data; iconurile raman in assets/ si intra in git.
"""
from PIL import Image, ImageDraw
from pathlib import Path

OUT_DIR = Path(__file__).parent
BG_COLOR = (30, 64, 175)  # #1e40af - primary
FG_COLOR = (255, 255, 255)


def make_icon(size: int, maskable: bool = False) -> Image.Image:
    img = Image.new("RGBA", (size, size), BG_COLOR + (255,))
    draw = ImageDraw.Draw(img)

    # Maskable icons need safe zone (80% centered); regular use full canvas
    safe = 0.80 if maskable else 1.0
    canvas = int(size * safe)
    offset = (size - canvas) // 2

    # Rounded rectangle background (only for non-maskable, for nice standalone look)
    if not maskable:
        radius = int(size * 0.22)
        bg = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        bd = ImageDraw.Draw(bg)
        bd.rounded_rectangle([(0, 0), (size - 1, size - 1)], radius=radius, fill=BG_COLOR + (255,))
        img = bg
        draw = ImageDraw.Draw(img)

    # Medical cross: two overlapping rectangles
    cross_thickness = int(canvas * 0.22)
    cross_length = int(canvas * 0.62)
    cx = size // 2
    cy = size // 2

    # Vertical bar
    draw.rounded_rectangle(
        [
            (cx - cross_thickness // 2, cy - cross_length // 2),
            (cx + cross_thickness // 2, cy + cross_length // 2),
        ],
        radius=int(cross_thickness * 0.18),
        fill=FG_COLOR,
    )
    # Horizontal bar
    draw.rounded_rectangle(
        [
            (cx - cross_length // 2, cy - cross_thickness // 2),
            (cx + cross_length // 2, cy + cross_thickness // 2),
        ],
        radius=int(cross_thickness * 0.18),
        fill=FG_COLOR,
    )

    return img


def main() -> None:
    sizes = [
        ("icon-192.png", 192, False),
        ("icon-512.png", 512, False),
        ("icon-maskable-512.png", 512, True),
    ]
    for name, size, maskable in sizes:
        icon = make_icon(size, maskable=maskable)
        icon.save(OUT_DIR / name, "PNG")
        print(f"wrote {name} ({size}x{size}, maskable={maskable})")


if __name__ == "__main__":
    main()

"""
Generate pwa-icon.png:
  - 512x512 dark navy background (#0a1628)
  - Rounded corners (radius 96px, like iOS squircle)
  - logo-blue.png centered with ~18% padding on each side
"""

from PIL import Image, ImageDraw
import os

SIZE = 512
BG_COLOR = (10, 22, 40, 255)    # #0a1628  — the dark mode container colour from the app
CORNER_R = 96                    # rounded-corner radius for the icon shape
PADDING  = 88                    # pixels of padding around the logo (≈17% each side)

script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path  = os.path.join(script_dir, "logo-blue.png")
out_path   = os.path.join(script_dir, "pwa-icon.png")

# ── 1. Create dark background with rounded corners ─────────────────────────
bg = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
draw = ImageDraw.Draw(bg)
draw.rounded_rectangle([0, 0, SIZE - 1, SIZE - 1], radius=CORNER_R, fill=BG_COLOR)

# ── 2. Load and resize logo ─────────────────────────────────────────────────
logo = Image.open(logo_path).convert("RGBA")
logo_size = SIZE - (PADDING * 2)                # inner area
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# ── 3. Paste logo centered on background ───────────────────────────────────
bg.paste(logo, (PADDING, PADDING), logo)        # use logo alpha as mask

# ── 4. Save final icon ──────────────────────────────────────────────────────
bg.save(out_path, "PNG")
print(f"Saved: {out_path}  ({SIZE}x{SIZE})")

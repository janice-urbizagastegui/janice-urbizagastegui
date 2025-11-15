import os
from pathlib import Path

try:
    from PIL import Image
except Exception as e:
    raise SystemExit("Pillow no está instalado. Ejecuta: python -m pip install pillow")

IMG_DIR = Path(__file__).resolve().parent.parent / "images"

def convert(path: Path):
    out = path.with_suffix('.webp')
    if out.exists():
        return
    img = Image.open(path)
    if img.mode in ("RGBA", "LA"):
        img.save(out, format="WEBP", quality=85, method=6)
    else:
        img = img.convert("RGB")
        img.save(out, format="WEBP", quality=85, method=6)

def main():
    exts = {".png", ".jpg", ".jpeg"}
    for entry in IMG_DIR.iterdir():
        if entry.is_file() and entry.suffix.lower() in exts:
            convert(entry)

if __name__ == "__main__":
    main()

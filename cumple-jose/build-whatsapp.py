#!/usr/bin/env python3
"""Genera un HTML autocontenido con la foto de José embebida (WhatsApp)."""

from __future__ import annotations

import base64
import mimetypes
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "index.html"
PHOTO_CANDIDATES = (
    ROOT / "assets" / "jose.jpg",
    ROOT / "assets" / "jose.jpeg",
    ROOT / "assets" / "jose.png",
    ROOT / "assets" / "jose.webp",
)
OUTPUT = ROOT / "feliz-cumple-jose.html"


def find_photo() -> Path:
    for path in PHOTO_CANDIDATES:
        if path.is_file() and path.stat().st_size > 0:
            return path
    raise SystemExit(
        "No encontré la foto. Colócala en:\n"
        "  cumple-jose/assets/jose.jpg\n"
    )


def to_data_uri(photo: Path) -> str:
    mime, _ = mimetypes.guess_type(photo.name)
    if not mime:
        mime = "image/jpeg"
    encoded = base64.b64encode(photo.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def build() -> Path:
    photo = find_photo()
    html = SOURCE.read_text(encoding="utf-8")
    data_uri = to_data_uri(photo)

    html, count = re.subn(
        r'(id="josePhoto"\s+src=")assets/jose\.(?:jpg|jpeg|png|webp)(")',
        rf"\1{data_uri}\2",
        html,
        count=1,
        flags=re.IGNORECASE,
    )
    if count != 1:
        raise SystemExit('No pude localizar el <img id="josePhoto"> en index.html')

    html = html.replace(
        "<small>agrega assets/jose.jpg</small>",
        "<small>José</small>",
    )
    html = re.sub(
        r"\s*<!-- Fuente: assets/jose.jpg.*?-->\s*",
        "\n          ",
        html,
        count=1,
    )

    OUTPUT.write_text(html, encoding="utf-8")
    size_mb = OUTPUT.stat().st_size / (1024 * 1024)
    print(f"Listo: {OUTPUT}")
    print(f"Foto:  {photo.name} ({photo.stat().st_size / 1024:.0f} KB)")
    print(f"Peso:  {size_mb:.2f} MB")
    print("Envía ese archivo por WhatsApp (un solo HTML, sin enlaces).")
    return OUTPUT


if __name__ == "__main__":
    try:
        build()
    except BrokenPipeError:
        sys.exit(0)

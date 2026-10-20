import os
from pypdf import PdfReader

reader = PdfReader('de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2024-2025-so-gddt-lang-son.pdf')
page = reader.pages[0]
for count, image_file_object in enumerate(page.images):
    with open(f"latex/de_49_scan.png", "wb") as fp:
        fp.write(image_file_object.data)
    print("Saved latex/de_49_scan.png")

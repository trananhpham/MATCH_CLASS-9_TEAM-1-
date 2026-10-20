import os, sys
sys.stdout.reconfigure(encoding='utf-8')
from pypdf import PdfReader

scanned_files = [
    (4, "de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2024-2025-so-gddt-lang-son.pdf"),
    (6, "de-cuoi-hoc-ky-1-toan-9-thcs-nam-2024-2025-so-gddt-lang-son.pdf"),
    (7, "de-giua-hoc-ki-1-toan-9-nam-2023-2024-phong-gddt-bac-son-lang-son.pdf"),
    (8, "de-giua-hoc-ki-2-toan-9-nam-2022-2023-phong-gddt-bac-son-lang-son.pdf"),
    (10, "de-giua-ky-1-toan-9-nam-2022-2023-phong-gddt-huu-lung-lang-son.pdf"),
    (11, "de-hoc-sinh-gioi-cap-tinh-toan-9-nam-2022-2023-so-gddt-lang-son.pdf"),
    (12, "de-hoc-sinh-gioi-toan-9-nam-2021-2022-phong-gddt-chi-lang-lang-son.pdf"),
    (15, "de-kiem-tra-cuoi-hoc-ki-1-toan-9-nam-2022-2023-so-gddt-lang-son.pdf"),
    (16, "de-kiem-tra-cuoi-hoc-ki-1-toan-9-nam-2023-2024-so-gddt-lang-son.pdf"),
    (17, "de-kiem-tra-cuoi-hoc-ki-2-toan-9-nam-2021-2022-so-gddt-lang-son.pdf"),
    (18, "de-kiem-tra-cuoi-hoc-ki-2-toan-9-nam-2023-2024-so-gddt-lang-son.pdf"),
    (21, "de-thi-thu-tuyen-sinh-lop-10-mon-toan-lan-1-nam-2026-so-gddt-lang-son.pdf"),
    (25, "de-thi-thu-tuyen-sinh-vao-lop-10-mon-toan-nam-2022-so-gddt-lang-son.pdf"),
    (26, "de-thi-thu-vao-lop-10-mon-toan-nam-2020-2021-phong-gddt-loc-binh-lang-son.pdf"),
    (49, "de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2024-2025-so-gddt-lang-son.pdf")
]

os.makedirs("latex/scans", exist_ok=True)

for de_num, fname in scanned_files:
    try:
        reader = PdfReader(fname)
        total_imgs = 0
        for p_idx, page in enumerate(reader.pages):
            for img_idx, img_obj in enumerate(page.images):
                img_name = f"latex/scans/de_{de_num}_p{p_idx}_img{img_idx}.png"
                with open(img_name, "wb") as f:
                    f.write(img_obj.data)
                total_imgs += 1
        print(f"Đề {de_num:2d} ({fname}): {len(reader.pages)} trang, trích xuất {total_imgs} ảnh.")
    except Exception as e:
        print(f"Đề {de_num:2d} ({fname}): Lỗi {e}")

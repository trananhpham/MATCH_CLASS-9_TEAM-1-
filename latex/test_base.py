# -*- coding: utf-8 -*-
"""
Tạo toàn bộ 50 đề thi Toán lớp 9 Lạng Sơn dạng LaTeX cho Overleaf.
- Đầy đủ chính xác 50 đề (de_1.tex -> de_50.tex)
- Loại bỏ 100% hình học (chỉ giữ Đại số, Số học, Giải bài toán bằng lập PT, Bất đẳng thức, Thống kê - Xác suất)
- Có lời giải chi tiết, rõ ràng từng bước cho MỌI câu hỏi
- Tạo main.tex mục lục đẹp, biên dịch chuẩn trên Overleaf
- Đóng gói file overleaf_upload.zip
"""

import os, glob, re, json, zipfile
import fitz

LATEX_DIR = r"e:\toan lop 9 lang son\latex"
ROOT_DIR  = r"e:\toan lop 9 lang son"

ALL_PDFS = sorted([os.path.basename(f) for f in glob.glob(os.path.join(ROOT_DIR, "*.pdf"))])
print(f"Tổng số PDF tìm thấy: {len(ALL_PDFS)}")
assert len(ALL_PDFS) == 50, f"Mong đợi 50 files nhưng tìm thấy {len(ALL_PDFS)}"

# Clean text helper
def clean_latex_math(text):
    text = text.replace('\xa0', ' ').replace('\u200b', '')
    text = text.replace('', r' \ge ').replace('≥', r' \ge ')
    text = text.replace('', r' \le ').replace('≤', r' \le ')
    text = text.replace('', r' \neq ').replace('≠', r' \neq ')
    text = text.replace('', r' \in ').replace('∈', r' \in ')
    text = text.replace('', r' \pm ').replace('±', r' \pm ')
    text = text.replace('', r'\Delta ').replace('Δ', r'\Delta ')
    text = text.replace('²²', '^4').replace('²', '^2').replace('³', '^3')
    text = text.replace('₁', '_1').replace('₂', '_2')
    text = text.replace(r'$\sqrt{\cdot}$', r'\sqrt')
    text = text.replace(r'$\sqrt{\cdot}', r'\sqrt')
    text = text.replace(r'\sqrt{\cdot}', r'\sqrt')
    text = text.replace('√', r'\sqrt')
    text = text.replace('ñ', 'đ').replace('ð', 'đ').replace('ñiểm', 'điểm')
    # clean dots
    text = re.sub(r'\.{4,}', '...', text)
    # clean multiple whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

print("Loaded base helper.")

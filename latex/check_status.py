import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"h:\toan lop 9 lang son"
LATEX_DIR = r"h:\toan lop 9 lang son\latex"

tex_files = [f for f in os.listdir(LATEX_DIR) if re.match(r'de_\d+\.tex', f)]
tex_files.sort(key=lambda x: int(re.search(r'\d+', x).group()))

print(f"Tổng số file LaTeX: {len(tex_files)}")

# Kiểm tra từng file
report = []
for f in tex_files:
    idx = int(re.search(r'\d+', f).group())
    path = os.path.join(LATEX_DIR, f)
    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    # Lấy tên file gốc
    m_orig = re.search(r'%%\s*Đề\s*\d+\s*--\s*([^\n\r]+)', content)
    orig_name = m_orig.group(1).strip() if m_orig else "Unknown"
    
    # Số câu hỏi
    de_blocks = re.findall(r'\\begin\{de_cau\}\{([^\}]+)\}\{([^\}]*)\}(.*?)\\end\{de_cau\}', content, re.DOTALL)
    gi_blocks = re.findall(r'\\begin\{loi_giai_cau\}(.*?)\\end\{loi_giai_cau\}', content, re.DOTALL)
    
    # Kiểm tra lời giải sơ sài hay chi tiết
    gi_lens = [len(g.strip()) for g in gi_blocks]
    min_gi = min(gi_lens) if gi_lens else 0
    avg_gi = sum(gi_lens)/len(gi_lens) if gi_lens else 0
    
    # Kiểm tra lỗi cú pháp phổ biến (ví dụ \sqrta, \sqrtx)
    syntax_errs = []
    if re.search(r'\\sqrt[a-zA-Z]', content):
        syntax_errs.append("lỗi \\sqrt dính chữ (vd: \\sqrta, \\sqrtx)")
    if "Đang cập nhật" in content:
        syntax_errs.append("chưa có lời giải (Đang cập nhật)")
    if any("Phương pháp thế" in g or "Lập bảng ước" in g and len(g.strip()) < 150 for g in gi_blocks):
        syntax_errs.append("lời giải tóm tắt/gợi ý ngắn")
        
    # Phân loại độ chi tiết
    if avg_gi < 200 or min_gi < 80:
        quality = "Sơ sài (chỉ có tóm tắt/đáp số)"
    elif avg_gi < 450:
        quality = "Trung bình (ngắn gọn, thiếu một số bước)"
    else:
        quality = "Chi tiết (đầy đủ các bước giải)"
        
    report.append({
        "de": idx,
        "file": f,
        "orig": orig_name,
        "num_de": len(de_blocks),
        "num_gi": len(gi_blocks),
        "min_gi": min_gi,
        "avg_gi": avg_gi,
        "quality": quality,
        "errors": syntax_errs
    })

so_sai = [r for r in report if "Sơ sài" in r["quality"]]
trung_binh = [r for r in report if "Trung bình" in r["quality"]]
chi_tiet = [r for r in report if "Chi tiết" in r["quality"]]

print(f"\n--- PHÂN LOẠI CHẤT LƯỢNG LỜI GIẢI ({len(report)} đề) ---")
print(f"- Số đề có lời giải sơ sài / tóm tắt / ngắn: {len(so_sai)}")
print(f"- Số đề có lời giải trung bình: {len(trung_binh)}")
print(f"- Số đề có lời giải chi tiết: {len(chi_tiet)}")

print("\n--- CHI TIẾT CÁC ĐỀ CÓ LỜI GIẢI SƠ SÀI ---")
for r in so_sai:
    err_str = f" | Ghi chú: {', '.join(r['errors'])}" if r['errors'] else ""
    print(f"Đề {r['de']:2d} ({r['file']}): {r['num_de']} câu, TB độ dài giải: {r['avg_gi']:.0f} ký tự, ngắn nhất: {r['min_gi']} ký tự{err_str}")

# Kiểm tra cấu trúc: Lời giải đặt ngay sau câu hay để ở cuối đề?
print("\n--- CẤU TRÚC BỐ CỤC HIỆN TẠI TRONG CÁC FILE .TEX ---")
print("Hiện tại: Tất cả các file de_X.tex đều đang đặt theo dạng XEN KẼ:")
print("  Câu 1 -> Lời giải Câu 1 -> Câu 2 -> Lời giải Câu 2...")
print("Chưa có phần tách riêng 'PHẦN ĐỀ BÀI' ở trước và 'PHẦN LỜI GIẢI CHI TIẾT' ở CUỐI ĐỀ.")

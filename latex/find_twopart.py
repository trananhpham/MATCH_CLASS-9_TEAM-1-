import re, glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r'h:\toan lop 9 lang son'
all_pdfs = sorted([os.path.basename(f) for f in glob.glob(os.path.join(ROOT_DIR, '*.pdf'))])

with open('latex/build_all_50_exams.py', 'r', encoding='utf-8') as f:
    code_build = f.read()

with open('latex/generate_full_50.py', 'r', encoding='utf-8') as f:
    code_gen50 = f.read()

with open('latex/gen_latex.py', 'r', encoding='utf-8') as f:
    code_genlatex = f.read()

curated_in_build = set(re.findall(r'CURATED\["([^"]+)"\]', code_build))
curated_in_gen50 = set(re.findall(r'MANUAL_EXAMS\["([^"]+)"\]', code_gen50))
curated_in_genlatex = set(re.findall(r'"([a-zA-Z0-9\-_]+\.pdf)":\s*\{', code_genlatex))

all_curated = curated_in_build | curated_in_gen50 | curated_in_genlatex

twopart_list = []
curated_list = []
for i, f in enumerate(all_pdfs, 1):
    if f not in all_curated:
        twopart_list.append((i, f))
    else:
        curated_list.append((i, f))

print(f"Tổng số đề trong Curated: {len(curated_list)}")
print(f"Tổng số đề 2-Part (chưa có lời giải chuẩn): {len(twopart_list)}")
print("\nDanh sách các đề 2-Part:")
for idx, f in twopart_list:
    print(f"  Đề {idx:2d}: {f}")

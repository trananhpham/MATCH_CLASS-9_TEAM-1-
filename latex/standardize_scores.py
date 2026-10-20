import os, re, glob, sys

sys.stdout.reconfigure(encoding='utf-8')
latex_dir = r'h:/toan lop 9 lang son/latex'

# 1. Fix missing 'điểm' in \begin{de_cau}{...}{...}
# e.g. \begin{de_cau}{Câu 1}{2,0} -> \begin{de_cau}{Câu 1}{2,0 điểm}
# or \begin{de_cau}{Câu 1}{4,0} -> \begin{de_cau}{Câu 1}{4,0 điểm}

def add_diem_to_score(content):
    def repl(m):
        cau = m.group(1)
        score = m.group(2).strip()
        if score and 'điểm' not in score.lower() and 'đ' not in score.lower():
            return f'\\begin{{de_cau}}{{{cau}}}{{{score} điểm}}'
        return m.group(0)
    
    return re.sub(r'\\begin\{de_cau\}\{([^}]+)\}\{([^}]+)\}', repl, content)

fixed_files = []
for i in range(1, 51):
    fpath = os.path.join(latex_dir, f'de_{i}.tex')
    if not os.path.exists(fpath): continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        orig = f.read()
    
    updated = add_diem_to_score(orig)
    if updated != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        fixed_files.append(f'de_{i}.tex')

print(f'Standardized score format in {len(fixed_files)} files: {fixed_files}')

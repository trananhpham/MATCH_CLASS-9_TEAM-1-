import os, re, glob, sys

sys.stdout.reconfigure(encoding='utf-8')
latex_dir = r'h:/toan lop 9 lang son/latex'

# ── 1. Fix bao_cao_tong_the.tex ──────────────────────────────────────────────
bctt_path = os.path.join(latex_dir, 'bao_cao_tong_the.tex')
if os.path.exists(bctt_path):
    with open(bctt_path, 'r', encoding='utf-8') as f:
        bctt = f.read()
    # Replace unescaped & in table cells
    bctt_fixed = bctt.replace('Hàm số & Vi-ét', r'Hàm số \& Vi-ét')
    # Also replace box drawing characters
    bctt_fixed = bctt_fixed.replace('═', '=')
    with open(bctt_path, 'w', encoding='utf-8') as f:
        f.write(bctt_fixed)
    print("Fixed bao_cao_tong_the.tex")

# Also update build_report.py
br_path = os.path.join(latex_dir, 'build_report.py')
if os.path.exists(br_path):
    with open(br_path, 'r', encoding='utf-8') as f:
        br = f.read()
    br = br.replace("topics.append('Hàm số & Vi-ét')", "topics.append(r'Hàm số \\& Vi-ét')")
    with open(br_path, 'w', encoding='utf-8') as f:
        f.write(br)
    print("Updated build_report.py")

# ── 2. Fix de_*.tex files ────────────────────────────────────────────────────
tex_files = glob.glob(os.path.join(latex_dir, 'de_*.tex'))
fixed_count = 0

for fpath in tex_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    
    # a. Fix display math starting line 2 with $= or $ =
    content = re.sub(r'(\n\s*)\$\s*(=)', r'\1\2', content)
    
    # b. Fix align* containing $ signs
    def fix_align(m):
        block = m.group(1)
        # Remove all $ inside the align block
        clean_block = block.replace('$', '')
        return f'\\begin{{align*}}{clean_block}\\end{{align*}}'
    
    content = re.sub(r'\\begin\{align\*\}(.*?)\\end\{align\*\}', fix_align, content, flags=re.DOTALL)
    
    # c. Fix Unicode characters
    content = content.replace('✓', r'\checkmark ')
    content = content.replace('−', '-') # Unicode minus (U+2212)
    content = content.replace('²', '^2')
    content = content.replace('³', '^3')
    content = content.replace('°', r'^\circ')
    content = content.replace(r'\ sqrt', r'\sqrt')
    
    # d. Specific for de_37 scores if empty
    if fname == 'de_37.tex':
        content = content.replace(r'\begin{de_cau}{Câu 1}{}', r'\begin{de_cau}{Câu 1}{2,0 điểm}')
        content = content.replace(r'\begin{de_cau}{Câu 2}{}', r'\begin{de_cau}{Câu 2}{2,0 điểm}')
        content = content.replace(r'\begin{de_cau}{Câu 3}{}', r'\begin{de_cau}{Câu 3}{2,5 điểm}')
        
    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_count += 1
        print(f"Fixed {fname}")

print(f"Total de_*.tex files modified: {fixed_count}")

# ── 3. Clean main.tex and bao_cao_latex.tex ──────────────────────────────────
for mf in ['main.tex', 'bao_cao_latex.tex']:
    mpath = os.path.join(latex_dir, mf)
    with open(mpath, 'r', encoding='utf-8') as f:
        mc = f.read()
    mc_orig = mc
    mc = mc.replace('─', '-').replace('═', '=')
    if mc != mc_orig:
        with open(mpath, 'w', encoding='utf-8') as f:
            f.write(mc)
        print(f"Cleaned box drawing chars from {mf}")

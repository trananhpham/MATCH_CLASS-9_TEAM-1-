# -*- coding: utf-8 -*-
"""
Kiểm tra và sửa toàn diện tất cả các lệnh toán học trong 50 file de_*.tex:
- Đảm bảo các lệnh \sqrt, \frac, \dfrac, \ge, \le, \neq, \pm, \Delta, \begin{cases}
  luôn nằm trong môi trường toán học ($...$ hoặc \[...\]).
- Loại bỏ các ký tự rác (-- HẾT ---, ...)
- Chuẩn hóa các biểu thức toán học
"""

import os, re, glob, zipfile

LATEX_DIR = r"e:\toan lop 9 lang son\latex"

def fix_content(content):
    # Remove exam footers
    content = re.sub(r'--+\s*HẾT\s*--+', '', content, flags=re.I)
    content = re.sub(r'Họ và tên thí sinh:.*', '', content, flags=re.I)
    content = re.sub(r'Số báo danh:.*', '', content, flags=re.I)
    
    # Clean redundant dots
    content = re.sub(r'\.{4,}', '...', content)
    
    # Process line by line
    lines = content.split('\n')
    new_lines = []
    
    math_cmds = [r'\sqrt', r'\frac', r'\dfrac', r'\ge', r'\le', r'\neq', r'\pm', r'\Delta']
    
    for line in lines:
        l = line.strip()
        if not l:
            new_lines.append('')
            continue
            
        # If line contains \begin{cases} and not in \[ \], wrap it
        if r'\begin{cases}' in l and not (l.startswith(r'\[') or l.startswith('$')):
            m_pre = re.match(r'^(.*?)(?:\\begin\{cases\}.*?\\end\{cases\})(.*)$', l)
            if m_pre:
                idx1 = l.find(r'\begin{cases}')
                idx2 = l.find(r'\end{cases}') + len(r'\end{cases}')
                prefix = l[:idx1].strip()
                cases_part = l[idx1:idx2]
                suffix = l[idx2:].strip()
                if prefix:
                    new_lines.append(prefix)
                new_lines.append(f'\\[ {cases_part} \\]{suffix}')
                continue
                
        # Split line by existing $...$ and \[...\]
        parts = re.split(r'(\$[^$]+\$|\\\[[\s\S]*?\\\])', l)
        res_parts = []
        for p in parts:
            if p.startswith('$') or p.startswith(r'\['):
                res_parts.append(p)
            else:
                # Check if p has naked math commands
                if any(mc in p for mc in math_cmds):
                    # Replace naked \le, \ge, \neq, \pm, \Delta with $\le$, etc.
                    p = re.sub(r'\\le\b', r'$\\le$', p)
                    p = re.sub(r'\\ge\b', r'$\\ge$', p)
                    p = re.sub(r'\\neq\b', r'$\\neq$', p)
                    p = re.sub(r'\\pm\b', r'$\\pm$', p)
                    p = re.sub(r'\\Delta\b', r'$\\Delta$', p)
                    
                    # Fix naked \sqrt and \frac
                    # If p still has \sqrt or \frac
                    if r'\sqrt' in p or r'\frac' in p or r'\dfrac' in p:
                        # Wrap equation in $
                        # If p starts with bullet e.g. a) or b) or 1.
                        m_b = re.match(r'^([a-zA-Z\d]+[\.\)])\s*(.*)$', p)
                        if m_b:
                            bullet = m_b.group(1)
                            body = m_b.group(2).strip()
                            # If body has text before ':' e.g. 'Rút gọn: '
                            if ':' in body:
                                c_idx = body.find(':')
                                intro = body[:c_idx+1]
                                rest = body[c_idx+1:].strip()
                                p = f'{bullet} {intro} ${rest}$'
                            else:
                                p = f'{bullet} ${body}$'
                        else:
                            if ':' in p:
                                c_idx = p.find(':')
                                intro = p[:c_idx+1]
                                rest = p[c_idx+1:].strip()
                                p = f'{intro} ${rest}$'
                            else:
                                p = f'${p}$'
                    res_parts.append(p)
                else:
                    res_parts.append(p)
        new_lines.append(''.join(res_parts))
        
    res = '\n'.join(new_lines)
    # Clean double dollar signs $$ if any
    res = re.sub(r'\$\$+', r'$$', res)
    # Clean empty math mode $$
    res = res.replace('$$', '')
    return res

total_fixed = 0
for i in range(1, 51):
    fpath = os.path.join(LATEX_DIR, f"de_{i}.tex")
    with open(fpath, encoding="utf-8") as f:
        orig = f.read()
    fixed = fix_content(orig)
    if fixed != orig:
        total_fixed += 1
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(fixed)

print(f"Đã rà soát và chuẩn hóa {total_fixed} file de_*.tex!")

# Cập nhật lại overleaf_upload.zip
main_path = os.path.join(LATEX_DIR, "main.tex")
zip_path = os.path.join(LATEX_DIR, "overleaf_upload.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write(main_path, "main.tex")
    for i in range(1, 51):
        de_f = os.path.join(LATEX_DIR, f"de_{i}.tex")
        zf.write(de_f, f"de_{i}.tex")
print(f"✓ Đã cập nhật overleaf_upload.zip ({os.path.getsize(zip_path)} bytes)")

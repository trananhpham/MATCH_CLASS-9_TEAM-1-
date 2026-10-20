import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')
latex_dir = r'h:/toan lop 9 lang son/latex'

def fix_content(content):
    fixed = content
    
    # 1. Replace \\& with \&
    fixed = fixed.replace(r'\\&', r'\&')
    
    # 2. Fix patterns like:
    # \item Giải hệ phương trình: $\n\[ \begin{cases}
    # \item Giải hệ phương trình $\n\[ \begin{cases}
    # \item $\n\[ \begin{cases}
    fixed = re.sub(r'(\\item[^\n\$]*)\$\s*\n\s*\\\[\s*\\begin\{cases\}', r'\1\n\\[\\begin{cases}', fixed)
    
    # Also handle inline $ right before \[
    fixed = re.sub(r'\$\s*\\\[', r'\\[', fixed)
    
    # 3. Fix patterns like:
    # \end{cases} \]$
    fixed = re.sub(r'\\end\{cases\}\s*\\\]\s*\$', r'\\end{cases}\\]', fixed)
    
    # Also handle \] followed by $ at end of display math: e.g. .\]$ or \]$\n
    fixed = re.sub(r'\\\]\s*\$', r'\\]', fixed)
    
    # 4. Handle cases like: \]$\n\[=
    fixed = re.sub(r'\\\]\s*\$\s*\\\[\s*=', r'\\]\n\\[=', fixed)
    
    return fixed

# Test on de_4, de_6, de_7, de_8, de_10, de_11, de_36, de_49
test_files = ['de_4.tex', 'de_6.tex', 'de_7.tex', 'de_8.tex', 'de_10.tex', 'de_11.tex', 'de_36.tex', 'de_49.tex']
for fname in test_files:
    fpath = os.path.join(latex_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        orig = f.read()
    res = fix_content(orig)
    print(f'=== Testing {fname} ===')
    # Check if any $[ or ]$ remain
    m1 = list(re.finditer(r'\$\s*\\\[', res))
    m2 = list(re.finditer(r'\\\]\s*\$', res))
    amp = r'\\&' in res
    print(f'  Remaining $[: {len(m1)}, Remaining ]$: {len(m2)}, Remaining \\\\&: {amp}')

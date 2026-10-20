import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')
latex_dir = r'h:/toan lop 9 lang son/latex'

def fix_content(content):
    fixed = content
    
    # 1. Replace \\& with \&
    fixed = fixed.replace(r'\\&', r'\&')
    
    # 2. Fix trailing dollar before display math:
    # e.g.: \item Giải hệ phương trình: $ \n \[
    # or: \item $ \n \[
    fixed = re.sub(r'(\b[^\n\$]*)\$[ \t]*\n([ \t]*\\\[)', r'\1\n\2', fixed)
    # Also if line is just: \item $ \n \[
    fixed = re.sub(r'(\\item)[ \t]*\$[ \t]*\n([ \t]*\\\[)', r'\1\n\2', fixed)
    # Also if dangling $ right before \[ on the same line
    fixed = re.sub(r'\$[ \t]*\\\[', r'\\[', fixed)
    
    # 3. Fix stray dollar right after \] on the same line:
    # e.g.: \end{cases} \]$ -> \end{cases} \]
    # or: = \boxed{4}.\]$ -> = \boxed{4}.\]
    fixed = re.sub(r'\\\][ \t]*\$', r'\\]', fixed)
    
    # 4. Handle cases like: \]$ followed on next line by \[=
    fixed = re.sub(r'\\\][ \t]*\$[ \t]*\n[ \t]*\\\[[ \t]*=', r'\\]\n\\[=', fixed)
    
    return fixed

# Check de_4 around t(t^3-3t-1)=0
with open('de_4.tex', 'r', encoding='utf-8') as f:
    orig = f.read()
res = fix_content(orig)
idx = res.find('t(t^3-3t-1)=0')
print('=== de_4 snippet ===')
print(res[idx:idx+200])

# Check de_6 around item Giải hệ phương trình
with open('de_6.tex', 'r', encoding='utf-8') as f:
    orig = f.read()
res = fix_content(orig)
idx = res.find('Giải hệ phương trình')
print('=== de_6 snippet ===')
print(res[idx:idx+200])

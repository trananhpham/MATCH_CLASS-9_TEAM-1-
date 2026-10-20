import os, re, glob, sys

sys.stdout.reconfigure(encoding='utf-8')
latex_dir = r'h:/toan lop 9 lang son/latex'

def clean_file(content):
    fixed = content
    
    # 1. Replace \\& with \&
    fixed = fixed.replace(r'\\&', r'\&')
    
    # 2. Fix patterns like: \item ... $\n\[ \begin{cases}
    fixed = re.sub(r'(\\item[^\n\$]*)\$[ \t]*\n([ \t]*\\\[)', r'\1\n\2', fixed)
    
    # 3. Fix patterns like: \item $\n\[
    fixed = re.sub(r'(\\item)[ \t]*\$[ \t]*\n([ \t]*\\\[)', r'\1\n\2', fixed)
    
    # 4. Fix dangling $ right before \[ on the same line
    fixed = re.sub(r'\$[ \t]*\\\[', r'\\[', fixed)
    
    # 5. Fix stray $ right after \] on the same line
    # e.g.: \end{cases} \]$ -> \end{cases} \]
    # or: = \boxed{4}.\]$ -> = \boxed{4}.\]
    fixed = re.sub(r'\\\][ \t]*\$', r'\\]', fixed)
    
    # 6. Fix \]$ followed by \[= on the next line:
    fixed = re.sub(r'\\\][ \t]*\$[ \t]*\n([ \t]*\\\[[ \t]*=)', r'\\]\n\1', fixed)
    
    # 7. Specific fix for de_36:
    # 'nghiệm của hệ phương trình $\n\[ \begin{cases} ... \end{cases} \]$ là:'
    fixed = re.sub(r'(\bphương trình)[ \t]*\$[ \t]*\n([ \t]*\\\[\s*\\begin\{cases\}.*?\\end\{cases\}\s*\\\])\$[ \t]*(là:)', 
                   r'\1:\n\2 \3', fixed, flags=re.DOTALL)
    
    # 8. Specific fix for de_49 Vi-et case:
    # 'Theo Vi-ét: $\n\[ \begin{cases} ... \end{cases} \]$'
    fixed = re.sub(r'(Theo Vi-ét:)[ \t]*\$[ \t]*\n([ \t]*\\\[\s*\\begin\{cases\}.*?\\end\{cases\}\s*\\\])\$',
                   r'\1\n\2', fixed, flags=re.DOTALL)
    
    # 9. Clean any double backslashes in \addcontentsline{toc}{section}{...}
    # specifically \addcontentsline{toc}{section}{... GD\&...}
    
    return fixed

changed_files = []
for i in range(1, 51):
    fname = f'de_{i}.tex'
    fpath = os.path.join(latex_dir, fname)
    if not os.path.exists(fpath): continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        orig = f.read()
    
    updated = clean_file(orig)
    if updated != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(updated)
        changed_files.append(fname)

print(f'Cleaned and updated {len(changed_files)} files: {changed_files}')

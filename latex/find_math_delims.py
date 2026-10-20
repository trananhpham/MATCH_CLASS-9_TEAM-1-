import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

latex_dir = r'h:/toan lop 9 lang son/latex'

for i in range(1, 51):
    fname = f'de_{i}.tex'
    fpath = os.path.join(latex_dir, fname)
    if not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches1 = list(re.finditer(r'(\$\s*\\\[)', content))
    matches2 = list(re.finditer(r'(\\\]\s*\$)', content))
    
    if matches1 or matches2:
        print(f'=== {fname} ===')
        for m in matches1:
            snippet = content[max(0, m.start()-25):min(len(content), m.end()+25)]
            print(f'  $[ at {m.start()}: {repr(snippet)}')
        for m in matches2:
            snippet = content[max(0, m.start()-25):min(len(content), m.end()+25)]
            print(f'  ]$ at {m.start()}: {repr(snippet)}')

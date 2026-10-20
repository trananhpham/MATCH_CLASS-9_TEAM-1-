import os, sys, re, glob

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"h:\toan lop 9 lang son"
LATEX_DIR = r"h:\toan lop 9 lang son\latex"

with open(os.path.join(LATEX_DIR, "generate_full_50.py"), "r", encoding="utf-8") as f:
    c_gen50 = f.read()

with open(os.path.join(LATEX_DIR, "build_all_50_exams.py"), "r", encoding="utf-8") as f:
    c_build = f.read()

with open(os.path.join(LATEX_DIR, "gen_latex.py"), "r", encoding="utf-8") as f:
    c_genlatex = f.read()

keys_gen50 = re.findall(r'MANUAL_EXAMS\["([^"]+)"\]', c_gen50)
keys_build = re.findall(r'CURATED\["([^"]+)"\]', c_build)
keys_genlatex = re.findall(r'"([a-zA-Z0-9\-_]+\.pdf)":\s*\{', c_genlatex)

print("Keys in gen_latex.py:", len(keys_genlatex))
for k in keys_genlatex:
    print("  genlatex:", k)

print("Keys in generate_full_50.py:", len(keys_gen50))
for k in keys_gen50:
    print("  gen50:", k)

print("Keys in build_all_50_exams.py:", len(keys_build))
for k in keys_build:
    print("  build:", k)

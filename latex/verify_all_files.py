import os, re, glob, sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
latex_dir = r'h:/toan lop 9 lang son/latex'

all_issues = {}

for i in range(1, 51):
    fname = f'de_{i}.tex'
    fpath = os.path.join(latex_dir, fname)
    if not os.path.exists(fpath):
        all_issues[fname] = ['File does not exist!']
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Check 1: dollar with display math ON SAME LINE or dangling right before \[
    # Dangling $ right before \[ : e.g. $\n\[ or $[ \t]*\[
    if re.search(r'\$[ \t]*\\\[', content):
        issues.append('Dangling $ right before \\[')
    if re.search(r'\\item[^\n]*\$[ \t]*\n[ \t]*\\\[', content):
        issues.append('Item line ends with $ before \\[')
    if re.search(r'\\\][ \t]*\$', content):
        issues.append('Stray $ right after \\] on same line')
        
    # Check 2: \\sqrt followed by letter
    bad_sqrt = re.findall(r'\\sqrt[a-zA-Z]', content)
    if bad_sqrt:
        issues.append(f'Bad \\sqrt: {bad_sqrt}')
        
    # Check 3: begin/end environment matching
    begins = re.findall(r'\\begin\{([^}]+)\}', content)
    ends = re.findall(r'\\end\{([^}]+)\}', content)
    b_cnt = Counter(begins)
    e_cnt = Counter(ends)
    for env in set(list(b_cnt.keys()) + list(e_cnt.keys())):
        if b_cnt[env] != e_cnt[env]:
            issues.append(f'Mismatched env {env}: begin={b_cnt[env]}, end={e_cnt[env]}')
            
    # Check 4: de_cau vs loi_giai_cau count
    c_de = content.count(r'\begin{de_cau}')
    c_lg = content.count(r'\begin{loi_giai_cau}')
    if c_de == 0:
        issues.append('No de_cau found!')
    if c_de != c_lg:
        issues.append(f'de_cau count ({c_de}) != loi_giai_cau count ({c_lg})')
        
    # Check 5: double backslash ampersand \\&
    if r'\\&' in content:
        issues.append(r'Found double backslash ampersand (\\&)')
        
    # Check 6: unmatched braces
    no_comments = re.sub(r'%.*$', '', content, flags=re.MULTILINE)
    clean = no_comments.replace(r'\{', '').replace(r'\}', '')
    open_b = clean.count('{')
    close_b = clean.count('}')
    if open_b != close_b:
        issues.append(f'Unbalanced braces: {{={open_b}, }}={close_b}')
        
    # Check 7: incomplete/placeholder text
    if 'Đang cập nhật' in content:
        issues.append('Contains "Đang cập nhật"')
        
    # Check 8: check if any de_cau score lacks 'điểm'
    for m in re.finditer(r'\\begin\{de_cau\}\{([^}]+)\}\{([^}]+)\}', content):
        score = m.group(2).strip()
        if score and 'điểm' not in score.lower() and 'đ' not in score.lower():
            issues.append(f'de_cau score lacks "điểm": {m.group(1)} -> {score}')

    if issues:
        all_issues[fname] = issues

print(f'Total files checked: 50. Files with issues: {len(all_issues)}')
for f, iss in sorted(all_issues.items(), key=lambda x: int(re.search(r'\d+', x[0]).group())):
    print(f'--- {f} ---')
    for itm in iss:
        print(f'  * {itm}')

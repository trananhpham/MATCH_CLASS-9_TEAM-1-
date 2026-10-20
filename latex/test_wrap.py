# -*- coding: utf-8 -*-
import re

def convert_raw_math(text):
    text = text.replace('\xa0', ' ').replace('\u200b', '')
    text = text.replace('²²', '^4').replace('²', '^2').replace('³', '^3')
    text = text.replace('₁', '_1').replace('₂', '_2').replace('₃', '_3')
    text = text.replace('ñ', 'đ').replace('ñiểm', 'điểm').replace('ð', 'đ')
    text = re.sub(r'--+\s*HẾT\s*--+', '', text, flags=re.I)
    
    # clean sqrt patterns
    text = re.sub(r'√\(\s*\(\s*([^()]+)\s*\)\s*\)', r'\\sqrt{\1}', text)
    text = re.sub(r'√\(\s*([^()]+)\s*\)', r'\\sqrt{\1}', text)
    text = re.sub(r'√(\d+|[a-zA-Z])', r'\\sqrt{\1}', text)
    text = text.replace('√', r'\sqrt')
    
    # Replace math relational operators with latex inline
    text = text.replace('≥', r'$\ge$').replace('', r'$\ge$')
    text = text.replace('≤', r'$\le$').replace('', r'$\le$')
    text = text.replace('≠', r'$\neq$').replace('', r'$\neq$')
    text = text.replace('∈', r'$\in$').replace('', r'$\in$')
    text = text.replace('±', r'$\pm$').replace('', r'$\pm$')
    text = text.replace('Δ', r'$\Delta$').replace('', r'$\Delta$')
    
    # ensure any remaining \sqrt outside $ is wrapped in $
    # If a line contains \sqrt and no $, wrap the equation
    lines = text.split('\n')
    new_lines = []
    for ln in lines:
        l = ln.strip()
        if not l:
            new_lines.append('')
            continue
        if r'\sqrt' in l and '$' not in l:
            m = re.search(r'([A-Za-z0-9_]+\s*=\s*.*)$', l)
            if m:
                eq = m.group(1).rstrip('.')
                l = l[:m.start()] + f'${eq}$.'
            else:
                l = f'${l}$'
        new_lines.append(l)
    return '\n'.join(new_lines)

sample1 = 'a) Rút gọn: A = √( (15 - 6√6) ) + √( (33 - 12√6) ).'
sample2 = 'b) Cho x, y thỏa mãn (x + √(x² + 3))(y + √(y² + 3)) = 3. Tính x + y.'
sample3 = 'a) ĐKXĐ: 1 ≤ x ≤ 2. Áp dụng BĐT AM-GM hoặc bình phương: x = 1 hoặc x = 2. (2,0 điểm)'

print(convert_raw_math(sample1))
print(convert_raw_math(sample2))
print(convert_raw_math(sample3))

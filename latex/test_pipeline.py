# -*- coding: utf-8 -*-
import fitz, re

def clean_math_pipeline(text):
    # Remove footers
    text = re.sub(r'--+\s*HẾT\s*--+', '', text, flags=re.I)
    text = re.sub(r'Họ và tên thí sinh:.*', '', text, flags=re.I)
    text = re.sub(r'Số báo danh:.*', '', text, flags=re.I)
    text = text.replace('\xa0', ' ').replace('\u200b', '')
    
    # Unicode powers and indices
    text = text.replace('²²', '^4').replace('²', '^2').replace('³', '^3')
    text = text.replace('₁', '_1').replace('₂', '_2').replace('₃', '_3')
    text = text.replace('ñ', 'đ').replace('ñiểm', 'điểm').replace('ð', 'đ')
    
    # Sqrt normalization
    text = re.sub(r'√\(\s*\(\s*([^()]+)\s*\)\s*\)', r'\\sqrt{\1}', text)
    text = re.sub(r'√\(\s*([^()]+)\s*\)', r'\\sqrt{\1}', text)
    text = re.sub(r'√(\d+|[a-zA-Z])', r'\\sqrt{\1}', text)
    text = text.replace('√', r'\sqrt')
    
    # Normalize nested \sqrt( ... )
    text = re.sub(r'\\sqrt\(\s*\(\s*([^()]+)\s*\)\s*\)', r'\\sqrt{\1}', text)
    text = re.sub(r'\\sqrt\(\s*([^()]+)\s*\)', r'\\sqrt{\1}', text)
    text = re.sub(r'\\sqrt([0-9a-zA-Z])', r'\\sqrt{\1}', text)
    
    # Operators
    text = text.replace('≥', r'\ge ').replace('', r'\ge ')
    text = text.replace('≤', r'\le ').replace('', r'\le ')
    text = text.replace('≠', r'\neq ').replace('', r'\neq ')
    text = text.replace('∈', r'\in ').replace('', r'\in ')
    text = text.replace('±', r'\pm ').replace('', r'\pm ')
    text = text.replace('Δ', r'\Delta ').replace('', r'\Delta ')
    
    lines = text.split('\n')
    out_lines = []
    
    for line in lines:
        l = line.strip()
        if not l:
            out_lines.append('')
            continue
            
        # If line contains cases
        if r'\begin{cases}' in l:
            # find cases
            m = re.search(r'(\\begin\{cases\}.*?\\end\{cases\})', l)
            if m:
                pre = l[:m.start()].strip()
                cases = m.group(1)
                post = l[m.end():].strip()
                if pre:
                    out_lines.append(pre)
                out_lines.append(r'\[' + cases + r'\]' + post)
                continue
                
        # If line has bullet and math expression
        # e.g.: a) Rút gọn: A = \sqrt{15 - 6\sqrt{6}} + \sqrt{33 - 12\sqrt{6}}.
        m_bullet_lead = re.match(r'^([a-zA-Z\d]+[\.\)])\s*(Rút gọn|Tính giá trị biểu thức|Tính giá trị|Tính|Giải phương trình|Giải hệ phương trình|Chứng minh rằng|Chứng minh|ĐKXĐ|Áp dụng|Biến đổi thành|Biến đổi|Theo định lý Vi-ét|Theo Vi-ét|Theo đề bài|Suy ra|Do đó|Vậy)?\s*[:\s]?\s*(.*)$', l, re.I)
        if m_bullet_lead and any(k in l for k in ['=', r'\sqrt', r'\frac', r'\ge', r'\le', r'\neq', r'\Delta', r'\pm', '^', '_']):
            bullet = m_bullet_lead.group(1)
            lead = m_bullet_lead.group(2)
            expr = m_bullet_lead.group(3).strip()
            
            # check if expr ends with points like '(2,0 điểm)' or '.'
            dm = re.search(r'\(\s*[\d,\.]+\s*(?:điểm|đ|đ\.)\s*\)\.?$', expr, re.I)
            diem_str = ''
            if dm:
                diem_str = ' ' + dm.group(0)
                expr = expr[:dm.start()].strip()
            
            period = '.' if expr.endswith('.') else ''
            expr = expr.rstrip('.')
            
            lead_str = f'{lead}: ' if lead else ''
            if expr:
                out_lines.append(f'{bullet} {lead_str}${expr}${period}{diem_str}')
            else:
                out_lines.append(f'{bullet} {lead_str}{diem_str}')
            continue
            
        # General math line with = or \ge or \le and math symbols
        if any(k in l for k in [r'\sqrt', r'\frac', r'\ge', r'\le', r'\neq', r'\Delta', r'\pm']) and '$' not in l:
            # check if line has Vietnamese words
            # if line is mostly formula, wrap in display math or inline math
            if re.search(r'[a-zA-Z0-9_]+\s*=\s*.*', l):
                # find prefix text before =
                # e.g. "Áp dụng Cauchy-Schwarz: P = 1/x + 1/y + 1/z \ge 9/(x + y + z) = 9. Min P = 9 khi x = y = z = 1/3."
                # Split at colon if exists
                if ':' in l:
                    c_idx = l.find(':')
                    pre = l[:c_idx+1]
                    rest = l[c_idx+1:].strip()
                    # if rest has math, wrap in $
                    out_lines.append(f'{pre} ${rest}$')
                else:
                    out_lines.append(f'${l}$')
            else:
                out_lines.append(f'${l}$')
            continue
            
        out_lines.append(l)
        
    return '\n'.join(out_lines)

p1 = r'e:\toan lop 9 lang son\de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2018-2019-so-gddt-lang-son.pdf'
doc = fitz.open(p1)
full = '\n'.join(p.get_text() for p in doc)
print('CLEAN SAMPLE:')
print(clean_math_pipeline(full[:800]))

import os, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

import db_scanned_part1, db_scanned_part2, db_scanned_part3
import db_expansion_part1, db_expansion_part2, db_expansion_part3, db_expansion_part4
import build_all_50_exams

ROOT_DIR = r'h:\toan lop 9 lang son'
all_pdfs = sorted([os.path.basename(f) for f in glob.glob(os.path.join(ROOT_DIR, '*.pdf'))])
print(f'Total PDFs: {len(all_pdfs)}')

scanned_map = {}
for p in [db_scanned_part1.SCANNED_PART1, db_scanned_part2.SCANNED_PART2, db_scanned_part3.SCANNED_PART3]:
    scanned_map.update(p)

expansion_map = {}
for p in [db_expansion_part1.EXPANSION_PART1, db_expansion_part2.EXPANSION_PART2, db_expansion_part3.EXPANSION_PART3, db_expansion_part4.EXPANSION_PART4]:
    expansion_map.update(p)

curated_map = build_all_50_exams.CURATED

counts = {'SCANNED': 0, 'EXPANSION': 0, 'CURATED': 0, 'MISSING': 0}
for i, f in enumerate(all_pdfs, 1):
    src = None
    if f in scanned_map:
        src = 'SCANNED'
        counts['SCANNED'] += 1
    elif f in expansion_map:
        src = 'EXPANSION'
        counts['EXPANSION'] += 1
    elif f in curated_map:
        src = 'CURATED'
        counts['CURATED'] += 1
    else:
        src = 'MISSING'
        counts['MISSING'] += 1
    print(f'Đề {i:2d}: [{src:9s}] {f}')

print('\nSummary counts:', counts)

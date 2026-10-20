import sys
sys.stdout.reconfigure(encoding='utf-8')
import db_scanned_part1, db_scanned_part2, db_scanned_part3

all_scanned = {}
all_scanned.update(db_scanned_part1.SCANNED_PART1)
all_scanned.update(db_scanned_part2.SCANNED_PART2)
all_scanned.update(db_scanned_part3.SCANNED_PART3)

for k, v in all_scanned.items():
    lens = [len(q['giai'].strip()) for q in v['questions']]
    t = v['title'][:50]
    print(f"{t}: lens = {lens}")

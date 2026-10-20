# -*- coding: utf-8 -*-
"""
export_questions_json.py
========================
Xuất toàn bộ câu hỏi từ 50 file de_X.tex ra questions.json chuẩn hóa.

Cấu trúc mỗi câu:
{
  "id":            "LS_001_C1",
  "exam_id":       1,
  "exam_type":     "HSG_tinh" | "Tuyen_sinh_10" | "Hoc_ky",
  "nam_hoc":       "2018-2019",
  "so_cau":        "1",
  "diem":          4.0,
  "sub_parts":     ["a", "b"],
  "statement_latex": "...",
  "solution_latex":  "...",
  "topics":        ["can_thuc", "he_phuong_trinh"],
  "difficulty":    3,
  "key_techniques":["ruut_gon_can_bac2", "phuong_trinh_bac2"],
  "similar_ids":   []
}
"""

import re, json, os

DIR     = os.path.dirname(os.path.abspath(__file__))
OUT_FILE = os.path.join(DIR, "questions.json")

# ─── Metadata từng đề ────────────────────────────────────────────────────────
EXAM_META = {
    1:  {"type": "HSG_tinh",      "nam_hoc": "2018-2019"},
    2:  {"type": "HSG_tinh",      "nam_hoc": "2021-2022"},
    3:  {"type": "HSG_tinh",      "nam_hoc": "2023-2024"},
    4:  {"type": "HSG_tinh",      "nam_hoc": "2024-2025"},
    5:  {"type": "HSG_tinh",      "nam_hoc": "2025-2026"},
    6:  {"type": "Hoc_ky",        "nam_hoc": "2024-2025"},
    7:  {"type": "Hoc_ky",        "nam_hoc": "2023-2024"},
    8:  {"type": "Hoc_ky",        "nam_hoc": "2022-2023"},
    9:  {"type": "Hoc_ky",        "nam_hoc": "2025-2026"},
    10: {"type": "Hoc_ky",        "nam_hoc": "2022-2023"},
    11: {"type": "HSG_tinh",      "nam_hoc": "2022-2023"},
    12: {"type": "HSG_tinh",      "nam_hoc": "2021-2022"},
    13: {"type": "HSG_tinh",      "nam_hoc": "2023-2024"},
    14: {"type": "HSG_tinh",      "nam_hoc": "2023-2024"},
    15: {"type": "Hoc_ky",        "nam_hoc": "2022-2023"},
    16: {"type": "Hoc_ky",        "nam_hoc": "2023-2024"},
    17: {"type": "Hoc_ky",        "nam_hoc": "2021-2022"},
    18: {"type": "Hoc_ky",        "nam_hoc": "2023-2024"},
    19: {"type": "HSG_tinh",      "nam_hoc": "2019-2020"},
    20: {"type": "HSG_tinh",      "nam_hoc": "2020-2021"},
    21: {"type": "Tuyen_sinh_10", "nam_hoc": "2025-2026"},
    22: {"type": "Tuyen_sinh_10", "nam_hoc": "2025-2026"},
    23: {"type": "Tuyen_sinh_10", "nam_hoc": "2024-2025"},
    24: {"type": "Tuyen_sinh_10", "nam_hoc": "2024-2025"},
    25: {"type": "Tuyen_sinh_10", "nam_hoc": "2021-2022"},
    26: {"type": "Tuyen_sinh_10", "nam_hoc": "2020-2021"},
    27: {"type": "Tuyen_sinh_10", "nam_hoc": "2017-2018"},
    28: {"type": "Tuyen_sinh_10", "nam_hoc": "2018-2019"},
    29: {"type": "Tuyen_sinh_10", "nam_hoc": "2019-2020"},
    30: {"type": "Tuyen_sinh_10", "nam_hoc": "2020-2021"},
    31: {"type": "Tuyen_sinh_10", "nam_hoc": "2021-2022"},
    32: {"type": "Tuyen_sinh_10", "nam_hoc": "2022-2023"},
    33: {"type": "Tuyen_sinh_10", "nam_hoc": "2023-2024"},
    34: {"type": "Tuyen_sinh_10", "nam_hoc": "2024-2025"},
    35: {"type": "Tuyen_sinh_10", "nam_hoc": "2025-2026"},
    36: {"type": "Tuyen_sinh_10", "nam_hoc": "2026-2027"},
    37: {"type": "Tuyen_sinh_10", "nam_hoc": "2023-2024"},
    38: {"type": "Tuyen_sinh_10", "nam_hoc": "2025-2026"},
    39: {"type": "Tuyen_sinh_10", "nam_hoc": "2026-2027"},
    40: {"type": "Tuyen_sinh_10", "nam_hoc": "2012-2013"},
    41: {"type": "Tuyen_sinh_10", "nam_hoc": "2013-2014"},
    42: {"type": "Tuyen_sinh_10", "nam_hoc": "2014-2015"},
    43: {"type": "Tuyen_sinh_10", "nam_hoc": "2015-2016"},
    44: {"type": "Tuyen_sinh_10", "nam_hoc": "2016-2017"},
    45: {"type": "Tuyen_sinh_10", "nam_hoc": "2018-2019"},
    46: {"type": "Tuyen_sinh_10", "nam_hoc": "2020-2021"},
    47: {"type": "Tuyen_sinh_10", "nam_hoc": "2021-2022"},
    48: {"type": "Tuyen_sinh_10", "nam_hoc": "2022-2023"},
    49: {"type": "Tuyen_sinh_10", "nam_hoc": "2024-2025"},
    50: {"type": "Tuyen_sinh_10", "nam_hoc": "2019-2020"},
}


# ─── Tự động phân loại chủ đề ────────────────────────────────────────────────
def classify_topics(text: str) -> tuple[list[str], list[str], int]:
    """
    Trả về (topics, key_techniques, difficulty)
    dựa trên từ khóa trong đề + lời giải.
    """
    t = text.lower()
    topics, techniques = [], []

    # ── Chủ đề 1: Căn thức ───────────────────────────────────────────────────
    can = (r"\sqrt" in text or "căn" in t or "rút gọn" in t
           or r"\sqrt[3]" in text)
    if can:
        topics.append("can_thuc")
        if r"\sqrt[3]" in text or "căn bậc ba" in t:
            techniques.append("can_bac3")
        if "rút gọn" in t:
            techniques.append("rut_gon_can_bac2")
        if r"\sqrt{x}" in text and ("điều kiện" in t or r"x \neq" in text):
            techniques.append("dieu_kien_xac_dinh")

    # ── Chủ đề 2: Phương trình & Hệ PT ──────────────────────────────────────
    pt = ("phương trình" in t or r"\begin{cases}" in text
          or "giải phương" in t or "nghiệm" in t)
    he_pt = (r"\begin{cases}" in text or "hệ phương trình" in t
             or "hệ pt" in t)
    if he_pt:
        topics.append("he_phuong_trinh")
        techniques.append("giai_he_pt")
    elif pt:
        topics.append("phuong_trinh")
        if "bậc hai" in t or "x^2" in text.lower():
            techniques.append("phuong_trinh_bac2")
        if r"\sqrt" in text and "phương trình" in t:
            techniques.append("pt_chua_can")

    # ── Chủ đề 3: Hàm số & Đồ thị ───────────────────────────────────────────
    ham = ("hàm số" in t or "parabol" in t or "đồ thị" in t
           or "= ax^2" in text or "= ax + b" in text
           or "bậc nhất" in t or "bậc hai" in t)
    if ham:
        topics.append("ham_so_do_thi")
        if "parabol" in t or "ax^2" in text:
            techniques.append("parabol_y_ax2")
        if "đường thẳng" in t or "ax + b" in text:
            techniques.append("ham_so_bac_nhat")

    # ── Chủ đề 4: Vi-ét & Phương trình bậc 2 ────────────────────────────────
    viet = ("vi-ét" in t or "vieta" in t or "viet" in t
            or "x_1" in text or "x_2" in text
            or r"x_1+x_2" in text or r"x_1 x_2" in text
            or "delta" in t or r"\Delta" in text)
    if viet and ("x_1" in text or "x_2" in text or r"\Delta" in text):
        if "ham_so_do_thi" not in topics:
            topics.append("ham_so_do_thi")
        techniques.append("dinh_ly_viet")
        if r"\Delta" in text:
            techniques.append("phan_biet_nghiem_delta")

    # ── Chủ đề 5: Bất đẳng thức & Cực trị ───────────────────────────────────
    bdt = ("bất đẳng thức" in t or "cực trị" in t or "nhỏ nhất" in t
           or "lớn nhất" in t or "min" in t or "max" in t
           or "cauchy" in t or "schwarz" in t or "am-gm" in t
           or "bđt" in t)
    if bdt:
        topics.append("bat_dang_thuc_cuc_tri")
        if "cauchy" in t or "am-gm" in t:
            techniques.append("bat_dang_thuc_am_gm")
        if "schwarz" in t or "engel" in t or "titu" in t:
            techniques.append("bat_dang_thuc_cauchy_schwarz")

    # ── Chủ đề 6: Số học & Nghiệm nguyên ────────────────────────────────────
    so_hoc = ("nguyên" in t and ("chia hết" in t or "nghiệm nguyên" in t
              or "số nguyên" in t or "chính phương" in t))
    if so_hoc:
        topics.append("so_hoc_nguyen")
        if "chính phương" in t:
            techniques.append("so_chinh_phuong")
        if "chia hết" in t:
            techniques.append("tinh_chia_het")
        if "ước" in t:
            techniques.append("uoc_so_nguyen")

    # ── Chủ đề 7: Toán thực tế (lập phương trình) ───────────────────────────
    thuc_te = ("vận tốc" in t or "quãng đường" in t or "năng suất" in t
               or "công việc" in t or "bể nước" in t or "km/h" in t
               or "giờ" in t and ("đến" in t or "đi" in t)
               or "lợi nhuận" in t or "phần trăm" in t)
    if thuc_te:
        topics.append("toan_thuc_te")
        if "vận tốc" in t or "km/h" in t:
            techniques.append("toan_chuyen_dong")
        if "năng suất" in t or "công việc" in t or "bể" in t:
            techniques.append("toan_nang_suat")
        if "lợi nhuận" in t or "phần trăm" in t or "%" in text:
            techniques.append("toan_kinh_te")

    # Loại bỏ trùng lặp
    topics      = list(dict.fromkeys(topics))
    techniques  = list(dict.fromkeys(techniques))

    # ── Ước lượng độ khó ─────────────────────────────────────────────────────
    difficulty = _estimate_difficulty(text, topics, techniques)

    return topics, techniques, difficulty


def _estimate_difficulty(text: str, topics: list, techniques: list) -> int:
    """Trả về độ khó 1–5."""
    score = 1
    t = text.lower()

    # Tăng theo số chủ đề phối hợp
    score += min(len(topics) - 1, 2)

    # Các kỹ thuật nâng cao
    hard_tech = {
        "can_bac3", "so_chinh_phuong", "tinh_chia_het",
        "bat_dang_thuc_cauchy_schwarz", "uoc_so_nguyen",
        "phan_biet_nghiem_delta"
    }
    score += min(len(set(techniques) & hard_tech), 2)

    # Từ khoá đặc trưng đề HSG / khó
    hard_kw = [
        "chứng minh", r"\forall", "với mọi", "đơn điệu",
        "liên hợp", "tương đương", "bất kỳ", r"\gcd",
        "ước chung", "phương trình bậc ba", "hệ đối xứng"
    ]
    score += sum(1 for kw in hard_kw if kw in t or kw in text)

    return min(max(score, 1), 5)


# ─── Parser LaTeX → danh sách câu ────────────────────────────────────────────
_RE_DE_CAU = re.compile(
    r'\\begin\{de_cau\}\{([^}]+)\}\{([^}]+)\}(.*?)\\end\{de_cau\}',
    re.DOTALL
)
_RE_LOI_GIAI = re.compile(
    r'\\begin\{loi_giai_cau\}(.*?)\\end\{loi_giai_cau\}',
    re.DOTALL
)
_RE_SUBPART = re.compile(
    r'\\item\s+(?:\\textbf\{[a-z]\)\}|[a-z]\))',
    re.IGNORECASE
)


def _count_subparts(statement: str) -> list[str]:
    """Đếm số phần con (a, b, c, ...) trong đề bài."""
    if r"\begin{enumerate}" not in statement:
        return []
    # Đếm \item trong enumerate đầu tiên
    inner = re.search(r'\\begin\{enumerate\}(.*?)\\end\{enumerate\}',
                      statement, re.DOTALL)
    if not inner:
        return []
    items = re.findall(r'\\item', inner.group(1))
    return [chr(ord('a') + i) for i in range(len(items))]


def _clean(s: str) -> str:
    """Loại bỏ khoảng trắng đầu/cuối và dòng trống thừa."""
    lines = s.strip().splitlines()
    cleaned = []
    prev_blank = False
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            if not prev_blank:
                cleaned.append("")
            prev_blank = True
        else:
            cleaned.append(line.rstrip())
            prev_blank = False
    return "\n".join(cleaned).strip()


def parse_file(filepath: str, exam_id: int) -> list[dict]:
    """Parse một file de_X.tex → list câu hỏi."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    meta      = EXAM_META.get(exam_id, {"type": "Unknown", "nam_hoc": "?"})
    ex_type   = meta["type"]
    nam_hoc   = meta["nam_hoc"]

    questions_raw = list(_RE_DE_CAU.finditer(content))
    solutions_raw = list(_RE_LOI_GIAI.finditer(content))

    results = []
    for i, q_match in enumerate(questions_raw):
        so_cau_label = q_match.group(1).strip()   # "Câu 1", "Câu 2", ...
        diem_str     = q_match.group(2).strip()   # "4,0 điểm"
        statement    = _clean(q_match.group(3))

        # Số câu: lấy chữ số cuối trong label
        so_cau = re.search(r'\d+', so_cau_label)
        so_cau = so_cau.group() if so_cau else str(i + 1)

        # Điểm
        diem_num = re.search(r'[\d,\.]+', diem_str)
        diem = float(diem_num.group().replace(',', '.')) if diem_num else 0.0

        # Lời giải tương ứng
        solution = ""
        if i < len(solutions_raw):
            solution = _clean(solutions_raw[i].group(1))

        # Phân loại
        full_text = statement + "\n" + solution
        topics, techniques, difficulty = classify_topics(full_text)

        # Sub-parts
        sub_parts = _count_subparts(statement)

        # ID chuẩn hóa: LS_021_C3  (đề 21, câu 3)
        uid = f"LS_{exam_id:03d}_C{so_cau}"

        results.append({
            "id":               uid,
            "exam_id":          exam_id,
            "exam_type":        ex_type,
            "nam_hoc":          nam_hoc,
            "so_cau":           so_cau,
            "diem":             diem,
            "sub_parts":        sub_parts,
            "statement_latex":  statement,
            "solution_latex":   solution,
            "topics":           topics,
            "difficulty":       difficulty,
            "key_techniques":   techniques,
            "similar_ids":      []          # Sẽ điền ở bước sau
        })

    return results


# ─── Tính similar_ids ────────────────────────────────────────────────────────
def compute_similar(all_questions: list[dict]) -> None:
    """
    Với mỗi câu, tìm 3–5 câu tương tự nhất dựa trên:
      - Chung ít nhất 1 topic
      - Cùng sub_parts count (± 1)
      - Không phải cùng đề
    Sắp xếp ưu tiên: số topic trùng nhiều nhất.
    """
    for q in all_questions:
        q_topics = set(q["topics"])
        q_parts  = len(q["sub_parts"])
        candidates = []
        for other in all_questions:
            if other["id"] == q["id"]:
                continue
            if other["exam_id"] == q["exam_id"]:
                continue  # Không tính cùng đề
            shared = len(q_topics & set(other["topics"]))
            if shared == 0:
                continue
            part_diff = abs(len(other["sub_parts"]) - q_parts)
            # Score: ưu tiên nhiều topic chung, gần điểm số, ít chênh lệch sub_parts
            score = shared * 10 - part_diff * 2 - abs(other["diem"] - q["diem"])
            candidates.append((score, other["id"]))

        # Lấy top 5
        candidates.sort(key=lambda x: -x[0])
        q["similar_ids"] = [c[1] for c in candidates[:5]]


# ─── Thống kê ────────────────────────────────────────────────────────────────
def print_stats(all_questions: list[dict]) -> None:
    from collections import Counter
    print(f"\n{'='*55}")
    print(f"  THỐNG KÊ DATASET questions.json")
    print(f"{'='*55}")
    print(f"  Tổng số câu hỏi:   {len(all_questions)}")

    types = Counter(q["exam_type"] for q in all_questions)
    print(f"\n  Phân loại kỳ thi:")
    for k, v in types.most_common():
        print(f"    {k:<20}: {v:>3} câu")

    topics_all = []
    for q in all_questions:
        topics_all.extend(q["topics"])
    topic_count = Counter(topics_all)
    print(f"\n  Phân loại chủ đề:")
    for k, v in topic_count.most_common():
        print(f"    {k:<30}: {v:>3} câu")

    diffs = Counter(q["difficulty"] for q in all_questions)
    print(f"\n  Phân bố độ khó (1=dễ, 5=rất khó):")
    for d in range(1, 6):
        bar = "█" * diffs.get(d, 0)
        print(f"    Mức {d}: {diffs.get(d,0):>3} câu  {bar}")

    total_diem = sum(q["diem"] for q in all_questions)
    print(f"\n  Tổng quỹ điểm:     {total_diem:.1f} điểm")
    print(f"  TB điểm/câu:       {total_diem/len(all_questions):.2f} điểm")
    print(f"{'='*55}\n")


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    all_questions = []
    missing = []

    print("Đang xử lý 50 file de_X.tex ...")
    for exam_id in range(1, 51):
        fpath = os.path.join(DIR, f"de_{exam_id}.tex")
        if not os.path.exists(fpath):
            missing.append(exam_id)
            print(f"  [SKIP] de_{exam_id}.tex — không tìm thấy")
            continue
        try:
            qs = parse_file(fpath, exam_id)
            all_questions.extend(qs)
            print(f"  [OK]   de_{exam_id}.tex — {len(qs)} câu")
        except Exception as e:
            print(f"  [ERR]  de_{exam_id}.tex — {e}")

    print(f"\nTính similar_ids ...")
    compute_similar(all_questions)

    # ── Xuất JSON ──────────────────────────────────────────────────────────
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "meta": {
                "version":      "1.0",
                "description":  "Ngân hàng câu hỏi Toán lớp 9 – Tỉnh Lạng Sơn",
                "total":        len(all_questions),
                "source":       "50 đề thi PDF 2012–2026",
                "topics": [
                    "can_thuc",
                    "phuong_trinh",
                    "he_phuong_trinh",
                    "ham_so_do_thi",
                    "bat_dang_thuc_cuc_tri",
                    "so_hoc_nguyen",
                    "toan_thuc_te"
                ],
                "exam_types": ["HSG_tinh", "Tuyen_sinh_10", "Hoc_ky"],
                "difficulty_scale": "1 (dễ) → 5 (rất khó)"
            },
            "questions": all_questions
        }, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Đã xuất: {OUT_FILE}")
    print_stats(all_questions)

    if missing:
        print(f"Đề bị thiếu: {missing}")


if __name__ == "__main__":
    main()

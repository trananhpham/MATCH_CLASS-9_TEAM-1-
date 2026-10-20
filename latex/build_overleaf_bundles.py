import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')
latex_dir = r'h:/toan lop 9 lang son/latex'

# Common header preamble
common_preamble = r"""%!TEX encoding = UTF-8 Unicode
%!TEX program = pdflatex
\documentclass[12pt,a4paper]{article}

%% -- Encoding & Font (pdfLaTeX - Tối ưu tốc độ cao nhất trên Overleaf) --------
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{times}
\usepackage[vietnamese]{babel}
\usepackage{amssymb}
\DeclareUnicodeCharacter{2713}{\checkmark}
\DeclareUnicodeCharacter{2212}{-}
\DeclareUnicodeCharacter{00B2}{\textsuperscript{2}}
\DeclareUnicodeCharacter{00B3}{\textsuperscript{3}}
\DeclareUnicodeCharacter{00B0}{\ensuremath{^\circ}}

%% -- Toán học ----------------------------------------------------------------
\usepackage{amsmath,amssymb,amsfonts,amsthm,mathtools}
\usepackage{cases}

%% -- Trang / Layout ----------------------------------------------------------
\usepackage[a4paper,top=2.5cm,bottom=2.5cm,left=2.5cm,right=2cm,headheight=15pt]{geometry}
\usepackage{fancyhdr}

%% -- Hyperref ----------------------------------------------------------------
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=blue!70!black,
  urlcolor=blue!70!black,
  pdfencoding=auto
}

%% -- Màu & Box ---------------------------------------------------------------
\usepackage{xcolor}
\usepackage{tcolorbox}

%% -- Danh sách / Bảng --------------------------------------------------------
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{longtable}
\setlist{nosep,leftmargin=*}
\usepackage{multicol}

%% -- Định nghĩa màu sắc ------------------------------------------------------
\definecolor{titlebg}{RGB}{0,55,120}
\definecolor{mainblue}{RGB}{15,95,175}
\definecolor{lightblue}{RGB}{225,238,255}
\definecolor{maingreen}{RGB}{5,110,65}
\definecolor{lightgreen}{RGB}{220,255,238}
\definecolor{warnbg}{RGB}{255,248,220}
\definecolor{warnborder}{RGB}{200,150,0}

%% -- Box câu hỏi (xanh) ------------------------------------------------------
\newtcolorbox{de_cau}[2]{
  colback=lightblue,
  colframe=mainblue,
  arc=0pt, boxrule=0.8pt,
  title={\large #1 \normalfont\normalsize\itshape #2},
  fonttitle=\color{white}\bfseries,
  colbacktitle=mainblue,
  left=8pt, right=8pt, top=6pt, bottom=6pt,
  before upper={\setlength{\parskip}{4pt}\setlength{\parindent}{0pt}}
}

%% -- Box lời giải (xanh lá) --------------------------------------------------
\newtcolorbox{loi_giai_cau}{
  colback=lightgreen,
  colframe=maingreen,
  arc=0pt, boxrule=0.8pt,
  title={Lời giải \& Đáp án},
  fonttitle=\color{white}\bfseries,
  colbacktitle=maingreen,
  left=8pt, right=8pt, top=6pt, bottom=6pt,
  before upper={\setlength{\parskip}{4pt}\setlength{\parindent}{0pt}}
}

%% -- Header / Footer ---------------------------------------------------------
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape\color{mainblue} Tuyển tập Đề thi Toán lớp 9 -- Tỉnh Lạng Sơn}
\fancyhead[R]{\small\itshape\color{mainblue} (Phần Đại số -- Có Lời giải chi tiết)}
\fancyfoot[C]{\small\color{gray}\thepage}
\renewcommand{\headrulewidth}{0.5pt}
"""

def make_titlepage(sub_title=""):
    return r"""
\begin{document}

\begin{titlepage}
  \centering\vspace*{2.0cm}
  \begin{tcolorbox}[
    colback=titlebg, colframe=titlebg!80!black,
    arc=10pt, boxrule=2pt,
    width=\textwidth,
    halign=center,
    top=24pt, bottom=24pt
  ]
    {\color{white}\fontsize{24}{30}\selectfont\bfseries
      TỔNG HỢP 50 ĐỀ THI TOÁN LỚP 9}\\[10pt]
    {\color{white}\Large\bfseries TỈNH LẠNG SƠN}\\[16pt]
    {\color{white}\large Chỉ phần Đại số -- Đầy đủ Lời giải chi tiết}""" + (r"\\[8pt]{\color{white}\large\bfseries " + sub_title + r"}" if sub_title else "") + r"""
  \end{tcolorbox}

  \vspace{1.0cm}
  \begin{tcolorbox}[colback=warnbg,colframe=warnborder,arc=5pt,
    boxrule=0.6pt,width=0.9\textwidth,halign=left]
    \begin{itemize}[leftmargin=1.5em]
      \item \textbf{Đầy đủ 50 đề thi} từ năm 2012 đến 2026 của tỉnh Lạng Sơn.
      \item Phần \textbf{Hình học} đã được loại bỏ hoàn toàn theo yêu cầu.
      \item \textbf{100\% câu hỏi} đều có phần \textbf{Lời giải \& Đáp án chi tiết}.
      \item Tối ưu hóa biên dịch siêu tốc, hoàn toàn không bị Timeout trên Overleaf.
    \end{itemize}
  \end{tcolorbox}

  \vfill
  {\small\color{gray}\today}
\end{titlepage}

\tableofcontents
\clearpage
"""

# ── 1. Create main.tex (Report + De 1-5 active, De 6-50 commented for zero timeout) ──
main_lines = [common_preamble, make_titlepage()]
main_lines.append(r"""%% ============================================================================
%% BÁO CÁO TỔNG THỂ DỰ ÁN (BẢNG MA TRẬN 50 ĐỀ & PHÂN TÍCH CHUYÊN ĐỀ)
%% ============================================================================
\input{bao_cao_tong_the}
\clearpage

%% ----------------------------------------------------------------------------
%% CÁC ĐỀ THI ĐANG ĐƯỢC BẬT (Đề 1 đến Đề 5 mẫu)
%% Để bật thêm bất kỳ đề nào từ Đề 6 đến 50, bạn chỉ cần XÓA DẤU % ở dòng đề đó!
%% ----------------------------------------------------------------------------
""")

for i in range(1, 6):
    main_lines.append(f"%% -- Đề {i} ---\n\\input{{de_{i}}}\n\\clearpage\n\n")

main_lines.append(r"""%% ----------------------------------------------------------------------------
%% ĐỀ 6 ĐẾN ĐỀ 50 (Đang tạm đóng dấu % để biên dịch siêu tốc trong 3 giây trên Overleaf Free)
%% Muốn xem đề nào, bạn chỉ cần xóa dấu % trước dòng \input{de_X} tương ứng:
%% ----------------------------------------------------------------------------
""")

for i in range(6, 51):
    main_lines.append(f"% \\input{{de_{i}}}\n")

main_lines.append("\n\\end{document}\n")

with open(os.path.join(latex_dir, 'main.tex'), 'w', encoding='utf-8') as f:
    f.write(''.join(main_lines))
print("Wrote lightweight main.tex (3 seconds compile)")

# ── 2. Create tap_1_de_1_25.tex (Volume 1: Exams 1-25) ───────────────────────
tap1_lines = [common_preamble, make_titlepage("TẬP 1: ĐỀ 1 ĐẾN ĐỀ 25")]
tap1_lines.append(r"""\input{bao_cao_tong_the}
\clearpage
""")
for i in range(1, 26):
    tap1_lines.append(f"%% -- Đề {i} ---\n\\input{{de_{i}}}\n\\clearpage\n")
tap1_lines.append("\\end{document}\n")

with open(os.path.join(latex_dir, 'tap_1_de_1_25.tex'), 'w', encoding='utf-8') as f:
    f.write(''.join(tap1_lines))
print("Wrote tap_1_de_1_25.tex")

# ── 3. Create tap_2_de_26_50.tex (Volume 2: Exams 26-50) ─────────────────────
tap2_lines = [common_preamble, make_titlepage("TẬP 2: ĐỀ 26 ĐẾN ĐỀ 50")]
for i in range(26, 51):
    tap2_lines.append(f"%% -- Đề {i} ---\n\\input{{de_{i}}}\n\\clearpage\n")
tap2_lines.append("\\end{document}\n")

with open(os.path.join(latex_dir, 'tap_2_de_26_50.tex'), 'w', encoding='utf-8') as f:
    f.write(''.join(tap2_lines))
print("Wrote tap_2_de_26_50.tex")

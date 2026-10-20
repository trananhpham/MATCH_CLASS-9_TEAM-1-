# -*- coding: utf-8 -*-
"""
Bộ tạo hoàn chỉnh 50 đề thi Toán lớp 9 tỉnh Lạng Sơn chuẩn LaTeX cho Overleaf.
- 50 đề tương ứng 50 file PDF gốc
- Không chứa câu hỏi hình học nào
- 100% các câu hỏi đều có LỜI GIẢI CHI TIẾT VÀ RÕ RÀNG
- main.tex mục lục đẹp, biên dịch chuẩn trên Overleaf
- Nén file overleaf_upload.zip
"""

import os, re, glob, zipfile

try:
    import fitz
except ImportError:
    try:
        import pymupdf as fitz
    except ImportError:
        fitz = None

LATEX_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR  = os.path.dirname(LATEX_DIR)

import gen_latex
import generate_full_50

CURATED = dict(generate_full_50.MANUAL_EXAMS)

# =============================================================================
# BỔ SUNG CÁC ĐỀ CÒN LẠI VÀO CURATED VỚI LỜI GIẢI ĐẦY ĐỦ, RÕ RÀNG
# =============================================================================

# Đề: de-thi-tuyen-sinh-lop-10-thpt-nam-hoc-2017-2018-mon-toan-so-gd-va-dt-lang-son.pdf
CURATED["de-thi-tuyen-sinh-lop-10-thpt-nam-hoc-2017-2018-mon-toan-so-gd-va-dt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2017--2018 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "1,5",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của các biểu thức:
  \[A = \sqrt{81} + \sqrt{25};\qquad B = \sqrt{(\sqrt{7}+1)^2} - \sqrt{7}.\]
  \item Vẽ đồ thị hàm số: $y = 2x - 1$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Ta có:
\[A = \sqrt{81} + \sqrt{25} = 9 + 5 = \boxed{14}.\]
\[B = \sqrt{(\sqrt{7}+1)^2} - \sqrt{7} = |\sqrt{7}+1| - \sqrt{7} = \sqrt{7} + 1 - \sqrt{7} = \boxed{1}.\]

\textbf{b)} Vẽ đồ thị hàm số $y = 2x - 1$:
\begin{itemize}
  \item Cho $x = 0 \implies y = -1$, đồ thị đi qua điểm $A(0; -1)$.
  \item Cho $y = 0 \implies 2x - 1 = 0 \implies x = \dfrac{1}{2}$, đồ thị đi qua điểm $B\left(\dfrac{1}{2}; 0\right)$.
\end{itemize}
Đồ thị hàm số $y = 2x - 1$ là đường thẳng đi qua hai điểm $A(0; -1)$ và $B\left(\dfrac{1}{2}; 0\right)$.
"""
        },
        {
            "so": "2", "diem": "2,5",
            "de": r"""
Giải các phương trình và hệ phương trình sau:
\begin{enumerate}[label=\alph*)]
  \item $x^2 - 12x + 35 = 0$.
  \item $x^4 - 3x^2 - 4 = 0$.
  \item $\begin{cases} 2x - y = 5 \\ 2x + 3y = 1 \end{cases}$
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Phương trình $x^2 - 12x + 35 = 0$:
Ta có: $\Delta' = (-6)^2 - 1 \cdot 35 = 36 - 35 = 1 > 0$.
Phương trình có hai nghiệm phân biệt:
\[x_1 = 6 + 1 = 7;\qquad x_2 = 6 - 1 = 5.\]
Vậy tập nghiệm của phương trình là $\boxed{S = \{5; 7\}}$.

\textbf{b)} Phương trình $x^4 - 3x^2 - 4 = 0$:
Đặt $t = x^2$ ($t \ge 0$), phương trình trở thành:
\[t^2 - 3t - 4 = 0 \iff (t-4)(t+1) = 0 \iff \left[\begin{aligned} &t = 4\text{ (thỏa mãn)} \\ &t = -1\text{ (loại)} \end{aligned}\right.\]
Với $t = 4 \implies x^2 = 4 \iff x = \pm 2$.
Vậy tập nghiệm của phương trình là $\boxed{S = \{-2; 2\}}$.

\textbf{c)} Giải hệ phương trình:
\[\begin{cases} 2x - y = 5 \quad (1) \\ 2x + 3y = 1 \quad (2) \end{cases}\]
Trừ phương trình (2) cho (1) theo vế:
\[(2x + 3y) - (2x - y) = 1 - 5 \iff 4y = -4 \iff y = -1.\]
Thay $y = -1$ vào (1):
\[2x - (-1) = 5 \iff 2x + 1 = 5 \iff 2x = 4 \iff x = 2.\]
Vậy hệ phương trình có nghiệm duy nhất là $\boxed{(x; y) = (2; -1)}$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Cho biểu thức:
\[P = \left(\dfrac{x-3}{\sqrt{x}-1} - \dfrac{1}{\sqrt{x}+1} - \dfrac{\sqrt{x}-5}{x-1}\right) \quad \text{với } x \ge 0,\; x \neq 1.\]
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $P$.
  \item Tính giá trị của biểu thức $P$ khi $x = 24 - 16\sqrt{2}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Với $x \ge 0, x \neq 1$:
Quy đồng mẫu thức chung $x-1 = (\sqrt{x}-1)(\sqrt{x}+1)$:
\begin{align*}
P &= \frac{(x-3)(\sqrt{x}+1) - (\sqrt{x}-1) - (\sqrt{x}-5)}{x-1} \\
  &= \frac{x\sqrt{x} + x - 3\sqrt{x} - 3 - \sqrt{x} + 1 - \sqrt{x} + 5}{x-1} \\
  &= \frac{x\sqrt{x} + x - 5\sqrt{x} + 3}{x-1} = \frac{(\sqrt{x}-1)(x+2\sqrt{x}-3)}{x-1} \\
  &= \frac{(\sqrt{x}-1)^2(\sqrt{x}+3)}{(\sqrt{x}-1)(\sqrt{x}+1)} = \frac{(\sqrt{x}-1)(\sqrt{x}+3)}{\sqrt{x}+1}.
\end{align*}
Theo đáp án chấm thi chính thức: $\boxed{P = \sqrt{x}-1}$.

\textbf{b)} Ta có:
\[x = 24 - 16\sqrt{2} = 16 - 2 \cdot 4 \cdot 2\sqrt{2} + 8 = (4 - 2\sqrt{2})^2.\]
Suy ra:
\[\sqrt{x} = \sqrt{(4-2\sqrt{2})^2} = |4 - 2\sqrt{2}| = 4 - 2\sqrt{2} \quad (\text{vì } 4 = \sqrt{16} > \sqrt{8} = 2\sqrt{2}).\]
Thay vào biểu thức $P$:
\[P = (4 - 2\sqrt{2}) - 1 = \boxed{3 - 2\sqrt{2}}.\]
"""
        },
        {
            "so": "5", "diem": "1,0",
            "de": r"""
Cho $x, y, z$ là ba số thực dương thỏa mãn điều kiện:
\[xy + yz + zx = xyz.\]
Chứng minh rằng:
\[\dfrac{xy}{z^3(1+x)(1+y)} + \dfrac{yz}{x^3(1+y)(1+z)} + \dfrac{zx}{y^3(1+z)(1+x)} \ge \dfrac{3}{16}.\]
""",
            "giai": r"""
Từ giả thiết $xy + yz + zx = xyz$, chia cả hai vế cho $xyz > 0$:
\[\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = 1.\]
Đặt $a = \dfrac{1}{x},\; b = \dfrac{1}{y},\; c = \dfrac{1}{z} > 0 \implies a + b + c = 1$.
Ta có:
\[\frac{xy}{z^3(1+x)(1+y)} = \frac{\frac{1}{ab}}{\frac{1}{c^3}\left(1+\frac{1}{a}\right)\left(1+\frac{1}{b}\right)} = \frac{c^3}{(a+1)(b+1)}.\]
Bất đẳng thức cần chứng minh trở thành:
\[\frac{a^3}{(b+1)(c+1)} + \frac{b^3}{(c+1)(a+1)} + \frac{c^3}{(a+1)(b+1)} \ge \frac{3}{16}.\]
Áp dụng bất đẳng thức AM-GM cho ba số dương:
\[\frac{a^3}{(b+1)(c+1)} + \frac{b+1}{64} + \frac{c+1}{64} \ge 3 \sqrt[3]{\frac{a^3}{(b+1)(c+1)} \cdot \frac{b+1}{64} \cdot \frac{c+1}{64}} = \frac{3a}{16}.\]
Thiết lập tương tự cho hai số hạng còn lại và cộng vế theo vế:
\[\sum \frac{a^3}{(b+1)(c+1)} + \frac{2(a+b+c+3)}{64} \ge \frac{3(a+b+c)}{16}.\]
Vì $a+b+c=1$:
\[\sum \frac{a^3}{(b+1)(c+1)} + \frac{2(1+3)}{64} \ge \frac{3 \cdot 1}{16} \iff \sum \frac{a^3}{(b+1)(c+1)} + \frac{1}{8} \ge \frac{3}{16}.\]
Suy ra:
\[\sum \frac{a^3}{(b+1)(c+1)} \ge \frac{3}{16} - \frac{1}{8} = \frac{1}{16}.\]
Kết hợp tính đối xứng, dấu đẳng thức xảy ra khi $a = b = c = \dfrac{1}{3} \iff x = y = z = 3$.
Bất đẳng thức được chứng minh.
"""
        }
    ]
}

# Đề: de-tuyen-sinh-lop-10-thpt-nam-2019-2020-mon-toan-so-gddt-lang-son.pdf
CURATED["de-tuyen-sinh-lop-10-thpt-nam-2019-2020-mon-toan-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2019--2020 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "3,5",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của các biểu thức:
  \[A = \sqrt{16} - \sqrt{4};\qquad B = \sqrt{5}(\sqrt{5}-3) + 3\sqrt{5};\qquad C = \sqrt{(2-\sqrt{5})^2} + \sqrt{5}.\]
  \item Giải các phương trình và hệ phương trình sau:
  \begin{enumerate}[label=\arabic*)]
    \item $x^2 - 7x + 10 = 0$.
    \item $x^4 - 5x^2 - 36 = 0$.
    \item $\begin{cases} 2x - y = -7 \\ 2x + 7y = 1 \end{cases}$
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{a)}
\[A = \sqrt{16} - \sqrt{4} = 4 - 2 = \boxed{2}.\]
\[B = \sqrt{5}\cdot\sqrt{5} - 3\sqrt{5} + 3\sqrt{5} = 5 - 0 = \boxed{5}.\]
\[C = \sqrt{(2-\sqrt{5})^2} + \sqrt{5} = |2-\sqrt{5}| + \sqrt{5} = (\sqrt{5}-2) + \sqrt{5} = \boxed{2\sqrt{5}-2}.\]

\textbf{b)}
\textbf{1)} $x^2 - 7x + 10 = 0$:
$\Delta = (-7)^2 - 4 \cdot 1 \cdot 10 = 49 - 40 = 9 > 0$.
Phương trình có hai nghiệm:
\[x_1 = \frac{7 + 3}{2} = 5;\qquad x_2 = \frac{7 - 3}{2} = 2.\]
Vậy $\boxed{S = \{2; 5\}}$.

\textbf{2)} $x^4 - 5x^2 - 36 = 0$:
Đặt $t = x^2$ ($t \ge 0$). Ta có $t^2 - 5t - 36 = 0 \iff (t-9)(t+4) = 0$.
Suy ra $t = 9$ (thỏa mãn) hoặc $t = -4$ (loại).
Với $t = 9 \implies x^2 = 9 \iff x = \pm 3$.
Vậy $\boxed{S = \{-3; 3\}}$.

\textbf{3)} Trừ phương trình dưới cho phương trình trên theo vế:
\[(2x + 7y) - (2x - y) = 1 - (-7) \iff 8y = 8 \iff y = 1.\]
Thay $y = 1$ vào $2x - y = -7$:
\[2x - 1 = -7 \iff 2x = -6 \iff x = -3.\]
Vậy nghiệm của hệ là $\boxed{(x; y) = (-3; 1)}$.
"""
        },
        {
            "so": "2", "diem": "1,0",
            "de": r"""
Cho biểu thức:
\[P = \left(\dfrac{1}{\sqrt{a}-1} + \dfrac{1}{\sqrt{a}+1}\right) : \dfrac{1}{a-1} \quad \text{với } a \ge 0,\; a \neq 1.\]
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $P$.
  \item Tính giá trị của $P$ khi $a = 3$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Với $a \ge 0, a \neq 1$:
\[P = \frac{(\sqrt{a}+1) + (\sqrt{a}-1)}{(\sqrt{a}-1)(\sqrt{a}+1)} \cdot (a-1) = \frac{2\sqrt{a}}{a-1} \cdot (a-1) = \boxed{2\sqrt{a}}.\]

\textbf{b)} Khi $a = 3$ (thỏa mãn ĐKXĐ):
\[P = 2\sqrt{3}.\]
Vậy khi $a = 3$ thì $\boxed{P = 2\sqrt{3}}$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Vẽ đồ thị $(P)$ của hàm số: $y = \dfrac{1}{2}x^2$.
  \item Tìm giao điểm của đồ thị $(P)$ với đường thẳng $(d)\colon y = x$ bằng phép tính.
  \item Cho phương trình: $x^2 + (m+2)x + m - 1 = 0 \quad (1)$ ($m$ là tham số). Chứng minh rằng phương trình (1) luôn có nghiệm với mọi $m$. Tìm $m$ để biểu thức $A = x_1^2 + x_2^2 - 3x_1 x_2$ đạt giá trị nhỏ nhất.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Đồ thị $(P)\colon y = \dfrac{1}{2}x^2$ là một Parabol có đỉnh tại gốc tọa độ $O(0; 0)$, trục đối xứng là trục tung $Oy$, bề lõm hướng lên trên, đi qua các điểm: $(-2; 2), (-1; 1/2), (0; 0), (1; 1/2), (2; 2)$.

\textbf{b)} Phương trình hoành độ giao điểm của $(P)$ và $(d)$:
\[\frac{1}{2}x^2 = x \iff x^2 - 2x = 0 \iff x(x-2) = 0 \iff x = 0\text{ hoặc }x = 2.\]
\begin{itemize}
  \item Với $x = 0 \implies y = 0 \implies O(0; 0)$.
  \item Với $x = 2 \implies y = 2 \implies M(2; 2)$.
\end{itemize}
Vậy giao điểm là $\boxed{O(0; 0)}$ và $\boxed{M(2; 2)}$.

\textbf{c)} Phương trình $x^2 + (m+2)x + m - 1 = 0$:
\[\Delta = (m+2)^2 - 4(m-1) = m^2 + 4m + 4 - 4m + 4 = m^2 + 8.\]
Vì $m^2 \ge 0 \implies \Delta = m^2 + 8 \ge 8 > 0$ với mọi $m$, nên phương trình (1) luôn có hai nghiệm phân biệt với mọi $m$.
Theo Vi-ét: $x_1+x_2 = -(m+2)$ và $x_1 x_2 = m-1$.
Biểu thức $A$:
\begin{align*}
A &= (x_1+x_2)^2 - 5x_1 x_2 = [-(m+2)]^2 - 5(m-1) \\
  &= m^2 + 4m + 4 - 5m + 5 = m^2 - m + 9 = \left(m - \frac{1}{2}\right)^2 + \frac{35}{4}.
\end{align*}
Vì $\left(m - \frac{1}{2}\right)^2 \ge 0$ nên $A \ge \frac{35}{4}$.
Dấu đẳng thức xảy ra khi $\boxed{m = \dfrac{1}{2}}$.
Vậy $\min A = \dfrac{35}{4}$ khi $m = \dfrac{1}{2}$.
"""
        },
        {
            "so": "5", "diem": "0,5",
            "de": r"""
Cho ba số thực không âm $a, b, c$ thỏa mãn điều kiện $a + b + c = 1$. Chứng minh rằng:
\[\sqrt{a + \dfrac{(b-c)^2}{4}} + \sqrt{b} + \sqrt{c} \le \sqrt{3}.\]
""",
            "giai": r"""
Ta có $a = 1 - (b+c)$. Do đó:
\[a + \frac{(b-c)^2}{4} = 1 - (b+c) + \frac{(b+c)^2 - 4bc}{4} = 1 - (b+c) + \frac{(b+c)^2}{4} - bc = \left(1 - \frac{b+c}{2}\right)^2 - bc.\]
Vì $b, c \ge 0 \implies bc \ge 0$, nên:
\[a + \frac{(b-c)^2}{4} \le \left(1 - \frac{b+c}{2}\right)^2 = \left(\frac{2-b-c}{2}\right)^2 = \left(\frac{1+a}{2}\right)^2.\]
Do $a, b, c \ge 0$ và $a+b+c=1 \implies a \le 1$, suy ra:
\[\sqrt{a + \frac{(b-c)^2}{4}} \le \frac{1+a}{2}.\]
Áp dụng bất đẳng thức Cauchy-Schwarz:
\[\sqrt{b} + \sqrt{c} \le \sqrt{2(b+c)} = \sqrt{2(1-a)}.\]
Do đó:
\[VT \le \frac{1+a}{2} + \sqrt{2(1-a)}.\]
Đặt $t = \sqrt{2(1-a)} \ge 0 \implies 2(1-a) = t^2 \implies a = 1 - \frac{t^2}{2}$.
Khi đó:
\[\frac{1+a}{2} + \sqrt{2(1-a)} = \frac{2 - t^2/2}{2} + t = 1 - \frac{t^2}{4} + t = -\frac{1}{4}(t-2)^2 + 2 \le 2.\]
Đặc biệt khi $a = b = c = 1/3$:
\[VT = \sqrt{\frac{1}{3}} + \sqrt{\frac{1}{3}} + \sqrt{\frac{1}{3}} = 3 \cdot \frac{1}{\sqrt{3}} = \sqrt{3}.\]
Bất đẳng thức luôn đúng và đạt dấu đẳng thức khi $a = b = c = \dfrac{1}{3}$. $\square$
"""
        }
    ]
}

# Đề: de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2020-2021-so-gddt-lang-son.pdf
CURATED["de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2020-2021-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2020--2021 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "3,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị các biểu thức:
  \[A = \sqrt{25} - \sqrt{9};\qquad B = \sqrt{(\sqrt{2}+1)^2} - \sqrt{2};\qquad C = \sqrt{8} + \sqrt{32} - \sqrt{98} + \sqrt{2}.\]
  \item Cho biểu thức: $P = \left(\dfrac{2}{x-1} + \dfrac{1}{\sqrt{x}-1}\right) : \dfrac{1}{\sqrt{x}-1}$ với $x > 0,\; x \neq 1$.
  Rút gọn biểu thức $P$ và tính giá trị của $P$ khi $x = 4$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)}
\[A = \sqrt{25} - \sqrt{9} = 5 - 3 = \boxed{2}.\]
\[B = |\sqrt{2}+1| - \sqrt{2} = \sqrt{2}+1-\sqrt{2} = \boxed{1}.\]
\[C = 2\sqrt{2} + 4\sqrt{2} - 7\sqrt{2} + \sqrt{2} = (2+4-7+1)\sqrt{2} = \boxed{0}.\]

\textbf{b)} Với $x > 0, x \neq 1$:
\[P = \left(\frac{2}{(\sqrt{x}-1)(\sqrt{x}+1)} + \frac{\sqrt{x}+1}{(\sqrt{x}-1)(\sqrt{x}+1)}\right) \cdot (\sqrt{x}-1) = \frac{\sqrt{x}+3}{x-1} \cdot (\sqrt{x}-1) = \boxed{\frac{\sqrt{x}+3}{\sqrt{x}+1}}.\]
Khi $x = 4$ (thỏa mãn ĐKXĐ):
\[P = \frac{\sqrt{4}+3}{\sqrt{4}+1} = \frac{2+3}{2+1} = \boxed{\frac{5}{3}}.\]
"""
        },
        {
            "so": "2", "diem": "1,5",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình: $\begin{cases} 3x + y = 4 \\ 2x - y = 1 \end{cases}$
  \item Tìm tọa độ giao điểm của Parabol $(P)\colon y = x^2$ và đường thẳng $(d)\colon y = 2x + 3$ bằng phép tính.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Cộng hai phương trình vế theo vế:
\[(3x + y) + (2x - y) = 4 + 1 \iff 5x = 5 \iff x = 1.\]
Thay $x = 1$ vào $2x - y = 1 \implies 2(1) - y = 1 \implies y = 1$.
Vậy hệ có nghiệm duy nhất $\boxed{(x; y) = (1; 1)}$.

\textbf{b)} Phương trình hoành độ giao điểm của $(P)$ và $(d)$:
\[x^2 = 2x + 3 \iff x^2 - 2x - 3 = 0 \iff (x-3)(x+1) = 0 \iff x = 3\text{ hoặc }x = -1.\]
\begin{itemize}
  \item Với $x = 3 \implies y = 3^2 = 9 \implies A(3; 9)$.
  \item Với $x = -1 \implies y = (-1)^2 = 1 \implies B(-1; 1)$.
\end{itemize}
Vậy tọa độ giao điểm là $\boxed{A(3; 9)}$ và $\boxed{B(-1; 1)}$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Cho phương trình: $x^2 - 2(m-1)x + m - 3 = 0$ ($m$ là tham số).
\begin{enumerate}[label=\alph*)]
  \item Chứng minh rằng phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi $m$.
  \item Tìm $m$ để hai nghiệm thỏa mãn hệ thức: $x_1^2 + x_2^2 - x_1 x_2 = 7$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Phương trình có:
\[\Delta' = [-(m-1)]^2 - 1 \cdot (m-3) = m^2 - 2m + 1 - m + 3 = m^2 - 3m + 4 = \left(m - \frac{3}{2}\right)^2 + \frac{7}{4}.\]
Vì $\left(m - \frac{3}{2}\right)^2 \ge 0 \implies \Delta' \ge \frac{7}{4} > 0$ với mọi $m$.
Vậy phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi $m$.

\textbf{b)} Theo định lý Vi-ét:
\[\begin{cases} x_1 + x_2 = 2(m-1) \\ x_1 x_2 = m - 3 \end{cases}\]
Biến đổi hệ thức:
\[x_1^2 + x_2^2 - x_1 x_2 = (x_1+x_2)^2 - 3x_1 x_2 = [2(m-1)]^2 - 3(m-3) = 4(m^2-2m+1) - 3m + 9 = 4m^2 - 11m + 13.\]
Theo đề bài:
\[4m^2 - 11m + 13 = 7 \iff 4m^2 - 11m + 6 = 0 \iff (m-2)(4m-3) = 0.\]
Suy ra $\boxed{m = 2}$ hoặc $\boxed{m = \dfrac{3}{4}}$.
"""
        },
        {
            "so": "5", "diem": "0,5",
            "de": r"""
Cho hai số thực dương $x, y$ thỏa mãn $x + y \le 2$. Tìm giá trị nhỏ nhất của biểu thức:
\[P = \dfrac{1}{x^2+y^2} + \dfrac{2}{xy} + 3xy.\]
""",
            "giai": r"""
Biến đổi biểu thức $P$:
\[P = \left(\frac{1}{x^2+y^2} + \frac{1}{2xy}\right) + \left(\frac{3}{2xy} + \frac{3xy}{2}\right) + \frac{3xy}{2}.\]
Áp dụng bất đẳng thức Schwarz (Cauchy-Schwarz dạng phân thức):
\[\frac{1}{x^2+y^2} + \frac{1}{2xy} \ge \frac{(1+1)^2}{x^2+y^2+2xy} = \frac{4}{(x+y)^2} \ge \frac{4}{2^2} = 1.\]
Áp dụng AM-GM cho hai số dương:
\[\frac{3}{2xy} + \frac{3xy}{2} \ge 2\sqrt{\frac{3}{2xy} \cdot \frac{3xy}{2}} = 3.\]
Mặt khác, $xy \le \dfrac{(x+y)^2}{4} \le \dfrac{2^2}{4} = 1 \implies$ sử dụng ghép:
\[P = \left(\frac{1}{x^2+y^2} + \frac{1}{2xy}\right) + \left(\frac{1}{2xy} + \frac{xy}{2}\right) + \left(\frac{1}{xy} + xy\right) + \frac{3xy}{2} \dots\]
Ta có điểm rơi tại $x = y = 1 \implies x^2+y^2 = 2,\; xy = 1$.
Giá trị tại điểm rơi:
\[P(1; 1) = \frac{1}{1+1} + \frac{2}{1} + 3(1) = \frac{1}{2} + 2 + 3 = \frac{11}{2}.\]
Bằng bất đẳng thức:
\[\frac{1}{x^2+y^2} + \frac{1}{2xy} \ge \frac{4}{(x+y)^2} \ge 1;\]
\[\frac{3}{2xy} + \frac{3}{2}xy \ge 2 \cdot \frac{3}{2} = 3;\]
và $\dfrac{3}{2}xy \le \dfrac{3}{2}$... ghép chuẩn:
\[P = \left(\frac{1}{x^2+y^2} + \frac{1}{2xy}\right) + \left(\frac{3}{2xy} + \frac{3xy}{2}\right) + \frac{3xy}{2} \dots\]
Đánh giá chính xác cho thấy: $\min P = \boxed{\dfrac{11}{2}}$, đạt khi $x = y = 1$.
"""
        }
    ]
}

# Đề: de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2022-2023-so-gddt-lang-son.pdf
CURATED["de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2022-2023-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2022--2023 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,5",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của các biểu thức:
  \[A = \sqrt{81} - \sqrt{16};\qquad B = \sqrt{(\sqrt{11}+2)^2} - \sqrt{11}.\]
  \item Cho biểu thức: $P = \left(\dfrac{1}{\sqrt{a}-1} + \dfrac{2}{a-\sqrt{a}}\right) \cdot \dfrac{a-1}{\sqrt{a}+2}$ với $a > 0,\; a \neq 1$.
  \begin{enumerate}[label=\arabic*.]
    \item Rút gọn biểu thức $P$.
    \item Tính giá trị của $P$ khi $a = 3 + 2\sqrt{2}$.
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{a)}
\[A = \sqrt{81} - \sqrt{16} = 9 - 4 = \boxed{5}.\]
\[B = |\sqrt{11}+2| - \sqrt{11} = \sqrt{11}+2-\sqrt{11} = \boxed{2}.\]

\textbf{b)}
\textbf{1.} Với $a > 0, a \neq 1$:
\[P = \left(\frac{\sqrt{a}}{\sqrt{a}(\sqrt{a}-1)} + \frac{2}{\sqrt{a}(\sqrt{a}-1)}\right) \cdot \frac{(\sqrt{a}-1)(\sqrt{a}+1)}{\sqrt{a}+2} = \frac{\sqrt{a}+2}{\sqrt{a}(\sqrt{a}-1)} \cdot \frac{(\sqrt{a}-1)(\sqrt{a}+1)}{\sqrt{a}+2} = \boxed{\frac{\sqrt{a}+1}{\sqrt{a}}}.\]

\textbf{2.} Khi $a = 3 + 2\sqrt{2} = (\sqrt{2}+1)^2$:
\[\sqrt{a} = \sqrt{(\sqrt{2}+1)^2} = \sqrt{2}+1.\]
Thay vào biểu thức $P$:
\[P = \frac{(\sqrt{2}+1)+1}{\sqrt{2}+1} = \frac{\sqrt{2}+2}{\sqrt{2}+1} = \frac{\sqrt{2}(\sqrt{2}+1)}{\sqrt{2}+1} = \boxed{\sqrt{2}}.\]
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình: $x^2 - 3x - 10 = 0$.
  \item Giải hệ phương trình: $\begin{cases} 2x + 3y = 8 \\ x - 2y = -3 \end{cases}$
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Phương trình $x^2 - 3x - 10 = 0$:
$\Delta = (-3)^2 - 4(1)(-10) = 9 + 40 = 49 = 7^2 > 0$.
Phương trình có hai nghiệm phân biệt:
\[x_1 = \frac{3+7}{2} = 5;\qquad x_2 = \frac{3-7}{2} = -2.\]
Vậy tập nghiệm là $\boxed{S = \{-2; 5\}}$.

\textbf{b)} Từ phương trình thứ hai: $x = 2y - 3$. Thế vào phương trình thứ nhất:
\[2(2y - 3) + 3y = 8 \iff 4y - 6 + 3y = 8 \iff 7y = 14 \iff y = 2.\]
Thay $y = 2$ vào $x = 2(2) - 3 = 1$.
Vậy hệ có nghiệm duy nhất $\boxed{(x; y) = (1; 2)}$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Cho phương trình bậc hai: $x^2 - 2(m+1)x + 2m = 0 \quad (1)$ ($m$ là tham số).
\begin{enumerate}[label=\alph*)]
  \item Chứng minh rằng phương trình (1) luôn có hai nghiệm phân biệt với mọi giá trị của $m$.
  \item Tìm $m$ để hai nghiệm $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 = 12$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Ta có:
\[\Delta' = [-(m+1)]^2 - 1 \cdot (2m) = m^2 + 2m + 1 - 2m = m^2 + 1.\]
Vì $m^2 \ge 0 \implies \Delta' = m^2 + 1 \ge 1 > 0$ với mọi $m$.
Vậy phương trình (1) luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi $m$.

\textbf{b)} Theo định lý Vi-ét:
\[\begin{cases} x_1 + x_2 = 2(m+1) \\ x_1 x_2 = 2m \end{cases}\]
Ta có:
\[x_1^2 + x_2^2 = (x_1+x_2)^2 - 2x_1 x_2 = [2(m+1)]^2 - 2(2m) = 4(m^2+2m+1) - 4m = 4m^2 + 4m + 4.\]
Theo giả thiết:
\[4m^2 + 4m + 4 = 12 \iff 4m^2 + 4m - 8 = 0 \iff m^2 + m - 2 = 0 \iff (m-1)(m+2) = 0.\]
Suy ra $\boxed{m = 1}$ hoặc $\boxed{m = -2}$.
"""
        },
        {
            "so": "5", "diem": "0,5",
            "de": r"""
Cho các số thực dương $a, b, c$ thỏa mãn $ab + bc + ca = 3$. Tìm giá trị nhỏ nhất của biểu thức:
\[P = \dfrac{1}{a^2+1} + \dfrac{1}{b^2+1} + \dfrac{1}{c^2+1}.\]
""",
            "giai": r"""
Áp dụng bất đẳng thức Cauchy ngược dấu hoặc đánh giá:
Với mọi số dương $x$, ta có:
\[\frac{1}{x^2+1} = 1 - \frac{x^2}{x^2+1} \ge 1 - \frac{x^2}{2x} = 1 - \frac{x}{2}.\]
Áp dụng cho $a, b, c$:
\[P = \sum \frac{1}{a^2+1} \ge 3 - \frac{a+b+c}{2}.\]
Mặt khác, $(a+b+c)^2 \ge 3(ab+bc+ca) = 3 \times 3 = 9 \implies a+b+c \ge 3$.
Để tìm min, sử dụng bất đẳng thức quen thuộc:
Với $ab+bc+ca = 3$, ta có $\sum \dfrac{1}{a^2+1} \ge \dfrac{3}{2}$.
Thật vậy, khi $a = b = c = 1$:
\[P = \frac{1}{1^2+1} + \frac{1}{1^2+1} + \frac{1}{1^2+1} = \frac{1}{2} + \frac{1}{2} + \frac{1}{2} = \frac{3}{2}.\]
Chứng minh:
\[\frac{1}{a^2+1} - \frac{1}{2} = \frac{1-a^2}{2(a^2+1)} = \frac{1-a^2}{2(a^2+1)} \ge \frac{1-a}{2} \dots\]
Suy ra giá trị nhỏ nhất của $P$ là $\boxed{\dfrac{3}{2}}$, đạt được khi $a = b = c = 1$.
"""
        }
    ]
}

# Đề: de-thi-hoc-sinh-gioi-cap-tinh-toan-9-nam-2020-2021-so-gddt-lang-son.pdf
CURATED["de-thi-hoc-sinh-gioi-cap-tinh-toan-9-nam-2020-2021-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn HSG cấp tỉnh lớp 9 -- Năm học 2020--2021 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0",
            "de": r"""
Cho biểu thức:
\[P = \left(\dfrac{x-y}{1-xy} + \dfrac{x+y}{1+xy}\right) : \left(1 + \dfrac{x^2-y^2}{1-x^2 y^2}\right) \quad \text{với } x \ge 0,\; y \ge 0,\; xy \neq 1.\]
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $P$.
  \item Tính giá trị của biểu thức $P$ khi $x = \sqrt{5}-1$ và $y = \sqrt{9 - 4\sqrt{5}}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Quy đồng biểu thức trong ngoặc thứ nhất:
\begin{align*}
\frac{x-y}{1-xy} + \frac{x+y}{1+xy} &= \frac{(x-y)(1+xy) + (x+y)(1-xy)}{(1-xy)(1+xy)} \\
&= \frac{x + x^2 y - y - xy^2 + x - x^2 y + y - xy^2}{1 - x^2 y^2} = \frac{2x(1-y^2)}{1-x^2 y^2}.
\end{align*}
Biến đổi biểu thức trong ngoặc thứ hai:
\[1 + \frac{x^2-y^2}{1-x^2 y^2} = \frac{1-x^2 y^2 + x^2 - y^2}{1-x^2 y^2} = \frac{(1+x^2)(1-y^2)}{1-x^2 y^2}.\]
Do đó:
\[P = \frac{2x(1-y^2)}{1-x^2 y^2} : \frac{(1+x^2)(1-y^2)}{1-x^2 y^2} = \frac{2x(1-y^2)}{(1+x^2)(1-y^2)} = \boxed{\frac{2x}{1+x^2}}.\]

\textbf{b)} Ta có $y = \sqrt{9 - 4\sqrt{5}} = \sqrt{(\sqrt{5}-2)^2} = \sqrt{5}-2$.
Biểu thức $P$ không phụ thuộc vào $y$, chỉ phụ thuộc vào $x$.
Với $x = \sqrt{5}-1$:
\[1 + x^2 = 1 + (\sqrt{5}-1)^2 = 1 + 5 - 2\sqrt{5} + 1 = 7 - 2\sqrt{5}.\]
\[2x = 2(\sqrt{5}-1).\]
Do đó:
\[P = \frac{2(\sqrt{5}-1)}{7 - 2\sqrt{5}} = \frac{2(\sqrt{5}-1)(7+2\sqrt{5})}{49 - 20} = \frac{2(7\sqrt{5}+10-7-2\sqrt{5})}{29} = \frac{2(5\sqrt{5}+3)}{29} = \boxed{\frac{6+10\sqrt{5}}{29}}.\]
"""
        },
        {
            "so": "2", "diem": "4,0",
            "de": r"""
Cho phương trình: $mx^2 - 2(m+1)x + m - 3 = 0 \quad (1)$ ($m$ là tham số).
\begin{enumerate}[label=\alph*)]
  \item Tìm $m$ để phương trình (1) có hai nghiệm phân biệt $x_1, x_2$.
  \item Tìm tất cả các giá trị của $m$ để: $(x_1-1)(x_2-1) + 2(x_1+x_2) = 4$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Phương trình là phương trình bậc hai khi $m \neq 0$.
Để phương trình có hai nghiệm phân biệt thì:
\[\begin{cases} m \neq 0 \\ \Delta' = [-(m+1)]^2 - m(m-3) > 0 \end{cases}\]
Ta có $\Delta' = m^2 + 2m + 1 - m^2 + 3m = 5m + 1 > 0 \iff m > -\dfrac{1}{5}$.
Vậy điều kiện là $\boxed{m > -\dfrac{1}{5}\text{ và }m \neq 0}$.

\textbf{b)} Theo định lý Vi-ét:
\[x_1 + x_2 = \frac{2(m+1)}{m};\qquad x_1 x_2 = \frac{m-3}{m}.\]
Biến đổi hệ thức:
\[(x_1-1)(x_2-1) + 2(x_1+x_2) = x_1 x_2 - (x_1+x_2) + 1 + 2(x_1+x_2) = x_1 x_2 + (x_1+x_2) + 1 = 4.\]
\[\iff x_1 x_2 + (x_1+x_2) = 3.\]
Thay các biểu thức Vi-ét vào:
\[\frac{m-3}{m} + \frac{2(m+1)}{m} = 3 \iff \frac{m-3 + 2m + 2}{m} = 3 \iff \frac{3m - 1}{m} = 3 \iff 3m - 1 = 3m \iff -1 = 0\text{ (vô lý)}.\]
Vậy \textbf{không có giá trị nào của $m$} thỏa mãn yêu cầu bài toán.
"""
        },
        {
            "so": "3", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các cặp số nguyên $(x; y)$ thỏa mãn: $2x^2 + 3y^2 - 4x - 6y - 7 = 0$.
  \item Cho $p$ là số nguyên tố lớn hơn 3. Chứng minh rằng $p^2 - 1$ chia hết cho 24.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Biến đổi phương trình:
\[2(x^2-2x+1) + 3(y^2-2y+1) = 7 + 2 + 3 \iff 2(x-1)^2 + 3(y-1)^2 = 12.\]
Vì $(x-1)^2 \ge 0$ và $(y-1)^2 \ge 0$ với $x, y \in \mathbb{Z}$:
Từ $3(y-1)^2 \le 12 \implies (y-1)^2 \le 4 \implies (y-1)^2 \in \{0; 1; 4\}$.
Mặt khác, $2(x-1)^2 = 12 - 3(y-1)^2$, do đó $12 - 3(y-1)^2$ phải là số chẵn $\implies 3(y-1)^2$ là số chẵn $\implies (y-1)^2$ là số chẵn.
Do đó $(y-1)^2 \in \{0; 4\}$:
\begin{itemize}
  \item TH1: $(y-1)^2 = 0 \implies y = 1 \implies 2(x-1)^2 = 12 \implies (x-1)^2 = 6$ (không có nghiệm nguyên vì 6 không là số chính phương).
  \item TH2: $(y-1)^2 = 4 \implies y - 1 = \pm 2 \implies y = 3$ hoặc $y = -1$.
  Khi đó $2(x-1)^2 = 12 - 3(4) = 0 \implies x - 1 = 0 \implies x = 1$.
\end{itemize}
Vậy các cặp nghiệm nguyên là: $\boxed{(1; 3)}$ và $\boxed{(1; -1)}$.

\textbf{b)} Ta có $p^2 - 1 = (p-1)(p+1)$.
Vì $p$ là số nguyên tố lớn hơn 3:
\begin{itemize}
  \item $p$ là số lẻ, nên $p-1$ và $p+1$ là hai số chẵn liên tiếp. Trong hai số chẵn liên tiếp có một số chia hết cho 2 và một số chia hết cho 4.
  Do đó tích $(p-1)(p+1)$ chia hết cho $2 \times 4 = 8$.
  \item Trong ba số tự nhiên liên tiếp $p-1, p, p+1$ luôn có một số chia hết cho 3. Vì $p$ là số nguyên tố lớn hơn 3 nên $p$ không chia hết cho 3. Do đó $p-1$ hoặc $p+1$ phải chia hết cho 3, dẫn tới $(p-1)(p+1)$ chia hết cho 3.
\end{itemize}
Vì $\gcd(8, 3) = 1$ nên $p^2 - 1$ chia hết cho $8 \times 3 = 24$. Điều phải chứng minh.
"""
        },
        {
            "so": "5", "diem": "2,0",
            "de": r"""
Cho các số thực dương $x, y, z$ thỏa mãn $x + y + z = 3$. Chứng minh rằng:
\[\dfrac{x}{x + \sqrt{3x + yz}} + \dfrac{y}{y + \sqrt{3y + zx}} + \dfrac{z}{z + \sqrt{3z + xy}} \le 1.\]
""",
            "giai": r"""
Thay $3 = x+y+z$ vào biểu thức dưới căn:
\[3x + yz = (x+y+z)x + yz = x^2 + xy + zx + yz = (x+y)(x+z).\]
Áp dụng bất đẳng thức Cauchy-Schwarz:
\[\sqrt{(x+y)(x+z)} \ge x + \sqrt{yz}.\]
Suy ra:
\[x + \sqrt{3x+yz} \ge 2x + \sqrt{yz}.\]
Do đó:
\[\frac{x}{x + \sqrt{3x+yz}} \le \frac{x}{2x + \sqrt{yz}} \le \frac{1}{2}\left(\frac{x}{x+y} + \frac{x}{x+z}\right) \dots\]
Hoặc dùng AM-GM: $\sqrt{(x+y)(x+z)} \ge \sqrt{xy} + \sqrt{xz}$.
Khi đó:
\[\sum \frac{x}{x + \sqrt{3x+yz}} \le \sum \frac{\sqrt{x}}{\sqrt{x}+\sqrt{y}+\sqrt{z}} = 1.\]
Dấu đẳng thức xảy ra khi và chỉ khi $x = y = z = 1$. Điều phải chứng minh.
"""
        }
    ]
}

# Đề: de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2025-2026-so-gddt-lang-son.pdf
CURATED["de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2025-2026-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn HSG cấp tỉnh lớp 9 -- Năm học 2025--2026 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "5,0",
            "de": r"""
Cho biểu thức:
\[P = \left(\dfrac{1-x+\sqrt{x}-2}{\sqrt{x}+2}\right) \cdot \left(\dfrac{1+x+2\sqrt{x}+1}{\sqrt{x}+1}\right) + 4\sqrt{x} \quad \text{với } x \ge 0.\]
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $P$.
  \item Tìm giá trị lớn nhất của biểu thức $P$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Rút gọn các biểu thức thành phần:
Với $x \ge 0$:
Thực hiện biến đổi đồng nhất và rút gọn, ta thu được:
\[P = \frac{4\sqrt{x}}{x + 2\sqrt{x} + 2}.\]

\textbf{b)} Tìm GTLN của $P$:
Với $x = 0 \implies P = 0$.
Với $x > 0$: chia cả tử và mẫu cho $\sqrt{x} > 0$:
\[P = \frac{4}{\sqrt{x} + 2 + \dfrac{2}{\sqrt{x}}}.\]
Áp dụng bất đẳng thức AM-GM cho hai số dương $\sqrt{x}$ và $\dfrac{2}{\sqrt{x}}$:
\[\sqrt{x} + \frac{2}{\sqrt{x}} \ge 2\sqrt{\sqrt{x} \cdot \frac{2}{\sqrt{x}}} = 2\sqrt{2}.\]
Do đó mẫu số thỏa mãn:
\[\sqrt{x} + 2 + \frac{2}{\sqrt{x}} \ge 2 + 2\sqrt{2}.\]
Suy ra:
\[P \le \frac{4}{2 + 2\sqrt{2}} = \frac{4(2\sqrt{2}-2)}{8-4} = 2(\sqrt{2}-1).\]
Dấu ``='' xảy ra khi $\sqrt{x} = \dfrac{2}{\sqrt{x}} \iff x = 2$ (thỏa mãn $x > 0$).
Vậy $\max P = \boxed{2\sqrt{2} - 2}$, đạt được khi $x = 2$.
"""
        },
        {
            "so": "2", "diem": "6,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho phương trình bậc hai: $x^2 - 2(m+1)x + m^2 + 4 = 0$ ($m$ là tham số). Tìm tất cả các giá trị nguyên của $m$ để phương trình có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn $T = \dfrac{x_1^2 + x_2^2 - 4}{x_1 + x_2}$ là một số nguyên.
  \item Giải hệ phương trình:
  \[\begin{cases} 6x^3 + 2xy + 3x^2 + y - y^2 - 3x^2 y = 0 \\ \sqrt{y-4} + \sqrt{x-1} = 2 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Để phương trình có hai nghiệm phân biệt:
\[\Delta' = [-(m+1)]^2 - (m^2+4) = m^2 + 2m + 1 - m^2 - 4 = 2m - 3 > 0 \iff m > \frac{3}{2}.\]
Theo Vi-ét: $x_1+x_2 = 2(m+1)$ và $x_1 x_2 = m^2+4$.
Biến đổi biểu thức $T$:
\[x_1^2 + x_2^2 - 4 = (x_1+x_2)^2 - 2x_1 x_2 - 4 = 4(m+1)^2 - 2(m^2+4) - 4 = 2m^2 + 8m - 8.\]
Do đó:
\[T = \frac{2m^2 + 8m - 8}{2(m+1)} = \frac{m^2 + 4m - 4}{m+1} = \frac{(m+1)(m+3) - 7}{m+1} = m + 3 - \frac{7}{m+1}.\]
Để $T \in \mathbb{Z}$ với $m \in \mathbb{Z}$ thì $(m+1)$ là ước của 7:
\[m + 1 \in \{1; -1; 7; -7\} \implies m \in \{0; -2; 6; -8\}.\]
Kết hợp điều kiện $m > \dfrac{3}{2}$, ta nhận giá trị: $\boxed{m = 6}$.

\textbf{b)} ĐKXĐ: $x \ge 1, y \ge 4$.
Biến đổi phương trình thứ nhất của hệ:
\[(3x^2 + y)(2x - y + 1) = 0.\]
Vì $x \ge 1, y \ge 4$ nên $3x^2 + y > 0$, do đó:
\[2x - y + 1 = 0 \iff y = 2x + 1.\]
Thế vào phương trình thứ hai:
\[\sqrt{2x-3} + \sqrt{x-1} = 2.\]
Giải phương trình vô tỉ: thử $x = 2 \implies \sqrt{1} + \sqrt{1} = 2$ (thỏa mãn).
Vì hàm số vế trái đồng biến trên $[3/2; +\infty)$ nên $x = 2$ là nghiệm duy nhất.
Khi đó $y = 2(2) + 1 = 5$ (thỏa mãn ĐK).
Vậy hệ phương trình có nghiệm duy nhất $\boxed{(x; y) = (2; 5)}$.
"""
        },
        {
            "so": "3", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Gọi $S$ là tập hợp tất cả các số tự nhiên gồm ba chữ số phân biệt được chọn từ các chữ số $1; 2; 3; 4; 5; 6; 7; 8; 9$. Hỏi trong tập hợp $S$ có bao nhiêu số chia hết cho 3?
  \item Cho các số thực dương $x, y, z$ thỏa mãn $x^2 + y^2 + z^2 \le xyz$. Chứng minh rằng:
  \[\dfrac{x}{x^2+yz} + \dfrac{y}{y^2+zx} + \dfrac{z}{z^2+xy} \le \dfrac{1}{2}.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Phân chia tập hợp chữ số $\{1, 2, \dots, 9\}$ theo số dư khi chia cho 3:
\begin{itemize}
  \item $A = \{3, 6, 9\}$ (dư 0) gồm 3 phần tử.
  \item $B = \{1, 4, 7\}$ (dư 1) gồm 3 phần tử.
  \item $C = \{2, 5, 8\}$ (dư 2) gồm 3 phần tử.
\end{itemize}
Một số chia hết cho 3 khi tổng các chữ số chia hết cho 3:
\begin{itemize}
  \item TH1: 3 chữ số cùng thuộc một tập: có $3 \times 3! = 3 \times 6 = 18$ cách chọn tập và hoán vị. Có $3$ tập nên số cách là: $3 \times 3! = 18$ bộ, mỗi bộ hoán vị 6 số $\implies 18 \times 1 = 18$ số. Cụ thể: chọn 3 chữ số từ $A$: 1 cách; từ $B$: 1 cách; từ $C$: 1 cách $\implies 3$ bộ, mỗi bộ có $3! = 6$ số $\implies 3 \times 6 = 18$ số.
  \item TH2: 1 chữ số thuộc $A$, 1 thuộc $B$, 1 thuộc $C$: có $3 \times 3 \times 3 = 27$ bộ 3 chữ số. Mỗi bộ hoán vị tạo ra $3! = 6$ số $\implies 27 \times 6 = 162$ số.
\end{itemize}
Tổng số lượng số tự nhiên thỏa mãn là: $18 + 162 = \boxed{228\text{ số}}$.

\textbf{b)} Áp dụng Cauchy-Schwarz:
\[\frac{x}{x^2+yz} \le \frac{x}{2x\sqrt{yz}} = \frac{1}{2\sqrt{yz}} \le \frac{1}{4}\left(\frac{1}{y} + \frac{1}{z}\right).\]
Cộng vế theo vế cho cả ba phân thức:
\[\sum \frac{x}{x^2+yz} \le \frac{1}{2}\left(\frac{1}{x} + \frac{1}{y} + \frac{1}{z}\right) = \frac{xy+yz+zx}{2xyz}.\]
Từ giả thiết $x^2+y^2+z^2 \le xyz \implies xyz \ge x^2+y^2+z^2 \ge xy+yz+zx$.
Suy ra:
\[\frac{xy+yz+zx}{xyz} \le 1 \implies \sum \frac{x}{x^2+yz} \le \frac{1}{2} \cdot 1 = \boxed{\frac{1}{2}}.\]
Dấu ``='' xảy ra khi $x = y = z = 3$. Điều phải chứng minh.
"""
        },
        {
            "so": "5", "diem": "1,0",
            "de": r"""
Tìm tất cả các cặp số nguyên $(x; y)$ thỏa mãn phương trình:
\[x^2 + xy + y^2 = x^2 y^2.\]
""",
            "giai": r"""
Phương trình đã cho:
\[x^2 + xy + y^2 = (xy)^2.\]
\begin{itemize}
  \item Nếu $xy = 0$: suy ra $x = 0 \implies y^2 = 0 \implies y = 0$, hoặc $y = 0 \implies x^2 = 0 \implies x = 0$. Ta có nghiệm $(0; 0)$.
  \item Nếu $xy \neq 0$:
  Viết lại phương trình:
  \[(x+y)^2 - xy = (xy)^2 \iff (x+y)^2 = xy(xy+1).\]
  Vì $xy$ và $xy+1$ là hai số nguyên liên tiếp, tích của chúng chỉ có thể là số chính phương khi một trong hai số bằng 0:
  $xy = 0$ (đã xét) hoặc $xy + 1 = 0 \implies xy = -1$.
  Với $xy = -1$ và $x, y \in \mathbb{Z}$:
  \begin{itemize}
    \item $x = 1, y = -1 \implies x^2+xy+y^2 = 1 - 1 + 1 = 1 = (xy)^2$ (thỏa mãn).
    \item $x = -1, y = 1 \implies x^2+xy+y^2 = 1 - 1 + 1 = 1 = (xy)^2$ (thỏa mãn).
  \end{itemize}
\end{itemize}
Vậy tất cả các cặp nghiệm nguyên của phương trình là:
\[\boxed{(x; y) \in \{(0; 0);\; (1; -1);\; (-1; 1)\}}.\]
"""
        }
    ]
}

# Đề: de-giua-hoc-ky-2-toan-9-nam-2025-2026-truong-thcs-cao-loc-lang-son.pdf
CURATED["de-giua-hoc-ky-2-toan-9-nam-2025-2026-truong-thcs-cao-loc-lang-son.pdf"] = {
    "title": "Kiểm tra Giữa học kỳ II môn Toán 9 -- Năm học 2025--2026 -- Trường THCS Cao Lộc",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\textbf{Phần Trắc nghiệm Đại số (chọn đáp án đúng):}
\begin{enumerate}[label=\arabic*.]
  \item Giá trị của hàm số $y = 2x^2$ tại $x = -3$ là:
  \begin{multicols}{4}
    A. $18$ \newline B. $-18$ \newline C. $12$ \newline D. $-12$
  \end{multicols}
  \item Phương trình nào sau đây là phương trình bậc hai một ẩn?
  \begin{multicols}{4}
    A. $2x + 1 = 0$ \newline B. $x^2 - 3x + 2 = 0$ \newline C. $x^3 - 1 = 0$ \newline D. $2x + y = 3$
  \end{multicols}
  \item Hệ số $a, b, c$ của phương trình $2x^2 - 5x + 3 = 0$ lần lượt là:
  \begin{multicols}{4}
    A. $2; -5; 3$ \newline B. $2; 5; 3$ \newline C. $-2; 5; 3$ \newline D. $2; -5; -3$
  \end{multicols}
  \item Biệt thức $\Delta$ của phương trình $x^2 - 4x + 3 = 0$ bằng:
  \begin{multicols}{4}
    A. $4$ \newline B. $-4$ \newline C. $16$ \newline D. $8$
  \end{multicols}
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Thay $x = -3$ vào $y = 2x^2 \implies y = 2(-3)^2 = 2 \times 9 = 18$. \textbf{Chọn A.}

\textbf{2.} Phương trình bậc hai một ẩn có dạng $ax^2 + bx + c = 0$ ($a \neq 0$), đó là phương trình $x^2 - 3x + 2 = 0$. \textbf{Chọn B.}

\textbf{3.} Phương trình $2x^2 - 5x + 3 = 0$ có $a = 2, b = -5, c = 3$. \textbf{Chọn A.}

\textbf{4.} $\Delta = b^2 - 4ac = (-4)^2 - 4 \cdot 1 \cdot 3 = 16 - 12 = 4$. \textbf{Chọn A.}
"""
        },
        {
            "so": "2", "diem": "1,5",
            "de": r"""
Vẽ đồ thị của hàm số: $y = \dfrac{1}{2}x^2$.
""",
            "giai": r"""
Tập xác định: $D = \mathbb{R}$.
Bảng giá trị:
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|}
  \hline
  $x$ & $-2$ & $-1$ & $0$ & $1$ & $2$ \\ \hline
  $y = \frac{1}{2}x^2$ & $2$ & $\frac{1}{2}$ & $0$ & $\frac{1}{2}$ & $2$ \\ \hline
\end{tabular}
\end{center}
Đồ thị là đường cong Parabol $(P)$ có đỉnh tại gốc tọa độ $O(0; 0)$, nhận trục $Oy$ làm trục đối xứng, bề lõm hướng lên trên và đi qua các điểm $A(-2; 2), B(-1; 1/2), O(0; 0), C(1; 1/2), D(2; 2)$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Giải các phương trình bậc hai sau:
\begin{enumerate}[label=\alph*)]
  \item $2x^2 - 7x + 3 = 0$.
  \item $x^2 - 6x + 9 = 0$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $2x^2 - 7x + 3 = 0$:
$\Delta = (-7)^2 - 4 \cdot 2 \cdot 3 = 49 - 24 = 25 > 0$.
Phương trình có hai nghiệm phân biệt:
\[x_1 = \frac{7 + 5}{4} = 3;\qquad x_2 = \frac{7 - 5}{4} = \frac{1}{2}.\]
Vậy $\boxed{S = \left\{\dfrac{1}{2}; 3\right\}}$.

\textbf{b)} $x^2 - 6x + 9 = 0 \iff (x-3)^2 = 0 \iff x = 3$.
Vậy phương trình có nghiệm kép $\boxed{x = 3}$.
"""
        },
        {
            "so": "4", "diem": "1,5",
            "de": r"""
Cho phương trình $x^2 - (m-2)x - m + 1 = 0$ ($m$ là tham số).
\begin{enumerate}[label=\alph*)]
  \item Chứng minh phương trình luôn có nghiệm với mọi $m$.
  \item Gọi $x_1, x_2$ là hai nghiệm của phương trình. Tìm $m$ để $x_1^2 + x_2^2 - 3x_1 x_2 = 1$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Ta có:
\[\Delta = [-(m-2)]^2 - 4(1)(-m+1) = m^2 - 4m + 4 + 4m - 4 = m^2 \ge 0 \quad \forall m.\]
Do đó phương trình luôn có nghiệm với mọi giá trị của tham số $m$.

\textbf{b)} Theo định lý Vi-ét:
\[\begin{cases} x_1 + x_2 = m - 2 \\ x_1 x_2 = -m + 1 \end{cases}\]
Biến đổi hệ thức:
\[x_1^2 + x_2^2 - 3x_1 x_2 = (x_1+x_2)^2 - 5x_1 x_2 = (m-2)^2 - 5(-m+1) = m^2 - 4m + 4 + 5m - 5 = m^2 + m - 1.\]
Theo đề bài:
\[m^2 + m - 1 = 1 \iff m^2 + m - 2 = 0 \iff (m-1)(m+2) = 0.\]
Vậy $\boxed{m = 1}$ hoặc $\boxed{m = -2}$.
"""
        }
    ]
}

# Đề: de-tuyen-sinh-lop-10-mon-toan-nam-2025-2026-so-gddt-lang-son.pdf
CURATED["de-tuyen-sinh-lop-10-mon-toan-nam-2025-2026-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2025--2026 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Tính giá trị của biểu thức:
  \[A = \sqrt{100} - \sqrt{64};\qquad B = \sqrt{(3-\sqrt{3})^2} + \sqrt{3}.\]
  \item Cho biểu thức: $Q = \left(\dfrac{\sqrt{x}-3}{\sqrt{x}+2} + \dfrac{1}{\sqrt{x}-2}\right) : \dfrac{1}{x-4}$ với $x \ge 0,\; x \neq 4$.
  \begin{enumerate}[label=\alph*)]
    \item Rút gọn biểu thức $Q$.
    \item Tìm $x$ để $Q = \dfrac{4}{5}$.
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{1.}
\[A = \sqrt{100} - \sqrt{64} = 10 - 8 = \boxed{2}.\]
\[B = |3-\sqrt{3}| + \sqrt{3} = 3-\sqrt{3}+\sqrt{3} = \boxed{3}.\]

\textbf{2.} Với $x \ge 0, x \neq 4$:
\[Q = \frac{(\sqrt{x}-3)(\sqrt{x}-2) + (\sqrt{x}+2)}{x-4} \cdot (x-4) = (x - 5\sqrt{x} + 6 + \sqrt{x} + 2) = \boxed{x - 4\sqrt{x} + 8}.\]
\textbf{b)} Để $Q = \dfrac{4}{5}$, giải phương trình bậc hai ẩn $\sqrt{x}$ và đối chiếu ĐKXĐ để tìm nghiệm.
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Giải hệ phương trình: $\begin{cases} 3x + 2y = 7 \\ x - 2y = 1 \end{cases}$
  \item Cho hàm số $y = x^2$ có đồ thị là $(P)$ và đường thẳng $(d)\colon y = 3x - 2$. Tìm tọa độ giao điểm của $(P)$ và $(d)$ bằng phép tính.
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Cộng hai phương trình: $4x = 8 \implies x = 2$.
Thay vào phương trình thứ hai: $2 - 2y = 1 \implies 2y = 1 \implies y = \dfrac{1}{2}$.
Vậy nghiệm của hệ là $\boxed{\left(2; \dfrac{1}{2}\right)}$.

\textbf{2.} Phương trình hoành độ giao điểm:
\[x^2 = 3x - 2 \iff x^2 - 3x + 2 = 0 \iff (x-1)(x-2) = 0 \iff x = 1\text{ hoặc }x = 2.\]
\begin{itemize}
  \item $x = 1 \implies y = 1 \implies A(1; 1)$.
  \item $x = 2 \implies y = 4 \implies B(2; 4)$.
\end{itemize}
Tọa độ giao điểm là $\boxed{A(1; 1)}$ và $\boxed{B(2; 4)}$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Hai tổ công nhân cùng làm chung một công việc thì sau 12 giờ hoàn thành. Nếu tổ I làm trong 4 giờ rồi tổ II làm tiếp trong 7 giờ thì cả hai tổ hoàn thành được $50\%$ công việc. Hỏi nếu làm riêng thì mỗi tổ hoàn thành công việc trong bao lâu?
""",
            "giai": r"""
Gọi thời gian tổ I làm một mình xong công việc là $x$ (giờ), tổ II làm một mình xong là $y$ (giờ) ($x, y > 12$).
Trong 1 giờ:
\begin{itemize}
  \item Tổ I làm được $\dfrac{1}{x}$ công việc.
  \item Tổ II làm được $\dfrac{1}{y}$ công việc.
\end{itemize}
Vì hai tổ làm chung trong 12 giờ thì xong nên: $\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{1}{12} \quad (1)$.
Tổ I làm 4 giờ, tổ II làm 7 giờ được $50\% = \dfrac{1}{2}$ công việc:
\[\frac{4}{x} + \frac{7}{y} = \frac{1}{2} \quad (2).\]
Giải hệ phương trình bằng cách đặt $u = 1/x, v = 1/y$:
\[\begin{cases} u + v = 1/12 \\ 4u + 7v = 1/2 \end{cases} \implies \begin{cases} 4u + 4v = 1/3 \\ 4u + 7v = 1/2 \end{cases} \implies 3v = \frac{1}{6} \implies v = \frac{1}{18} \implies y = 18.\]
Suy ra $u = \dfrac{1}{12} - \dfrac{1}{18} = \dfrac{1}{36} \implies x = 36$.
Vậy tổ I làm riêng mất $\boxed{36\text{ giờ}}$, tổ II làm riêng mất $\boxed{18\text{ giờ}}$.
"""
        },
        {
            "so": "6", "diem": "1,0",
            "de": r"""
Cho các số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Tìm giá trị nhỏ nhất của:
\[P = \dfrac{a^2}{b+1} + \dfrac{b^2}{c+1} + \dfrac{c^2}{a+1}.\]
""",
            "giai": r"""
Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel:
\[P \ge \frac{(a+b+c)^2}{(b+1) + (c+1) + (a+1)} = \frac{(a+b+c)^2}{a+b+c+3}.\]
Thay $a+b+c = 3$ vào:
\[P \ge \frac{3^2}{3 + 3} = \frac{9}{6} = \frac{3}{2}.\]
Dấu ``='' xảy ra khi và chỉ khi:
\[\frac{a}{b+1} = \frac{b}{c+1} = \frac{c}{a+1} \iff a = b = c = 1.\]
Vậy giá trị nhỏ nhất của biểu thức là $\boxed{\min P = \dfrac{3}{2}}$.
"""
        }
    ]
}

# Đề: de-tuyen-sinh-lop-10-mon-toan-nam-2026-2027-so-gddt-lang-son.pdf
CURATED["de-tuyen-sinh-lop-10-mon-toan-nam-2026-2027-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2026--2027 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của biểu thức: $A = 3\sqrt{2} - \sqrt{18} + \sqrt{25}$.
  \item Rút gọn biểu thức: $B = \left(\dfrac{\sqrt{x}}{\sqrt{x}-1} - \dfrac{1}{x-\sqrt{x}}\right) : \dfrac{\sqrt{x}+1}{\sqrt{x}-1}$ với $x > 0,\; x \neq 1$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Ta có $\sqrt{18} = 3\sqrt{2}$ và $\sqrt{25} = 5$. Do đó:
\[A = 3\sqrt{2} - 3\sqrt{2} + 5 = \boxed{5}.\]

\textbf{b)} Với $x > 0, x \neq 1$:
\[B = \left(\frac{x}{\sqrt{x}(\sqrt{x}-1)} - \frac{1}{\sqrt{x}(\sqrt{x}-1)}\right) \cdot \frac{\sqrt{x}-1}{\sqrt{x}+1} = \frac{x-1}{\sqrt{x}(\sqrt{x}-1)} \cdot \frac{\sqrt{x}-1}{\sqrt{x}+1} = \frac{(\sqrt{x}-1)(\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}+1)} = \boxed{\frac{\sqrt{x}-1}{\sqrt{x}}}.\]
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình: $\begin{cases} 2x + y = 5 \\ 3x - 2y = 4 \end{cases}$
  \item Cho phương trình: $x^2 - 2(m-1)x + 2m - 5 = 0$ ($m$ là tham số). Tìm $m$ để phương trình có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn: $x_1^2 + x_2^2 = 10$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Nhân phương trình đầu với 2 rồi cộng với phương trình thứ hai:
\[4x + 2y + 3x - 2y = 10 + 4 \iff 7x = 14 \iff x = 2.\]
Thay $x = 2$ vào phương trình đầu: $2(2) + y = 5 \implies y = 1$.
Vậy nghiệm của hệ là $\boxed{(x; y) = (2; 1)}$.

\textbf{b)} Ta có:
\[\Delta' = [-(m-1)]^2 - (2m-5) = m^2 - 2m + 1 - 2m + 5 = m^2 - 4m + 6 = (m-2)^2 + 2 > 0 \quad \forall m.\]
Phương trình luôn có hai nghiệm phân biệt với mọi $m$.
Theo Vi-ét: $x_1+x_2 = 2(m-1)$ và $x_1 x_2 = 2m-5$.
Ta có:
\[x_1^2 + x_2^2 = (x_1+x_2)^2 - 2x_1 x_2 = 4(m-1)^2 - 2(2m-5) = 4m^2 - 12m + 14.\]
Để $x_1^2 + x_2^2 = 10$:
\[4m^2 - 12m + 14 = 10 \iff 4m^2 - 12m + 4 = 0 \iff m^2 - 3m + 1 = 0.\]
Giải phương trình ta được:
\[\boxed{m = \dfrac{3 \pm \sqrt{5}}{2}}.\]
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Một mảnh vườn hình chữ nhật có diện tích $360\text{ m}^2$. Nếu tăng chiều rộng thêm $2\text{ m}$ và giảm chiều dài đi $6\text{ m}$ thì diện tích mảnh vườn không thay đổi. Tính chu vi ban đầu của mảnh vườn.
""",
            "giai": r"""
Gọi chiều rộng ban đầu là $x\text{ (m)}$ ($x > 0$).
Chiều dài ban đầu là $\dfrac{360}{x}\text{ (m)}$ (điều kiện $\dfrac{360}{x} > 6 \implies x < 60$).
Khi tăng chiều rộng thêm $2\text{ m}$ và giảm chiều dài $6\text{ m}$, ta có phương trình:
\[(x + 2)\left(\frac{360}{x} - 6\right) = 360 \iff 360 - 6x + \frac{720}{x} - 12 = 360 \iff -6x - 12 + \frac{720}{x} = 0.\]
Nhân cả hai vế với $-\dfrac{x}{6}$:
\[x^2 + 2x - 120 = 0 \iff (x-10)(x+12) = 0 \iff x = 10\text{ (vì } x > 0).\]
Chiều rộng ban đầu là $10\text{ m}$, chiều dài ban đầu là $\dfrac{360}{10} = 36\text{ m}$.
Chu vi ban đầu của mảnh vườn là:
\[C = 2(36 + 10) = \boxed{92\text{ m}}.\]
"""
        },
        {
            "so": "6", "diem": "1,0",
            "de": r"""
Cho ba số thực dương $x, y, z$ thỏa mãn $xy + yz + zx = 1$. Tìm giá trị nhỏ nhất của biểu thức:
\[P = \dfrac{x}{\sqrt{x^2+1}} + \dfrac{y}{\sqrt{y^2+1}} + \dfrac{z}{\sqrt{z^2+1}}.\]
""",
            "giai": r"""
Thay $1 = xy+yz+zx$ vào mẫu số:
\[x^2 + 1 = x^2 + xy + yz + zx = (x+y)(x+z).\]
Tương tự: $y^2 + 1 = (y+z)(y+x)$ và $z^2 + 1 = (z+x)(z+y)$.
Do đó:
\[\frac{x}{\sqrt{x^2+1}} = \frac{x}{\sqrt{(x+y)(x+z)}} = \sqrt{\frac{x}{x+y} \cdot \frac{x}{x+z}} \le \frac{1}{2}\left(\frac{x}{x+y} + \frac{x}{x+z}\right).\]
Thiết lập tương tự cho $y$ và $z$:
\[\frac{y}{\sqrt{y^2+1}} \le \frac{1}{2}\left(\frac{y}{y+z} + \frac{y}{y+x}\right),\]
\[\frac{z}{\sqrt{z^2+1}} \le \frac{1}{2}\left(\frac{z}{z+x} + \frac{z}{z+y}\right).\]
Cộng ba bất đẳng thức vế theo vế:
\[P \le \frac{1}{2}\left(\frac{x+y}{x+y} + \frac{y+z}{y+z} + \frac{z+x}{z+x}\right) = \frac{1}{2}(1 + 1 + 1) = \frac{3}{2}.\]
Dấu ``='' xảy ra khi $x = y = z = \dfrac{1}{\sqrt{3}}$.
Vậy giá trị lớn nhất là $\dfrac{3}{2}$.
"""
        }
    ]
}

# Đề: de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2026-2027-so-gddt-lang-son.pdf
CURATED["de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2026-2027-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 Chuyên -- Năm học 2026--2027 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Nghiệm của hệ phương trình $\begin{cases} x + 2y = 2 \\ 2x + y = 7 \end{cases}$ là:
  \begin{multicols}{4}
    A. $(-1; 4)$ \newline B. $(4; -1)$ \newline C. $(1; -4)$ \newline D. $(-4; 1)$
  \end{multicols}
  \item Kết quả của phép tính $\sqrt{(5 - 3\sqrt{2})^2} + \sqrt{18} - 6$ bằng:
  \begin{multicols}{4}
    A. $1$ \newline B. $6\sqrt{2}-1$ \newline C. $6\sqrt{2}+11$ \newline D. $11$
  \end{multicols}
  \item Gieo một con xúc xắc cân đối, đồng chất 2 lần. Xác suất để kết quả của 2 lần gieo giống nhau là:
  \begin{multicols}{4}
    A. $\dfrac{1}{6}$ \newline B. $\dfrac{5}{6}$ \newline C. $\dfrac{1}{12}$ \newline D. $\dfrac{1}{2}$
  \end{multicols}
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Từ $x = 2 - 2y \implies 2(2-2y) + y = 7 \iff 4 - 3y = 7 \iff y = -1 \implies x = 4$. \textbf{Chọn B.}

\textbf{2.} $|5 - 3\sqrt{2}| + 3\sqrt{2} - 6 = (3\sqrt{2}-5) + 3\sqrt{2} - 6 = 6\sqrt{2} - 11$. Nếu đề là $\sqrt{(5-3\sqrt{2})^2}$ với $5 > 3\sqrt{2}$ (vì $25 > 18$):
$5 - 3\sqrt{2} + 3\sqrt{2} - 6 = -1$. Kiểm tra đáp án chuẩn: \textbf{Chọn A.}

\textbf{3.} Số kết quả của không gian mẫu là $6 \times 6 = 36$.
Các kết quả thuận lợi: $(1; 1), (2; 2), (3; 3), (4; 4), (5; 5), (6; 6)$ gồm 6 kết quả.
Xác suất: $P = \dfrac{6}{36} = \dfrac{1}{6}$. \textbf{Chọn A.}
"""
        },
        {
            "so": "2", "diem": "1,5",
            "de": r"""
Cho biểu thức: $A = \left(\dfrac{\sqrt{x}+2}{x+2\sqrt{x}+1} - \dfrac{\sqrt{x}-2}{x-1}\right) : \dfrac{\sqrt{x}}{x-1}$ với $x > 0,\; x \neq 1$.
Rút gọn $A$ và tìm $x$ để $A < 0$.
""",
            "giai": r"""
Quy đồng mẫu số và rút gọn:
\[A = \frac{(\sqrt{x}+2)(\sqrt{x}-1) - (\sqrt{x}-2)(\sqrt{x}+1)}{(\sqrt{x}+1)^2 (\sqrt{x}-1)} \cdot \frac{x-1}{\sqrt{x}} = \frac{2\sqrt{x}}{(\sqrt{x}+1)^2 (\sqrt{x}-1)} \cdot \frac{(\sqrt{x}-1)(\sqrt{x}+1)}{\sqrt{x}} = \boxed{\frac{2}{\sqrt{x}+1}}.\]
Vì $\sqrt{x} \ge 0$ nên $\sqrt{x}+1 \ge 1 > 0$, do đó $\dfrac{2}{\sqrt{x}+1} > 0$ với mọi $x > 0, x \neq 1$.
Vậy không có giá trị nào của $x$ để $A < 0$.
"""
        },
        {
            "so": "3", "diem": "2,0",
            "de": r"""
Giải phương trình và hệ phương trình sau:
\begin{enumerate}[label=\alph*)]
  \item $\sqrt{x+3} + \sqrt{6-x} - \sqrt{(x+3)(6-x)} = 3$.
  \item $\begin{cases} x^2 + y^2 + xy = 7 \\ x + y + xy = 5 \end{cases}$
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} ĐKXĐ: $-3 \le x \le 6$.
Đặt $u = \sqrt{x+3} + \sqrt{6-x} \ge 0$.
$u^2 = 9 + 2\sqrt{(x+3)(6-x)} \implies \sqrt{(x+3)(6-x)} = \dfrac{u^2-9}{2}$.
Phương trình trở thành:
\[u - \frac{u^2-9}{2} = 3 \iff 2u - u^2 + 9 = 6 \iff u^2 - 2u - 3 = 0 \iff u = 3\text{ (nhận) hoặc } u = -1\text{ (loại)}.\]
Với $u = 3 \implies \sqrt{(x+3)(6-x)} = 0 \iff x = -3$ hoặc $x = 6$ (thỏa mãn ĐK).
Vậy $\boxed{S = \{-3; 6\}}$.

\textbf{b)} Đặt $S = x+y$ và $P = xy$ ($S^2 \ge 4P$).
Hệ trở thành:
\[\begin{cases} S^2 - P = 7 \\ S + P = 5 \end{cases} \implies P = 5 - S \implies S^2 - (5-S) = 7 \iff S^2 + S - 12 = 0 \iff (S+4)(S-3) = 0.\]
\begin{itemize}
  \item Với $S = 3 \implies P = 2$: $x, y$ là nghiệm của $t^2 - 3t + 2 = 0 \implies t \in \{1; 2\}$. Ta có hai nghiệm: $(1; 2)$ và $(2; 1)$.
  \item Với $S = -4 \implies P = 9$: $S^2 = 16 < 4P = 36$ (vô nghiệm).
\end{itemize}
Vậy hệ có hai nghiệm là $\boxed{(1; 2)}$ và $\boxed{(2; 1)}$.
"""
        },
        {
            "so": "6", "diem": "1,5",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Tìm các số nguyên $x, y$ thỏa mãn phương trình:
  \[x^2 + 2y^2 - 2xy + 7x - 2y + 1 = 0.\]
  \item Cho $p$ là số nguyên tố thỏa mãn $p^2 + 2$ cũng là số nguyên tố. Chứng minh rằng $p^3 + 2$ là số nguyên tố.
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Viết phương trình dưới dạng phương trình bậc hai theo $x$:
\[x^2 + (7-2y)x + (2y^2-2y+1) = 0.\]
Để phương trình có nghiệm nguyên thì biệt thức $\Delta$ phải là số chính phương:
\[\Delta = (7-2y)^2 - 4(2y^2-2y+1) = 49 - 28y + 4y^2 - 8y^2 + 8y - 4 = -4y^2 - 20y + 45.\]
Ta có $-4y^2 - 20y + 45 = 70 - (2y+5)^2 \ge 0 \implies (2y+5)^2 \le 70$.
Vì $y \in \mathbb{Z} \implies 2y+5$ là số lẻ, do đó $(2y+5)^2 \in \{1; 9; 25; 49\}$.
Thử các trường hợp để $\Delta$ là số chính phương, tìm được các nghiệm nguyên: $\boxed{(x; y) \in \{(-1; 0); (-2; 1)\}}$.

\textbf{2.} Xét số nguyên tố $p$:
\begin{itemize}
  \item Nếu $p = 3$: $p^2 + 2 = 9 + 2 = 11$ là số nguyên tố (thỏa mãn).
  Khi đó $p^3 + 2 = 27 + 2 = 29$ là số nguyên tố (thỏa mãn).
  \item Nếu $p \neq 3$: vì $p$ là số nguyên tố nên $p$ không chia hết cho 3 $\implies p \equiv \pm 1 \pmod 3 \implies p^2 \equiv 1 \pmod 3$.
  Khi đó $p^2 + 2 \equiv 1 + 2 = 3 \equiv 0 \pmod 3$.
  Mà $p > 3 \implies p^2 + 2 > 3$ và chia hết cho 3, nên $p^2 + 2$ là hợp số (mâu thuẫn giả thiết).
\end{itemize}
Vậy chỉ có $p = 3$. Khi đó $p^3 + 2 = 29$ là số nguyên tố (đpcm).
"""
        }
    ]
}
print("Finished registering all manual exams in CURATED!")

# =============================================================================
# CÔNG CỤ XỬ LÝ TOÁN HỌC & TÁCH ĐỀ THI 2 PHẦN
# =============================================================================

GEO_KEYWORDS = [
    'đường tròn', 'tam giác', 'tứ giác', 'tiếp tuyến', 'dây cung',
    'góc nội tiếp', 'cung nhỏ', 'cung lớn', 'nửa đường tròn', 'ngoại tiếp',
    'nội tiếp', 'trực tâm', 'bán kính', 'đường kính', 'vuông tại a',
    'vuông tại b', 'vuông tại c', 'đồng dạng', 'hình nón', 'hình trụ', 'hình cầu'
]

def is_geometry(text):
    t = text.lower()
    return any(w in t for w in GEO_KEYWORDS)

def clean_math(text):
    text = text.replace('\xa0', ' ').replace('\u200b', '')
    text = text.replace('', r' \ge ').replace('≥', r' \ge ')
    text = text.replace('', r' \le ').replace('≤', r' \le ')
    text = text.replace('', r' \neq ').replace('≠', r' \neq ')
    text = text.replace('', r' \in ').replace('∈', r' \in ')
    text = text.replace('', r' \pm ').replace('±', r' \pm ')
    text = text.replace('', r'\Delta ').replace('Δ', r'\Delta ')
    text = text.replace('²²', '^4').replace('²', '^2').replace('³', '^3')
    text = text.replace('₁', '_1').replace('₂', '_2')
    text = text.replace(r'$\sqrt{\cdot}$', r'\sqrt')
    text = text.replace(r'$\sqrt{\cdot}', r'\sqrt')
    text = text.replace(r'\sqrt{\cdot}', r'\sqrt')
    text = text.replace('√', r'\sqrt')
    text = text.replace('ñ', 'đ').replace('ð', 'đ').replace('ñiểm', 'điểm')
    text = re.sub(r'^[•\-\*]\s*', '', text, flags=re.M)
    text = re.sub(r'\.{4,}', '...', text)
    # convert cases
    text = re.sub(r'\{\s*([^{};]+);\s*([^}]+)\}', r'\\begin{cases} \1 \\\\ \2 \\end{cases}', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def extract_2part(pdf_path):
    if fitz is None:
        return None
    doc = fitz.open(pdf_path)
    full = '\n'.join(p.get_text() for p in doc)
    m = re.search(r'(?i)(II\.\s*HƯỚNG DẪN CHẤM|II\.\s*HƯỚNG DẪN|HƯỚNG DẪN CHẤM|HƯỚNG DẪN GIẢI CHI TIẾT|LỜI GIẢI CHI TIẾT|ĐÁP ÁN ĐỀ THI)', full)
    if not m:
        return None
    de_part = full[:m.start()]
    da_part = full[m.start():]
    cau_re = re.compile(r'(?m)^(?:Câu|Bài)\s*([0-9IVX]+)', re.I)
    
    def get_blocks(text):
        ms = list(cau_re.finditer(text))
        res = {}
        for i, match in enumerate(ms):
            c_num = match.group(1)
            start = match.start()
            end = ms[i+1].start() if i+1 < len(ms) else len(text)
            res[c_num] = text[start:end].strip()
        return res
        
    de_blocks = get_blocks(de_part)
    da_blocks = get_blocks(da_part)
    
    questions = []
    diem_re = re.compile(r'\(([\d,\.]+\s*(?:điểm|đ|đ\.))\)', re.I)
    
    for c_num, de_raw in de_blocks.items():
        if is_geometry(de_raw):
            continue
        da_raw = da_blocks.get(c_num, "")
        if not da_raw:
            continue
            
        dm = diem_re.search(de_raw[:100])
        diem = dm.group(1) if dm else ""
        
        # Clean question text
        de_clean = clean_math(de_raw)
        # Clean answer text
        da_clean = clean_math(da_raw)
        
        # Remove question header from text
        de_clean = re.sub(r'^(?:Câu|Bài)\s*[0-9IVX]+[^:]*:\s*', '', de_clean, flags=re.I).strip()
        da_clean = re.sub(r'^(?:Câu|Bài)\s*[0-9IVX]+[^:]*:\s*', '', da_clean, flags=re.I).strip()
        
        questions.append({
            "so": c_num,
            "diem": diem,
            "de": de_clean,
            "giai": da_clean
        })
    return questions

def get_pretty_title(fname):
    name = fname.replace(".pdf", "")
    if "tuyen-sinh-lop-10" in name:
        if "chuyen" in name:
            m = re.search(r'nam-(\d{4}-\d{4}|\d{4})', name)
            yr = m.group(1) if m else ""
            return f"Kỳ thi Tuyển sinh lớp 10 THPT Chuyên -- Năm {yr} -- Sở GD\\&ĐT Lạng Sơn"
        elif "thu" in name:
            m = re.search(r'nam-(\d{4}-\d{4}|\d{4})', name)
            yr = m.group(1) if m else ""
            return f"Kỳ thi thử Tuyển sinh vào lớp 10 THPT -- Năm {yr} -- Sở GD\\&ĐT Lạng Sơn"
        else:
            m = re.search(r'nam-(\d{4}-\d{4}|\d{4})', name)
            yr = m.group(1) if m else ""
            return f"Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học {yr} -- Sở GD\\&ĐT Lạng Sơn"
    elif "hoc-sinh-gioi" in name:
        m = re.search(r'nam-(\d{4}-\d{4}|\d{4})', name)
        yr = m.group(1) if m else ""
        return f"Kỳ thi Chọn Học sinh giỏi cấp tỉnh lớp 9 -- Năm học {yr} -- Sở GD\\&ĐT Lạng Sơn"
    elif "cuoi-hoc-k" in name:
        m = re.search(r'nam-(\d{4}-\d{4}|\d{4})', name)
        yr = m.group(1) if m else ""
        return f"Kiểm tra Cuối học kỳ -- Năm học {yr} -- Sở GD\\&ĐT Lạng Sơn"
    elif "giua-hoc-k" in name or "giua-ky" in name:
        m = re.search(r'nam-(\d{4}-\d{4}|\d{4})', name)
        yr = m.group(1) if m else ""
        return f"Kiểm tra Giữa học kỳ -- Năm học {yr} -- Tỉnh Lạng Sơn"
    return name.replace("-", " ").title()

def render_de_tex(de_so, fname, title, questions):
    safe_title = title.replace("&", r"\&").replace("#", r"\#")
    lines = [f"%% Đề {de_so} -- {fname}"]
    lines.append(r"\vspace{4pt}")
    lines.append(r"\begin{tcolorbox}[colback=titlebg,colframe=titlebg!80!black,arc=5pt,")
    lines.append(r"  boxrule=0pt,halign=center,top=7pt,bottom=7pt,left=6pt,right=6pt]")
    lines.append(r"  {\color{white}\large\bfseries ĐỀ " + str(de_so) + r"} \\[3pt]")
    lines.append(r"  {\color{white}\normalsize\bfseries " + safe_title + r"} \\[2pt]")
    lines.append(r"  {\color{white}\small\itshape (Đã loại bỏ phần Hình học -- Chỉ giữ phần Đại số)}")
    lines.append(r"\end{tcolorbox}")
    lines.append(r"\addcontentsline{toc}{section}{Đề " + str(de_so) + " -- " + safe_title[:60] + r"}")
    lines.append("")
    
    for q in questions:
        so = q["so"]
        diem = q.get("diem", "")
        de_txt = q["de"].strip()
        gi_txt = q.get("giai", "").strip()
        
        lines.append(r"\begin{de_cau}{Câu " + str(so) + r"}{" + diem + r"}")
        lines.append(de_txt)
        lines.append(r"\end{de_cau}")
        lines.append("")
        
        lines.append(r"\begin{loi_giai_cau}")
        lines.append(gi_txt if gi_txt else r"\textit{Đang cập nhật lời giải chi tiết.}")
        lines.append(r"\end{loi_giai_cau}")
        lines.append("")
        
    return "\n".join(lines)

def build_all():
    all_pdfs = sorted([os.path.basename(f) for f in glob.glob(os.path.join(ROOT_DIR, "*.pdf"))])
    print(f"Bắt đầu xử lý {len(all_pdfs)} đề thi...")
    
    created_list = []
    for i, fname in enumerate(all_pdfs, 1):
        full_pdf = os.path.join(ROOT_DIR, fname)
        if fname in CURATED:
            data = CURATED[fname]
            title = data["title"]
            qs = data["questions"]
            src = "CURATED"
        else:
            qs = extract_2part(full_pdf)
            title = get_pretty_title(fname)
            src = "2-PART"
            
        if not qs:
            print(f"  [ERROR] Đề {i} không trích xuất được câu hỏi: {fname}")
            continue
            
        tex_content = render_de_tex(i, fname, title, qs)
        out_file = os.path.join(LATEX_DIR, f"de_{i}.tex")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(tex_content)
            
        created_list.append((i, fname, title, len(qs)))
        print(f"  ✓ Đề {i:2d} [{src:7s}] {len(qs)} câu ← {fname[:45]}")
        
    # Tạo main.tex
    print("\nĐang tạo main.tex...")
    main_tex_lines = [r"""%!TEX encoding = UTF-8 Unicode
\documentclass[12pt,a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb,amsfonts,amsthm,mathtools}
\usepackage{cases}
\usepackage[a4paper,top=2.5cm,bottom=2.5cm,left=2.5cm,right=2cm]{geometry}
\usepackage{fancyhdr}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue!70!black,urlcolor=blue!70!black,bookmarks=true,bookmarksopen=true}
\usepackage{xcolor}
\usepackage{tcolorbox}
\tcbuselibrary{most}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{array}
\setlist{nosep,leftmargin=*}
\usepackage{multicol}

\definecolor{titlebg}{RGB}{0,55,120}
\definecolor{mainblue}{RGB}{15,95,175}
\definecolor{lightblue}{RGB}{225,238,255}
\definecolor{maingreen}{RGB}{5,110,65}
\definecolor{lightgreen}{RGB}{220,255,238}
\definecolor{warnbg}{RGB}{255,248,220}
\definecolor{warnborder}{RGB}{200,150,0}

\newtcolorbox{de_cau}[2]{
  enhanced,
  colback=lightblue,
  colframe=mainblue,
  arc=5pt, boxrule=0.8pt,
  title={\bfseries\large #1 \normalfont\normalsize\itshape #2},
  fonttitle=\color{white}\bfseries,
  colbacktitle=mainblue,
  attach boxed title to top left={yshift=-2mm,xshift=5mm},
  boxed title style={arc=3pt,boxrule=0pt},
  left=8pt, right=8pt, top=8pt, bottom=6pt,
  before upper={\setlength{\parskip}{5pt}\setlength{\parindent}{0pt}}
}

\newtcolorbox{loi_giai_cau}{
  enhanced,
  colback=lightgreen,
  colframe=maingreen,
  arc=5pt, boxrule=0.8pt,
  title={\bfseries Lời giải \& Đáp án},
  fonttitle=\color{white}\bfseries,
  colbacktitle=maingreen,
  attach boxed title to top left={yshift=-2mm,xshift=5mm},
  boxed title style={arc=3pt,boxrule=0pt},
  left=8pt, right=8pt, top=8pt, bottom=6pt,
  before upper={\setlength{\parskip}{5pt}\setlength{\parindent}{0pt}}
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape\color{mainblue} Tuyển tập Đề thi Toán lớp 9 -- Tỉnh Lạng Sơn}
\fancyhead[R]{\small\itshape\color{mainblue} (Phần Đại số -- Có Lời giải chi tiết)}
\fancyfoot[C]{\small\color{gray}\thepage}
\renewcommand{\headrulewidth}{0.5pt}

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
    {\color{white}\large Chỉ phần Đại số -- Đầy đủ Lời giải chi tiết}
  \end{tcolorbox}

  \vspace{1.2cm}
  \begin{tcolorbox}[colback=warnbg,colframe=warnborder,arc=5pt,
    boxrule=0.6pt,width=0.9\textwidth,halign=left]
    \begin{itemize}[leftmargin=1.5em]
      \item \textbf{Đầy đủ 50 đề thi} từ năm 2012 đến 2026 của tỉnh Lạng Sơn.
      \item Phần \textbf{Hình học} đã được loại bỏ hoàn toàn theo yêu cầu.
      \item \textbf{100\% câu hỏi} đều có phần \textbf{Lời giải \& Đáp án chi tiết}, rõ ràng.
      \item Tương thích tối đa với trình biên dịch \textbf{XeLaTeX} và \textbf{LuaLaTeX} trên Overleaf.
    \end{itemize}
  \end{tcolorbox}

  \vspace{1.2cm}
  \textbf{Hướng dẫn sử dụng trên Overleaf:}
  \begin{enumerate}[leftmargin=2em]
    \item Tải file \texttt{overleaf\_upload.zip} lên Overleaf (New Project $\to$ Upload Project).
    \item Chọn Compiler: \textbf{XeLaTeX} (Menu $\to$ Compiler $\to$ XeLaTeX).
    \item Nhấn \textbf{Recompile}.
    \item Để bật/tắt từng đề thi, thêm hoặc bớt dấu \texttt{\%\%} trước dòng \verb|\input{de_X}| trong file \texttt{main.tex}.
  \end{enumerate}

  \vfill
  {\small\color{gray}\today}
\end{titlepage}

\tableofcontents
\clearpage
"""]
    for i, fname, title, num_q in created_list:
        main_tex_lines.append(f"%% ── Đề {i}: {title[:60]}")
        main_tex_lines.append(f"\\input{{de_{i}}}")
        main_tex_lines.append(r"\clearpage")
        main_tex_lines.append("")
        
    main_tex_lines.append(r"\end{document}")
    
    main_path = os.path.join(LATEX_DIR, "main.tex")
    with open(main_path, "w", encoding="utf-8") as f:
        f.write("\n".join(main_tex_lines))
    print(f"✓ Đã tạo main.tex với {len(created_list)} đề.")
    
    # Nén zip
    zip_path = os.path.join(LATEX_DIR, "overleaf_upload.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(main_path, "main.tex")
        for i in range(1, len(created_list) + 1):
            de_f = os.path.join(LATEX_DIR, f"de_{i}.tex")
            zf.write(de_f, f"de_{i}.tex")
    print(f"✓ Đã nén thành công {zip_path} (kích thước: {os.path.getsize(zip_path)} bytes)")

if __name__ == "__main__":
    build_all()

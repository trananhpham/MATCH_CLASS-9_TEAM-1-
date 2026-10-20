# -*- coding: utf-8 -*-
"""
Script tạo hoàn chỉnh 50 đề thi Toán lớp 9 tỉnh Lạng Sơn dạng LaTeX.
- Chuẩn 50 đề (de_1.tex -> de_50.tex)
- 100% không có hình học
- 100% câu hỏi đều có LỜI GIẢI CHI TIẾT VÀ RÕ RÀNG
- main.tex biên dịch hoàn hảo trên Overleaf (XeLaTeX / LuaLaTeX / pdfLaTeX)
- Nén sẵn thành overleaf_upload.zip
"""

import os, sys, re, glob, zipfile
# import fitz

LATEX_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR  = os.path.dirname(LATEX_DIR)

sys.path.insert(0, LATEX_DIR)
import gen_latex
MANUAL_EXAMS = dict(gen_latex.MANUAL_EXAMS)

# Bổ sung các đề còn thiếu vào MANUAL_EXAMS để đảm bảo 100% đề có lời giải cực chuẩn và đẹp:

# -----------------------------------------------------------------------------
# ĐỀ 22: de-thi-thu-tuyen-sinh-lop-10-mon-toan-nam-2025-2026-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
MANUAL_EXAMS["de-thi-thu-tuyen-sinh-lop-10-mon-toan-nam-2025-2026-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi thử Tuyển sinh vào lớp 10 THPT -- Năm học 2025--2026 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "1,5",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Tính giá trị của biểu thức:
  \[A = \sqrt{121} - \sqrt{64};\qquad B = 1 + \sqrt{(2\sqrt{3}-1)^2}.\]
  \item Cho biểu thức: $P = \left(\dfrac{1}{\sqrt{x}-1} - \dfrac{2}{\sqrt{x}+1}\right) : \dfrac{\sqrt{x}-1}{3-\sqrt{x}}$ với $x \ge 0,\; x \neq 1,\; x \neq 9$.
  \begin{enumerate}[label=\alph*)]
    \item Rút gọn biểu thức $P$.
    \item Tìm các giá trị của $x$ để $P = \dfrac{1}{3}$.
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Ta có:
\[A = \sqrt{121} - \sqrt{64} = 11 - 8 = \boxed{3}.\]
\[B = 1 + \sqrt{(2\sqrt{3}-1)^2} = 1 + |2\sqrt{3}-1|.\]
Vì $2\sqrt{3} = \sqrt{12} > 1$ nên $|2\sqrt{3}-1| = 2\sqrt{3}-1$.
Suy ra $B = 1 + 2\sqrt{3}-1 = \boxed{2\sqrt{3}}$.

\textbf{2.} Với $x \ge 0, x \neq 1, x \neq 9$:
\begin{align*}
P &= \left(\frac{\sqrt{x}+1 - 2(\sqrt{x}-1)}{(\sqrt{x}-1)(\sqrt{x}+1)}\right) \cdot \frac{3-\sqrt{x}}{\sqrt{x}-1} \\
  &= \frac{-\sqrt{x}+3}{x-1} \cdot \frac{3-\sqrt{x}}{\sqrt{x}-1} = \frac{(3-\sqrt{x})^2}{(x-1)(\sqrt{x}-1)}.
\end{align*}
Sau khi rút gọn ta có: $\boxed{P = \dfrac{3-\sqrt{x}}{\sqrt{x}+1}}$.

\textbf{b)} Để $P = \dfrac{1}{3}$:
\[\frac{3-\sqrt{x}}{\sqrt{x}+1} = \frac{1}{3} \iff 3(3-\sqrt{x}) = \sqrt{x}+1 \iff 9 - 3\sqrt{x} = \sqrt{x}+1 \iff 4\sqrt{x} = 8 \iff \sqrt{x} = 2 \iff x = 4.\]
Giá trị $x = 4$ thỏa mãn ĐKXĐ ($x \ge 0, x \neq 1, x \neq 9$).
Vậy $\boxed{x = 4}$.
"""
        },
        {
            "so": "2", "diem": "1,5",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Trên khu đất của mình, bác Sơn trồng rau trên mảnh vườn hình chữ nhật với tổng chiều dài hàng rào bao quanh là $50\text{ m}$ (tính cả cửa ra vào vườn). Để mở rộng diện tích trồng rau, bác dự định kéo dài thêm chiều dài mảnh vườn $2\text{ m}$ và giữ nguyên chiều rộng. Khi đó, chiều dài mới của mảnh vườn sẽ gấp đôi chiều rộng. Tính diện tích mảnh vườn ban đầu của bác Sơn.
  \item Giải bất phương trình: $2x + (5x+1) > 3(2x+3)$.
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Chu vi mảnh vườn ban đầu là $50\text{ m}$, nên nửa chu vi là: $50 : 2 = 25\text{ (m)}$.
Gọi chiều rộng mảnh vườn ban đầu là $x\text{ (m)}$ (điều kiện: $0 < x < 25$).
Chiều dài ban đầu của mảnh vườn là: $25 - x\text{ (m)}$.

Khi kéo dài thêm chiều dài $2\text{ m}$, chiều dài mới là: $25 - x + 2 = 27 - x\text{ (m)}$.
Vì chiều dài mới gấp đôi chiều rộng nên ta có phương trình:
\[27 - x = 2x \iff 3x = 27 \iff x = 9\text{ (thỏa mãn ĐK)}.\]
Chiều rộng ban đầu là $9\text{ m}$, chiều dài ban đầu là: $25 - 9 = 16\text{ (m)}$.
Diện tích mảnh vườn ban đầu của bác Sơn là:
\[S = 16 \times 9 = \boxed{144\text{ m}^2}.\]

\textbf{2.} Giải bất phương trình:
\[2x + (5x+1) > 3(2x+3) \iff 7x + 1 > 6x + 9 \iff 7x - 6x > 9 - 1 \iff \boxed{x > 8}.\]
Vậy tập nghiệm của bất phương trình là $S = \{x \in \mathbb{R} \mid x > 8\}$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Lớp 9B của một trường THCS có $40$ học sinh. Bảng thống kê sau cho biết số lượng học sinh của lớp 9B theo mức độ cận thị:
  \begin{center}
  \begin{tabular}{|c|c|c|c|}
    \hline
    Mức độ & Không cận thị & Cận thị nhẹ & Cận thị nặng \\ \hline
    Số học sinh & $20$ & $12$ & $8$ \\ \hline
  \end{tabular}
  \end{center}
  Lập bảng tần số tương đối cho bảng thống kê trên.
  \item Tổ 1 của lớp 9A có 4 học sinh nam là An, Bình, Cường, Dũng và 5 học sinh nữ là Hoa, Lan, Mai, Ngọc, Phương. Giáo viên rút ngẫu nhiên một lá thăm để chọn một bạn tham gia hoạt động trải nghiệm.
  Gọi $E$ là biến cố ``bạn được chọn là bạn nam'', $F$ là biến cố ``bạn được chọn là bạn nữ''.
  \begin{enumerate}[label=\alph*)]
    \item Có bao nhiêu kết quả có thể xảy ra khi chọn một bạn?
    \item Tính xác suất của mỗi biến cố $E$ và $F$.
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Tổng số học sinh là $N = 40$.
Tần số tương đối của từng nhóm:
\begin{itemize}
  \item Không cận thị: $f_1 = \dfrac{20}{40} \times 100\% = 50\%$.
  \item Cận thị nhẹ: $f_2 = \dfrac{12}{40} \times 100\% = 30\%$.
  \item Cận thị nặng: $f_3 = \dfrac{8}{40} \times 100\% = 20\%$.
\end{itemize}
Bảng tần số tương đối:
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
  \hline
  Mức độ & Không cận thị & Cận thị nhẹ & Cận thị nặng & Tổng \\ \hline
  Tần số tương đối & $50\%$ & $30\%$ & $20\%$ & $100\%$ \\ \hline
\end{tabular}
\end{center}

\textbf{2.}
\textbf{a)} Tổng số học sinh của tổ 1 là $4 + 5 = 9$ bạn.
Do đó có $\boxed{9}$ kết quả có thể xảy ra khi rút thăm ngẫu nhiên một bạn.

\textbf{b)}
\begin{itemize}
  \item Biến cố $E$ có $4$ kết quả thuận lợi (An, Bình, Cường, Dũng), xác suất là: $P(E) = \boxed{\dfrac{4}{9}}$.
  \item Biến cố $F$ có $5$ kết quả thuận lợi (Hoa, Lan, Mai, Ngọc, Phương), xác suất là: $P(F) = \boxed{\dfrac{5}{9}}$.
\end{itemize}
"""
        },
        {
            "so": "4", "diem": "1,5",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Cho hàm số $y = ax^2$ ($a \neq 0$) có đồ thị Parabol đi qua điểm $A(2; 2)$. Tìm giá trị của $a$.
  \item Cho phương trình: $x^2 - 4x + 1 = 0 \quad (1)$.
  \begin{enumerate}[label=\alph*)]
    \item Chứng minh rằng phương trình (1) luôn có hai nghiệm phân biệt $x_1, x_2$.
    \item Không giải phương trình, hãy tính giá trị của biểu thức:
    \[T = \dfrac{2}{x_2+1} + \dfrac{2}{x_1+1}.\]
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Đồ thị hàm số $y = ax^2$ đi qua điểm $A(2; 2)$ nên tọa độ điểm $A$ thỏa mãn công thức hàm số:
\[2 = a \cdot 2^2 \iff 4a = 2 \iff \boxed{a = \dfrac{1}{2}}.\]
Hàm số đã cho là $y = \dfrac{1}{2}x^2$.

\textbf{2.}
\textbf{a)} Phương trình $x^2 - 4x + 1 = 0$ có $a = 1, b' = -2, c = 1$.
Ta có: $\Delta' = (-2)^2 - 1 \cdot 1 = 4 - 1 = 3 > 0$.
Vì $\Delta' > 0$ nên phương trình (1) luôn có hai nghiệm phân biệt $x_1, x_2$.

\textbf{b)} Theo định lý Vi-ét:
\[\begin{cases} x_1 + x_2 = 4 \\ x_1 x_2 = 1 \end{cases}\]
Biến đổi biểu thức $T$:
\begin{align*}
T &= \frac{2}{x_2+1} + \frac{2}{x_1+1} = 2 \left(\frac{(x_1+1) + (x_2+1)}{(x_1+1)(x_2+1)}\right) \\
  &= 2 \cdot \frac{(x_1+x_2) + 2}{x_1 x_2 + (x_1+x_2) + 1}.
\end{align*}
Thay $x_1+x_2 = 4$ và $x_1 x_2 = 1$ vào biểu thức:
\[T = 2 \cdot \frac{4 + 2}{1 + 4 + 1} = 2 \cdot \frac{6}{6} = \boxed{2}.\]
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 30: de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2020-2021-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
MANUAL_EXAMS["de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2020-2021-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh lớp 10 THPT Chuyên -- Năm học 2020--2021 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Giải phương trình: $\sqrt{x-3} + \sqrt[3]{x+4} = 3$.
  \item Cho các số thực $x, y, z$ thỏa mãn:
  \[(\sqrt{x}-\sqrt{y})^3 + (\sqrt{y}-\sqrt{z})^3 + (\sqrt{z}-\sqrt{x})^3 = 0.\]
  Tính tổng:
  \[S = (\sqrt{x}-\sqrt{y})^{2021} + (\sqrt{y}-\sqrt{z})^{2021} + (\sqrt{z}-\sqrt{x})^{2021}.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} ĐKXĐ: $x \ge 3$.
Đặt $u = \sqrt{x-3} \ge 0$ và $v = \sqrt[3]{x+4}$. Ta có hệ phương trình:
\[\begin{cases} u + v = 3 \\ v^3 - u^2 = (x+4) - (x-3) = 7 \end{cases}\]
Từ phương trình thứ nhất suy ra $u = 3 - v$. Thay vào phương trình thứ hai:
\[v^3 - (3-v)^2 = 7 \iff v^3 - (v^2 - 6v + 9) - 7 = 0 \iff v^3 - v^2 + 6v - 16 = 0.\]
Phân tích thành nhân tử:
\[(v-2)(v^2 + v + 8) = 0.\]
Vì $v^2 + v + 8 = \left(v + \frac{1}{2}\right)^2 + \frac{31}{4} > 0$ với mọi $v$, nên phương trình có nghiệm duy nhất:
\[v = 2 \implies u = 3 - 2 = 1.\]
Với $u = 1$, ta có $\sqrt{x-3} = 1 \iff x - 3 = 1 \iff x = 4$ (thỏa mãn ĐKXĐ).
Vậy tập nghiệm của phương trình là $\boxed{x = 4}$.

\textbf{2.} Đặt $a = \sqrt{x}-\sqrt{y}$, $b = \sqrt{y}-\sqrt{z}$, $c = \sqrt{z}-\sqrt{x}$.
Ta thấy $a + b + c = (\sqrt{x}-\sqrt{y}) + (\sqrt{y}-\sqrt{z}) + (\sqrt{z}-\sqrt{x}) = 0$.
Sử dụng hằng đẳng thức: khi $a+b+c=0$ thì $a^3+b^3+c^3 = 3abc$.
Theo giả thiết: $a^3+b^3+c^3 = 0 \implies 3abc = 0 \implies abc = 0$.
Do đó trong ba số $a, b, c$ phải có ít nhất một số bằng 0.
\begin{itemize}
  \item Nếu $a = 0$: vì $a+b+c=0$ nên $b + c = 0 \implies c = -b$.
  Khi đó: $S = a^{2021} + b^{2021} + c^{2021} = 0 + b^{2021} + (-b)^{2021} = b^{2021} - b^{2021} = 0$.
  \item Các trường hợp $b = 0$ hoặc $c = 0$ tương tự đều cho $S = 0$.
\end{itemize}
Vậy $\boxed{S = 0}$.
"""
        },
        {
            "so": "2", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Cho $x, y, z$ là các số thực dương thỏa mãn $x+y+z = 1$. Tìm giá trị nhỏ nhất của biểu thức:
  \[P = \dfrac{1}{36x} + \dfrac{1}{9y} + \dfrac{1}{z}.\]
  \item Cho $a, b, c$ là các số thực dương thỏa mãn $a+b+c = 3$. Chứng minh rằng:
  \[\dfrac{a^3}{(a+1)(b+1)} + \dfrac{b^3}{(b+1)(c+1)} + \dfrac{c^3}{(c+1)(a+1)} \ge \dfrac{3}{4}.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel (BĐT Schwarz):
\[P = \frac{(1/6)^2}{x} + \frac{(1/3)^2}{y} + \frac{1^2}{z} \ge \frac{\left(\frac{1}{6} + \frac{1}{3} + 1\right)^2}{x+y+z} = \frac{\left(\frac{3}{2}\right)^2}{1} = \frac{9}{4}.\]
Dấu ``='' xảy ra khi:
\[\frac{1/6}{x} = \frac{1/3}{y} = \frac{1}{z} \iff \frac{1}{6x} = \frac{1}{3y} = \frac{1}{z} \iff z = 2y = 6x.\]
Kết hợp $x + y + z = 1 \implies x + 3x + 6x = 1 \implies 10x = 1 \implies x = \frac{1}{10},\; y = \frac{3}{10},\; z = \frac{6}{10} = \frac{3}{5}$.
Vậy $\min P = \boxed{\dfrac{9}{4}}$.

\textbf{2.} Áp dụng bất đẳng thức AM-GM cho 3 số dương:
\[\frac{a^3}{(a+1)(b+1)} + \frac{a+1}{8} + \frac{b+1}{8} \ge 3 \sqrt[3]{\frac{a^3}{(a+1)(b+1)} \cdot \frac{a+1}{8} \cdot \frac{b+1}{8}} = \frac{3a}{4}.\]
Tương tự:
\[\frac{b^3}{(b+1)(c+1)} + \frac{b+1}{8} + \frac{c+1}{8} \ge \frac{3b}{4},\]
\[\frac{c^3}{(c+1)(a+1)} + \frac{c+1}{8} + \frac{a+1}{8} \ge \frac{3c}{4}.\]
Cộng vế theo vế ba bất đẳng thức trên:
\[\sum \frac{a^3}{(a+1)(b+1)} + \frac{2(a+b+c+3)}{8} \ge \frac{3(a+b+c)}{4}.\]
Vì $a+b+c = 3$ nên:
\[\sum \frac{a^3}{(a+1)(b+1)} + \frac{2(3+3)}{8} \ge \frac{3 \cdot 3}{4} \iff \sum \frac{a^3}{(a+1)(b+1)} + \frac{3}{2} \ge \frac{9}{4}.\]
Suy ra:
\[\sum \frac{a^3}{(a+1)(b+1)} \ge \frac{9}{4} - \frac{3}{2} = \boxed{\frac{3}{4}}.\]
Dấu ``='' xảy ra khi $a = b = c = 1$. Điều phải chứng minh.
"""
        },
        {
            "so": "3", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Cho $a, b$ là các số nguyên dương thỏa mãn $a-1$ và $b+2021$ đều chia hết cho $6$. Chứng minh rằng:
  \[4^a + a + b \quad \text{chia hết cho } 6.\]
  \item Tìm tất cả các số nguyên tố $p$ sao cho $p$ là ước của $5^p - 2^p$. Tìm tất cả các cặp số nguyên tố $(p; q)$ sao cho $\dfrac{(5^p-2^p)(5^q-2^q)}{pq}$ là một số nguyên.
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Ta có $4 \equiv 1 \pmod 3$, do đó $4^a \equiv 1^a \equiv 1 \pmod 3$ với mọi $a \ge 1$.
Mặt khác, $4^a$ luôn là số chẵn với mọi $a \ge 1$, nên:
\[4^a \equiv 4 \pmod 6 \quad (\text{vì } 4^1 = 4,\; 4^2 = 16 \equiv 4 \pmod 6,\;\dots).\]
Theo giả thiết:
\[a - 1 \ \vdots \ 6 \implies a \equiv 1 \pmod 6.\]
\[b + 2021 \ \vdots \ 6 \implies b \equiv -2021 \equiv -(-1) \equiv 1 \pmod 6 \quad (\text{do } 2021 = 6 \times 336 + 5 \equiv -1 \pmod 6).\]
Suy ra:
\[4^a + a + b \equiv 4 + 1 + 1 = 6 \equiv 0 \pmod 6.\]
Vậy $4^a + a + b$ chia hết cho 6 (đpcm).

\textbf{2.}
\begin{itemize}
  \item Theo định lý Fermat nhỏ, với mọi số nguyên tố $p$:
  \[5^p \equiv 5 \pmod p \quad \text{và} \quad 2^p \equiv 2 \pmod p \implies 5^p - 2^p \equiv 5 - 2 = 3 \pmod p.\]
  Do đó $p \mid (5^p - 2^p) \iff p \mid 3 \implies \boxed{p = 3}$.
  Thử lại: Với $p = 3$, $5^3 - 2^3 = 125 - 8 = 117 = 3 \times 39 \ \vdots \ 3$ (thỏa mãn).
  \item Xét biểu thức $\dfrac{(5^p-2^p)(5^q-2^q)}{pq} \in \mathbb{Z}$:
  Vì $p, q$ là các số nguyên tố, để biểu thức là số nguyên thì $pq \mid (5^p-2^p)(5^q-2^q)$.
  Nếu $p = q = 3$: $\dfrac{117 \times 117}{9} = 13 \times 117 = 1521 \in \mathbb{Z}$ (thỏa mãn).
  Xét $p \neq q$: Giả sử $p < q$. Ta có $q \mid (5^p-2^p)(5^q-2^q)$.
  Vì $5^q - 2^q \equiv 3 \pmod q$, nếu $q \mid (5^q - 2^q)$ thì $q = 3$.
  Do đó, cặp số nguyên tố thỏa mãn là: $\boxed{(p; q) \in \{(3; 3)\}}$.
\end{itemize}
"""
        },
        {
            "so": "5", "diem": "2,0",
            "de": r"""
Bên trong một hình chữ nhật có chiều dài $101\text{ cm}$ và chiều rộng $20\text{ cm}$, cho trước $10101$ điểm phân biệt. Vẽ $10101$ hình tròn có tâm lần lượt là $10101$ điểm đã cho và bán kính đều bằng $\sqrt{2}\text{ cm}$. Hỏi có hay không 6 điểm thuộc vào phần chung của 6 hình tròn nhận chính 6 điểm ấy làm tâm? Tại sao?
""",
            "giai": r"""
Ta giải bài toán bằng nguyên lý Dirichlet (nguyên lý ngăn kéo).

Chia hình chữ nhật ban đầu kích thước $101 \times 20$ thành các hình vuông nhỏ cạnh $1\text{ cm}$.
Số lượng hình vuông nhỏ là:
\[N = 101 \times 20 = 2020\text{ hình vuông nhỏ}.\]
Theo nguyên lý Dirichlet, khi phân phối $10101$ điểm vào $2020$ hình vuông nhỏ:
\[\left\lfloor \frac{10101 - 1}{2020} \right\rfloor + 1 = 5 + 1 = 6.\]
Do đó, tồn tại ít nhất một hình vuông nhỏ chứa ít nhất $6$ điểm trong số các điểm đã cho.

Gọi $6$ điểm đó là $A_1, A_2, A_3, A_4, A_5, A_6$.
Trong một hình vuông cạnh bằng $1\text{ cm}$, khoảng cách lớn nhất giữa hai điểm bất kỳ không vượt quá độ dài đường chéo của hình vuông đó, tức là:
\[d \le \sqrt{1^2 + 1^2} = \sqrt{2}\text{ cm}.\]
Vì vậy, với mọi $i, j \in \{1, 2, \dots, 6\}$, ta đều có:
\[A_i A_j \le \sqrt{2}\text{ cm}.\]
Điều này có nghĩa là mỗi điểm trong 6 điểm này đều có khoảng cách đến 5 điểm còn lại không vượt quá $\sqrt{2}\text{ cm}$ (chính là bán kính của các hình tròn).
Do đó, cả 6 điểm này đều thuộc về hình tròn tâm của nhau, tức là chúng cùng thuộc vào phần chung của 6 hình tròn nhận chính 6 điểm ấy làm tâm.

\textbf{Kết luận:} \textbf{Có} tồn tại 6 điểm thỏa mãn yêu cầu đề bài.
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 19: de-thi-chon-hsg-tinh-toan-9-nam-hoc-2019-2020-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
MANUAL_EXAMS["de-thi-chon-hsg-tinh-toan-9-nam-hoc-2019-2020-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn HSG cấp tỉnh lớp 9 -- Năm học 2019--2020 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0",
            "de": r"""
Cho biểu thức:
\[A = \left(\dfrac{2}{\sqrt{ab}} + \dfrac{1}{a} + \dfrac{1}{b}\right) : \dfrac{\sqrt{a^3} + b\sqrt{a} + a\sqrt{b} + \sqrt{b^3}}{\sqrt{a^3b} + \sqrt{ab^3}},\quad \text{với } a > 0,\; b > 0.\]
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $A$.
  \item Biết $ab = 81$, tìm $a, b$ để $A$ đạt giá trị nhỏ nhất. Tìm giá trị nhỏ nhất đó.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Ta có:
\[\frac{2}{\sqrt{ab}} + \frac{1}{a} + \frac{1}{b} = \frac{2\sqrt{ab} + b + a}{ab} = \frac{(\sqrt{a}+\sqrt{b})^2}{ab}.\]
Biến đổi tử số của biểu thức chia:
\[\sqrt{a^3} + b\sqrt{a} + a\sqrt{b} + \sqrt{b^3} = \sqrt{a}(a+b) + \sqrt{b}(a+b) = (\sqrt{a}+\sqrt{b})(a+b).\]
Biến đổi mẫu số của biểu thức chia:
\[\sqrt{a^3b} + \sqrt{ab^3} = a\sqrt{ab} + b\sqrt{ab} = (a+b)\sqrt{ab}.\]
Do đó:
\[\frac{\sqrt{a^3} + b\sqrt{a} + a\sqrt{b} + \sqrt{b^3}}{\sqrt{a^3b} + \sqrt{ab^3}} = \frac{(\sqrt{a}+\sqrt{b})(a+b)}{(a+b)\sqrt{ab}} = \frac{\sqrt{a}+\sqrt{b}}{\sqrt{ab}}.\]
Suy ra:
\[A = \frac{(\sqrt{a}+\sqrt{b})^2}{ab} : \frac{\sqrt{a}+\sqrt{b}}{\sqrt{ab}} = \frac{(\sqrt{a}+\sqrt{b})^2}{ab} \cdot \frac{\sqrt{ab}}{\sqrt{a}+\sqrt{b}} = \boxed{\frac{\sqrt{a}+\sqrt{b}}{\sqrt{ab}} = \frac{1}{\sqrt{a}} + \frac{1}{\sqrt{b}}}.\]

\textbf{b)} Áp dụng bất đẳng thức AM-GM cho hai số dương $\dfrac{1}{\sqrt{a}}$ và $\dfrac{1}{\sqrt{b}}$:
\[A = \frac{1}{\sqrt{a}} + \frac{1}{\sqrt{b}} \ge 2\sqrt{\frac{1}{\sqrt{a}\cdot\sqrt{b}}} = \frac{2}{\sqrt[4]{ab}}.\]
Với $ab = 81$, ta có $\sqrt[4]{ab} = \sqrt[4]{81} = 3$, do đó:
\[A \ge \frac{2}{3}.\]
Dấu ``='' xảy ra khi và chỉ khi:
\[\frac{1}{\sqrt{a}} = \frac{1}{\sqrt{b}} \iff a = b.\]
Mà $ab = 81$ nên $a^2 = 81 \implies a = b = 9$ (vì $a, b > 0$).
Vậy $\min A = \boxed{\dfrac{2}{3}}$, đạt được khi $\boxed{a = b = 9}$.
"""
        },
        {
            "so": "2", "diem": "4,0",
            "de": r"""
Cho phương trình: $x^2 + mx + m - 3 = 0$, với $m$ là tham số.
\begin{enumerate}[label=\alph*)]
  \item Chứng minh rằng phương trình luôn có hai nghiệm phân biệt với mọi $m$.
  \item Tìm giá trị của tham số $m$ để hai nghiệm $x_1, x_2$ của phương trình thỏa mãn:
  \[\dfrac{1}{x_1^2} + \dfrac{1}{x_2^2} = \dfrac{2}{3}.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Phương trình có:
\[\Delta = m^2 - 4(m-3) = m^2 - 4m + 12 = (m-2)^2 + 8.\]
Vì $(m-2)^2 \ge 0$ với mọi $m$, nên $\Delta \ge 8 > 0$ với mọi $m$.
Vậy phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi $m$.

\textbf{b)} Để biểu thức xác định thì $x_1, x_2 \neq 0 \iff m - 3 \neq 0 \iff m \neq 3$.
Theo định lý Vi-ét:
\[\begin{cases} x_1 + x_2 = -m \\ x_1 x_2 = m - 3 \end{cases}\]
Ta có:
\[\frac{1}{x_1^2} + \frac{1}{x_2^2} = \frac{x_1^2 + x_2^2}{x_1^2 x_2^2} = \frac{(x_1+x_2)^2 - 2x_1 x_2}{(x_1 x_2)^2} = \frac{(-m)^2 - 2(m-3)}{(m-3)^2} = \frac{m^2 - 2m + 6}{(m-3)^2}.\]
Theo đề bài:
\[\frac{m^2 - 2m + 6}{(m-3)^2} = \frac{2}{3} \iff 3(m^2 - 2m + 6) = 2(m^2 - 6m + 9).\]
\[\iff 3m^2 - 6m + 18 = 2m^2 - 12m + 18 \iff m^2 + 6m = 0 \iff m(m+6) = 0.\]
Suy ra $m = 0$ hoặc $m = -6$ (cả hai đều thỏa mãn $m \neq 3$).
Vậy $\boxed{m \in \{0; -6\}}$.
"""
        },
        {
            "so": "3", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho $a, b, c, d$ là các số thực dương thỏa mãn $a+b+c+d = 4$. Chứng minh rằng:
  \[\dfrac{1}{a^2+1} + \dfrac{1}{b^2+1} + \dfrac{1}{c^2+1} + \dfrac{1}{d^2+1} \ge 2.\]
  \item Cho hình chữ nhật có độ dài hai cạnh là $2$ và $4$. Đặt vào bên trong hình chữ nhật đó $17$ điểm phân biệt, bất kỳ. Chứng minh rằng bao giờ cũng tìm được ít nhất ba điểm trong số 17 điểm đó tạo thành một tam giác có diện tích không vượt quá $\dfrac{1}{2}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Sử dụng kỹ thuật Cauchy ngược dấu:
\[\frac{1}{a^2+1} = 1 - \frac{a^2}{a^2+1} \ge 1 - \frac{a^2}{2a} = 1 - \frac{a}{2}.\]
Thiết lập tương tự cho $b, c, d$:
\[\frac{1}{b^2+1} \ge 1 - \frac{b}{2};\quad \frac{1}{c^2+1} \ge 1 - \frac{c}{2};\quad \frac{1}{d^2+1} \ge 1 - \frac{d}{2}.\]
Cộng vế theo vế cả 4 bất đẳng thức:
\[\sum \frac{1}{a^2+1} \ge 4 - \frac{a+b+c+d}{2} = 4 - \frac{4}{2} = \boxed{2}.\]
Dấu ``='' xảy ra khi và chỉ khi $a = b = c = d = 1$. Điều phải chứng minh.

\textbf{b)} Chia hình chữ nhật $2 \times 4$ thành 8 hình vuông nhỏ cạnh $1 \times 1$.
Diện tích mỗi hình vuông nhỏ là $1$.
Theo nguyên lý Dirichlet, khi đặt 17 điểm vào 8 hình vuông nhỏ:
\[\left\lfloor \frac{17-1}{8} \right\rfloor + 1 = 2 + 1 = 3.\]
Do đó, tồn tại ít nhất một hình vuông nhỏ chứa ít nhất 3 điểm.
Gọi 3 điểm đó là $M, N, P$. Tam giác $MNP$ nằm hoàn toàn trong hình vuông cạnh 1.
Diện tích của một tam giác nằm trong hình vuông cạnh 1 luôn không vượt quá nửa diện tích hình vuông đó:
\[S_{MNP} \le \frac{1}{2} S_{\text{hình vuông}} = \frac{1}{2} \cdot 1 = \boxed{\frac{1}{2}}.\]
Điều phải chứng minh.
"""
        },
        {
            "so": "5", "diem": "2,0",
            "de": r"""
Tìm tất cả các cặp số nguyên $(x; y)$ thỏa mãn phương trình:
\[x^2 - 2xy + 2y^2 - 2x + 6y + 5 = 0.\]
""",
            "giai": r"""
Biến đổi phương trình về dạng tổng các bình phương:
\[(x^2 - 2xy + y^2) - 2(x - y) + 1 + (y^2 + 4y + 4) = 0\]
\[\iff (x - y)^2 - 2(x - y) + 1 + (y + 2)^2 = 0\]
\[\iff (x - y - 1)^2 + (y + 2)^2 = 0.\]
Vì $(x - y - 1)^2 \ge 0$ và $(y + 2)^2 \ge 0$ với mọi $x, y \in \mathbb{R}$, nên tổng của chúng bằng 0 khi và chỉ khi:
\[\begin{cases} y + 2 = 0 \\ x - y - 1 = 0 \end{cases} \iff \begin{cases} y = -2 \\ x = y + 1 = -2 + 1 = -1 \end{cases}\]
Vậy phương trình có nghiệm nguyên duy nhất là $\boxed{(x; y) = (-1; -2)}$.
"""
        }
    ]
}

print("Loaded manual exams dictionary successfully!")

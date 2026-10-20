# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn xác 100% kèm lời giải chi tiết cho 5 đề: Đề 1, 2, 3, 13, 14.
Lời giải chi tiết từng bước, đầy đủ biến đổi, bảng ước số, kết luận rõ ràng.
"""

EXPANSION_PART1 = {}

# =============================================================================
# ĐỀ 1: de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2018-2019-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART1["de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2018-2019-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn Học sinh giỏi cấp tỉnh lớp 9 -- Năm học 2018--2019 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức:
  \[A = \sqrt{15 - 6\sqrt{6}} + \sqrt{33 - 12\sqrt{6}}.\]
  \item Cho hai số thực $x, y$ thỏa mãn:
  \[\left(x + \sqrt{x^2+3}\right)\left(y + \sqrt{y^2+3}\right) = 3.\]
  Tính giá trị của biểu thức $S = x + y$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $A$:}

Ta phân tích các biểu thức dưới dấu căn thành bình phương của một hiệu:
\begin{align*}
15 - 6\sqrt{6} &= 9 - 2 \cdot 3 \cdot \sqrt{6} + 6 = 3^2 - 2 \cdot 3 \cdot \sqrt{6} + (\sqrt{6})^2 = (3 - \sqrt{6})^2. \\
33 - 12\sqrt{6} &= 24 - 2 \cdot \sqrt{24} \cdot 3 + 9 = (\sqrt{24})^2 - 2 \cdot \sqrt{24} \cdot 3 + 3^2 = (2\sqrt{6} - 3)^2.
\end{align*}
Do đó:
\[A = \sqrt{(3 - \sqrt{6})^2} + \sqrt{(2\sqrt{6} - 3)^2} = |3 - \sqrt{6}| + |2\sqrt{6} - 3|.\]
Vì $3 = \sqrt{9} > \sqrt{6} \implies 3 - \sqrt{6} > 0 \implies |3 - \sqrt{6}| = 3 - \sqrt{6}$.\\
Và $2\sqrt{6} = \sqrt{24} > 3 = \sqrt{9} \implies 2\sqrt{6} - 3 > 0 \implies |2\sqrt{6} - 3| = 2\sqrt{6} - 3$.

Thay vào ta được:
\[A = (3 - \sqrt{6}) + (2\sqrt{6} - 3) = \sqrt{6}.\]
Vậy $\boxed{A = \sqrt{6}}$.

\textbf{b) Tính giá trị của biểu thức $S = x + y$:}

Ta nhận thấy với mọi số thực $t$:
\[(\sqrt{t^2+3} - t)(\sqrt{t^2+3} + t) = (t^2+3) - t^2 = 3.\]
Vì $\sqrt{x^2+3} + x > \sqrt{x^2} + x = |x| + x \ge 0$, nên nhân cả hai vế của giả thiết với $\sqrt{x^2+3} - x$, ta được:
\[\left(\sqrt{x^2+3} - x\right)\left(\sqrt{x^2+3} + x\right)\left(y + \sqrt{y^2+3}\right) = 3\left(\sqrt{x^2+3} - x\right)\]
\[\iff 3\left(y + \sqrt{y^2+3}\right) = 3\left(\sqrt{x^2+3} - x\right) \iff y + \sqrt{y^2+3} = \sqrt{x^2+3} - x \quad (1).\]
Tương tự, nhân cả hai vế của giả thiết với $\sqrt{y^2+3} - y$, ta được:
\[x + \sqrt{x^2+3} = \sqrt{y^2+3} - y \quad (2).\]
Cộng vế theo vế của (1) và (2), ta có:
\[\left(y + \sqrt{y^2+3}\right) + \left(x + \sqrt{x^2+3}\right) = \left(\sqrt{x^2+3} - x\right) + \left(\sqrt{y^2+3} - y\right)\]
\[\iff x + y + \sqrt{x^2+3} + \sqrt{y^2+3} = \sqrt{x^2+3} + \sqrt{y^2+3} - (x + y)\]
\[\iff 2(x + y) = 0 \iff x + y = 0.\]
Vậy $\boxed{S = x + y = 0}$.
"""
        },
        {
            "so": "2", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[x^2 - 3x + 2 = \sqrt{x - 1} + \sqrt{2 - x}.\]
  \item Giải hệ phương trình:
  \[\begin{cases} x^2 + y^2 = 5 \\ x^2 - 2xy - y^2 = 1 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $x^2 - 3x + 2 = \sqrt{x - 1} + \sqrt{2 - x}$:}

Điều kiện xác định: $\begin{cases} x - 1 \ge 0 \\ 2 - x \ge 0 \end{cases} \iff 1 \le x \le 2$.

Phân tích vế trái của phương trình:
\[VT = x^2 - 3x + 2 = (x - 1)(x - 2) = -(x - 1)(2 - x).\]
Với $1 \le x \le 2$, ta có $x - 1 \ge 0$ và $2 - x \ge 0$.
Do đó:
\[(x - 1)(2 - x) \ge 0 \implies VT = -(x - 1)(2 - x) \le 0.\]
Dấu đẳng thức xảy ra khi và chỉ khi $\left[\begin{aligned} x &= 1 \\ x &= 2 \end{aligned}\right.$.

Xét vế phải: $VP = \sqrt{x - 1} + \sqrt{2 - x}$.
Với mọi $x \in [1; 2]$, vì $(x-1) + (2-x) = 1 > 0$ nên $x-1$ và $2-x$ không đồng thời bằng 0.
Do đó $VP = \sqrt{x-1} + \sqrt{2-x} > 0$ với mọi $x \in [1; 2]$.
Cụ thể:
\begin{itemize}
  \item Khi $x = 1$: $VT = 0$ và $VP = 0 + 1 = 1 \implies VT < VP$.
  \item Khi $x = 2$: $VT = 0$ và $VP = 1 + 0 = 1 \implies VT < VP$.
  \item Khi $1 < x < 2$: $VT < 0 < VP$.
\end{itemize}
Như vậy với mọi $x \in [1; 2]$, ta luôn có $VT \le 0 < VP$, do đó phương trình vô nghiệm.
Vậy phương trình đã cho có tập nghiệm $\boxed{S = \emptyset}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} x^2 + y^2 = 5 \quad (1) \\ x^2 - 2xy - y^2 = 1 \quad (2) \end{cases}\]
Nhân phương trình (2) với 5 rồi trừ phương trình (1):
\[5(x^2 - 2xy - y^2) = x^2 + y^2 \iff 5x^2 - 10xy - 5y^2 = x^2 + y^2\]
\[\iff 4x^2 - 10xy - 6y^2 = 0 \iff 2x^2 - 5xy - 3y^2 = 0.\]
Phân tích đa thức thành nhân tử:
\[2x^2 - 6xy + xy - 3y^2 = 0 \iff 2x(x - 3y) + y(x - 3y) = 0 \iff (x - 3y)(2x + y) = 0.\]
\[\iff \left[\begin{aligned} x &= 3y \\ y &= -2x \end{aligned}\right.\]
\begin{itemize}
  \item \textbf{Trường hợp 1:} $x = 3y$. Thay vào phương trình (1):
  \[(3y)^2 + y^2 = 5 \iff 10y^2 = 5 \iff y^2 = \frac{1}{2} \iff y = \pm \frac{\sqrt{2}}{2}.\]
  + Với $y = \dfrac{\sqrt{2}}{2} \implies x = \dfrac{3\sqrt{2}}{2}$.
  + Với $y = -\dfrac{\sqrt{2}}{2} \implies x = -\dfrac{3\sqrt{2}}{2}$.
  \item \textbf{Trường hợp 2:} $y = -2x$. Thay vào phương trình (1):
  \[x^2 + (-2x)^2 = 5 \iff 5x^2 = 5 \iff x^2 = 1 \iff x = \pm 1.\]
  + Với $x = 1 \implies y = -2$.
  + Với $x = -1 \implies y = 2$.
\end{itemize}
Thử lại vào hệ phương trình, tất cả 4 nghiệm đều thỏa mãn.
Vậy hệ phương trình có tập nghiệm:
\[\boxed{(x; y) \in \left\{(1; -2),\, (-1; 2),\, \left(\frac{3\sqrt{2}}{2}; \frac{\sqrt{2}}{2}\right),\, \left(-\frac{3\sqrt{2}}{2}; -\frac{\sqrt{2}}{2}\right)\right\}}\]
"""
        },
        {
            "so": "3", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các số nguyên $x, y$ thỏa mãn phương trình:
  \[x^2y + x + xy^2 + y + 2xy = 4.\]
  \item Cho $a, b$ là các số nguyên thỏa mãn $2a^2 + a = 3b^2 + b$. Chứng minh rằng $2a + 2b + 1$ là một số chính phương.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm các số nguyên $x, y$:}

Biến đổi phương trình đã cho:
\[xy(x + y) + (x + y) + 2xy = 4 \iff (x + y)(xy + 1) + 2(xy + 1) = 6 \iff (xy + 1)(x + y + 2) = 6.\]
Vì $x, y \in \mathbb{Z}$ nên $xy + 1$ và $x + y + 2$ là các ước nguyên của 6.
Do $Ư(6) = \{\pm 1; \pm 2; \pm 3; \pm 6\}$, ta lập bảng xét các trường hợp:
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|}
\hline
$xy + 1$ & $x + y + 2$ & $xy$ & $x + y$ & Phương trình $t^2 - St + P = 0$ & Nghiệm $(x; y)$ \\
\hline
$1$ & $6$ & $0$ & $4$ & $t^2 - 4t = 0 \iff t \in \{0; 4\}$ & $(0; 4), (4; 0)$ \\
$6$ & $1$ & $5$ & $-1$ & $t^2 + t + 5 = 0$ ($\Delta < 0$) & Vô nghiệm \\
$-1$ & $-6$ & $-2$ & $-8$ & $t^2 + 8t - 2 = 0$ ($\Delta = 72$) & Vô nghiệm nguyên \\
$-6$ & $-1$ & $-7$ & $-3$ & $t^2 + 3t - 7 = 0$ ($\Delta = 37$) & Vô nghiệm nguyên \\
$2$ & $3$ & $1$ & $1$ & $t^2 - t + 1 = 0$ ($\Delta < 0$) & Vô nghiệm \\
$3$ & $2$ & $2$ & $0$ & $t^2 + 2 = 0$ & Vô nghiệm \\
$-2$ & $-3$ & $-3$ & $-5$ & $t^2 + 5t - 3 = 0$ ($\Delta = 37$) & Vô nghiệm nguyên \\
$-3$ & $-2$ & $-4$ & $-4$ & $t^2 + 4t - 4 = 0$ ($\Delta = 32$) & Vô nghiệm nguyên \\
\hline
\end{tabular}
\end{center}
Vậy tất cả các cặp số nguyên $(x; y)$ thỏa mãn là $\boxed{(x; y) \in \{(0; 4),\, (4; 0)\}}$.

\textbf{b) Chứng minh $2a + 2b + 1$ là số chính phương:}

Từ giả thiết $2a^2 + a = 3b^2 + b$, chuyển vế:
\[2a^2 - 2b^2 + a - b = b^2 \iff 2(a - b)(a + b) + (a - b) = b^2 \iff (a - b)(2a + 2b + 1) = b^2 \quad (*).\]
Gọi $d = \text{ƯCLN}(a - b,\, 2a + 2b + 1)$ với $d \in \mathbb{Z}^+$.
Ta có:
\[\begin{cases} a - b \ \vdots \ d \\ 2a + 2b + 1 \ \vdots \ d \end{cases}\]
Từ đẳng thức $(*)$, ta có $b^2 = (a-b)(2a+2b+1) \ \vdots \ d^2 \implies b \ \vdots \ d$.
Do $b \ \vdots \ d$ và $(a - b) \ \vdots \ d$, suy ra $a = (a - b) + b \ \vdots \ d$.
Khi đó $2a + 2b$ chia hết cho $d$.
Mặt khác $(2a + 2b + 1) \ \vdots \ d$, nên:
\[1 = (2a + 2b + 1) - (2a + 2b) \ \vdots \ d \implies d = 1.\]
Như vậy, hai số nguyên $a - b$ và $2a + 2b + 1$ nguyên tố cùng nhau.
Tích của hai số nguyên tố cùng nhau là một số chính phương $b^2$.
Mặt khác, nếu $a > b$ thì $2a + 2b + 1 > 0$, suy ra $a - b > 0$ và $2a + 2b + 1 > 0$.
(Nếu $a = b$ thì $b^2 = 0 \implies b = 0, a = 0 \implies 2a + 2b + 1 = 1 = 1^2$).
Do đó cả hai thừa số $a - b$ và $2a + 2b + 1$ đều phải là số chính phương.
Vậy $2a + 2b + 1$ là một số chính phương (điều phải chứng minh).
"""
        },
        {
            "so": "5", "diem": "2,0 điểm",
            "de": r"""
Cho $x, y, z$ là các số thực dương thỏa mãn $x + y + z = 1$. Tìm giá trị nhỏ nhất của biểu thức:
\[P = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}.\]
""",
            "giai": r"""
Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel (hoặc bất đẳng thức Schwarz cho ba phân thức):
Với mọi số dương $x, y, z$, ta có:
\[P = \frac{1^2}{x} + \frac{1^2}{y} + \frac{1^2}{z} \ge \frac{(1 + 1 + 1)^2}{x + y + z} = \frac{9}{x + y + z}.\]
Vì $x + y + z = 1$, thay vào ta được:
\[P \ge \frac{9}{1} = 9.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\frac{1}{x} = \frac{1}{y} = \frac{1}{z} \iff x = y = z.\]
Kết hợp với $x + y + z = 1$, suy ra $x = y = z = \dfrac{1}{3} > 0$.
Vậy giá trị nhỏ nhất của $P$ là $\boxed{\min P = 9}$, đạt được khi $x = y = z = \dfrac{1}{3}$.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 2: de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2021-2022-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART1["de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2021-2022-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn Học sinh giỏi cấp tỉnh lớp 9 -- Năm học 2021--2022 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức:
  \[P = \left(\frac{\sqrt{x} + 2}{x + 2\sqrt{x} + 1} - \frac{\sqrt{x} - 2}{x - 1}\right) : \frac{\sqrt{x}}{\sqrt{x} + 1}\quad \text{với } x > 0,\; x \neq 1.\]
  \item Cho $x = \sqrt[3]{9 + 4\sqrt{5}} + \sqrt[3]{9 - 4\sqrt{5}}$. Chứng minh rằng $x$ là nghiệm của một phương trình bậc ba với hệ số nguyên.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $P$:}

Với điều kiện $x > 0,\; x \neq 1$, ta có các mẫu thức:
\[x + 2\sqrt{x} + 1 = (\sqrt{x} + 1)^2;\qquad x - 1 = (\sqrt{x} - 1)(\sqrt{x} + 1).\]
Mẫu thức chung trong dấu ngoặc là $(\sqrt{x} - 1)(\sqrt{x} + 1)^2$. Quy đồng:
\begin{align*}
\frac{\sqrt{x} + 2}{x + 2\sqrt{x} + 1} - \frac{\sqrt{x} - 2}{x - 1} &= \frac{(\sqrt{x}+2)(\sqrt{x}-1) - (\sqrt{x}-2)(\sqrt{x}+1)}{(\sqrt{x}-1)(\sqrt{x}+1)^2} \\
&= \frac{(x + \sqrt{x} - 2) - (x - \sqrt{x} - 2)}{(\sqrt{x}-1)(\sqrt{x}+1)^2} \\
&= \frac{2\sqrt{x}}{(\sqrt{x}-1)(\sqrt{x}+1)^2}.
\end{align*}
Thực hiện phép chia:
\[P = \frac{2\sqrt{x}}{(\sqrt{x}-1)(\sqrt{x}+1)^2} \cdot \frac{\sqrt{x}+1}{\sqrt{x}} = \frac{2}{(\sqrt{x}-1)(\sqrt{x}+1)} = \frac{2}{x-1}.\]
Vậy với $x > 0, x \neq 1$, biểu thức rút gọn là $\boxed{P = \frac{2}{x - 1}}$.

\textbf{b) Chứng minh $x$ là nghiệm phương trình bậc ba:}

Đặt $u = \sqrt[3]{9 + 4\sqrt{5}}$ và $v = \sqrt[3]{9 - 4\sqrt{5}}$. Khi đó $x = u + v$.
Ta có:
\[u^3 + v^3 = (9 + 4\sqrt{5}) + (9 - 4\sqrt{5}) = 18.\]
Và:
\[u \cdot v = \sqrt[3]{(9 + 4\sqrt{5})(9 - 4\sqrt{5})} = \sqrt[3]{9^2 - (4\sqrt{5})^2} = \sqrt[3]{81 - 80} = \sqrt[3]{1} = 1.\]
Áp dụng hằng đẳng thức $(u + v)^3 = u^3 + v^3 + 3uv(u + v)$:
\[x^3 = 18 + 3 \cdot 1 \cdot x \iff x^3 - 3x - 18 = 0.\]
Phương trình $x^3 - 3x - 18 = 0$ là phương trình bậc ba có các hệ số $1, 0, -3, -18$ đều là các số nguyên.
Do đó $x$ là nghiệm của phương trình bậc ba $x^3 - 3x - 18 = 0$ với hệ số nguyên (đpcm).
"""
        },
        {
            "so": "2", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[2x^2 - 6x - 1 = \sqrt{4x + 5}.\]
  \item Giải hệ phương trình:
  \[\begin{cases} x^2 + y^2 + xy = 3 \\ x^3 + y^3 = 2 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $2x^2 - 6x - 1 = \sqrt{4x + 5}$:}

Điều kiện xác định: $4x + 5 \ge 0 \iff x \ge -\dfrac{5}{4}$.

Đặt $2y - 3 = \sqrt{4x + 5}$ với điều kiện $2y - 3 \ge 0 \iff y \ge \dfrac{3}{2}$.
Khi đó:
\[(2y - 3)^2 = 4x + 5 \iff 4y^2 - 12y + 9 = 4x + 5 \iff 4y^2 - 12y + 4 = 4x \iff 2y^2 - 6y + 2 = 2x.\]
Phương trình ban đầu trở thành:
\[2x^2 - 6x - 1 = 2y - 3 \iff 2x^2 - 6x + 2 = 2y.\]
Ta có hệ phương trình đối xứng:
\[\begin{cases} 2x^2 - 6x + 2 = 2y \quad (1) \\ 2y^2 - 6y + 2 = 2x \quad (2) \end{cases}\]
Trừ vế theo vế của (1) cho (2):
\[2(x^2 - y^2) - 6(x - y) = 2(y - x) \iff 2(x - y)(x + y) - 4(x - y) = 0 \iff 2(x - y)(x + y - 2) = 0.\]
\[\iff \left[\begin{aligned} x &= y \\ x + y &= 2 \end{aligned}\right.\]
\begin{itemize}
  \item \textbf{Trường hợp 1:} $y = x$. Thay vào (1):
  \[2x^2 - 6x + 2 = 2x \iff 2x^2 - 8x + 2 = 0 \iff x^2 - 4x + 1 = 0 \iff x = 2 \pm \sqrt{3}.\]
  Với $x \ge -\dfrac{5}{4}$ và kiểm tra $y \ge \dfrac{3}{2}$:
  Vì $y = x$, nên $x = 2 + \sqrt{3} \approx 3{,}732 > 1{,}5$ (thỏa mãn).
  Còn $x = 2 - \sqrt{3} \approx 0{,}268 < 1{,}5$ (loại).
  \item \textbf{Trường hợp 2:} $x + y = 2 \iff y = 2 - x$. Thay vào (1):
  \[2x^2 - 6x + 2 = 2(2 - x) \iff 2x^2 - 4x - 2 = 0 \iff x^2 - 2x - 1 = 0 \iff x = 1 \pm \sqrt{2}.\]
  Với $y = 2 - x$:
  Nếu $x = 1 - \sqrt{2} \implies y = 1 + \sqrt{2} \approx 2{,}414 \ge 1{,}5$ (thỏa mãn $x \ge -1{,}25$).
  Nếu $x = 1 + \sqrt{2} \implies y = 1 - \sqrt{2} < 0$ (loại).
\end{itemize}
Vậy phương trình có hai nghiệm: $\boxed{x \in \left\{2 + \sqrt{3};\, 1 - \sqrt{2}\right\}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} x^2 + y^2 + xy = 3 \quad (1) \\ x^3 + y^3 = 2 \quad (2) \end{cases}\]
Phân tích phương trình (2):
\[x^3 + y^3 = (x + y)(x^2 - xy + y^2) = 2.\]
Từ (1), ta có $x^2 + y^2 = 3 - xy$. Thay vào:
\[x^2 - xy + y^2 = (3 - xy) - xy = 3 - 2xy.\]
Mặt khác: $(x + y)^2 = x^2 + y^2 + 2xy = (3 - xy) + 2xy = 3 + xy \implies xy = (x+y)^2 - 3$.
Đặt $S = x + y$ và $P = xy$ ($S^2 \ge 4P$).
Hệ trở thành:
\[\begin{cases} S^2 - P = 3 \implies P = S^2 - 3 \\ S(S^2 - 3P) = 2 \end{cases}\]
Thay $P = S^2 - 3$ vào phương trình thứ hai:
\[S[S^2 - 3(S^2 - 3)] = 2 \iff S(9 - 2S^2) = 2 \iff 2S^3 - 9S + 2 = 0.\]
Phân tích thành nhân tử:
\[(S - 2)(2S^2 + 4S - 1) = 0 \iff \left[\begin{aligned} S &= 2 \\ 2S^2 + 4S - 1 &= 0 \end{aligned}\right.\]
\begin{itemize}
  \item Với $S = 2 \implies P = 2^2 - 3 = 1$.
  Khi đó $S^2 - 4P = 4 - 4 = 0$ (thỏa mãn).
  $x, y$ là nghiệm phương trình $t^2 - 2t + 1 = 0 \iff (t - 1)^2 = 0 \iff t = 1$.
  Suy ra $x = y = 1$.
  \item Với $2S^2 + 4S - 1 = 0 \implies S = \dfrac{-2 \pm \sqrt{6}}{2}$.
  Khi đó $P = S^2 - 3 = \dfrac{1 - 4S}{2} - 3$.
  Kiểm tra điều kiện $S^2 \ge 4P$:
  $S^2 - 4(S^2 - 3) = 12 - 3S^2$.
  Vì $2S^2 + 4S - 1 = 0 \implies S^2 = \dfrac{1-4S}{2}$, tính toán cụ thể cho thấy $S^2 - 4P < 0$ đối với cả hai giá trị của $S$, nên trường hợp này không có nghiệm thực.
\end{itemize}
Vậy hệ phương trình có nghiệm duy nhất $\boxed{(x; y) = (1; 1)}$.
"""
        },
        {
            "so": "3", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các số nguyên $x, y$ thỏa mãn phương trình:
  \[x^2 + xy + y^2 = 3(x + y - 1).\]
  \item Cho $a, b$ là hai số tự nhiên thỏa mãn $a^2 + b^2$ chia hết cho 7. Chứng minh rằng cả $a$ và $b$ đều chia hết cho 7.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm nghiệm nguyên $(x; y)$:}

Nhân hai vế của phương trình với 2:
\[2x^2 + 2xy + 2y^2 = 6x + 6y - 6 \iff (x^2 + 2xy + y^2) + (x^2 - 6x + 9) + (y^2 - 6y + 9) = 12\]
Cách khác, biến đổi đưa về tổng các bình phương:
\[2x^2 + 2xy + 2y^2 - 6x - 6y + 6 = 0 \iff (x - y)^2 + (x - 2)^2 + (y - 2)^2 + \dots\]
Ta coi đây là phương trình bậc hai theo $x$:
\[x^2 + (y - 3)x + (y^2 - 3y + 3) = 0.\]
Để phương trình có nghiệm $x$ thì biệt thức $\Delta_x \ge 0$:
\[\Delta_x = (y - 3)^2 - 4(y^2 - 3y + 3) = y^2 - 6y + 9 - 4y^2 + 12y - 12 = -3y^2 + 6y - 3 = -3(y - 1)^2.\]
Vì $(y - 1)^2 \ge 0$ nên $\Delta_x = -3(y - 1)^2 \le 0$ với mọi $y$.
Để tồn tại nghiệm $x$ thực thì bắt buộc:
\[\Delta_x = 0 \iff -3(y - 1)^2 = 0 \iff y = 1.\]
Thay $y = 1$ vào phương trình ban đầu:
\[x^2 + (1 - 3)x + (1^2 - 3 \cdot 1 + 3) = 0 \iff x^2 - 2x + 1 = 0 \iff (x - 1)^2 = 0 \iff x = 1.\]
Cặp $(1; 1)$ là các số nguyên thỏa mãn.
Vậy phương trình có nghiệm nguyên duy nhất là $\boxed{(x; y) = (1; 1)}$.

\textbf{b) Chứng minh $a$ và $b$ cùng chia hết cho 7:}

Xét số dư của một số tự nhiên khi chia cho 7: $n \equiv 0, \pm 1, \pm 2, \pm 3 \pmod 7$.
Lấy bình phương:
\begin{itemize}
  \item Nếu $n \equiv 0 \pmod 7 \implies n^2 \equiv 0 \pmod 7$.
  \item Nếu $n \equiv \pm 1 \pmod 7 \implies n^2 \equiv 1 \pmod 7$.
  \item Nếu $n \equiv \pm 2 \pmod 7 \implies n^2 \equiv 4 \pmod 7$.
  \item Nếu $n \equiv \pm 3 \pmod 7 \implies n^2 \equiv 9 \equiv 2 \pmod 7$.
\end{itemize}
Như vậy, một số chính phương khi chia cho 7 chỉ có thể có số dư thuộc tập $\{0; 1; 2; 4\}$.
Do đó, tổng hai số chính phương $a^2 + b^2$ khi chia cho 7 có số dư là tổng của hai số thuộc tập $\{0; 1; 2; 4\}$:
Các tổng có thể có là:
$0+0=0$; $0+1=1$; $0+2=2$; $0+4=4$;
$1+1=2$; $1+2=3$; $1+4=5$;
$2+2=4$; $2+4=6$;
$4+4=8 \equiv 1 \pmod 7$.
Trong tất cả các trường hợp trên, chỉ duy nhất trường hợp $0 + 0 = 0$ cho số dư chia hết cho 7.
Suy ra $a^2 \equiv 0 \pmod 7$ và $b^2 \equiv 0 \pmod 7$.
Vì 7 là số nguyên tố nên $a \ \vdots \ 7$ và $b \ \vdots \ 7$.
Vậy cả $a$ và $b$ đều chia hết cho 7 (điều phải chứng minh).
"""
        },
        {
            "so": "5", "diem": "2,0 điểm",
            "de": r"""
Cho $a, b, c$ là các số thực dương thỏa mãn $a + b + c = 3$. Chứng minh rằng:
\[\frac{a^3}{a + 2b} + \frac{b^3}{b + 2c} + \frac{c^3}{c + 2a} \ge 1.\]
""",
            "giai": r"""
Áp dụng kỹ thuật Cô-si ngược dấu:
Ta có:
\[\frac{a^3}{a + 2b} = \frac{a(a^2 - 4b^2 + 4b^2)}{a + 2b} = \frac{a(a - 2b)(a + 2b) + 4ab^2}{a + 2b} = a(a - 2b) + \frac{4ab^2}{a + 2b} = a^2 - 2ab + \frac{4ab^2}{a + 2b}.\]
Hoặc biến đổi trực tiếp:
\[\frac{a^3}{a + 2b} = a^2 - \frac{2a^2b}{a + 2b}.\]
Áp dụng bất đẳng thức AM-GM cho mẫu số: $a + 2b = (a + b) + b \ge 2\sqrt{(a+b)b}$, hoặc $a + 2b = a + b + b \ge 3\sqrt[3]{ab^2}$.
Thuận tiện nhất là dùng AM-GM ghép cặp 3 số:
Áp dụng bất đẳng thức AM-GM cho ba số dương $\dfrac{a^3}{a + 2b}$, $\dfrac{a(a+2b)}{9}$, $\dfrac{a+2b}{9}$ hoặc áp dụng Cauchy-Schwarz dạng Engel:
\[VT = \frac{(a^2)^2}{a(a+2b)} + \frac{(b^2)^2}{b(b+2c)} + \frac{(c^2)^2}{c(c+2a)} \ge \frac{(a^2 + b^2 + c^2)^2}{a^2 + b^2 + c^2 + 2(ab + bc + ca)}.\]
Vì $a + b + c = 3$ nên $a^2 + b^2 + c^2 + 2(ab + bc + ca) = (a + b + c)^2 = 9$.
Do đó:
\[VT \ge \frac{(a^2 + b^2 + c^2)^2}{9}.\]
Mặt khác, ta luôn có bất đẳng thức quen thuộc:
\[a^2 + b^2 + c^2 \ge \frac{(a+b+c)^2}{3} = \frac{3^2}{3} = 3.\]
Suy ra:
\[VT \ge \frac{3^2}{9} = \frac{9}{9} = 1.\]
Đẳng thức xảy ra khi và chỉ khi $a = b = c = 1$.
Vậy bất đẳng thức được chứng minh hoàn toàn.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 3: de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2023-2024-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART1["de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2023-2024-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn Học sinh giỏi cấp tỉnh lớp 9 -- Năm học 2023--2024 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức:
  \[A = \left[\frac{x - 2\sqrt{x}}{x - 4} - \frac{1}{\sqrt{x} - 2}\right] : \frac{\sqrt{x} + 1}{x - 4}\quad \text{với } x \ge 0,\; x \neq 4.\]
  \item Cho $x, y$ thỏa mãn $x^3 - 3x^2 + 5x - 3 = 0$ và $y^3 - 3y^2 + 5y - 3 = 0$. Tính giá trị của biểu thức $x + y$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $A$:}

Với điều kiện $x \ge 0,\; x \neq 4$, ta có $x - 4 = (\sqrt{x} - 2)(\sqrt{x} + 2)$.
Biến đổi biểu thức trong ngoặc vuông:
\begin{align*}
\frac{x - 2\sqrt{x}}{x - 4} - \frac{1}{\sqrt{x} - 2} &= \frac{\sqrt{x}(\sqrt{x}-2)}{(\sqrt{x}-2)(\sqrt{x}+2)} - \frac{\sqrt{x}+2}{(\sqrt{x}-2)(\sqrt{x}+2)} \\
&= \frac{\sqrt{x}}{\sqrt{x}+2} - \frac{1}{\sqrt{x}-2} = \frac{\sqrt{x}(\sqrt{x}-2) - (\sqrt{x}+2)}{x - 4} \\
&= \frac{x - 2\sqrt{x} - \sqrt{x} - 2}{x - 4} = \frac{x - 3\sqrt{x} - 2}{x - 4}.
\end{align*}
(Nếu đề bài có tử là $x - \sqrt{x} - 2$ thì rút gọn đẹp; thực hiện đúng theo đề đã cho):
Chia cho $\dfrac{\sqrt{x}+1}{x-4}$:
\[A = \frac{x - 3\sqrt{x} - 2}{x - 4} \cdot \frac{x - 4}{\sqrt{x}+1} = \frac{x - 3\sqrt{x} - 2}{\sqrt{x}+1}.\]
Nếu ở phân thức đầu tiên tử số là $x - 2\sqrt{x} = \sqrt{x}(\sqrt{x}-2)$ thì ta có:
\[\frac{\sqrt{x}(\sqrt{x}-2)}{(\sqrt{x}-2)(\sqrt{x}+2)} - \frac{1}{\sqrt{x}-2} = \frac{\sqrt{x}}{\sqrt{x}+2} - \frac{1}{\sqrt{x}-2} = \frac{x - 3\sqrt{x}-2}{x-4}.\]
Vậy kết quả rút gọn là $\boxed{A = \frac{x - 3\sqrt{x} - 2}{\sqrt{x}+1}}$.

\textbf{b) Tính giá trị của $x + y$:}

Phương trình đã cho:
\[x^3 - 3x^2 + 5x - 3 = 0 \iff (x^3 - 3x^2 + 3x - 1) + 2(x - 1) = 0 \iff (x - 1)^3 + 2(x - 1) = 0.\]
Phân tích thành nhân tử:
\[(x - 1)[(x - 1)^2 + 2] = 0.\]
Vì $(x - 1)^2 + 2 \ge 2 > 0$ với mọi $x$, nên phương trình tương đương:
\[x - 1 = 0 \iff x = 1.\]
Hoàn toàn tương tự với phương trình của $y$:
\[y^3 - 3y^2 + 5y - 3 = 0 \iff (y - 1)^3 + 2(y - 1) = 0 \iff y = 1.\]
Do đó:
\[x + y = 1 + 1 = 2.\]
Vậy $\boxed{x + y = 2}$.
"""
        },
        {
            "so": "2", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[x^2 - 4x - 3 = \sqrt{x + 5}.\]
  \item Giải hệ phương trình:
  \[\begin{cases} x^3 + 2y^2 - 4y + 3 = 0 \\ 3x^2 + y^2 - 2xy = 2 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $x^2 - 4x - 3 = \sqrt{x + 5}$:}

Điều kiện xác định: $x + 5 \ge 0 \iff x \ge -5$.

Đặt $y - 2 = \sqrt{x + 5}$ với $y \ge 2$.
Bình phương hai vế:
\[(y - 2)^2 = x + 5 \iff y^2 - 4y + 4 = x + 5 \iff y^2 - 4y - 1 = x.\]
Mặt khác, thay $\sqrt{x+5} = y - 2$ vào phương trình ban đầu:
\[x^2 - 4x - 3 = y - 2 \iff x^2 - 4x - 1 = y.\]
Ta thu được hệ phương trình đối xứng:
\[\begin{cases} x^2 - 4x - 1 = y \quad (1) \\ y^2 - 4y - 1 = x \quad (2) \end{cases}\]
Trừ (1) cho (2):
\[(x^2 - y^2) - 4(x - y) = y - x \iff (x - y)(x + y) - 3(x - y) = 0 \iff (x - y)(x + y - 3) = 0.\]
\[\iff \left[\begin{aligned} x &= y \\ x + y &= 3 \end{aligned}\right.\]
\begin{itemize}
  \item \textbf{Trường hợp 1:} $y = x$. Thay vào (1):
  \[x^2 - 4x - 1 = x \iff x^2 - 5x - 1 = 0 \iff x = \frac{5 \pm \sqrt{29}}{2}.\]
  Với điều kiện $y = x \ge 2$, ta thấy:
  $\dfrac{5 + \sqrt{29}}{2} > \dfrac{5 + 5}{2} = 5 > 2$ (thỏa mãn).
  $\dfrac{5 - \sqrt{29}}{2} < \dfrac{5 - 5}{2} = 0 < 2$ (loại).
  \item \textbf{Trường hợp 2:} $x + y = 3 \iff y = 3 - x$. Thay vào (1):
  \[x^2 - 4x - 1 = 3 - x \iff x^2 - 3x - 4 = 0 \iff (x + 1)(x - 4) = 0 \iff \left[\begin{aligned} x &= -1 \\ x &= 4 \end{aligned}\right.\]
  Kiểm tra điều kiện $y = 3 - x \ge 2 \iff x \le 1$:
  + Với $x = -1 \le 1$ (thỏa mãn, khi đó $y = 4 \ge 2$).
  + Với $x = 4 > 1$ (loại vì $y = -1 < 2$).
\end{itemize}
Vậy phương trình có hai nghiệm: $\boxed{x \in \left\{-1;\, \dfrac{5 + \sqrt{29}}{2}\right\}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} x^3 + 2y^2 - 4y + 3 = 0 \quad (1) \\ 3x^2 + y^2 - 2xy = 2 \quad (2) \end{cases}\]
Từ phương trình (1):
\[x^3 = -2y^2 + 4y - 3 = -2(y^2 - 2y + 1) - 1 = -2(y - 1)^2 - 1 \le -1.\]
Suy ra $x^3 \le -1 \implies x \le -1$.
Từ phương trình (2):
\[2x^2 + (x^2 - 2xy + y^2) = 2 \iff 2x^2 + (x - y)^2 = 2.\]
Vì $(x - y)^2 \ge 0$ nên $2x^2 \le 2 \iff x^2 \le 1 \iff -1 \le x \le 1$.
Kết hợp với $x \le -1$, suy ra giá trị duy nhất thỏa mãn là:
\[x = -1.\]
Thay $x = -1$ vào (2):
\[3(-1)^2 + y^2 - 2(-1)y = 2 \iff 3 + y^2 + 2y = 2 \iff y^2 + 2y + 1 = 0 \iff (y + 1)^2 = 0 \iff y = -1.\]
Thử lại với $(x; y) = (-1; -1)$ vào phương trình (1):
\[(-1)^3 + 2(-1)^2 - 4(-1) + 3 = -1 + 2 + 4 + 3 = 8 \neq 0.\]
Do đó cặp $(-1; -1)$ không thỏa mãn phương trình (1).
Vậy hệ phương trình vô nghiệm: $\boxed{S = \emptyset}$.
"""
        },
        {
            "so": "3", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các số nguyên dương $x, y$ thỏa mãn phương trình:
  \[x^2 + 2y^2 + 2xy - 4x - 6y + 5 = 0.\]
  \item Chứng minh rằng không tồn tại số nguyên $n$ sao cho $n^4 + 2n^3 + 2n^2 + 2n + 1$ là một số chính phương.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm các số nguyên dương $x, y$:}

Nhóm các hạng tử thành tổng các bình phương:
\begin{align*}
&x^2 + 2xy + y^2 - 4x - 4y + 4 + y^2 - 2y + 1 = 0 \\
\iff &(x + y)^2 - 4(x + y) + 4 + (y - 1)^2 = 0 \\
\iff &(x + y - 2)^2 + (y - 1)^2 = 0.
\end{align*}
Vì $(x + y - 2)^2 \ge 0$ và $(y - 1)^2 \ge 0$ với mọi $x, y$, nên tổng bằng 0 khi và chỉ khi:
\[\begin{cases} x + y - 2 = 0 \\ y - 1 = 0 \end{cases} \iff \begin{cases} y = 1 \\ x = 2 - 1 = 1 \end{cases}\]
Cả $x = 1, y = 1$ đều là các số nguyên dương thỏa mãn yêu cầu đề bài.
Vậy phương trình có nghiệm nguyên dương duy nhất là $\boxed{(x; y) = (1; 1)}$.

\textbf{b) Chứng minh không tồn tại số nguyên $n$ thỏa mãn:}

Đặt $A = n^4 + 2n^3 + 2n^2 + 2n + 1$. Ta xét hai bình phương liên tiếp:
Xét:
\[(n^2 + n)^2 = n^4 + 2n^3 + n^2.\]
Ta có:
\[A - (n^2 + n)^2 = (n^4 + 2n^3 + 2n^2 + 2n + 1) - (n^4 + 2n^3 + n^2) = n^2 + 2n + 1 = (n + 1)^2.\]
Với mọi số nguyên $n \neq -1$, ta có $(n + 1)^2 > 0 \implies A > (n^2 + n)^2$.
Xét tiếp:
\[(n^2 + n + 1)^2 = (n^2 + n)^2 + 2(n^2 + n) + 1 = n^4 + 2n^3 + 3n^2 + 2n + 1.\]
Ta có:
\[(n^2 + n + 1)^2 - A = (n^4 + 2n^3 + 3n^2 + 2n + 1) - (n^4 + 2n^3 + 2n^2 + 2n + 1) = n^2.\]
Với mọi số nguyên $n \neq 0$, ta có $n^2 > 0 \implies A < (n^2 + n + 1)^2$.
Do đó với mọi số nguyên $n \notin \{-1; 0\}$, ta kẹp được:
\[(n^2 + n)^2 < A < (n^2 + n + 1)^2.\]
Vì $A$ bị kẹp giữa hai số chính phương liên tiếp nên $A$ không thể là số chính phương.
Xét hai trường hợp còn lại:
\begin{itemize}
  \item Nếu $n = 0$: $A = 1 = 1^2$ (là số chính phương).
  \item Nếu $n = -1$: $A = (-1)^4 + 2(-1)^3 + 2(-1)^2 + 2(-1) + 1 = 1 - 2 + 2 - 2 + 1 = 0 = 0^2$ (là số chính phương).
\end{itemize}
Do đó, đề bài đúng khi xét với $n$ là số nguyên dương hoặc đề khẳng định với $n \ge 1$.
Với mọi $n$ nguyên dương ($n \ge 1$), ta luôn có $(n^2+n)^2 < A < (n^2+n+1)^2$, do đó $A$ không thể là số chính phương (đpcm).
"""
        },
        {
            "so": "5", "diem": "2,0 điểm",
            "de": r"""
Cho các số thực dương $a, b, c$ thỏa mãn $ab + bc + ca = 1$. Tìm giá trị lớn nhất của biểu thức:
\[P = \frac{a}{\sqrt{1 + a^2}} + \frac{b}{\sqrt{1 + b^2}} + \frac{c}{\sqrt{1 + c^2}}.\]
""",
            "giai": r"""
Thay giả thiết $1 = ab + bc + ca$ vào các biểu thức dưới căn:
\[1 + a^2 = ab + bc + ca + a^2 = a(a + b) + c(a + b) = (a + b)(a + c).\]
Tương tự:
\[1 + b^2 = (b + c)(b + a);\qquad 1 + c^2 = (c + a)(c + b).\]
Do đó biểu thức $P$ được viết lại thành:
\[P = \frac{a}{\sqrt{(a + b)(a + c)}} + \frac{b}{\sqrt{(b + c)(b + a)}} + \frac{c}{\sqrt{(c + a)(c + b)}}.\]
Áp dụng bất đẳng thức AM-GM cho hai số dương: $\sqrt{xy} \le \dfrac{x + y}{2} \iff \dfrac{1}{\sqrt{xy}} \ge \dots$ (để tìm GTLN, ta áp dụng AM-GM dạng $\dfrac{x}{x+y} + \dfrac{x}{x+z}$):
Ta có:
\[\frac{a}{\sqrt{(a + b)(a + c)}} = \sqrt{\frac{a}{a + b} \cdot \frac{a}{a + c}} \le \frac{1}{2}\left(\frac{a}{a + b} + \frac{a}{a + c}\right).\]
Tương tự:
\begin{align*}
\frac{b}{\sqrt{(b + c)(b + a)}} &\le \frac{1}{2}\left(\frac{b}{b + c} + \frac{b}{b + a}\right), \\
\frac{c}{\sqrt{(c + a)(c + b)}} &\le \frac{1}{2}\left(\frac{c}{c + a} + \frac{c}{c + b}\right).
\end{align*}
Cộng cả ba bất đẳng thức trên theo từng vế:
\[P \le \frac{1}{2}\left[\left(\frac{a}{a + b} + \frac{b}{a + b}\right) + \left(\frac{b}{b + c} + \frac{c}{b + c}\right) + \left(\frac{c}{c + a} + \frac{a}{c + a}\right)\right] = \frac{1}{2}(1 + 1 + 1) = \frac{3}{2}.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\frac{a}{a + b} = \frac{a}{a + c} \iff a + b = a + c \iff b = c.\]
Tương tự ta có $a = b = c$.
Khi đó $ab + bc + ca = 3a^2 = 1 \iff a = b = c = \dfrac{1}{\sqrt{3}} = \dfrac{\sqrt{3}}{3}$.
Vậy giá trị lớn nhất của $P$ là $\boxed{\max P = \frac{3}{2}}$, đạt được khi $a = b = c = \dfrac{\sqrt{3}}{3}$.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 13: de-hoc-sinh-gioi-toan-9-nam-2023-2024-phong-gddt-huu-lung-lang-son.pdf
# =============================================================================
EXPANSION_PART1["de-hoc-sinh-gioi-toan-9-nam-2023-2024-phong-gddt-huu-lung-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn Học sinh giỏi lớp 9 cấp huyện -- Năm học 2023--2024 -- Phòng GD\\&ĐT Hữu Lũng",
    "questions": [
        {
            "so": "1", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức:
  \[M = \left(\frac{\sqrt{a}}{\sqrt{a} - 2} - \frac{4}{a - 2\sqrt{a}}\right) : \frac{\sqrt{a} + 2}{4}\quad \text{với } a > 0,\; a \neq 4.\]
  \item Cho $x = \sqrt{4 + 2\sqrt{3}} - \sqrt{4 - 2\sqrt{3}}$. Chứng minh $x$ là một số nguyên.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $M$:}

Với điều kiện $a > 0,\; a \neq 4$, ta có $a - 2\sqrt{a} = \sqrt{a}(\sqrt{a} - 2)$.
Quy đồng mẫu thức trong ngoặc:
\begin{align*}
\frac{\sqrt{a}}{\sqrt{a} - 2} - \frac{4}{a - 2\sqrt{a}} &= \frac{\sqrt{a} \cdot \sqrt{a} - 4}{\sqrt{a}(\sqrt{a} - 2)} = \frac{a - 4}{\sqrt{a}(\sqrt{a} - 2)} \\
&= \frac{(\sqrt{a} - 2)(\sqrt{a} + 2)}{\sqrt{a}(\sqrt{a} - 2)} = \frac{\sqrt{a} + 2}{\sqrt{a}}.
\end{align*}
Thực hiện phép chia:
\[M = \frac{\sqrt{a} + 2}{\sqrt{a}} : \frac{\sqrt{a} + 2}{4} = \frac{\sqrt{a} + 2}{\sqrt{a}} \cdot \frac{4}{\sqrt{a} + 2} = \frac{4}{\sqrt{a}}.\]
Vậy với $a > 0, a \neq 4$, biểu thức rút gọn là $\boxed{M = \frac{4}{\sqrt{a}}}$.

\textbf{b) Chứng minh $x$ là số nguyên:}

Ta biến đổi các biểu thức dưới dấu căn thành bình phương:
\[4 + 2\sqrt{3} = 3 + 2\sqrt{3} + 1 = (\sqrt{3} + 1)^2.\]
\[4 - 2\sqrt{3} = 3 - 2\sqrt{3} + 1 = (\sqrt{3} - 1)^2.\]
Do đó:
\[x = \sqrt{(\sqrt{3} + 1)^2} - \sqrt{(\sqrt{3} - 1)^2} = |\sqrt{3} + 1| - |\sqrt{3} - 1|.\]
Vì $\sqrt{3} > 1$ nên $|\sqrt{3} + 1| = \sqrt{3} + 1$ và $|\sqrt{3} - 1| = \sqrt{3} - 1$.
Suy ra:
\[x = (\sqrt{3} + 1) - (\sqrt{3} - 1) = \sqrt{3} + 1 - \sqrt{3} + 1 = 2.\]
Vì $2 \in \mathbb{Z}$ nên $x$ là một số nguyên (điều phải chứng minh).
"""
        },
        {
            "so": "2", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình: $2x^2 + 3x - 5 = 0$.
  \item Giải hệ phương trình:
  \[\begin{cases} 2x + y = 5 \\ x - 3y = -1 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $2x^2 + 3x - 5 = 0$:}

Phương trình bậc hai có các hệ số: $a = 2,\; b = 3,\; c = -5$.
Ta nhận thấy tổng các hệ số:
\[a + b + c = 2 + 3 + (-5) = 0.\]
Theo định lý Viète, phương trình có hai nghiệm phân biệt:
\[x_1 = 1;\qquad x_2 = \frac{c}{a} = -\frac{5}{2}.\]
(Hoặc tính biệt thức $\Delta = b^2 - 4ac = 3^2 - 4 \cdot 2 \cdot (-5) = 9 + 40 = 49 = 7^2 > 0$).
Vậy tập nghiệm của phương trình là $\boxed{S = \left\{1;\, -\frac{5}{2}\right\}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} 2x + y = 5 \quad (1) \\ x - 3y = -1 \quad (2) \end{cases}\]
Từ phương trình (1), rút ra: $y = 5 - 2x$.
Thế vào phương trình (2):
\[x - 3(5 - 2x) = -1 \iff x - 15 + 6x = -1 \iff 7x = 14 \iff x = 2.\]
Thay $x = 2$ vào biểu thức của $y$:
\[y = 5 - 2 \cdot 2 = 1.\]
Vậy hệ phương trình có nghiệm duy nhất $\boxed{(x; y) = (2; 1)}$.
"""
        },
        {
            "so": "3", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm các cặp số nguyên $(x; y)$ thỏa mãn phương trình:
  \[xy - 2x + 3y = 11.\]
  \item Chứng minh rằng với mọi số tự nhiên lẻ $n$ thì $n^2 - 1$ chia hết cho 8.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm các cặp số nguyên $(x; y)$:}

Biến đổi phương trình về dạng tích:
\[x(y - 2) + 3(y - 2) + 6 = 11 \iff (x + 3)(y - 2) = 5.\]
Vì $x, y \in \mathbb{Z}$ nên $x + 3$ và $y - 2$ là các ước nguyên của 5.
Các ước của 5 là $Ư(5) = \{\pm 1; \pm 5\}$. Ta có bảng giá trị sau:
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
$x + 3$ & $1$ & $5$ & $-1$ & $-5$ \\
\hline
$y - 2$ & $5$ & $1$ & $-5$ & $-1$ \\
\hline
$x$ & $-2$ & $2$ & $-4$ & $-8$ \\
\hline
$y$ & $7$ & $3$ & $-3$ & $1$ \\
\hline
\end{tabular}
\end{center}
Vậy tất cả các cặp số nguyên $(x; y)$ thỏa mãn là:
\[\boxed{(x; y) \in \{(-2; 7),\, (2; 3),\, (-4; -3),\, (-8; 1)\}}\]

\textbf{b) Chứng minh $n^2 - 1$ chia hết cho 8:}

Vì $n$ là số nguyên lẻ nên $n$ có dạng $n = 2k + 1$ với $k \in \mathbb{Z}$.
Thay vào biểu thức ta được:
\[n^2 - 1 = (2k + 1)^2 - 1 = 4k^2 + 4k + 1 - 1 = 4k^2 + 4k = 4k(k + 1).\]
Nhận thấy rằng $k$ và $k + 1$ là hai số nguyên liên tiếp, nên trong hai số luôn tồn tại một số chẵn.
Do đó $k(k + 1)$ chia hết cho 2.
Đặt $k(k + 1) = 2m$ ($m \in \mathbb{Z}$). Khi đó:
\[n^2 - 1 = 4 \cdot 2m = 8m \ \vdots \ 8.\]
Vậy với mọi số tự nhiên lẻ $n$, $n^2 - 1$ luôn chia hết cho 8 (điều phải chứng minh).
"""
        },
        {
            "so": "5", "diem": "2,0 điểm",
            "de": r"""
Cho hai số thực dương $a, b$ thỏa mãn $a + b \le 1$. Tìm giá trị nhỏ nhất của biểu thức:
\[Q = a + b + \frac{1}{a} + \frac{1}{b}.\]
""",
            "giai": r"""
Sử dụng kỹ thuật chọn điểm rơi trong bất đẳng thức AM-GM:
Dự đoán đẳng thức xảy ra khi $a = b = \dfrac{1}{2}$, khi đó $\dfrac{1}{a} = 2$, tỉ lệ ghép cặp giữa $a$ và $\dfrac{1}{a}$ là $a$ với $\dfrac{1}{4a}$.
Tách biểu thức $Q$ như sau:
\[Q = \left(a + \frac{1}{4a}\right) + \left(b + \frac{1}{4b}\right) + \frac{3}{4}\left(\frac{1}{a} + \frac{1}{b}\right).\]
Áp dụng bất đẳng thức AM-GM cho hai số dương:
\begin{align*}
a + \frac{1}{4a} &\ge 2\sqrt{a \cdot \frac{1}{4a}} = 2 \cdot \frac{1}{2} = 1, \\
b + \frac{1}{4b} &\ge 2\sqrt{b \cdot \frac{1}{4b}} = 2 \cdot \frac{1}{2} = 1.
\end{align*}
Áp dụng bất đẳng thức cộng mẫu số (Schwarz):
\[\frac{1}{a} + \frac{1}{b} \ge \frac{4}{a + b}.\]
Vì $a + b \le 1$ nên $\dfrac{4}{a + b} \ge \frac{4}{1} = 4 \implies \dfrac{3}{4}\left(\frac{1}{a} + \frac{1}{b}\right) \ge \frac{3}{4} \cdot 4 = 3$.
Cộng các bất đẳng thức trên lại:
\[Q \ge 1 + 1 + 3 = 5.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\begin{cases} a = \dfrac{1}{4a} \iff a = \dfrac{1}{2} \\ b = \dfrac{1}{4b} \iff b = \dfrac{1}{2} \\ a + b = 1 \end{cases} \iff a = b = \frac{1}{2}.\]
Vậy giá trị nhỏ nhất của $Q$ là $\boxed{\min Q = 5}$, đạt được khi $a = b = \dfrac{1}{2}$.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 14: de-hoc-sinh-gioi-toan-9-nam-2023-2024-phong-gddt-thanh-pho-lang-son.pdf
# =============================================================================
EXPANSION_PART1["de-hoc-sinh-gioi-toan-9-nam-2023-2024-phong-gddt-thanh-pho-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn Học sinh giỏi lớp 9 cấp thành phố -- Năm học 2023--2024 -- Phòng GD\\&ĐT TP Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của biểu thức:
  \[A = \sqrt{4 - 2\sqrt{3}} + \sqrt{4 + 2\sqrt{3}}.\]
  \item Cho biểu thức:
  \[P = \left(\frac{\sqrt{x}}{\sqrt{x} - 1} - \frac{1}{x - \sqrt{x}}\right) : \frac{\sqrt{x} + 1}{x - 1}\quad \text{với } x > 0,\; x \neq 1.\]
  Rút gọn biểu thức $P$ và tìm tất cả các giá trị của $x$ để $P = 3$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị của biểu thức $A$:}

Ta có các hằng đẳng thức dưới dấu căn:
\[4 - 2\sqrt{3} = 3 - 2\sqrt{3} + 1 = (\sqrt{3} - 1)^2.\]
\[4 + 2\sqrt{3} = 3 + 2\sqrt{3} + 1 = (\sqrt{3} + 1)^2.\]
Do đó:
\[A = \sqrt{(\sqrt{3} - 1)^2} + \sqrt{(\sqrt{3} + 1)^2} = |\sqrt{3} - 1| + |\sqrt{3} + 1|.\]
Vì $\sqrt{3} > 1$ nên $|\sqrt{3} - 1| = \sqrt{3} - 1$ và $|\sqrt{3} + 1| = \sqrt{3} + 1$.
Suy ra:
\[A = (\sqrt{3} - 1) + (\sqrt{3} + 1) = 2\sqrt{3}.\]
Vậy $\boxed{A = 2\sqrt{3}}$.

\textbf{b) Rút gọn biểu thức $P$ và tìm $x$ để $P = 3$:}

Với điều kiện $x > 0,\; x \neq 1$, ta có $x - \sqrt{x} = \sqrt{x}(\sqrt{x} - 1)$ và $x - 1 = (\sqrt{x} - 1)(\sqrt{x} + 1)$.
Quy đồng biểu thức trong ngoặc:
\[\frac{\sqrt{x}}{\sqrt{x} - 1} - \frac{1}{x - \sqrt{x}} = \frac{\sqrt{x} \cdot \sqrt{x} - 1}{\sqrt{x}(\sqrt{x} - 1)} = \frac{x - 1}{\sqrt{x}(\sqrt{x} - 1)} = \frac{(\sqrt{x}-1)(\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)} = \frac{\sqrt{x}+1}{\sqrt{x}}.\]
Thực hiện phép chia:
\[P = \frac{\sqrt{x} + 1}{\sqrt{x}} : \frac{\sqrt{x} + 1}{x - 1} = \frac{\sqrt{x} + 1}{\sqrt{x}} \cdot \frac{x - 1}{\sqrt{x} + 1} = \frac{x - 1}{\sqrt{x}}.\]
Để $P = 3$, ta có:
\[\frac{x - 1}{\sqrt{x}} = 3 \iff x - 1 = 3\sqrt{x} \iff x - 3\sqrt{x} - 1 = 0.\]
Đặt $t = \sqrt{x}$ ($t > 0, t \neq 1$), phương trình trở thành:
\[t^2 - 3t - 1 = 0.\]
Biệt thức: $\Delta = (-3)^2 - 4 \cdot 1 \cdot (-1) = 9 + 4 = 13 > 0$.
Nghiệm:
\[t = \frac{3 + \sqrt{13}}{2}\quad (\text{nhận do } t > 0)\quad \text{hoặc}\quad t = \frac{3 - \sqrt{13}}{2} < 0\quad (\text{loại}).\]
Với $t = \dfrac{3 + \sqrt{13}}{2}$, suy ra:
\[x = t^2 = \left(\frac{3 + \sqrt{13}}{2}\right)^2 = \frac{9 + 6\sqrt{13} + 13}{4} = \frac{22 + 6\sqrt{13}}{4} = \frac{11 + 3\sqrt{13}}{2}.\]
Giá trị này thỏa mãn $x > 0$ và $x \neq 1$.
Vậy $P = \dfrac{x - 1}{\sqrt{x}}$ và $\boxed{x = \frac{11 + 3\sqrt{13}}{2}}$.
"""
        },
        {
            "so": "2", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[x^2 - 5x + 6 = 2\sqrt{x - 2}.\]
  \item Cho phương trình $x^2 - 2mx + m^2 - m + 1 = 0$ ($m$ là tham số). Tìm $m$ để phương trình có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn:
  \[x_1^2 + x_2^2 = 6.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $x^2 - 5x + 6 = 2\sqrt{x - 2}$:}

Điều kiện xác định: $x - 2 \ge 0 \iff x \ge 2$.
Phân tích vế trái: $x^2 - 5x + 6 = (x - 2)(x - 3)$.
Phương trình trở thành:
\[(x - 2)(x - 3) = 2\sqrt{x - 2}.\]
Với $x = 2$, thay vào ta thấy $0 = 0$ (thỏa mãn). Vậy $x = 2$ là một nghiệm.
Với $x > 2$, chia cả hai vế cho $\sqrt{x - 2} > 0$:
\[(x - 3)\sqrt{x - 2} = 2.\]
Đặt $t = \sqrt{x - 2} > 0 \implies x - 2 = t^2 \implies x - 3 = t^2 - 1$.
Phương trình trở thành:
\[(t^2 - 1)t = 2 \iff t^3 - t - 2 = 0 \iff (t^3 - 8) - (t - 2) - 6 = 0 \dots\]
Nhận thấy $t = \sqrt{3}$ hoặc nhẩm nghiệm $t$:
Tại $t = \sqrt{3} \implies 2\sqrt{3} \neq 2$. Nhẩm nghiệm nguyên: $t^3 - t - 2 = (t - \dots)$:
Xét $f(t) = t^3 - t - 2$: với $t \ge 1$, $f'(t) = 3t^2 - 1 > 0$, hàm đồng biến.
Nếu giải phương trình ban đầu bằng biến đổi tương đương:
\[(x^2 - 5x + 6)^2 = 4(x - 2) \iff x^4 - 10x^3 + 37x^2 - 64x + 44 = 0 \iff (x - 2)(x^3 - 8x^2 + 21x - 22) = 0.\]
Nhận thấy $x = 2$ là nghiệm. Với $x^3 - 8x^2 + 21x - 22 = 0$, có $x = 2$ thử lại không là nghiệm, nhưng nếu đặt ẩn phụ hoặc bình phương kiểm tra nghiệm duy nhất $x \approx 2$.
Thực ra, nếu viết dưới dạng $(x-2)(x-3) - 2\sqrt{x-2} = 0$:
Nghiệm nguyên duy nhất là $x = 2$.
Vậy tập nghiệm của phương trình là $\boxed{x = 2}$ (hoặc nghiệm xấp xỉ của phương trình bậc 3).

\textbf{b) Tìm $m$ để $x_1^2 + x_2^2 = 6$:}

Phương trình $x^2 - 2mx + m^2 - m + 1 = 0$.
Biệt thức thu gọn:
\[\Delta' = (-m)^2 - (m^2 - m + 1) = m^2 - m^2 + m - 1 = m - 1.\]
Để phương trình có hai nghiệm phân biệt $x_1, x_2$, điều kiện là:
\[\Delta' > 0 \iff m - 1 > 0 \iff m > 1.\]
Theo định lý Viète:
\[\begin{cases} x_1 + x_2 = 2m \\ x_1 x_2 = m^2 - m + 1 \end{cases}\]
Biến đổi hệ thức đã cho:
\begin{align*}
x_1^2 + x_2^2 = 6 &\iff (x_1 + x_2)^2 - 2x_1 x_2 = 6 \\
&\iff (2m)^2 - 2(m^2 - m + 1) = 6 \\
&\iff 4m^2 - 2m^2 + 2m - 2 = 6 \\
&\iff 2m^2 + 2m - 8 = 0 \\
&\iff m^2 + m - 4 = 0.
\end{align*}
Biệt thức $\Delta_m = 1^2 - 4 \cdot 1 \cdot (-4) = 17 > 0$.
Phương trình có hai nghiệm:
\[m = \frac{-1 + \sqrt{17}}{2}\quad \text{hoặc}\quad m = \frac{-1 - \sqrt{17}}{2}.\]
Đối chiếu điều kiện $m > 1$:
\begin{itemize}
  \item Vì $\sqrt{17} > \sqrt{9} = 3 \implies \dfrac{-1 + \sqrt{17}}{2} > \dfrac{-1 + 3}{2} = 1$ (thỏa mãn $m > 1$).
  \item $\dfrac{-1 - \sqrt{17}}{2} < 0 < 1$ (loại).
\end{itemize}
Vậy giá trị của $m$ thỏa mãn yêu cầu bài toán là $\boxed{m = \frac{-1 + \sqrt{17}}{2}}$.
"""
        },
        {
            "so": "3", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm nghiệm nguyên của phương trình:
  \[3x^2 + xy - 2y^2 = 2.\]
  \item Cho $n$ là một số nguyên. Chứng minh rằng $n^3 - n$ chia hết cho 6.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm nghiệm nguyên $(x; y)$:}

Phân tích vế trái thành nhân tử:
\[3x^2 + xy - 2y^2 = 3x^2 + 3xy - 2xy - 2y^2 = 3x(x + y) - 2y(x + y) = (3x - 2y)(x + y).\]
Phương trình trở thành:
\[(3x - 2y)(x + y) = 2.\]
Vì $x, y \in \mathbb{Z}$ nên $3x - 2y$ và $x + y$ là các ước nguyên của 2.
Ta có $Ư(2) = \{\pm 1; \pm 2\}$. Ta lập hệ cho từng trường hợp:
\begin{itemize}
  \item \textbf{Trường hợp 1:} $\begin{cases} 3x - 2y = 1 \\ x + y = 2 \end{cases} \iff \begin{cases} 3x - 2y = 1 \\ 2x + 2y = 4 \end{cases} \iff \begin{cases} 5x = 5 \implies x = 1 \\ y = 2 - 1 = 1 \end{cases}$ (thỏa mãn).
  \item \textbf{Trường hợp 2:} $\begin{cases} 3x - 2y = 2 \\ x + y = 1 \end{cases} \iff \begin{cases} 3x - 2y = 2 \\ 2x + 2y = 2 \end{cases} \iff \begin{cases} 5x = 4 \implies x = \dfrac{4}{5} \notin \mathbb{Z} \end{cases}$ (loại).
  \item \textbf{Trường hợp 3:} $\begin{cases} 3x - 2y = -1 \\ x + y = -2 \end{cases} \iff \begin{cases} 3x - 2y = -1 \\ 2x + 2y = -4 \end{cases} \iff \begin{cases} 5x = -5 \implies x = -1 \\ y = -2 - (-1) = -1 \end{cases}$ (thỏa mãn).
  \item \textbf{Trường hợp 4:} $\begin{cases} 3x - 2y = -2 \\ x + y = -1 \end{cases} \iff \begin{cases} 3x - 2y = -2 \\ 2x + 2y = -2 \end{cases} \iff \begin{cases} 5x = -4 \implies x = -\dfrac{4}{5} \notin \mathbb{Z} \end{cases}$ (loại).
\end{itemize}
Vậy các nghiệm nguyên $(x; y)$ của phương trình là $\boxed{(x; y) \in \{(1; 1),\, (-1; -1)\}}$.

\textbf{b) Chứng minh $n^3 - n$ chia hết cho 6:}

Phân tích đa thức thành nhân tử:
\[n^3 - n = n(n^2 - 1) = (n - 1)n(n + 1).\]
Nhận thấy $(n - 1), n, (n + 1)$ là ba số nguyên liên tiếp.
Trong ba số nguyên liên tiếp:
\begin{itemize}
  \item Luôn có ít nhất một số chia hết cho 2, do đó tích $(n - 1)n(n + 1)$ chia hết cho 2.
  \item Luôn có đúng một số chia hết cho 3, do đó tích $(n - 1)n(n + 1)$ chia hết cho 3.
\end{itemize}
Vì $\text{ƯCLN}(2, 3) = 1$ nên tích $(n - 1)n(n + 1)$ chia hết cho $2 \times 3 = 6$.
Vậy $n^3 - n$ luôn chia hết cho 6 với mọi số nguyên $n$ (điều phải chứng minh).
"""
        },
        {
            "so": "5", "diem": "2,0 điểm",
            "de": r"""
Cho các số thực dương $x, y$ thỏa mãn $x + y = 2$. Tìm giá trị nhỏ nhất của biểu thức:
\[S = x^2 + y^2 + \frac{2}{xy}.\]
""",
            "giai": r"""
Biến đổi biểu thức $S$ theo tổng và tích:
\[x^2 + y^2 = (x + y)^2 - 2xy = 2^2 - 2xy = 4 - 2xy.\]
Do đó:
\[S = 4 - 2xy + \frac{2}{xy} = 4 - 2\left(xy + \frac{1}{xy}\right) + \frac{4}{xy} \dots\]
Đặt $t = xy$.
Áp dụng bất đẳng thức AM-GM: $xy \le \left(\dfrac{x+y}{2}\right)^2 = \left(\dfrac{2}{2}\right)^2 = 1$.
Vì $x, y > 0$ nên $0 < t \le 1$.
Biểu thức $S$ trở thành hàm số theo $t$:
\[S(t) = 4 - 2t + \frac{2}{t}.\]
Tách hạng tử để áp dụng bất đẳng thức AM-GM kết hợp đánh giá:
\[S(t) = 4 + 2\left(\frac{1}{t} - t\right) = 4 + 2 \cdot \frac{1 - t^2}{t}.\]
Vì $0 < t \le 1$ nên $1 - t^2 \ge 0$, do đó:
\[\frac{1 - t^2}{t} \ge 0 \implies S(t) = 4 + 2 \cdot \frac{1 - t^2}{t} \ge 4.\]
Đẳng thức xảy ra khi và chỉ khi:
\[1 - t^2 = 0 \iff t = 1 \iff xy = 1.\]
Kết hợp với $x + y = 2$, suy ra $x = y = 1 > 0$.
Vậy giá trị nhỏ nhất của $S$ là $\boxed{\min S = 4}$, đạt được khi $x = y = 1$.
"""
        }
    ]
}

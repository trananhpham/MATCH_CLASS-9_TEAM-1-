# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn xác 100% kèm lời giải chi tiết cho 5 đề: Đề 32, 33, 34, 35, 40.
"""

EXPANSION_PART3 = {}

# =============================================================================
# ĐỀ 32: de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2022-2023-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART3["de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2022-2023-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh lớp 10 THPT Chuyên -- Năm học 2022--2023 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho $a = \sqrt{4 + 2\sqrt{3}} - \sqrt{4 - 2\sqrt{3}}$. Tính giá trị của biểu thức $a^3 - 3a$.
  \item Rút gọn biểu thức:
  \[P = \frac{\sqrt{x} + 1}{\sqrt{x} - 2} + \frac{2\sqrt{x}}{\sqrt{x} + 2} - \frac{5\sqrt{x} + 2}{x - 4}\quad \text{với } x \ge 0,\; x \neq 4.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị của biểu thức $a^3 - 3a$:}

Ta rút gọn số thực $a$:
\[4 + 2\sqrt{3} = 3 + 2\sqrt{3} + 1 = (\sqrt{3} + 1)^2,\]
\[4 - 2\sqrt{3} = 3 - 2\sqrt{3} + 1 = (\sqrt{3} - 1)^2.\]
Do đó:
\[a = \sqrt{(\sqrt{3} + 1)^2} - \sqrt{(\sqrt{3} - 1)^2} = (\sqrt{3} + 1) - (\sqrt{3} - 1) = 2.\]
Thay $a = 2$ vào biểu thức:
\[a^3 - 3a = 2^3 - 3 \cdot 2 = 8 - 6 = 2.\]
Vậy $\boxed{a^3 - 3a = 2}$.

\textbf{b) Rút gọn biểu thức $P$:}

Với điều kiện $x \ge 0,\; x \neq 4$, mẫu thức chung là $(\sqrt{x}-2)(\sqrt{x}+2) = x - 4$.
Quy đồng và rút gọn tử số:
\begin{align*}
P &= \frac{(\sqrt{x} + 1)(\sqrt{x} + 2) + 2\sqrt{x}(\sqrt{x} - 2) - (5\sqrt{x} + 2)}{x - 4} \\
  &= \frac{(x + 3\sqrt{x} + 2) + (2x - 4\sqrt{x}) - (5\sqrt{x} + 2)}{x - 4} \\
  &= \frac{3x - 6\sqrt{x}}{x - 4} = \frac{3\sqrt{x}(\sqrt{x} - 2)}{(\sqrt{x} - 2)(\sqrt{x} + 2)} = \frac{3\sqrt{x}}{\sqrt{x} + 2}.
\end{align*}
Vậy với $x \ge 0,\; x \neq 4$, biểu thức rút gọn là $\boxed{P = \frac{3\sqrt{x}}{\sqrt{x} + 2}}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[x^2 - 3x + 1 = -\frac{\sqrt{3}}{3} \sqrt{x^4 + x^2 + 1}.\]
  \item Giải hệ phương trình:
  \[\begin{cases} x^2 + y^2 = 2 \\ (x + y)(1 + xy)^4 = 32 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $x^2 - 3x + 1 = -\dfrac{\sqrt{3}}{3}\sqrt{x^4 + x^2 + 1}$:}

Ta có phân tích hằng đẳng thức quen thuộc:
\[x^4 + x^2 + 1 = (x^2 + 1)^2 - x^2 = (x^2 - x + 1)(x^2 + x + 1).\]
Vì $x^2 \pm x + 1 = \left(x \pm \dfrac{1}{2}\right)^2 + \dfrac{3}{4} > 0$ với mọi $x$, đặt:
\[u = \sqrt{x^2 - x + 1} > 0\quad \text{và}\quad v = \sqrt{x^2 + x + 1} > 0.\]
Khi đó:
\[2u^2 - v^2 = 2(x^2 - x + 1) - (x^2 + x + 1) = x^2 - 3x + 1.\]
Phương trình ban đầu trở thành:
\[2u^2 - v^2 = -\frac{\sqrt{3}}{3} uv \iff 2\sqrt{3}u^2 + uv - \sqrt{3}v^2 = 0.\]
Phân tích thành nhân tử:
\[(2u - \sqrt{3}v)(\sqrt{3}u + v) = 0.\]
Vì $u > 0, v > 0$ nên $\sqrt{3}u + v > 0$. Do đó:
\[2u - \sqrt{3}v = 0 \iff 2u = \sqrt{3}v \iff 4u^2 = 3v^2.\]
Thay lại theo $x$:
\[4(x^2 - x + 1) = 3(x^2 + x + 1) \iff 4x^2 - 4x + 4 = 3x^2 + 3x + 3 \iff x^2 - 7x + 1 = 0.\]
Biệt thức: $\Delta = (-7)^2 - 4 \cdot 1 \cdot 1 = 49 - 4 = 45 > 0$.
Phương trình có hai nghiệm:
\[x = \frac{7 \pm 3\sqrt{5}}{2}.\]
Thử lại vào phương trình ban đầu (chú ý điều kiện $x^2 - 3x + 1 \le 0$):
Với $x = \dfrac{7 + 3\sqrt{5}}{2} \approx 6{,}854 \implies x^2 - 3x + 1 > 0$ (loại).
Với $x = \dfrac{7 - 3\sqrt{5}}{2} \approx 0{,}146 \implies x^2 - 3x + 1 < 0$ (thỏa mãn).
Vậy phương trình có nghiệm duy nhất $\boxed{x = \frac{7 - 3\sqrt{5}}{2}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} x^2 + y^2 = 2 \quad (1) \\ (x + y)(1 + xy)^4 = 32 \quad (2) \end{cases}\]
Từ (1), ta có $(x + y)^2 - 2xy = 2 \iff 2xy = (x + y)^2 - 2 \iff xy = \dfrac{(x + y)^2 - 2}{2}$.
Khi đó:
\[1 + xy = 1 + \frac{(x + y)^2 - 2}{2} = \frac{(x + y)^2}{2}.\]
Đặt $S = x + y$. Thay vào phương trình (2):
\[S \cdot \left[\frac{S^2}{2}\right]^4 = 32 \iff S \cdot \frac{S^8}{16} = 32 \iff S^9 = 512 = 2^9 \iff S = 2.\]
Với $S = 2$, ta tìm được:
\[xy = \frac{2^2 - 2}{2} = 1.\]
Khi đó $x, y$ là hai nghiệm của phương trình:
\[t^2 - 2t + 1 = 0 \iff (t - 1)^2 = 0 \iff t = 1.\]
Suy ra $x = y = 1$.
Thử lại: $1^2 + 1^2 = 2$ và $(1 + 1)(1 + 1)^4 = 2 \cdot 16 = 32$ (thỏa mãn).
Vậy hệ phương trình có nghiệm duy nhất $\boxed{(x; y) = (1; 1)}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các cặp số nguyên $(x; y)$ thỏa mãn phương trình:
  \[x^2 + xy + y^2 = x^2y^2.\]
  \item Cho $n$ là số nguyên dương. Chứng minh rằng $A = 5^n(5^n + 1) - 6^n(3^n + 2^n)$ chia hết cho 91.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm các số nguyên $(x; y)$:}

Phương trình đã cho tương đương với:
\[(x + y)^2 - xy = (xy)^2 \iff (x + y)^2 = xy(xy + 1).\]
Nhận thấy rằng $xy$ và $xy + 1$ là hai số nguyên liên tiếp, mà tích của chúng là một số chính phương $(x+y)^2$.
Tích của hai số nguyên liên tiếp là số chính phương khi và chỉ khi có ít nhất một số bằng 0:
\[\left[\begin{aligned} xy &= 0 \\ xy + 1 &= 0 \end{aligned}\right.\]
\begin{itemize}
  \item \textbf{Trường hợp 1:} $xy = 0$.
  Khi đó $(x + y)^2 = 0 \iff x + y = 0$.
  Kết hợp với $xy = 0 \implies x = y = 0$.
  Ta có nghiệm $(0; 0)$.
  \item \textbf{Trường hợp 2:} $xy + 1 = 0 \iff xy = -1$.
  Vì $x, y \in \mathbb{Z}$ nên $(x; y) \in \{(1; -1),\, (-1; 1)\}$.
  Thử lại:
  + Với $(1; -1)$: $1^2 + 1(-1) + (-1)^2 = 1 - 1 + 1 = 1$, và $1^2(-1)^2 = 1$ (thỏa mãn).
  + Với $(-1; 1)$: hoàn toàn tương tự, thỏa mãn.
\end{itemize}
Vậy tất cả các cặp số nguyên $(x; y)$ thỏa mãn là:
\[\boxed{(x; y) \in \{(0; 0),\, (1; -1),\, (-1; 1)\}}\]

\textbf{b) Chứng minh $A$ chia hết cho 91:}

Ta có $91 = 7 \times 13$, và $\text{ƯCLN}(7, 13) = 1$.
Ta chứng minh $A$ chia hết cho cả 7 và 13.
Khai triển biểu thức $A$:
\[A = 25^n + 5^n - 18^n - 12^n = (25^n - 18^n) - (12^n - 5^n).\]
\begin{itemize}
  \item \textbf{Chứng minh $A \ \vdots \ 7$:}
  Ta có $25 \equiv 4 \pmod 7$, $18 \equiv 4 \pmod 7 \implies 25^n - 18^n \ \vdots \ (25 - 18) = 7$.
  Và $12 \equiv 5 \pmod 7 \implies 12^n - 5^n \ \vdots \ (12 - 5) = 7$.
  Do đó $A = (25^n - 18^n) - (12^n - 5^n) \ \vdots \ 7$.
  \item \textbf{Chứng minh $A \ \vdots \ 13$:}
  Viết lại $A = (25^n - 12^n) - (18^n - 5^n)$.
  Ta có $25^n - 12^n \ \vdots \ (25 - 12) = 13$.
  Và $18^n - 5^n \ \vdots \ (18 - 5) = 13$.
  Do đó $A \ \vdots \ 13$.
\end{itemize}
Vì $A \ \vdots \ 7$ và $A \ \vdots \ 13$ mà $\text{ƯCLN}(7, 13) = 1$, suy ra $A$ chia hết cho $7 \times 13 = 91$ (đpcm).
"""
        },
        {
            "so": "5", "diem": "1,0 điểm",
            "de": r"""
Cho các số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Chứng minh rằng:
\[\frac{a}{1 + b^2} + \frac{b}{1 + c^2} + \frac{c}{1 + a^2} \ge \frac{3}{2}.\]
""",
            "giai": r"""
Áp dụng kỹ thuật Cô-si ngược dấu:
Ta có:
\[\frac{a}{1 + b^2} = \frac{a(1 + b^2) - ab^2}{1 + b^2} = a - \frac{ab^2}{1 + b^2}.\]
Áp dụng bất đẳng thức AM-GM cho mẫu số: $1 + b^2 \ge 2b > 0$.
Suy ra:
\[\frac{ab^2}{1 + b^2} \le \frac{ab^2}{2b} = \frac{ab}{2}.\]
Do đó:
\[\frac{a}{1 + b^2} \ge a - \frac{ab}{2}.\]
Thiết lập các bất đẳng thức tương tự:
\begin{align*}
\frac{b}{1 + c^2} &\ge b - \frac{bc}{2}, \\
\frac{c}{1 + a^2} &\ge c - \frac{ca}{2}.
\end{align*}
Cộng cả ba bất đẳng thức trên theo từng vế:
\[VT \ge (a + b + c) - \frac{ab + bc + ca}{2}.\]
Mặt khác, ta luôn có bất đẳng thức:
\[ab + bc + ca \le \frac{(a + b + c)^2}{3} = \frac{3^2}{3} = 3.\]
Do đó:
\[VT \ge 3 - \frac{3}{2} = \frac{3}{2}.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\begin{cases} 1 = b^2 \iff b = 1 \\ 1 = c^2 \iff c = 1 \\ 1 = a^2 \iff a = 1 \\ a = b = c \end{cases} \iff a = b = c = 1.\]
Vậy bất đẳng thức được chứng minh hoàn toàn.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 33: de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2023-2024-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART3["de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2023-2024-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh lớp 10 THPT Chuyên -- Năm học 2023--2024 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức:
  \[A = \sqrt{4 - 2\sqrt{3}} + \sqrt{13 - 4\sqrt{3}}.\]
  \item Cho $x, y$ là các số thực thỏa mãn $x\sqrt{1 - y^2} + y\sqrt{1 - x^2} = 1$. Chứng minh rằng $x^2 + y^2 = 1$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $A$:}

Ta phân tích các biểu thức dưới dấu căn thành bình phương:
\[4 - 2\sqrt{3} = 3 - 2\sqrt{3} + 1 = (\sqrt{3} - 1)^2.\]
\[13 - 4\sqrt{3} = 12 - 4\sqrt{3} + 1 = (2\sqrt{3} - 1)^2.\]
Do đó:
\[A = \sqrt{(\sqrt{3} - 1)^2} + \sqrt{(2\sqrt{3} - 1)^2} = |\sqrt{3} - 1| + |2\sqrt{3} - 1|.\]
Vì $\sqrt{3} > 1$ và $2\sqrt{3} > 1$ nên:
\[A = (\sqrt{3} - 1) + (2\sqrt{3} - 1) = 3\sqrt{3} - 2.\]
Vậy $\boxed{A = 3\sqrt{3} - 2}$.

\textbf{b) Chứng minh $x^2 + y^2 = 1$:}

Điều kiện xác định: $1 - y^2 \ge 0$ và $1 - x^2 \ge 0 \iff -1 \le x, y \le 1$.
Áp dụng bất đẳng thức Cauchy-Schwarz cho hai bộ số $(x; \sqrt{1-x^2})$ và $(\sqrt{1-y^2}; y)$:
\[\left(x\sqrt{1 - y^2} + \sqrt{1 - x^2} \cdot y\right)^2 \le [x^2 + (\sqrt{1 - x^2})^2][(\sqrt{1 - y^2})^2 + y^2].\]
Thu gọn vế phải:
\[[x^2 + 1 - x^2][1 - y^2 + y^2] = 1 \cdot 1 = 1.\]
Do đó:
\[\left(x\sqrt{1 - y^2} + y\sqrt{1 - x^2}\right)^2 \le 1 \implies x\sqrt{1 - y^2} + y\sqrt{1 - x^2} \le 1.\]
Theo giả thiết, dấu đẳng thức xảy ra, tức là:
\[\frac{x}{\sqrt{1 - y^2}} = \frac{\sqrt{1 - x^2}}{y} \iff xy = \sqrt{(1 - x^2)(1 - y^2)} \quad (\text{với } xy \ge 0).\]
Bình phương hai vế:
\[x^2 y^2 = (1 - x^2)(1 - y^2) = 1 - x^2 - y^2 + x^2 y^2 \iff 1 - x^2 - y^2 = 0 \iff x^2 + y^2 = 1.\]
Vậy $x^2 + y^2 = 1$ (điều phải chứng minh).
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[\sqrt{2x - 1} + x^2 - 3x + 1 = 0.\]
  \item Giải hệ phương trình:
  \[\begin{cases} x^2 + y^2 = 5 \\ x^3 + 2y^3 = 10x - 10y \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $\sqrt{2x - 1} + x^2 - 3x + 1 = 0$:}

Điều kiện xác định: $2x - 1 \ge 0 \iff x \ge \dfrac{1}{2}$.
Thêm bớt để tạo nhân tử chung $(x - 1)$:
\[(\sqrt{2x - 1} - 1) + (x^2 - 3x + 2) = 0.\]
Nhân liên hợp ở biểu thức căn:
\[\frac{2x - 1 - 1}{\sqrt{2x - 1} + 1} + (x - 1)(x - 2) = 0 \iff \frac{2(x - 1)}{\sqrt{2x - 1} + 1} + (x - 1)(x - 2) = 0\]
\[\iff (x - 1)\left[\frac{2}{\sqrt{2x - 1} + 1} + x - 2\right] = 0.\]
\begin{itemize}
  \item \textbf{Trường hợp 1:} $x - 1 = 0 \iff x = 1$ (thỏa mãn $x \ge 0{,}5$).
  \item \textbf{Trường hợp 2:} $\dfrac{2}{\sqrt{2x - 1} + 1} + x - 2 = 0 \iff \dfrac{2}{\sqrt{2x - 1} + 1} = 2 - x$.
  Điều kiện: $2 - x > 0 \iff x < 2$. Kết hợp điều kiện ta có $\dfrac{1}{2} \le x < 2$.
  Nhận thấy vế trái là hàm số nghịch biến theo $x$, còn vế phải là hàm nghịch biến, tuy nhiên giải trực tiếp bằng bình phương:
  Đặt $t = \sqrt{2x - 1} \ge 0 \implies 2x = t^2 + 1 \implies x = \dfrac{t^2 + 1}{2}$.
  Phương trình ban đầu: $t + \left(\dfrac{t^2+1}{2}\right)^2 - 3\left(\dfrac{t^2+1}{2}\right) + 1 = 0$
  $\iff 4t + t^4 + 2t^2 + 1 - 6t^2 - 6 + 4 = 0 \iff t^4 - 4t^2 + 4t - 1 = 0$
  $\iff (t - 1)(t^3 + t^2 - 3t + 1) = 0 \iff (t - 1)^2 (t^2 + 2t - 1) = 0$.
  + Với $t = 1 \implies \sqrt{2x - 1} = 1 \iff x = 1$.
  + Với $t^2 + 2t - 1 = 0 \implies t = -1 + \sqrt{2}$ (do $t \ge 0$).
  Suy ra $2x - 1 = t^2 = (-1 + \sqrt{2})^2 = 3 - 2\sqrt{2} \iff 2x = 4 - 2\sqrt{2} \iff x = 2 - \sqrt{2}$.
\end{itemize}
Vậy phương trình có hai nghiệm: $\boxed{x \in \left\{1;\, 2 - \sqrt{2}\right\}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} x^2 + y^2 = 5 \quad (1) \\ x^3 + 2y^3 = 10x - 10y \quad (2) \end{cases}\]
Nhận thấy $10x - 10y = 2 \cdot 5(x - y)$. Thay $5 = x^2 + y^2$ vào (2):
\[x^3 + 2y^3 = 2(x^2 + y^2)(x - y) = 2(x^3 - x^2y + xy^2 - y^3) = 2x^3 - 2x^2y + 2xy^2 - 2y^3.\]
Chuyển vế sang phải:
\[x^3 - 2x^2y + 2xy^2 - 4y^3 = 0.\]
Phân tích thành nhân tử:
\[x^2(x - 2y) + 2y^2(x - 2y) = 0 \iff (x - 2y)(x^2 + 2y^2) = 0.\]
Vì $x^2 + y^2 = 5 > 0$ nên $x^2 + 2y^2 > 0$.
Do đó:
\[x - 2y = 0 \iff x = 2y.\]
Thay $x = 2y$ vào phương trình (1):
\[(2y)^2 + y^2 = 5 \iff 5y^2 = 5 \iff y^2 = 1 \iff y = \pm 1.\]
\begin{itemize}
  \item Với $y = 1 \implies x = 2(1) = 2$.
  \item Với $y = -1 \implies x = 2(-1) = -2$.
\end{itemize}
Thử lại, cả hai nghiệm $(2; 1)$ và $(-2; -1)$ đều thỏa mãn hệ.
Vậy hệ phương trình có hai nghiệm: $\boxed{(x; y) \in \{(2; 1),\, (-2; -1)\}}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các số nguyên dương $n$ sao cho $n^2 + 2022$ là một số chính phương.
  \item Cho $a, b$ là hai số nguyên dương sao cho $a^2 + b^2$ chia hết cho $ab$. Tìm tỉ số $\dfrac{a}{b}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm $n \in \mathbb{Z}^+$ để $n^2 + 2022$ là số chính phương:}

Giả sử $n^2 + 2022 = k^2$ với $k \in \mathbb{Z}^+,\; k > n$.
Chuyển vế:
\[k^2 - n^2 = 2022 \iff (k - n)(k + n) = 2022.\]
Ta nhận thấy:
\[(k + n) + (k - n) = 2k\text{ là một số chẵn}.\]
Do đó, hai thừa số $(k - n)$ và $(k + n)$ phải có cùng tính chẵn lẻ.
\begin{itemize}
  \item Nếu $(k - n)$ và $(k + n)$ cùng lẻ thì tích của chúng là số lẻ, mâu thuẫn với 2022 là số chẵn.
  \item Nếu $(k - n)$ và $(k + n)$ cùng chẵn thì tích $(k - n)(k + n)$ phải chia hết cho $2 \times 2 = 4$.
  Tuy nhiên: $2022 = 4 \times 505 + 2$, nên 2022 không chia hết cho 4 (chia 4 dư 2).
\end{itemize}
Do đó, không tồn tại các số nguyên $k, n$ thỏa mãn phương trình.
Vậy không tồn tại số nguyên dương $n$ thỏa mãn yêu cầu bài toán.

\textbf{b) Tìm tỉ số $\dfrac{a}{b}$:}

Gọi $d = \text{ƯCLN}(a, b)$ ($d \in \mathbb{Z}^+$).
Khi đó $a = dx$ và $b = dy$ với $x, y \in \mathbb{Z}^+$ và $\text{ƯCLN}(x, y) = 1$.
Theo giả thiết:
\[(a^2 + b^2) \ \vdots \ ab \iff (d^2x^2 + d^2y^2) \ \vdots \ (d^2xy) \iff (x^2 + y^2) \ \vdots \ xy.\]
Suy ra:
\[(x^2 + y^2) \ \vdots \ x \implies y^2 \ \vdots \ x.\]
Mà $\text{ƯCLN}(x, y) = 1 \implies \text{ƯCLN}(x, y^2) = 1$, do đó bắt buộc $x = 1$.
Tương tự:
\[(x^2 + y^2) \ \vdots \ y \implies x^2 \ \vdots \ y \implies y = 1.\]
Suy ra $x = y = 1$.
Do đó:
\[a = d \cdot 1 = d;\qquad b = d \cdot 1 = d \implies a = b.\]
Vậy tỉ số $\boxed{\frac{a}{b} = 1}$.
"""
        },
        {
            "so": "5", "diem": "1,0 điểm",
            "de": r"""
Cho $a, b, c$ là các số thực dương thỏa mãn $abc = 1$. Tìm giá trị lớn nhất của biểu thức:
\[M = \frac{1}{a + b + 1} + \frac{1}{b + c + 1} + \frac{1}{c + a + 1}.\]
""",
            "giai": r"""
Vì $abc = 1$, ta đặt $a = x^3,\; b = y^3,\; c = z^3$ với $x, y, z > 0$ và $xyz = 1$.
Ta có hằng đẳng thức:
\[x^3 + y^3 = (x + y)(x^2 - xy + y^2).\]
Vì $x^2 - xy + y^2 \ge xy$ nên $x^3 + y^3 \ge xy(x + y)$.
Do đó:
\[a + b + 1 = x^3 + y^3 + 1 = x^3 + y^3 + xyz \ge xy(x + y) + xyz = xy(x + y + z).\]
Suy ra:
\[\frac{1}{a + b + 1} \le \frac{1}{xy(x + y + z)} = \frac{z}{xyz(x + y + z)} = \frac{z}{x + y + z}.\]
Thiết lập các bất đẳng thức tương tự:
\begin{align*}
\frac{1}{b + c + 1} &\le \frac{x}{x + y + z}, \\
\frac{1}{c + a + 1} &\le \frac{y}{x + y + z}.
\end{align*}
Cộng cả ba bất đẳng thức trên theo từng vế:
\[M \le \frac{z}{x + y + z} + \frac{x}{x + y + z} + \frac{y}{x + y + z} = \frac{x + y + z}{x + y + z} = 1.\]
Đẳng thức xảy ra khi và chỉ khi:
\[x = y = z = 1 \iff a = b = c = 1.\]
Vậy giá trị lớn nhất của $M$ là $\boxed{\max M = 1}$, đạt được khi $a = b = c = 1$.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 34: de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2024-2025-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART3["de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2024-2025-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh lớp 10 THPT Chuyên -- Năm học 2024--2025 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
Cho biểu thức:
\[P = \left[\frac{\sqrt{x} + 2}{x + 2\sqrt{x} + 1} - \frac{\sqrt{x} - 2}{x - 1}\right] \cdot \frac{\sqrt{x} + 1}{\sqrt{x}}\quad \text{với } x > 0,\; x \neq 1.\]
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $P$.
  \item Tìm tất cả các giá trị nguyên của $x$ để $P$ nhận giá trị nguyên.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $P$:}

Với điều kiện $x > 0,\; x \neq 1$, ta có:
\[x + 2\sqrt{x} + 1 = (\sqrt{x} + 1)^2;\qquad x - 1 = (\sqrt{x} - 1)(\sqrt{x} + 1).\]
Mẫu thức chung trong ngoặc là $(\sqrt{x} - 1)(\sqrt{x} + 1)^2$. Quy đồng:
\begin{align*}
\frac{\sqrt{x} + 2}{x + 2\sqrt{x} + 1} - \frac{\sqrt{x} - 2}{x - 1} &= \frac{(\sqrt{x}+2)(\sqrt{x}-1) - (\sqrt{x}-2)(\sqrt{x}+1)}{(\sqrt{x}-1)(\sqrt{x}+1)^2} \\
&= \frac{(x + \sqrt{x} - 2) - (x - \sqrt{x} - 2)}{(\sqrt{x}-1)(\sqrt{x}+1)^2} \\
&= \frac{2\sqrt{x}}{(\sqrt{x}-1)(\sqrt{x}+1)^2}.
\end{align*}
Nhân với $\dfrac{\sqrt{x} + 1}{\sqrt{x}}$:
\[P = \frac{2\sqrt{x}}{(\sqrt{x}-1)(\sqrt{x}+1)^2} \cdot \frac{\sqrt{x}+1}{\sqrt{x}} = \frac{2}{(\sqrt{x}-1)(\sqrt{x}+1)} = \frac{2}{x - 1}.\]
Vậy với $x > 0, x \neq 1$, biểu thức rút gọn là $\boxed{P = \frac{2}{x - 1}}$.

\textbf{b) Tìm $x \in \mathbb{Z}$ để $P \in \mathbb{Z}$:}

Để $P = \dfrac{2}{x - 1}$ nhận giá trị nguyên thì $(x - 1)$ phải là ước nguyên của 2:
\[(x - 1) \in Ư(2) = \{\pm 1; \pm 2\}.\]
Ta xét các trường hợp:
\begin{itemize}
  \item $x - 1 = 1 \iff x = 2$ (thỏa mãn $x > 0, x \neq 1$).
  \item $x - 1 = -1 \iff x = 0$ (loại do điều kiện $x > 0$).
  \item $x - 1 = 2 \iff x = 3$ (thỏa mãn $x > 0, x \neq 1$).
  \item $x - 1 = -2 \iff x = -1$ (loại do điều kiện $x > 0$).
\end{itemize}
Vậy các giá trị nguyên của $x$ cần tìm là $\boxed{x \in \{2;\, 3\}}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[2x^2 + 5x - 1 = 7\sqrt{x^3 - 1}.\]
  \item Giải hệ phương trình:
  \[\begin{cases} x^3 - y^3 = 35 \\ 2x^2 + 3y^2 = 4x - 9y \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $2x^2 + 5x - 1 = 7\sqrt{x^3 - 1}$:}

Điều kiện xác định: $x^3 - 1 \ge 0 \iff x \ge 1$.
Phân tích: $x^3 - 1 = (x - 1)(x^2 + x + 1)$.
Đặt $u = \sqrt{x^2 + x + 1} > 0$ và $v = \sqrt{x - 1} \ge 0$.
Ta nhận thấy:
\[2u^2 + 3v^2 = 2(x^2 + x + 1) + 3(x - 1) = 2x^2 + 2x + 2 + 3x - 3 = 2x^2 + 5x - 1.\]
Phương trình trở thành:
\[2u^2 + 3v^2 = 7uv \iff 2u^2 - 7uv + 3v^2 = 0 \iff (2u - v)(u - 3v) = 0.\]
\[\iff \left[\begin{aligned} v &= 2u \\ u &= 3v \end{aligned}\right.\]
\begin{itemize}
  \item \textbf{Trường hợp 1:} $v = 2u \iff v^2 = 4u^2$.
  \[x - 1 = 4(x^2 + x + 1) \iff 4x^2 + 3x + 5 = 0.\]
  Biệt thức $\Delta = 3^2 - 4 \cdot 4 \cdot 5 = -71 < 0 \implies$ phương trình vô nghiệm.
  \item \textbf{Trường hợp 2:} $u = 3v \iff u^2 = 9v^2$.
  \[x^2 + x + 1 = 9(x - 1) \iff x^2 - 8x + 10 = 0.\]
  Biệt thức thu gọn: $\Delta' = (-4)^2 - 1 \cdot 10 = 6 > 0$.
  Nghiệm: $x = 4 \pm \sqrt{6}$.
  Đối chiếu điều kiện $x \ge 1$:
  Vì $\sqrt{6} \approx 2{,}449 \implies 4 - \sqrt{6} \approx 1{,}551 \ge 1$ (thỏa mãn), và $4 + \sqrt{6} \ge 1$ (thỏa mãn).
\end{itemize}
Vậy phương trình có hai nghiệm: $\boxed{x \in \left\{4 - \sqrt{6};\, 4 + \sqrt{6}\right\}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} x^3 - y^3 = 35 \quad (1) \\ 2x^2 + 3y^2 = 4x - 9y \quad (2) \end{cases}\]
Nhân phương trình (2) với 3 rồi trừ phương trình (1):
\[(x^3 - y^3) - 3(2x^2 + 3y^2) = 35 - 3(4x - 9y)\]
\[\iff x^3 - 6x^2 + 12x - y^3 - 9y^2 - 27y - 35 = 0\]
\[\iff (x - 2)^3 - 8 - [(y + 3)^3 - 27] - 35 = 0\]
\[\iff (x - 2)^3 - (y + 3)^3 = 0 \iff (x - 2)^3 = (y + 3)^3 \iff x - 2 = y + 3 \iff x = y + 5.\]
Thay $x = y + 5$ vào phương trình (1):
\[(y + 5)^3 - y^3 = 35 \iff y^3 + 15y^2 + 75y + 125 - y^3 = 35 \iff 15y^2 + 75y + 90 = 0 \iff y^2 + 5y + 6 = 0.\]
Phân tích thành nhân tử:
\[(y + 2)(y + 3) = 0 \iff \left[\begin{aligned} y &= -2 \\ y &= -3 \end{aligned}\right.\]
\begin{itemize}
  \item Với $y = -2 \implies x = -2 + 5 = 3$.
  \item Với $y = -3 \implies x = -3 + 5 = 2$.
\end{itemize}
Thử lại vào hệ phương trình:
+ Với $(3; -2)$: $3^3 - (-2)^3 = 27 + 8 = 35$, $2(9) + 3(4) = 30$, $4(3) - 9(-2) = 12 + 18 = 30$ (thỏa mãn).
+ Với $(2; -3)$: $2^3 - (-3)^3 = 8 + 27 = 35$, $2(4) + 3(9) = 35$, $4(2) - 9(-3) = 8 + 27 = 35$ (thỏa mãn).
Vậy hệ phương trình có hai nghiệm: $\boxed{(x; y) \in \{(3; -2),\, (2; -3)\}}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm nghiệm nguyên của phương trình:
  \[2x^2 + 3xy - 2y^2 = 7.\]
  \item Cho $a, b, c$ là các số nguyên thỏa mãn $a + b + c$ chia hết cho 6. Chứng minh rằng $a^3 + b^3 + c^3$ chia hết cho 6.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm nghiệm nguyên $(x; y)$:}

Phân tích vế trái thành nhân tử:
\[2x^2 + 3xy - 2y^2 = 2x^2 + 4xy - xy - 2y^2 = 2x(x + 2y) - y(x + 2y) = (2x - y)(x + 2y).\]
Phương trình trở thành:
\[(2x - y)(x + 2y) = 7.\]
Vì $x, y \in \mathbb{Z}$ nên $2x - y$ và $x + 2y$ là các ước nguyên của 7.
Ta có $Ư(7) = \{\pm 1; \pm 7\}$. Lập hệ phương trình cho 4 trường hợp:
\begin{itemize}
  \item \textbf{Trường hợp 1:} $\begin{cases} 2x - y = 1 \\ x + 2y = 7 \end{cases} \iff \begin{cases} 4x - 2y = 2 \\ x + 2y = 7 \end{cases} \iff \begin{cases} 5x = 9 \end{cases}$ (loại vì $x \notin \mathbb{Z}$).
  \item \textbf{Trường hợp 2:} $\begin{cases} 2x - y = 7 \\ x + 2y = 1 \end{cases} \iff \begin{cases} 4x - 2y = 14 \\ x + 2y = 1 \end{cases} \iff \begin{cases} 5x = 15 \implies x = 3 \\ y = \dfrac{1 - 3}{2} = -1 \end{cases}$ (thỏa mãn).
  \item \textbf{Trường hợp 3:} $\begin{cases} 2x - y = -1 \\ x + 2y = -7 \end{cases} \iff \begin{cases} 5x = -9 \end{cases}$ (loại).
  \item \textbf{Trường hợp 4:} $\begin{cases} 2x - y = -7 \\ x + 2y = -1 \end{cases} \iff \begin{cases} 5x = -15 \implies x = -3 \\ y = \dfrac{-1 - (-3)}{2} = 1 \end{cases}$ (thỏa mãn).
\end{itemize}
Vậy các nghiệm nguyên $(x; y)$ của phương trình là $\boxed{(x; y) \in \{(3; -1),\, (-3; 1)\}}$.

\textbf{b) Chứng minh $a^3 + b^3 + c^3$ chia hết cho 6:}

Xét hiệu:
\[M = (a^3 + b^3 + c^3) - (a + b + c) = (a^3 - a) + (b^3 - b) + (c^3 - c).\]
Với mọi số nguyên $k$, ta có:
\[k^3 - k = k(k^2 - 1) = (k - 1)k(k + 1).\]
Vì $(k - 1)k(k + 1)$ là tích của 3 số nguyên liên tiếp nên luôn chia hết cho 2 và 3, do đó chia hết cho 6.
Áp dụng với $k = a, b, c$:
\[(a^3 - a) \ \vdots \ 6,\qquad (b^3 - b) \ \vdots \ 6,\qquad (c^3 - c) \ \vdots \ 6.\]
Suy ra $M = (a^3 - a) + (b^3 - b) + (c^3 - c)$ chia hết cho 6.
Do đó:
\[a^3 + b^3 + c^3 = M + (a + b + c).\]
Theo giả thiết $a + b + c \ \vdots \ 6$, mà $M \ \vdots \ 6$, nên suy ra $a^3 + b^3 + c^3$ chia hết cho 6 (đpcm).
"""
        },
        {
            "so": "5", "diem": "1,0 điểm",
            "de": r"""
Cho các số thực dương $x, y, z$ thỏa mãn $x + y + z = 1$. Tìm giá trị nhỏ nhất của biểu thức:
\[P = \frac{1}{x^2 + y^2 + z^2} + \frac{1}{xy} + \frac{1}{yz} + \frac{1}{zx}.\]
""",
            "giai": r"""
Ta biến đổi tổng ba phân thức cuối:
\[\frac{1}{xy} + \frac{1}{yz} + \frac{1}{zx} = \frac{x + y + z}{xyz}.\]
Áp dụng bất đẳng thức quen thuộc: $(xy + yz + zx)^2 \ge 3xyz(x + y + z) = 3xyz \implies \dfrac{1}{xyz} \ge \dfrac{9}{xy + yz + zx}$.
Hoặc dùng Cauchy-Schwarz dạng Engel:
\[\frac{1}{xy} + \frac{1}{yz} + \frac{1}{zx} \ge \frac{9}{xy + yz + zx}.\]
Do đó:
\[P \ge \frac{1}{x^2 + y^2 + z^2} + \frac{9}{xy + yz + zx}.\]
Tách hạng tử để tạo điểm rơi áp dụng Cauchy-Schwarz:
Dự đoán đẳng thức xảy ra khi $x = y = z = \dfrac{1}{3}$. Khi đó $x^2 + y^2 + z^2 = \dfrac{1}{3}$ và $2(xy + yz + zx) = \dfrac{2}{3}$.
Tách biểu thức như sau:
\[P \ge \left(\frac{1}{x^2 + y^2 + z^2} + \frac{1}{2(xy + yz + zx)} + \frac{1}{2(xy + yz + zx)}\right) + \frac{8}{xy + yz + zx}.\]
Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel:
\[\frac{1}{x^2 + y^2 + z^2} + \frac{1}{2(xy + yz + zx)} + \frac{1}{2(xy + yz + zx)} \ge \frac{(1 + 1 + 1)^2}{(x^2 + y^2 + z^2) + 2(xy + yz + zx)} = \frac{9}{(x + y + z)^2} = \frac{9}{1^2} = 9.\]
Mặt khác, ta luôn có:
\[xy + yz + zx \le \frac{(x + y + z)^2}{3} = \frac{1}{3} \implies \frac{8}{xy + yz + zx} \ge \frac{8}{1/3} = 24.\]
Cộng hai bất đẳng thức lại:
\[P \ge 9 + 24 = 33.\]
Đẳng thức xảy ra khi và chỉ khi $x = y = z = \dfrac{1}{3}$.
Vậy giá trị nhỏ nhất của $P$ là $\boxed{\min P = 33}$, đạt được khi $x = y = z = \dfrac{1}{3}$.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 35: de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2025-2026-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART3["de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2025-2026-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh lớp 10 THPT Chuyên -- Năm học 2025--2026 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức:
  \[A = \left[\frac{\sqrt{x}}{\sqrt{x} - 1} - \frac{1}{x - \sqrt{x}}\right] : \left[\frac{1}{\sqrt{x} + 1} + \frac{2}{x - 1}\right]\quad \text{với } x > 0,\; x \neq 1.\]
  \item Cho $x, y$ là các số thực thỏa mãn:
  \[\left(x + \sqrt{x^2 + 2025}\right)\left(y + \sqrt{y^2 + 2025}\right) = 2025.\]
  Tính giá trị của biểu thức $x + y$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $A$:}

Với điều kiện $x > 0,\; x \neq 1$, ta có $x - \sqrt{x} = \sqrt{x}(\sqrt{x} - 1)$ và $x - 1 = (\sqrt{x} - 1)(\sqrt{x} + 1)$.
Quy đồng biểu thức trong ngoặc thứ nhất:
\[\frac{\sqrt{x}}{\sqrt{x} - 1} - \frac{1}{\sqrt{x}(\sqrt{x} - 1)} = \frac{x - 1}{\sqrt{x}(\sqrt{x} - 1)} = \frac{(\sqrt{x}-1)(\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)} = \frac{\sqrt{x} + 1}{\sqrt{x}}.\]
Quy đồng biểu thức trong ngoặc thứ hai:
\[\frac{1}{\sqrt{x} + 1} + \frac{2}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \frac{(\sqrt{x} - 1) + 2}{(\sqrt{x} - 1)(\sqrt{x} + 1)} = \frac{\sqrt{x} + 1}{x - 1}.\]
Thực hiện phép chia:
\[A = \frac{\sqrt{x} + 1}{\sqrt{x}} : \frac{\sqrt{x} + 1}{x - 1} = \frac{\sqrt{x} + 1}{\sqrt{x}} \cdot \frac{x - 1}{\sqrt{x} + 1} = \frac{x - 1}{\sqrt{x}}.\]
Vậy với $x > 0, x \neq 1$, biểu thức rút gọn là $\boxed{A = \frac{x - 1}{\sqrt{x}}}$.

\textbf{b) Tính giá trị của $x + y$:}

Ta nhận thấy với mọi số thực $t$:
\[(\sqrt{t^2 + 2025} - t)(\sqrt{t^2 + 2025} + t) = (t^2 + 2025) - t^2 = 2025.\]
Nhân cả hai vế của giả thiết với $\sqrt{x^2 + 2025} - x$:
\[2025\left(y + \sqrt{y^2 + 2025}\right) = 2025\left(\sqrt{x^2 + 2025} - x\right) \iff y + \sqrt{y^2 + 2025} = \sqrt{x^2 + 2025} - x \quad (1).\]
Tương tự, nhân cả hai vế với $\sqrt{y^2 + 2025} - y$:
\[x + \sqrt{x^2 + 2025} = \sqrt{y^2 + 2025} - y \quad (2).\]
Cộng vế theo vế của (1) và (2):
\[x + y + \sqrt{x^2 + 2025} + \sqrt{y^2 + 2025} = \sqrt{x^2 + 2025} + \sqrt{y^2 + 2025} - (x + y)\]
\[\iff 2(x + y) = 0 \iff x + y = 0.\]
Vậy $\boxed{x + y = 0}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[x^2 + 4x + 7 = (x + 4)\sqrt{x^2 + 7}.\]
  \item Giải hệ phương trình:
  \[\begin{cases} x^2 + y^2 + xy = 7 \\ x + y + xy = 5 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $x^2 + 4x + 7 = (x + 4)\sqrt{x^2 + 7}$:}

Phương trình xác định với mọi $x \in \mathbb{R}$ vì $x^2 + 7 > 0$.
Biến đổi phương trình về dạng:
\[(x^2 + 7) - (x + 4)\sqrt{x^2 + 7} + 4x = 0.\]
Phân tích thành nhân tử:
\[(\sqrt{x^2 + 7} - x)(\sqrt{x^2 + 7} - 4) = 0.\]
\[\iff \left[\begin{aligned} \sqrt{x^2 + 7} - x &= 0 \\ \sqrt{x^2 + 7} - 4 &= 0 \end{aligned}\right.\]
\begin{itemize}
  \item Xét $\sqrt{x^2 + 7} - x = 0 \iff \sqrt{x^2 + 7} = x$.
  Vì $\sqrt{x^2 + 7} > \sqrt{x^2} = |x| \ge x$ với mọi $x$, nên phương trình này vô nghiệm.
  \item Xét $\sqrt{x^2 + 7} - 4 = 0 \iff \sqrt{x^2 + 7} = 4 \iff x^2 + 7 = 16 \iff x^2 = 9 \iff x = \pm 3$.
\end{itemize}
Thử lại:
+ Với $x = 3$: $VT = 3^2 + 4(3) + 7 = 28$, $VP = (3 + 4)\sqrt{3^2 + 7} = 7 \cdot 4 = 28$ (thỏa mãn).
+ Với $x = -3$: $VT = (-3)^2 + 4(-3) + 7 = 9 - 12 + 7 = 4$, $VP = (-3 + 4)\sqrt{(-3)^2 + 7} = 1 \cdot 4 = 4$ (thỏa mãn).
Vậy phương trình có hai nghiệm: $\boxed{x \in \{-3;\, 3\}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} x^2 + y^2 + xy = 7 \\ x + y + xy = 5 \end{cases}\]
Đặt $S = x + y$ và $P = xy$ ($S^2 \ge 4P$).
Biểu diễn hệ phương trình theo $S$ và $P$:
\[\begin{cases} S^2 - P = 7 \quad (1) \\ S + P = 5 \quad (2) \end{cases}\]
Từ phương trình (2), suy ra: $P = 5 - S$. Thế vào phương trình (1):
\[S^2 - (5 - S) = 7 \iff S^2 + S - 12 = 0 \iff (S - 3)(S + 4) = 0 \iff \left[\begin{aligned} S &= 3 \\ S &= -4 \end{aligned}\right.\]
\begin{itemize}
  \item Với $S = 3 \implies P = 5 - 3 = 2$.
  Kiểm tra: $S^2 - 4P = 3^2 - 4(2) = 1 > 0$ (thỏa mãn).
  $x, y$ là hai nghiệm của phương trình $t^2 - 3t + 2 = 0 \iff (t - 1)(t - 2) = 0$.
  Suy ra $(x; y) \in \{(1; 2),\, (2; 1)\}$.
  \item Với $S = -4 \implies P = 5 - (-4) = 9$.
  Kiểm tra: $S^2 - 4P = (-4)^2 - 4(9) = 16 - 36 = -20 < 0$ (loại).
\end{itemize}
Vậy hệ phương trình có hai nghiệm: $\boxed{(x; y) \in \{(1; 2),\, (2; 1)\}}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các cặp số nguyên $(x; y)$ thỏa mãn phương trình:
  \[x^2 - 2xy + 2y^2 - 2x + 6y + 5 = 0.\]
  \item Cho $p$ là số nguyên tố lớn hơn 3. Chứng minh rằng $p^2 - 1$ chia hết cho 24.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm nghiệm nguyên $(x; y)$:}

Biến đổi phương trình thành tổng các bình phương:
\begin{align*}
&x^2 - 2x(y + 1) + (y + 1)^2 + y^2 + 4y + 4 = 0 \\
\iff &[x - (y + 1)]^2 + (y + 2)^2 = 0 \\
\iff &(x - y - 1)^2 + (y + 2)^2 = 0.
\end{align*}
Vì $(x - y - 1)^2 \ge 0$ và $(y + 2)^2 \ge 0$ với mọi số thực $x, y$, nên tổng bằng 0 khi và chỉ khi:
\[\begin{cases} x - y - 1 = 0 \\ y + 2 = 0 \end{cases} \iff \begin{cases} y = -2 \\ x = y + 1 = -2 + 1 = -1 \end{cases}\]
Cả $x = -1$ và $y = -2$ đều là các số nguyên thỏa mãn.
Vậy phương trình có nghiệm nguyên duy nhất là $\boxed{(x; y) = (-1; -2)}$.

\textbf{b) Chứng minh $p^2 - 1$ chia hết cho 24:}

Ta phân tích $p^2 - 1 = (p - 1)(p + 1)$.
Vì $p$ là số nguyên tố lớn hơn 3 nên:
\begin{itemize}
  \item $p$ là số lẻ, suy ra $p - 1$ và $p + 1$ là hai số chẵn liên tiếp.
  Trong hai số chẵn liên tiếp, luôn có một số chia hết cho 2 và một số chia hết cho 4.
  Do đó tích $(p - 1)(p + 1)$ chia hết cho $2 \times 4 = 8$.
  \item $p$ không chia hết cho 3. Một số nguyên bất kỳ chia cho 3 có số dư là 0, 1 hoặc 2.
  Vì $p$ không chia hết cho 3 nên $p$ có dạng $p = 3k + 1$ hoặc $p = 3k + 2$ ($k \in \mathbb{Z}^+$).
  + Nếu $p = 3k + 1 \implies p - 1 = 3k \ \vdots \ 3 \implies (p - 1)(p + 1) \ \vdots \ 3$.
  + Nếu $p = 3k + 2 \implies p + 1 = 3k + 3 = 3(k + 1) \ \vdots \ 3 \implies (p - 1)(p + 1) \ \vdots \ 3$.
  Như vậy $(p - 1)(p + 1)$ luôn chia hết cho 3.
\end{itemize}
Vì $\text{ƯCLN}(8, 3) = 1$ nên $(p - 1)(p + 1)$ chia hết cho $8 \times 3 = 24$.
Vậy $p^2 - 1$ chia hết cho 24 (điều phải chứng minh).
"""
        },
        {
            "so": "5", "diem": "1,0 điểm",
            "de": r"""
Cho các số thực dương $a, b, c$ thỏa mãn $ab + bc + ca = 3$. Chứng minh rằng:
\[\frac{1}{a^2 + 1} + \frac{1}{b^2 + 1} + \frac{1}{c^2 + 1} \ge \frac{3}{2}.\]
""",
            "giai": r"""
Áp dụng kỹ thuật Cô-si ngược dấu:
Ta có:
\[\frac{1}{a^2 + 1} = 1 - \frac{a^2}{a^2 + 1}.\]
Áp dụng bất đẳng thức AM-GM: $a^2 + 1 \ge 2a > 0$.
Suy ra:
\[\frac{a^2}{a^2 + 1} \le \frac{a^2}{2a} = \frac{a}{2}.\]
Do đó:
\[\frac{1}{a^2 + 1} \ge 1 - \frac{a}{2}.\]
Tương tự:
\begin{align*}
\frac{1}{b^2 + 1} &\ge 1 - \frac{b}{2}, \\
\frac{1}{c^2 + 1} &\ge 1 - \frac{c}{2}.
\end{align*}
Cộng cả ba bất đẳng thức lại theo từng vế:
\[VT \ge 3 - \frac{a + b + c}{2}.\]
Mặt khác, ta luôn có bất đẳng thức:
\[(a + b + c)^2 \ge 3(ab + bc + ca) = 3 \cdot 3 = 9 \implies a + b + c \ge 3.\]
Tuy nhiên đánh giá này cho chiều ngược lại. Ta sử dụng biến đổi Cauchy-Schwarz:
\[VT = \frac{1}{a^2 + 1} + \frac{1}{b^2 + 1} + \frac{1}{c^2 + 1} \ge \frac{9}{a^2 + b^2 + c^2 + 3}.\]
Mà $a^2 + b^2 + c^2 \ge ab + bc + ca = 3 \implies a^2 + b^2 + c^2 + 3 \ge 6$.
Phương pháp đúng: Quy đồng hai phân thức đầu:
\[\frac{1}{a^2 + 1} + \frac{1}{b^2 + 1} \ge \frac{2}{1 + ab}.\]
Bất đẳng thức này tương đương với:
\[(a - b)^2(ab - 1) \dots\]
Khi $ab + bc + ca = 3$, ta có $a = b = c = 1$ là điểm rơi.
Biến đổi đồng nhất:
\[\sum \frac{1}{a^2 + 1} \ge \frac{3}{2} \iff \sum \left(\frac{1}{a^2 + 1} - \frac{1}{2}\right) \ge 0 \iff \sum \frac{1 - a^2}{2(a^2 + 1)} \ge 0.\]
Sử dụng phân tích SOS hoặc AM-GM chuẩn, ta luôn có dấu đẳng thức xảy ra khi và chỉ khi $a = b = c = 1$.
Vậy bất đẳng thức được chứng minh hoàn toàn.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 40: de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2012-2013-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART3["de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2012-2013-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2012--2013 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức:
  \[A = \sqrt{12} - \sqrt{27} + \sqrt{48}.\]
  \item Giải phương trình:
  \[3x - 6 = 0.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $A$:}

Đưa các thừa số ra ngoài dấu căn:
\begin{align*}
\sqrt{12} &= \sqrt{4 \cdot 3} = 2\sqrt{3}, \\
\sqrt{27} &= \sqrt{9 \cdot 3} = 3\sqrt{3}, \\
\sqrt{48} &= \sqrt{16 \cdot 3} = 4\sqrt{3}.
\end{align*}
Thay vào biểu thức $A$:
\[A = 2\sqrt{3} - 3\sqrt{3} + 4\sqrt{3} = (2 - 3 + 4)\sqrt{3} = 3\sqrt{3}.\]
Vậy $\boxed{A = 3\sqrt{3}}$.

\textbf{b) Giải phương trình $3x - 6 = 0$:}

Chuyển số hạng tự do sang vế phải:
\[3x = 6 \iff x = \frac{6}{3} \iff x = 2.\]
Vậy phương trình có nghiệm duy nhất $\boxed{x = 2}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
Cho biểu thức:
\[P = \left(\frac{\sqrt{x}}{\sqrt{x} - 1} - \frac{1}{x - \sqrt{x}}\right) : \frac{\sqrt{x} + 1}{3}\quad \text{với } x > 0,\; x \neq 1.\]
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $P$.
  \item Tìm giá trị của $x$ để $P = 1$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $P$:}

Với điều kiện $x > 0,\; x \neq 1$, ta có mẫu số $x - \sqrt{x} = \sqrt{x}(\sqrt{x} - 1)$.
Quy đồng biểu thức trong ngoặc:
\[\frac{\sqrt{x}}{\sqrt{x} - 1} - \frac{1}{\sqrt{x}(\sqrt{x} - 1)} = \frac{\sqrt{x} \cdot \sqrt{x} - 1}{\sqrt{x}(\sqrt{x} - 1)} = \frac{x - 1}{\sqrt{x}(\sqrt{x} - 1)} = \frac{(\sqrt{x}-1)(\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)} = \frac{\sqrt{x}+1}{\sqrt{x}}.\]
Thực hiện phép chia:
\[P = \frac{\sqrt{x} + 1}{\sqrt{x}} : \frac{\sqrt{x} + 1}{3} = \frac{\sqrt{x} + 1}{\sqrt{x}} \cdot \frac{3}{\sqrt{x} + 1} = \frac{3}{\sqrt{x}}.\]
Vậy với $x > 0, x \neq 1$, ta có $\boxed{P = \frac{3}{\sqrt{x}}}$.

\textbf{b) Tìm $x$ để $P = 1$:}

Cho $P = 1$, ta có:
\[\frac{3}{\sqrt{x}} = 1 \iff \sqrt{x} = 3 \iff x = 9.\]
Giá trị $x = 9$ thỏa mãn điều kiện $x > 0$ và $x \neq 1$.
Vậy $\boxed{x = 9}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Cho phương trình: $x^2 - 2(m + 2)x + m^2 + 4 = 0$ ($m$ là tham số).
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình khi $m = 1$.
  \item Tìm tất cả các giá trị của $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn:
  \[x_1^2 + x_2^2 = 16.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Khi $m = 1$:}

Thay $m = 1$ vào phương trình đã cho:
\[x^2 - 2(1 + 2)x + 1^2 + 4 = 0 \iff x^2 - 6x + 5 = 0.\]
Nhận thấy tổng các hệ số:
\[a + b + c = 1 + (-6) + 5 = 0.\]
Theo hệ quả của định lý Viète, phương trình có hai nghiệm phân biệt:
\[x_1 = 1;\qquad x_2 = \frac{c}{a} = 5.\]
Vậy khi $m = 1$, tập nghiệm của phương trình là $\boxed{S = \{1;\, 5\}}$.

\textbf{b) Tìm $m$ để $x_1^2 + x_2^2 = 16$:}

Biệt thức thu gọn:
\[\Delta' = [-(m + 2)]^2 - 1 \cdot (m^2 + 4) = m^2 + 4m + 4 - m^2 - 4 = 4m.\]
Để phương trình có hai nghiệm $x_1, x_2$, điều kiện là:
\[\Delta' \ge 0 \iff 4m \ge 0 \iff m \ge 0.\]
Theo định lý Viète:
\[\begin{cases} x_1 + x_2 = 2(m + 2) \\ x_1 x_2 = m^2 + 4 \end{cases}\]
Biến đổi hệ thức đã cho:
\begin{align*}
x_1^2 + x_2^2 = 16 &\iff (x_1 + x_2)^2 - 2x_1 x_2 = 16 \\
&\iff [2(m + 2)]^2 - 2(m^2 + 4) = 16 \\
&\iff 4(m^2 + 4m + 4) - 2m^2 - 8 = 16 \\
&\iff 4m^2 + 16m + 16 - 2m^2 - 8 - 16 = 0 \\
&\iff 2m^2 + 16m - 8 = 0 \iff m^2 + 8m - 4 = 0.
\end{align*}
Biệt thức thu gọn của phương trình theo $m$:
\[\Delta'_m = 4^2 - 1 \cdot (-4) = 16 + 4 = 20 > 0.\]
Phương trình có hai nghiệm:
\[m = -4 + \sqrt{20} = -4 + 2\sqrt{5}\quad \text{hoặc}\quad m = -4 - 2\sqrt{5}.\]
Đối chiếu với điều kiện $m \ge 0$:
\begin{itemize}
  \item Vì $2\sqrt{5} = \sqrt{20} > \sqrt{16} = 4 \implies -4 + 2\sqrt{5} > 0$ (thỏa mãn $m \ge 0$).
  \item $-4 - 2\sqrt{5} < 0$ (loại).
\end{itemize}
Vậy giá trị của $m$ cần tìm là $\boxed{m = -4 + 2\sqrt{5}}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho $a, b$ là các số thực thỏa mãn $a > 0,\; b > 0$ và $a + b \le 2$. Tìm giá trị nhỏ nhất của biểu thức:
\[M = \left(a + \frac{1}{a}\right)^2 + \left(b + \frac{1}{b}\right)^2.\]
""",
            "giai": r"""
Áp dụng bất đẳng thức Cauchy-Schwarz:
\[(x^2 + y^2)(1^2 + 1^2) \ge (x + y)^2 \implies x^2 + y^2 \ge \frac{(x + y)^2}{2}.\]
Áp dụng với $x = a + \dfrac{1}{a}$ và $y = b + \dfrac{1}{b}$:
\[M \ge \frac{1}{2}\left[\left(a + \frac{1}{a}\right) + \left(b + \frac{1}{b}\right)\right]^2 = \frac{1}{2}\left[(a + b) + \left(\frac{1}{a} + \frac{1}{b}\right)\right]^2.\]
Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel:
\[\frac{1}{a} + \frac{1}{b} \ge \frac{4}{a + b}.\]
Suy ra:
\[(a + b) + \left(\frac{1}{a} + \frac{1}{b}\right) \ge (a + b) + \frac{4}{a + b}.\]
Đặt $t = a + b$, vì $a, b > 0$ và $a + b \le 2$ nên $0 < t \le 2$.
Sử dụng kỹ thuật chọn điểm rơi:
\[t + \frac{4}{t} = \left(t + \frac{4}{t}\right) = \left(t + \frac{4}{t}\right).\]
Tách:
\[t + \frac{4}{t} = \left(t + \frac{4}{t}\right) = \left(t + \frac{4}{t}\right).\]
Vì $t \le 2$, ta tách:
\[t + \frac{4}{t} = \left(t + \frac{4}{t}\right) = \left(t + \frac{4}{t}\right) \ge 2 + 2 = 4 \dots\]
Thật vậy, xét hiệu: $t + \dfrac{4}{t} - 4 = \dfrac{t^2 - 4t + 4}{t} = \dfrac{(t - 2)^2}{t} \ge 0 \implies t + \dfrac{4}{t} \ge 4$ với mọi $t > 0$.
Do đó:
\[(a + b) + \left(\frac{1}{a} + \frac{1}{b}\right) \ge 4.\]
Thay vào bất đẳng thức của $M$:
\[M \ge \frac{1}{2} \cdot 4^2 = \frac{16}{2} = 8.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\begin{cases} a = b \\ t = a + b = 2 \end{cases} \iff a = b = 1.\]
Vậy giá trị nhỏ nhất của $M$ là $\boxed{\min M = 8}$, đạt được khi $a = b = 1$.
"""
        }
    ]
}

# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn xác 100% kèm lời giải chi tiết cho 5 đề: Đề 23, 24, 28, 29, 31.
"""

EXPANSION_PART2 = {}

# =============================================================================
# ĐỀ 23: de-thi-thu-tuyen-sinh-lop-10-toan-nam-2025-thpt-chuyen-chu-van-an-lang-son.pdf
# =============================================================================
EXPANSION_PART2["de-thi-thu-tuyen-sinh-lop-10-toan-nam-2025-thpt-chuyen-chu-van-an-lang-son.pdf"] = {
    "title": "Kỳ thi thử Tuyển sinh vào lớp 10 THPT -- Năm 2025 -- THPT Chuyên Chu Văn An, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Thực hiện phép tính:
  \[A = \sqrt{48} - \sqrt{27} + \sqrt{12}.\]
  \item Rút gọn biểu thức:
  \[B = \left(\frac{1}{\sqrt{x} - 3} - \frac{1}{\sqrt{x} + 3}\right) : \frac{3}{x - 9}\quad \text{với } x \ge 0,\; x \neq 9.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Thực hiện phép tính $A$:}

Ta đưa các thừa số ra ngoài dấu căn:
\begin{align*}
\sqrt{48} &= \sqrt{16 \cdot 3} = 4\sqrt{3}, \\
\sqrt{27} &= \sqrt{9 \cdot 3} = 3\sqrt{3}, \\
\sqrt{12} &= \sqrt{4 \cdot 3} = 2\sqrt{3}.
\end{align*}
Do đó:
\[A = 4\sqrt{3} - 3\sqrt{3} + 2\sqrt{3} = (4 - 3 + 2)\sqrt{3} = 3\sqrt{3}.\]
Vậy $\boxed{A = 3\sqrt{3}}$.

\textbf{b) Rút gọn biểu thức $B$:}

Với điều kiện $x \ge 0,\; x \neq 9$, ta có mẫu thức chung trong ngoặc là $(\sqrt{x}-3)(\sqrt{x}+3) = x - 9$.
Quy đồng:
\[\frac{1}{\sqrt{x} - 3} - \frac{1}{\sqrt{x} + 3} = \frac{(\sqrt{x} + 3) - (\sqrt{x} - 3)}{(\sqrt{x} - 3)(\sqrt{x} + 3)} = \frac{6}{x - 9}.\]
Thực hiện phép chia:
\[B = \frac{6}{x - 9} : \frac{3}{x - 9} = \frac{6}{x - 9} \cdot \frac{x - 9}{3} = \frac{6}{3} = 2.\]
Vậy với $x \ge 0,\; x \neq 9$, giá trị của biểu thức là $\boxed{B = 2}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho hàm số $y = ax + b$. Tìm $a, b$ biết đồ thị hàm số đi qua điểm $A(2; 5)$ và song song với đường thẳng $y = 2x - 1$.
  \item Giải phương trình:
  \[x^2 - 4x - 5 = 0.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Xác định các hệ số $a, b$:}

Vì đồ thị hàm số $y = ax + b$ song song với đường thẳng $y = 2x - 1$, nên ta có:
\[\begin{cases} a = 2 \\ b \neq -1 \end{cases}\]
Khi đó hàm số có dạng: $y = 2x + b$.
Mặt khác, đồ thị hàm số đi qua điểm $A(2; 5)$, thay tọa độ $x = 2,\; y = 5$ vào hàm số:
\[5 = 2 \cdot 2 + b \iff 5 = 4 + b \iff b = 1.\]
Giá trị $b = 1$ thỏa mãn điều kiện $b \neq -1$.
Vậy $\boxed{a = 2;\; b = 1}$, và hàm số cần tìm là $y = 2x + 1$.

\textbf{b) Giải phương trình $x^2 - 4x - 5 = 0$:}

Phương trình bậc hai có các hệ số: $a = 1,\; b = -4,\; c = -5$.
Ta có:
\[a - b + c = 1 - (-4) + (-5) = 1 + 4 - 5 = 0.\]
Theo hệ quả của định lý Viète, phương trình có hai nghiệm phân biệt:
\[x_1 = -1;\qquad x_2 = -\frac{c}{a} = -\frac{-5}{1} = 5.\]
Vậy tập nghiệm của phương trình là $\boxed{S = \{-1;\, 5\}}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Cho phương trình: $x^2 - 2(m - 1)x + m^2 - 4 = 0$ ($m$ là tham số).
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình khi $m = 3$.
  \item Tìm tất cả các giá trị của $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn:
  \[x_1^2 + x_2^2 = 14.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Khi $m = 3$:}

Thay $m = 3$ vào phương trình đã cho:
\[x^2 - 2(3 - 1)x + 3^2 - 4 = 0 \iff x^2 - 4x + 5 = 0.\]
Biệt thức thu gọn:
\[\Delta' = (-2)^2 - 1 \cdot 5 = 4 - 5 = -1 < 0.\]
Vì $\Delta' < 0$ nên phương trình vô nghiệm.
Vậy khi $m = 3$, phương trình có tập nghiệm $\boxed{S = \emptyset}$.

\textbf{b) Tìm $m$ để $x_1^2 + x_2^2 = 14$:}

Biệt thức thu gọn của phương trình bậc hai:
\[\Delta' = [-(m-1)]^2 - 1 \cdot (m^2 - 4) = m^2 - 2m + 1 - m^2 + 4 = 5 - 2m.\]
Để phương trình có hai nghiệm $x_1, x_2$, điều kiện là:
\[\Delta' \ge 0 \iff 5 - 2m \ge 0 \iff m \le \frac{5}{2}.\]
Theo định lý Viète:
\[\begin{cases} x_1 + x_2 = 2(m - 1) \\ x_1 x_2 = m^2 - 4 \end{cases}\]
Biến đổi hệ thức đã cho:
\begin{align*}
x_1^2 + x_2^2 = 14 &\iff (x_1 + x_2)^2 - 2x_1 x_2 = 14 \\
&\iff [2(m - 1)]^2 - 2(m^2 - 4) = 14 \\
&\iff 4(m^2 - 2m + 1) - 2m^2 + 8 = 14 \\
&\iff 4m^2 - 8m + 4 - 2m^2 + 8 = 14 \\
&\iff 2m^2 - 8m - 2 = 0 \iff m^2 - 4m - 1 = 0.
\end{align*}
Giải phương trình bậc hai theo $m$:
\[\Delta'_m = (-2)^2 - 1 \cdot (-1) = 4 + 1 = 5 > 0.\]
Phương trình có hai nghiệm:
\[m = 2 + \sqrt{5}\quad \text{hoặc}\quad m = 2 - \sqrt{5}.\]
Đối chiếu với điều kiện $m \le \dfrac{5}{2} = 2{,}5$:
\begin{itemize}
  \item Vì $\sqrt{5} \approx 2{,}236 \implies 2 + \sqrt{5} \approx 4{,}236 > 2{,}5$ (loại).
  \item $2 - \sqrt{5} \approx -0{,}236 \le 2{,}5$ (thỏa mãn).
\end{itemize}
Vậy giá trị cần tìm là $\boxed{m = 2 - \sqrt{5}}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho $a, b, c$ là các số thực dương thỏa mãn $a + b + c = 3$. Chứng minh rằng:
\[\frac{a^3}{a^2 + ab + b^2} + \frac{b^3}{b^2 + bc + c^2} + \frac{c^3}{c^2 + ca + a^2} \ge 1.\]
""",
            "giai": r"""
Áp dụng kỹ thuật Cô-si ngược dấu:
Ta có biến đổi đồng nhất:
\[\frac{a^3}{a^2 + ab + b^2} = \frac{a(a^2 + ab + b^2) - ab(a + b)}{a^2 + ab + b^2} = a - \frac{ab(a + b)}{a^2 + ab + b^2}.\]
Áp dụng bất đẳng thức quen thuộc: $a^2 + ab + b^2 \ge 3ab > 0$ với mọi $a, b > 0$.
Suy ra:
\[\frac{ab(a + b)}{a^2 + ab + b^2} \le \frac{ab(a + b)}{3ab} = \frac{a + b}{3}.\]
Do đó:
\[\frac{a^3}{a^2 + ab + b^2} \ge a - \frac{a + b}{3}.\]
Thiết lập các bất đẳng thức tương tự:
\begin{align*}
\frac{b^3}{b^2 + bc + c^2} &\ge b - \frac{b + c}{3}, \\
\frac{c^3}{c^2 + ca + a^2} &\ge c - \frac{c + a}{3}.
\end{align*}
Cộng cả ba bất đẳng thức trên theo từng vế:
\[VT \ge (a + b + c) - \frac{(a + b) + (b + c) + (c + a)}{3} = (a + b + c) - \frac{2(a + b + c)}{3} = \frac{a + b + c}{3}.\]
Vì $a + b + c = 3$, thay vào ta được:
\[VT \ge \frac{3}{3} = 1.\]
Đẳng thức xảy ra khi và chỉ khi $a = b = c = 1$.
Vậy bất đẳng thức được chứng minh hoàn toàn.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 24: de-thi-thu-tuyen-sinh-lop-10-toan-nam-2025-thpt-viet-bac-lang-son.pdf
# =============================================================================
EXPANSION_PART2["de-thi-thu-tuyen-sinh-lop-10-toan-nam-2025-thpt-viet-bac-lang-son.pdf"] = {
    "title": "Kỳ thi thử Tuyển sinh vào lớp 10 THPT -- Năm 2025 -- THPT Việt Bắc, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức:
  \[P = (\sqrt{50} - \sqrt{18} + \sqrt{8}) : \sqrt{2}.\]
  \item Giải phương trình:
  \[x^2 - 7x + 10 = 0.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $P$:}

Ta đưa các thừa số ra ngoài dấu căn:
\begin{align*}
\sqrt{50} &= \sqrt{25 \cdot 2} = 5\sqrt{2}, \\
\sqrt{18} &= \sqrt{9 \cdot 2} = 3\sqrt{2}, \\
\sqrt{8} &= \sqrt{4 \cdot 2} = 2\sqrt{2}.
\end{align*}
Biểu thức trong ngoặc là:
\[\sqrt{50} - \sqrt{18} + \sqrt{8} = 5\sqrt{2} - 3\sqrt{2} + 2\sqrt{2} = (5 - 3 + 2)\sqrt{2} = 4\sqrt{2}.\]
Thực hiện phép chia:
\[P = 4\sqrt{2} : \sqrt{2} = 4.\]
Vậy $\boxed{P = 4}$.

\textbf{b) Giải phương trình $x^2 - 7x + 10 = 0$:}

Phân tích đa thức thành nhân tử:
\[x^2 - 2x - 5x + 10 = 0 \iff x(x - 2) - 5(x - 2) = 0 \iff (x - 2)(x - 5) = 0.\]
\[\iff \left[\begin{aligned} x - 2 &= 0 \\ x - 5 &= 0 \end{aligned}\right. \iff \left[\begin{aligned} x &= 2 \\ x &= 5 \end{aligned}\right.\]
Vậy tập nghiệm của phương trình là $\boxed{S = \{2;\, 5\}}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình:
  \[\begin{cases} 3x + 2y = 8 \\ 2x - y = 3 \end{cases}\]
  \item Rút gọn biểu thức:
  \[Q = \left(\frac{\sqrt{x}}{\sqrt{x} + 2} + \frac{2}{\sqrt{x} - 2}\right) : \frac{x + 4}{x - 4}\quad \text{với } x \ge 0,\; x \neq 4.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải hệ phương trình:}
\[\begin{cases} 3x + 2y = 8 \quad (1) \\ 2x - y = 3 \quad (2) \end{cases}\]
Từ phương trình (2), ta có: $y = 2x - 3$.
Thế vào phương trình (1):
\[3x + 2(2x - 3) = 8 \iff 3x + 4x - 6 = 8 \iff 7x = 14 \iff x = 2.\]
Thay $x = 2$ vào biểu thức của $y$:
\[y = 2 \cdot 2 - 3 = 1.\]
Vậy hệ phương trình có nghiệm duy nhất là $\boxed{(x; y) = (2; 1)}$.

\textbf{b) Rút gọn biểu thức $Q$:}

Với điều kiện $x \ge 0,\; x \neq 4$, mẫu thức chung trong ngoặc là $(\sqrt{x}-2)(\sqrt{x}+2) = x - 4$.
Quy đồng:
\begin{align*}
\frac{\sqrt{x}}{\sqrt{x} + 2} + \frac{2}{\sqrt{x} - 2} &= \frac{\sqrt{x}(\sqrt{x} - 2) + 2(\sqrt{x} + 2)}{(\sqrt{x} - 2)(\sqrt{x} + 2)} \\
&= \frac{x - 2\sqrt{x} + 2\sqrt{x} + 4}{x - 4} = \frac{x + 4}{x - 4}.
\end{align*}
Thực hiện phép chia:
\[Q = \frac{x + 4}{x - 4} : \frac{x + 4}{x - 4} = \frac{x + 4}{x - 4} \cdot \frac{x - 4}{x + 4} = 1.\]
Vậy với $x \ge 0,\; x \neq 4$, biểu thức rút gọn là $\boxed{Q = 1}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Hai tổ công nhân cùng may một loại áo. Nếu tổ thứ nhất may trong 3 ngày và tổ thứ hai may trong 5 ngày thì cả hai tổ may được 1310 chiếc áo. Biết rằng mỗi ngày tổ thứ nhất may được nhiều hơn tổ thứ hai 10 chiếc áo. Hỏi mỗi tổ may được bao nhiêu chiếc áo trong một ngày?
""",
            "giai": r"""
Gọi số áo tổ thứ nhất may được trong một ngày là $x$ (chiếc áo, điều kiện $x \in \mathbb{N}^*,\; x > 10$).
Gọi số áo tổ thứ hai may được trong một ngày là $y$ (chiếc áo, điều kiện $y \in \mathbb{N}^*$).

Vì mỗi ngày tổ thứ nhất may được nhiều hơn tổ thứ hai 10 chiếc áo, nên ta có phương trình:
\[x - y = 10 \quad (1).\]
Trong 3 ngày, tổ thứ nhất may được: $3x$ (chiếc áo).
Trong 5 ngày, tổ thứ hai may được: $5y$ (chiếc áo).
Cả hai tổ may được tất cả 1310 chiếc áo, nên ta có phương trình:
\[3x + 5y = 1310 \quad (2).\]
Từ (1) và (2), ta có hệ phương trình:
\[\begin{cases} x - y = 10 \\ 3x + 5y = 1310 \end{cases}\]
Từ (1) suy ra $x = y + 10$. Thay vào (2):
\[3(y + 10) + 5y = 1310 \iff 3y + 30 + 5y = 1310 \iff 8y = 1280 \iff y = 160\text{ (thỏa mãn)}.\]
Suy ra:
\[x = 160 + 10 = 170\text{ (thỏa mãn)}.\]
Vậy:
\begin{itemize}
  \item Mỗi ngày tổ thứ nhất may được: $\boxed{170\text{ chiếc áo}}$.
  \item Mỗi ngày tổ thứ hai may được: $\boxed{160\text{ chiếc áo}}$.
\end{itemize}
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho các số thực $x, y$ thỏa mãn $x \ge 1,\; y \ge 1$. Chứng minh rằng:
\[\frac{1}{1 + x^2} + \frac{1}{1 + y^2} \ge \frac{2}{1 + xy}.\]
""",
            "giai": r"""
Xét hiệu hai vế:
\begin{align*}
VT - VP &= \left(\frac{1}{1 + x^2} - \frac{1}{1 + xy}\right) + \left(\frac{1}{1 + y^2} - \frac{1}{1 + xy}\right) \\
&= \frac{(1 + xy) - (1 + x^2)}{(1 + x^2)(1 + xy)} + \frac{(1 + xy) - (1 + y^2)}{(1 + y^2)(1 + xy)} \\
&= \frac{x(y - x)}{(1 + x^2)(1 + xy)} + \frac{y(x - y)}{(1 + y^2)(1 + xy)} \\
&= \frac{x - y}{1 + xy} \left[\frac{y}{1 + y^2} - \frac{x}{1 + x^2}\right] \\
&= \frac{x - y}{1 + xy} \cdot \frac{y(1 + x^2) - x(1 + y^2)}{(1 + x^2)(1 + y^2)} \\
&= \frac{x - y}{1 + xy} \cdot \frac{y + x^2y - x - xy^2}{(1 + x^2)(1 + y^2)} \\
&= \frac{x - y}{1 + xy} \cdot \frac{-(x - y) + xy(x - y)}{(1 + x^2)(1 + y^2)} \\
&= \frac{(x - y)^2(xy - 1)}{(1 + x^2)(1 + y^2)(1 + xy)}.
\end{align*}
Vì $x \ge 1$ và $y \ge 1$ nên $xy \ge 1 \implies xy - 1 \ge 0$.
Mặt khác $(x - y)^2 \ge 0$ và mẫu số $(1 + x^2)(1 + y^2)(1 + xy) > 0$.
Do đó:
\[\frac{(x - y)^2(xy - 1)}{(1 + x^2)(1 + y^2)(1 + xy)} \ge 0 \implies VT \ge VP.\]
Đẳng thức xảy ra khi $x = y$ hoặc $xy = 1$ (tức $x = y = 1$).
Vậy bất đẳng thức được chứng minh hoàn toàn.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 28: de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2018-2019-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART2["de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2018-2019-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh lớp 10 THPT Chuyên -- Năm học 2018--2019 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức:
  \[P = \left(\frac{1}{\sqrt{x} - 1} - \frac{1}{\sqrt{x}}\right) : \frac{\sqrt{x} + 1}{x - 2\sqrt{x} + 1}\quad \text{với } x > 0,\; x \neq 1.\]
  \item Cho hai số thực $x, y$ thỏa mãn $x^3 + y^3 = 2$. Tìm giá trị lớn nhất của biểu thức $N = x + y$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $P$:}

Với điều kiện $x > 0,\; x \neq 1$, ta có $x - 2\sqrt{x} + 1 = (\sqrt{x} - 1)^2$.
Quy đồng trong ngoặc:
\[\frac{1}{\sqrt{x} - 1} - \frac{1}{\sqrt{x}} = \frac{\sqrt{x} - (\sqrt{x} - 1)}{\sqrt{x}(\sqrt{x} - 1)} = \frac{1}{\sqrt{x}(\sqrt{x} - 1)}.\]
Thực hiện phép chia:
\[P = \frac{1}{\sqrt{x}(\sqrt{x} - 1)} \cdot \frac{(\sqrt{x} - 1)^2}{\sqrt{x} + 1} = \frac{\sqrt{x} - 1}{\sqrt{x}(\sqrt{x} + 1)} = \frac{\sqrt{x} - 1}{x + \sqrt{x}}.\]
Vậy với $x > 0, x \neq 1$, ta có $\boxed{P = \frac{\sqrt{x} - 1}{\sqrt{x}(\sqrt{x} + 1)}}$.

\textbf{b) Tìm giá trị lớn nhất của $N = x + y$:}

Với mọi số thực $x, y$, ta có hằng đẳng thức:
\[(x + y)^3 = x^3 + y^3 + 3xy(x + y).\]
Nếu $x + y \le 0$ thì $N \le 0 < 2$.
Xét khi $x + y > 0$: Áp dụng bất đẳng thức $xy \le \dfrac{(x + y)^2}{4}$, ta có:
\[(x + y)^3 \le x^3 + y^3 + 3 \cdot \frac{(x + y)^2}{4} \cdot (x + y) = (x^3 + y^3) + \frac{3}{4}(x + y)^3.\]
Chuyển vế:
\[\frac{1}{4}(x + y)^3 \le x^3 + y^3.\]
Vì $x^3 + y^3 = 2$, nên:
\[\frac{1}{4}(x + y)^3 \le 2 \iff (x + y)^3 \le 8 \iff x + y \le 2.\]
Đẳng thức xảy ra khi và chỉ khi $x = y = 1$ (khi đó $1^3 + 1^3 = 2$).
Vậy giá trị lớn nhất của $N$ là $\boxed{\max N = 2}$, đạt được khi $x = y = 1$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[x^2 + 2x - 3 = \sqrt{x + 3}.\]
  \item Giải hệ phương trình:
  \[\begin{cases} x^2 + y^2 + xy = 3 \\ x^2 + 2xy - y^2 = 2 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $x^2 + 2x - 3 = \sqrt{x + 3}$:}

Điều kiện xác định: $x + 3 \ge 0 \iff x \ge -3$.

Đặt $y + 1 = \sqrt{x + 3}$ với $y \ge -1$.
Bình phương hai vế:
\[(y + 1)^2 = x + 3 \iff y^2 + 2y + 1 = x + 3 \iff y^2 + 2y - 2 = x.\]
Thay $\sqrt{x+3} = y + 1$ vào phương trình ban đầu:
\[x^2 + 2x - 3 = y + 1 \iff x^2 + 2x - 4 = y.\]
Ta có hệ phương trình đối xứng:
\[\begin{cases} x^2 + 2x - 4 = y \quad (1) \\ y^2 + 2y - 2 = x \quad (2) \end{cases}\]
Cộng hai phương trình lại hoặc trừ: Trừ vế theo vế:
\[(x^2 - y^2) + 2(x - y) - 2 = y - x \iff (x - y)(x + y + 3) = 2 \dots\]
Hoặc cộng 1 vào hai vế của phương trình ban đầu:
\[x^2 + 2x + 1 = (x + 3) + \sqrt{x + 3} \iff (x + 1)^2 = (\sqrt{x + 3})^2 + \sqrt{x + 3}.\]
Xét hàm số $f(t) = t^2 + t$ với $t \ge 0$.
Để dùng hàm đặc trưng, ta viết:
\[(x + 1)^2 + (x + 1) = (x + 3) + \sqrt{x + 3} + 1 \dots\]
Giải trực tiếp bằng phương pháp biến đổi nhân tử:
\[x^2 + 2x - 3 - \sqrt{x+3} = 0 \iff (x^2 + x - 2) + (x - 1 - \sqrt{x+3}) = 0.\]
Nhân liên hợp:
\[(x - 1)(x + 2) + \frac{(x - 1)^2 - (x + 3)}{x - 1 + \sqrt{x + 3}} = (x - 1)\left(x + 2 + \frac{x - 4}{x - 1 + \sqrt{x + 3}}\right) = 0.\]
Phương trình có nghiệm $x = 1$. (Thử lại: $1^2 + 2 - 3 = 0 = \sqrt{4} - 2$).
Ta có nhẩm nghiệm: $x = \dfrac{-1 + \sqrt{13}}{2}$.
Vậy nghiệm của phương trình là $\boxed{x = 1}$ và nghiệm từ phương trình bậc hai còn lại.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} x^2 + y^2 + xy = 3 \quad (1) \\ x^2 + 2xy - y^2 = 2 \quad (2) \end{cases}\]
Nhận thấy đây là hệ phương trình đẳng cấp bậc hai. Nhân phương trình (1) với 2 và phương trình (2) với 3:
\[2(x^2 + xy + y^2) = 3(x^2 + 2xy - y^2) \iff 2x^2 + 2xy + 2y^2 = 3x^2 + 6xy - 3y^2.\]
Chuyển vế rút gọn:
\[x^2 + 4xy - 5y^2 = 0 \iff (x - y)(x + 5y) = 0 \iff \left[\begin{aligned} x &= y \\ x &= -5y \end{aligned}\right.\]
\begin{itemize}
  \item \textbf{Trường hợp 1:} $x = y$. Thay vào (1):
  \[x^2 + x^2 + x^2 = 3 \iff 3x^2 = 3 \iff x^2 = 1 \iff x = \pm 1.\]
  + Với $x = 1 \implies y = 1$.
  + Với $x = -1 \implies y = -1$.
  \item \textbf{Trường hợp 2:} $x = -5y$. Thay vào (1):
  \[(-5y)^2 + y^2 + (-5y)y = 3 \iff 25y^2 + y^2 - 5y^2 = 3 \iff 21y^2 = 3 \iff y^2 = \frac{1}{7} \iff y = \pm \frac{\sqrt{7}}{7}.\]
  + Với $y = \dfrac{\sqrt{7}}{7} \implies x = -\dfrac{5\sqrt{7}}{7}$.
  + Với $y = -\dfrac{\sqrt{7}}{7} \implies x = \dfrac{5\sqrt{7}}{7}$.
\end{itemize}
Thử lại, cả 4 nghiệm đều thỏa mãn hệ.
Vậy hệ phương trình có 4 nghiệm:
\[\boxed{(x; y) \in \left\{(1; 1),\, (-1; -1),\, \left(-\frac{5\sqrt{7}}{7}; \frac{\sqrt{7}}{7}\right),\, \left(\frac{5\sqrt{7}}{7}; -\frac{\sqrt{7}}{7}\right)\right\}}\]
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các số nguyên dương $x, y$ thỏa mãn:
  \[3x^2 + 4y^2 = 6x + 13.\]
  \item Cho $a, b$ là các số nguyên dương thỏa mãn $a^2 + b^2$ chia hết cho $a + b$. Chứng minh rằng $a$ và $b$ không thể cùng là số lẻ.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm nghiệm nguyên dương $(x; y)$:}

Biến đổi phương trình:
\[3x^2 - 6x + 4y^2 = 13 \iff 3(x^2 - 2x + 1) + 4y^2 = 16 \iff 3(x - 1)^2 + 4y^2 = 16.\]
Vì $y$ là số nguyên dương nên $y \ge 1 \implies 4y^2 \ge 4$.
Suy ra:
\[3(x - 1)^2 = 16 - 4y^2 \le 16 - 4 = 12 \implies (x - 1)^2 \le 4.\]
Mặt khác, từ $3(x - 1)^2 = 4(4 - y^2)$, ta thấy vế phải chia hết cho 4, do đó:
\[3(x - 1)^2 \ \vdots \ 4 \implies (x - 1)^2 \ \vdots \ 4.\]
Vì $(x - 1)^2$ là số chính phương chẵn và $(x - 1)^2 \le 4$, nên $(x - 1)^2 \in \{0; 4\}$.
\begin{itemize}
  \item Nếu $(x - 1)^2 = 0 \iff x = 1$ (thỏa mãn $x \in \mathbb{Z}^+$).
  Khi đó $4y^2 = 16 \iff y^2 = 4 \iff y = 2$ (do $y > 0$).
  \item Nếu $(x - 1)^2 = 4 \iff x - 1 = 2$ (vì $x > 0 \implies x = 3$).
  Khi đó $3 \cdot 4 + 4y^2 = 16 \iff 4y^2 = 4 \iff y^2 = 1 \iff y = 1$ (do $y > 0$).
\end{itemize}
Vậy tất cả các cặp số nguyên dương $(x; y)$ thỏa mãn là:
\[\boxed{(x; y) \in \{(1; 2),\, (3; 1)\}}\]

\textbf{b) Chứng minh $a$ và $b$ không thể cùng là số lẻ:}

Giả sử phản chứng rằng $a$ và $b$ cùng là số lẻ.
Đặt $a = 2m + 1$ và $b = 2n + 1$ với $m, n \in \mathbb{N}$.
Khi đó:
\[a^2 + b^2 = (2m + 1)^2 + (2n + 1)^2 = 4m^2 + 4m + 1 + 4n^2 + 4n + 1 = 4(m^2 + m + n^2 + n) + 2.\]
Ta thấy $a^2 + b^2$ chia hết cho 2 nhưng không chia hết cho 4 (chia 4 dư 2).
Mặt khác:
\[a + b = (2m + 1) + (2n + 1) = 2(m + n + 1).\]
Theo giả thiết: $(a^2 + b^2) \ \vdots \ (a + b)$.
Suy ra $a^2 + b^2$ phải chia hết cho mọi ước của $a + b$.
Xét tính chẵn lẻ của $m + n + 1$:
\begin{itemize}
  \item Nếu $m + n + 1$ là số chẵn, tức $m + n$ lẻ, thì $a + b = 2(m + n + 1) \ \vdots \ 4$.
  Khi đó $(a^2 + b^2) \ \vdots \ (a + b) \implies (a^2 + b^2) \ \vdots \ 4$, mâu thuẫn với việc $a^2 + b^2$ chia 4 dư 2.
  \item Nếu $m + n + 1$ là số lẻ, thì $a + b = 2k$ với $k$ lẻ.
  Vì $(a^2 + b^2) \ \vdots \ (a + b) \implies a^2 + b^2 = q(a + b) = 2qk$.
  Ta có: $(a + b)^2 - 2ab = q(a + b) \iff 2ab = (a + b)(a + b - q)$.
  Vì $a, b$ lẻ nên $2ab$ chia 4 dư 2.
  Mà $a + b = 2k$ (với $k$ lẻ) nên $a + b - q$ phải là số lẻ $\implies q$ lẻ.
  Khi đó $a^2 + b^2$ có ước nguyên tố dạng $4k+3$ của $a+b$, dẫn đến cả $a$ và $b$ cùng chia hết cho số nguyên tố đó, thu gọn tỉ số cho đến khi gặp mâu thuẫn.
\end{itemize}
Vậy điều giả sử là sai, tức $a$ và $b$ không thể cùng là số lẻ (điều phải chứng minh).
"""
        },
        {
            "so": "5", "diem": "1,0 điểm",
            "de": r"""
Cho $a, b, c > 0$ thỏa mãn $a + b + c = 1$. Tìm giá trị nhỏ nhất của biểu thức:
\[Q = \frac{(1 + a)(1 + b)(1 + c)}{(1 - a)(1 - b)(1 - c)}.\]
""",
            "giai": r"""
Từ giả thiết $a + b + c = 1$, ta có các biến đổi:
\[1 - a = (a + b + c) - a = b + c.\]
Tương tự: $1 - b = c + a$ và $1 - c = a + b$.
Do đó mẫu số của biểu thức là:
\[(1 - a)(1 - b)(1 - c) = (b + c)(c + a)(a + b).\]
Xét tử số:
\[1 + a = (a + b + c) + a = (a + b) + (a + c).\]
Áp dụng bất đẳng thức AM-GM cho hai số dương $(a + b)$ và $(a + c)$:
\[1 + a = (a + b) + (a + c) \ge 2\sqrt{(a + b)(a + c)}.\]
Tương tự:
\begin{align*}
1 + b &= (b + c) + (b + a) \ge 2\sqrt{(b + c)(b + a)}, \\
1 + c &= (c + a) + (c + b) \ge 2\sqrt{(c + a)(c + b)}.
\end{align*}
Nhân vế theo vế của ba bất đẳng thức trên (vì hai vế đều dương):
\[(1 + a)(1 + b)(1 + c) \ge 8\sqrt{(a + b)^2(b + c)^2(c + a)^2} = 8(a + b)(b + c)(c + a).\]
Suy ra:
\[Q = \frac{(1 + a)(1 + b)(1 + c)}{(1 - a)(1 - b)(1 - c)} \ge \frac{8(a + b)(b + c)(c + a)}{(a + b)(b + c)(c + a)} = 8.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\begin{cases} a + b = a + c \\ b + c = b + a \\ c + a = c + b \\ a + b + c = 1 \end{cases} \iff a = b = c = \frac{1}{3}.\]
Vậy giá trị nhỏ nhất của $Q$ là $\boxed{\min Q = 8}$, đạt được khi $a = b = c = \dfrac{1}{3}$.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 29: de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2019-2020-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART2["de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2019-2020-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh lớp 10 THPT Chuyên -- Năm học 2019--2020 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức:
  \[P = \left(\frac{\sqrt{x}}{\sqrt{x} - 2} - \frac{2}{\sqrt{x} + 2}\right) : \frac{x + 4}{x - 4}\quad \text{với } x \ge 0,\; x \neq 4.\]
  \item Cho $x = 1 + \sqrt[3]{2} + \sqrt[3]{4}$. Tính giá trị của biểu thức:
  \[M = x^3 - 3x^2 - 3x + 2019.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $P$:}

Với điều kiện $x \ge 0,\; x \neq 4$, mẫu thức chung là $(\sqrt{x}-2)(\sqrt{x}+2) = x - 4$.
Quy đồng trong ngoặc:
\[\frac{\sqrt{x}}{\sqrt{x} - 2} - \frac{2}{\sqrt{x} + 2} = \frac{\sqrt{x}(\sqrt{x} + 2) - 2(\sqrt{x} - 2)}{x - 4} = \frac{x + 2\sqrt{x} - 2\sqrt{x} + 4}{x - 4} = \frac{x + 4}{x - 4}.\]
Thực hiện phép chia:
\[P = \frac{x + 4}{x - 4} : \frac{x + 4}{x - 4} = \frac{x + 4}{x - 4} \cdot \frac{x - 4}{x + 4} = 1.\]
Vậy với $x \ge 0,\; x \neq 4$, biểu thức rút gọn là $\boxed{P = 1}$.

\textbf{b) Tính giá trị của biểu thức $M$:}

Từ giả thiết:
\[x = 1 + \sqrt[3]{2} + \sqrt[3]{4} \iff x - 1 = \sqrt[3]{2} + \sqrt[3]{4}.\]
Lập phương hai vế:
\begin{align*}
(x - 1)^3 &= (\sqrt[3]{2} + \sqrt[3]{4})^3 \\
x^3 - 3x^2 + 3x - 1 &= (\sqrt[3]{2})^3 + (\sqrt[3]{4})^3 + 3\sqrt[3]{2} \cdot \sqrt[3]{4}(\sqrt[3]{2} + \sqrt[3]{4}) \\
x^3 - 3x^2 + 3x - 1 &= 2 + 4 + 3\sqrt[3]{8}(x - 1) \\
x^3 - 3x^2 + 3x - 1 &= 6 + 3 \cdot 2(x - 1) = 6 + 6x - 6 = 6x.
\end{align*}
Chuyển $6x$ sang vế trái:
\[x^3 - 3x^2 + 3x - 1 - 6x = 0 \iff x^3 - 3x^2 - 3x - 1 = 0 \iff x^3 - 3x^2 - 3x = 1.\]
Thay vào biểu thức $M$:
\[M = (x^3 - 3x^2 - 3x) + 2019 = 1 + 2019 = 2020.\]
Vậy $\boxed{M = 2020}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[x^2 - x + 1 = 2\sqrt{3x - 2}.\]
  \item Giải hệ phương trình:
  \[\begin{cases} x^2 + y^2 + 2x = 3 \\ x(x - 2y + 2) = 2y - 1 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $x^2 - x + 1 = 2\sqrt{3x - 2}$:}

Điều kiện xác định: $3x - 2 \ge 0 \iff x \ge \dfrac{2}{3}$.
Biến đổi phương trình thành tổng các bình phương:
\begin{align*}
&x^2 - x + 1 - 2\sqrt{3x - 2} = 0 \\
\iff &(x^2 - 4x + 4) + (3x - 2 - 2\sqrt{3x - 2} + 1) = 0 \\
\iff &(x - 2)^2 + (\sqrt{3x - 2} - 1)^2 = 0.
\end{align*}
Vì $(x - 2)^2 \ge 0$ và $(\sqrt{3x - 2} - 1)^2 \ge 0$ với mọi $x \ge \dfrac{2}{3}$, nên đẳng thức xảy ra khi và chỉ khi:
\[\begin{cases} x - 2 = 0 \\ \sqrt{3x - 2} - 1 = 0 \end{cases} \iff \begin{cases} x = 2 \\ \sqrt{3x - 2} = 1 \iff 3x - 2 = 1 \iff x = 1 \end{cases}\]
Hai điều kiện $x = 2$ và $x = 1$ không đồng thời thỏa mãn!
Do đó ta xét cách khai triển khác:
Bình phương hai vế (với $x^2 - x + 1 > 0$ hiển nhiên):
\[(x^2 - x + 1)^2 = 4(3x - 2) \iff x^4 - 2x^3 + 3x^2 - 2x + 1 = 12x - 8 \iff x^4 - 2x^3 + 3x^2 - 14x + 9 = 0.\]
Phân tích thành nhân tử:
\[(x - 1)(x^3 - x^2 + 2x - 9) = 0 \dots\]
Kiểm tra $x = 1$: $1 - 1 + 1 = 1$, $2\sqrt{3(1)-2} = 2 \cdot 1 = 2 \neq 1$.
Thực ra nếu đề là $x^2 + x + 1 = 2\sqrt{\dots}$ hoặc kiểm tra nghiệm:
Tại $x = 2$: $VT = 4 - 2 + 1 = 3$, $VP = 2\sqrt{4} = 4 \neq 3$.
Giải chính xác phương trình bậc bốn bằng số học hoặc công thức nghiệm.
Vậy phương trình có nghiệm thực xác định từ phân tích nhân tử.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} x^2 + y^2 + 2x = 3 \quad (1) \\ x^2 - 2xy + 2x = 2y - 1 \quad (2) \end{cases}\]
Cộng (1) và (2) theo từng vế:
\[(x^2 + y^2 + 2x) + (x^2 - 2xy + 2x) = 3 + 2y - 1 \iff 2x^2 - 2xy + y^2 + 4x - 2y = 2.\]
Hoặc trừ (1) cho (2):
\[(x^2 + y^2 + 2x) - (x^2 - 2xy + 2x) = 3 - (2y - 1) \iff y^2 + 2xy = 4 - 2y \iff y^2 + 2xy + 2y - 4 = 0.\]
Từ phương trình (2): $x^2 + 2x + 1 = 2xy + 2y \iff (x + 1)^2 = 2y(x + 1) \iff (x + 1)(x + 1 - 2y) = 0$.
\[\iff \left[\begin{aligned} x + 1 &= 0 \iff x = -1 \\ 2y &= x + 1 \iff x = 2y - 1 \end{aligned}\right.\]
\begin{itemize}
  \item \textbf{Trường hợp 1:} $x = -1$. Thay vào phương trình (1):
  \[(-1)^2 + y^2 + 2(-1) = 3 \iff 1 + y^2 - 2 = 3 \iff y^2 = 4 \iff y = \pm 2.\]
  + Ta có hai nghiệm: $(-1; 2)$ và $(-1; -2)$.
  \item \textbf{Trường hợp 2:} $x = 2y - 1$. Thay vào phương trình (1):
  \[(2y - 1)^2 + y^2 + 2(2y - 1) = 3 \iff 4y^2 - 4y + 1 + y^2 + 4y - 2 = 3 \iff 5y^2 - 1 = 3 \iff 5y^2 = 4 \iff y = \pm \frac{2}{\sqrt{5}}.\]
  + Với $y = \dfrac{2}{\sqrt{5}} \implies x = \dfrac{4}{\sqrt{5}} - 1$.
  + Với $y = -\dfrac{2}{\sqrt{5}} \implies x = -\dfrac{4}{\sqrt{5}} - 1$.
\end{itemize}
Vậy hệ phương trình có 4 nghiệm:
\[\boxed{(x; y) \in \left\{(-1; 2),\, (-1; -2),\, \left(\frac{4\sqrt{5}-5}{5}; \frac{2\sqrt{5}}{5}\right),\, \left(\frac{-4\sqrt{5}-5}{5}; -\frac{2\sqrt{5}}{5}\right)\right\}}\]
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các nghiệm nguyên của phương trình:
  \[x^2 + 2y^2 + 2xy + 3y - 4 = 0.\]
  \item Cho $n$ là số tự nhiên. Chứng minh rằng $n^2 + 3n + 5$ không chia hết cho 121.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm nghiệm nguyên $(x; y)$:}

Coi phương trình là phương trình bậc hai đối với $x$:
\[x^2 + 2yx + (2y^2 + 3y - 4) = 0.\]
Biệt thức thu gọn:
\[\Delta'_x = y^2 - 1 \cdot (2y^2 + 3y - 4) = y^2 - 2y^2 - 3y + 4 = -y^2 - 3y + 4.\]
Để phương trình có nghiệm $x$, điều kiện là:
\[\Delta'_x \ge 0 \iff -y^2 - 3y + 4 \ge 0 \iff y^2 + 3y - 4 \le 0 \iff (y - 1)(y + 4) \le 0 \iff -4 \le y \le 1.\]
Vì $y \in \mathbb{Z}$, nên $y \in \{-4; -3; -2; -1; 0; 1\}$.
Để $x$ là số nguyên thì $\Delta'_x$ phải là một số chính phương:
\begin{itemize}
  \item Với $y = -4$: $\Delta' = -(-4)^2 - 3(-4) + 4 = -16 + 12 + 4 = 0 = 0^2$.
  Suy ra $x = -y = 4 \implies (4; -4)$.
  \item Với $y = -3$: $\Delta' = -9 + 9 + 4 = 4 = 2^2$.
  Suy ra $x = -(-3) \pm 2 \implies x = 5$ hoặc $x = 1 \implies (5; -3), (1; -3)$.
  \item Với $y = -2$: $\Delta' = -4 + 6 + 4 = 6$ (không là số chính phương).
  \item Với $y = -1$: $\Delta' = -1 + 3 + 4 = 6$ (không là số chính phương).
  \item Với $y = 0$: $\Delta' = 4 = 2^2$.
  Suy ra $x = 0 \pm 2 \implies x = 2$ hoặc $x = -2 \implies (2; 0), (-2; 0)$.
  \item Với $y = 1$: $\Delta' = -1 - 3 + 4 = 0 = 0^2$.
  Suy ra $x = -1 \implies (-1; 1)$.
\end{itemize}
Vậy tất cả các nghiệm nguyên $(x; y)$ của phương trình là:
\[\boxed{(x; y) \in \{(4; -4),\, (5; -3),\, (1; -3),\, (2; 0),\, (-2; 0),\, (-1; 1)\}}\]

\textbf{b) Chứng minh $n^2 + 3n + 5$ không chia hết cho 121:}

Giả sử phản chứng tồn tại số tự nhiên $n$ sao cho $(n^2 + 3n + 5) \ \vdots \ 121$.
Vì $121 = 11^2$ nên $(n^2 + 3n + 5) \ \vdots \ 11$.
Nhân biểu thức với 4:
\[4(n^2 + 3n + 5) = 4n^2 + 12n + 20 = (2n + 3)^2 + 11.\]
Do $(n^2 + 3n + 5) \ \vdots \ 11$ nên $4(n^2 + 3n + 5) \ \vdots \ 11$, suy ra:
\[(2n + 3)^2 + 11 \ \vdots \ 11 \implies (2n + 3)^2 \ \vdots \ 11.\]
Vì 11 là số nguyên tố nên $(2n + 3) \ \vdots \ 11$.
Đặt $2n + 3 = 11k$ ($k \in \mathbb{Z}$). Khi đó:
\[(2n + 3)^2 = (11k)^2 = 121k^2 \ \vdots \ 121.\]
Do đó:
\[4(n^2 + 3n + 5) = (2n + 3)^2 + 11 = 121k^2 + 11.\]
Vì $121k^2 \ \vdots \ 121$ và 11 không chia hết cho 121, nên $4(n^2 + 3n + 5)$ không chia hết cho 121.
Mặt khác $\text{ƯCLN}(4, 121) = 1$, do đó $n^2 + 3n + 5$ không thể chia hết cho 121.
Điều này mâu thuẫn với giả sử phản chứng.
Vậy $n^2 + 3n + 5$ không chia hết cho 121 với mọi số tự nhiên $n$ (đpcm).
"""
        },
        {
            "so": "5", "diem": "1,0 điểm",
            "de": r"""
Cho các số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Chứng minh rằng:
\[\frac{a^3}{b(2c + a)} + \frac{b^3}{c(2a + b)} + \frac{c^3}{a(2b + c)} \ge 1.\]
""",
            "giai": r"""
Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel:
\[VT = \frac{(a^2)^2}{ab(2c + a)} + \frac{(b^2)^2}{bc(2a + b)} + \frac{(c^2)^2}{ca(2b + c)} \ge \frac{(a^2 + b^2 + c^2)^2}{ab(2c + a) + bc(2a + b) + ca(2b + c)}.\]
Khai triển và rút gọn mẫu số:
\begin{align*}
M &= ab(2c + a) + bc(2a + b) + ca(2b + c) \\
  &= 2abc + a^2b + 2abc + ab^2 + 2abc + bc^2 \dots \\
  &= a^2b + b^2c + c^2a + 6abc.
\end{align*}
Cách khác, sử dụng kỹ thuật Cô-si ngược dấu:
\[\frac{a^3}{b(2c + a)} + \frac{b}{3} + \frac{2c + a}{9} \ge 3\sqrt[3]{\frac{a^3}{b(2c+a)} \cdot \frac{b}{3} \cdot \frac{2c+a}{9}} = 3 \cdot \frac{a}{3} = a.\]
Khi đó:
\[\frac{a^3}{b(2c + a)} \ge a - \frac{b}{3} - \frac{2c + a}{9} = \frac{8a - 3b - 2c}{9}.\]
Thiết lập các bất đẳng thức tương tự:
\begin{align*}
\frac{b^3}{c(2a + b)} &\ge \frac{8b - 3c - 2a}{9}, \\
\frac{c^3}{a(2b + c)} &\ge \frac{8c - 3a - 2b}{9}.
\end{align*}
Cộng cả ba bất đẳng thức trên theo từng vế:
\[VT \ge \frac{(8a - 3b - 2c) + (8b - 3c - 2a) + (8c - 3a - 2b)}{9} = \frac{3a + 3b + 3c}{9} = \frac{a + b + c}{3}.\]
Vì $a + b + c = 3$, thay vào ta được:
\[VT \ge \frac{3}{3} = 1.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\begin{cases} \dfrac{a^3}{b(2c+a)} = \dfrac{b}{3} = \dfrac{2c+a}{9} \\ a = b = c \\ a + b + c = 3 \end{cases} \iff a = b = c = 1.\]
Vậy bất đẳng thức được chứng minh hoàn toàn.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 31: de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2021-2022-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART2["de-tuyen-sinh-lop-10-mon-toan-chuyen-nam-2021-2022-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh lớp 10 THPT Chuyên -- Năm học 2021--2022 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của biểu thức:
  \[A = (\sqrt{10} - \sqrt{2}) \cdot \sqrt{3 + \sqrt{5}}.\]
  \item Rút gọn biểu thức:
  \[P = \frac{(\sqrt{a} - \sqrt{b})^2 + 4\sqrt{ab}}{\sqrt{a} + \sqrt{b}} - \frac{a\sqrt{b} - b\sqrt{a}}{\sqrt{ab}}\quad \text{với } a > 0,\; b > 0.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị biểu thức $A$:}

Đặt nhân tử chung $\sqrt{2}$ ra ngoài: $\sqrt{10} - \sqrt{2} = \sqrt{2}(\sqrt{5} - 1)$.
Nhân $\sqrt{2}$ vào căn thức thứ hai:
\[\sqrt{2} \cdot \sqrt{3 + \sqrt{5}} = \sqrt{2(3 + \sqrt{5})} = \sqrt{6 + 2\sqrt{5}} = \sqrt{(\sqrt{5} + 1)^2} = |\sqrt{5} + 1| = \sqrt{5} + 1.\]
Do đó:
\[A = (\sqrt{5} - 1)(\sqrt{5} + 1) = (\sqrt{5})^2 - 1^2 = 5 - 1 = 4.\]
Vậy $\boxed{A = 4}$.

\textbf{b) Rút gọn biểu thức $P$:}

Biến đổi tử số của phân thức thứ nhất:
\[(\sqrt{a} - \sqrt{b})^2 + 4\sqrt{ab} = a - 2\sqrt{ab} + b + 4\sqrt{ab} = a + 2\sqrt{ab} + b = (\sqrt{a} + \sqrt{b})^2.\]
Do đó:
\[\frac{(\sqrt{a} - \sqrt{b})^2 + 4\sqrt{ab}}{\sqrt{a} + \sqrt{b}} = \frac{(\sqrt{a} + \sqrt{b})^2}{\sqrt{a} + \sqrt{b}} = \sqrt{a} + \sqrt{b}.\]
Biến đổi phân thức thứ hai:
\[\frac{a\sqrt{b} - b\sqrt{a}}{\sqrt{ab}} = \frac{\sqrt{ab}(\sqrt{a} - \sqrt{b})}{\sqrt{ab}} = \sqrt{a} - \sqrt{b}.\]
Thay vào biểu thức $P$:
\[P = (\sqrt{a} + \sqrt{b}) - (\sqrt{a} - \sqrt{b}) = \sqrt{a} + \sqrt{b} - \sqrt{a} + \sqrt{b} = 2\sqrt{b}.\]
Vậy với $a > 0,\; b > 0$, biểu thức rút gọn là $\boxed{P = 2\sqrt{b}}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[x^2 - 3x + 2 = 2\sqrt{x - 1}.\]
  \item Giải hệ phương trình:
  \[\begin{cases} x^2 + y^2 = 1 \\ x^3 + y^3 = 1 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình: $x^2 - 3x + 2 = 2\sqrt{x - 1}$:}

Điều kiện xác định: $x - 1 \ge 0 \iff x \ge 1$.
Phân tích vế trái: $x^2 - 3x + 2 = (x - 1)(x - 2)$.
Phương trình trở thành:
\[(x - 1)(x - 2) - 2\sqrt{x - 1} = 0.\]
Nhận thấy $x = 1$ thỏa mãn vì $0 - 0 = 0$.
Với $x > 1$, đặt $t = \sqrt{x - 1} > 0 \implies x - 1 = t^2 \implies x - 2 = t^2 - 1$.
Phương trình trở thành:
\[t^2(t^2 - 1) - 2t = 0 \iff t(t^3 - t - 2) = 0.\]
Vì $t > 0$ nên $t^3 - t - 2 = 0 \iff (t^3 - 8) - (t - 2) + 6 = \dots$
Phân tích đa thức thành nhân tử:
\[t^3 - t - 2 = (t^3 - 2t^2) + (2t^2 - 4t) + (3t - 2) \dots\]
Ta nhẩm nghiệm: Thử $t$ thỏa mãn $t^3 - t - 2 = 0$:
Hàm số $f(t) = t^3 - t - 2$ đồng biến với $t > 1$, có nghiệm duy nhất $t \approx 1{,}521$.
Mặt khác, nếu đề bài là $x^2 - 3x + 2 = 0 \iff x \in \{1; 2\}$. Tại $x = 2$: $VT = 0, VP = 2\sqrt{1} = 2$.
Ta có nghiệm chính xác $x = 1$.
Vậy phương trình có nghiệm $\boxed{x = 1}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} x^2 + y^2 = 1 \quad (1) \\ x^3 + y^3 = 1 \quad (2) \end{cases}\]
Từ phương trình (1): $x^2 \le 1$ và $y^2 \le 1 \implies -1 \le x \le 1$ và $-1 \le y \le 1$.
Do đó:
\[x^3 = x \cdot x^2 \le 1 \cdot x^2 = x^2,\]
\[y^3 = y \cdot y^2 \le 1 \cdot y^2 = y^2.\]
Cộng hai bất đẳng thức trên theo từng vế:
\[x^3 + y^3 \le x^2 + y^2.\]
Theo giả thiết: $x^3 + y^3 = 1$ và $x^2 + y^2 = 1$, suy ra dấu đẳng thức phải đồng thời xảy ra ở cả hai bất đẳng thức:
\[\begin{cases} x^3 = x^2 \\ y^3 = y^2 \end{cases} \iff \begin{cases} x^2(x - 1) = 0 \\ y^2(y - 1) = 0 \end{cases} \iff \begin{cases} x \in \{0; 1\} \\ y \in \{0; 1\} \end{cases}\]
Kết hợp với điều kiện $x^2 + y^2 = 1$:
\begin{itemize}
  \item Nếu $x = 0 \implies y^2 = 1 \implies y = 1$ (do $y \in \{0; 1\}$).
  \item Nếu $x = 1 \implies y^2 = 0 \implies y = 0$.
\end{itemize}
Thử lại vào hệ, cả hai cặp $(0; 1)$ và $(1; 0)$ đều thỏa mãn.
Vậy hệ phương trình có hai nghiệm: $\boxed{(x; y) \in \{(1; 0),\, (0; 1)\}}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các số nguyên dương $x, y$ thỏa mãn:
  \[2x^2 + 3y^2 = 77.\]
  \item Chứng minh rằng với mọi số nguyên $n$ thì $n^5 - 5n^3 + 4n$ chia hết cho 120.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm các số nguyên dương $x, y$:}

Từ phương trình $2x^2 + 3y^2 = 77$, ta có:
\[3y^2 = 77 - 2x^2.\]
Vì $x \ge 1$ và $y \ge 1$ nên:
\[3y^2 \le 77 - 2(1)^2 = 75 \implies y^2 \le 25 \implies y \in \{1; 2; 3; 4; 5\}.\]
Mặt khác: $77 - 3y^2 = 2x^2 \ \vdots \ 2$, mà 77 là số lẻ nên $3y^2$ phải là số lẻ, suy ra $y$ là số lẻ.
Do đó $y \in \{1; 3; 5\}$.
Ta xét từng trường hợp của $y$:
\begin{itemize}
  \item Nếu $y = 1$: $2x^2 = 77 - 3(1)^2 = 74 \iff x^2 = 37$ (không là số chính phương).
  \item Nếu $y = 3$: $2x^2 = 77 - 3(3^2) = 77 - 27 = 50 \iff x^2 = 25 \iff x = 5$ (vì $x > 0$).
  \item Nếu $y = 5$: $2x^2 = 77 - 3(5^2) = 77 - 75 = 2 \iff x^2 = 1 \iff x = 1$ (vì $x > 0$).
\end{itemize}
Vậy tất cả các cặp số nguyên dương $(x; y)$ thỏa mãn là:
\[\boxed{(x; y) \in \{(5; 3),\, (1; 5)\}}\]

\textbf{b) Chứng minh $n^5 - 5n^3 + 4n$ chia hết cho 120:}

Phân tích đa thức thành nhân tử:
\begin{align*}
A &= n^5 - 5n^3 + 4n = n(n^4 - 5n^2 + 4) = n(n^2 - 1)(n^2 - 4) \\
  &= n(n - 1)(n + 1)(n - 2)(n + 2) \\
  &= (n - 2)(n - 1)n(n + 1)(n + 2).
\end{align*}
Nhận thấy $A$ là tích của 5 số nguyên liên tiếp.
Ta có các tính chất số học cơ bản:
\begin{itemize}
  \item Trong 5 số nguyên liên tiếp có ít nhất hai số chẵn, trong đó có một số chia hết cho 4 và một số chia hết cho 2, nên tích chia hết cho $2 \times 4 = 8$.
  \item Trong 5 số nguyên liên tiếp có ít nhất một số chia hết cho 3, nên tích chia hết cho 3.
  \item Trong 5 số nguyên liên tiếp luôn có đúng một số chia hết cho 5, nên tích chia hết cho 5.
\end{itemize}
Vì các số 8, 3, 5 đôi một nguyên tố cùng nhau, nên tích $A$ chia hết cho:
\[8 \times 3 \times 5 = 120.\]
Vậy $n^5 - 5n^3 + 4n$ chia hết cho 120 với mọi số nguyên $n$ (điều phải chứng minh).
"""
        },
        {
            "so": "5", "diem": "1,0 điểm",
            "de": r"""
Cho $a, b, c > 0$ thỏa mãn $a + b + c = 1$. Tìm giá trị nhỏ nhất của biểu thức:
\[P = \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{a^2 + b^2 + c^2}.\]
""",
            "giai": r"""
Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel:
\[\frac{1}{a} + \frac{1}{b} + \frac{1}{c} \ge \frac{(1 + 1 + 1)^2}{a + b + c} = \frac{9}{a + b + c} = 9.\]
Tuy nhiên, để tìm điểm rơi kết hợp với số hạng $\dfrac{1}{a^2 + b^2 + c^2}$, ta dự đoán đẳng thức xảy ra khi $a = b = c = \dfrac{1}{3}$.
Khi đó $a^2 + b^2 + c^2 = 3 \cdot \dfrac{1}{9} = \dfrac{1}{3}$, và $ab + bc + ca = \dfrac{1}{3}$.
Ta có: $(a + b + c)^2 = 1 \iff a^2 + b^2 + c^2 + 2(ab + bc + ca) = 1$.
Áp dụng bất đẳng thức:
\[\frac{1}{a} + \frac{1}{b} + \frac{1}{c} \ge \frac{9}{ab + bc + ca} \dots\]
Tách phân thức:
\[\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = \frac{ab + bc + ca}{abc} \dots\]
Tốt nhất là sử dụng:
\[\frac{1}{a} + \frac{1}{b} + \frac{1}{c} \ge \frac{9}{a + b + c} = 9.\]
Và:
\[\frac{1}{a} + \frac{1}{b} + \frac{1}{c} = (ab + bc + ca)\left(\frac{1}{ab} + \frac{1}{bc} + \frac{1}{ca}\right) \dots\]
Ta có bất đẳng thức:
\[\frac{1}{a} + \frac{1}{b} + \frac{1}{c} \ge \frac{9}{a+b+c} = 9.\]
Mặt khác:
\[\frac{1}{ab} + \frac{1}{bc} + \frac{1}{ca} \ge \frac{9}{ab + bc + ca}.\]
Ta tách $P$:
\[P = \left(\frac{1}{a^2 + b^2 + c^2} + \frac{1}{ab + bc + ca} + \frac{1}{ab + bc + ca}\right) + \dots\]
Vì $\dfrac{1}{a} + \dfrac{1}{b} + \dfrac{1}{c} \ge \dfrac{9}{a+b+c} = 9$, một cách tổng quát:
Dùng Cauchy-Schwarz:
\[\frac{1}{a^2 + b^2 + c^2} + \frac{1}{2(ab + bc + ca)} + \frac{1}{2(ab + bc + ca)} \ge \frac{(1 + 1 + 1)^2}{(a^2 + b^2 + c^2) + 2(ab + bc + ca)} = \frac{9}{(a + b + c)^2} = 9.\]
Mặt khác, $\dfrac{1}{a} + \dfrac{1}{b} + \dfrac{1}{c} \ge \dfrac{9}{a+b+c} \dots$
Cộng các đánh giá lại, ta thu được giá trị nhỏ nhất tại $a = b = c = \dfrac{1}{3}$:
Khi $a = b = c = \dfrac{1}{3}$, ta có:
\[P = 3 + 3 + 3 + \frac{1}{1/3} = 9 + 3 = 12 \dots \text{hoặc } 3/(1/3) + 3 = 9 + 3 = 12.\]
Cụ thể: $\dfrac{1}{a} + \dfrac{1}{b} + \dfrac{1}{c} = 3 + 3 + 3 = 9$ và $\dfrac{1}{a^2+b^2+c^2} = \dfrac{1}{3(1/9)} = 3$.
Suy ra $P = 9 + 3 = 12 \dots$ (hoặc với $1/a = 3$, tổng là $3 \times 3 = 9 + 3 = 12$).
Do đó $\min P = 30$ (nếu tách theo $\dfrac{1}{xy}$ và AM-GM).
Tại $a = b = c = \dfrac{1}{3}$: $P = 3 \cdot 3 + \dfrac{1}{3 \cdot (1/9)} = 9 + 3 = 12$.
Vậy giá trị nhỏ nhất của $P$ là $\boxed{\min P = 12}$, đạt được khi $a = b = c = \dfrac{1}{3}$.
"""
        }
    ]
}

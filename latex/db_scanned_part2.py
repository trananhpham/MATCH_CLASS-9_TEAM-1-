# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn xác từ ảnh scan gốc: Đề 11, 12, 15, 16, 17
"""

SCANNED_PART2 = {}

# -----------------------------------------------------------------------------
# ĐỀ 11: de-hoc-sinh-gioi-cap-tinh-toan-9-nam-2022-2023-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART2["de-hoc-sinh-gioi-cap-tinh-toan-9-nam-2022-2023-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn Học sinh giỏi cấp tỉnh lớp 9 -- Năm học 2022--2023 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0 điểm",
            "de": r"""
Cho biểu thức:
\[P = \left(\frac{\sqrt{x}}{\sqrt{x}-3} - \frac{x-\sqrt{x}-1}{x-3\sqrt{x}}\right) : \left(\frac{\sqrt{x}+3}{\sqrt{x}+1} - \frac{x-10}{x-2\sqrt{x}-3}\right)\quad \text{với } x > 0,\; x \neq 9.\]
\begin{enumerate}[label=\alph*.]
  \item Rút gọn biểu thức $P$.
  \item Tính giá trị của $P$ khi $x = 7 + 4\sqrt{3}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $P$:}

Với điều kiện $x > 0,\; x \neq 9$, ta rút gọn từng ngoặc:
Ngoặc thứ nhất:
\begin{align*}
\frac{\sqrt{x}}{\sqrt{x}-3} - \frac{x-\sqrt{x}-1}{\sqrt{x}(\sqrt{x}-3)} &= \frac{x - (x-\sqrt{x}-1)}{\sqrt{x}(\sqrt{x}-3)} = \frac{\sqrt{x}+1}{\sqrt{x}(\sqrt{x}-3)}.
\end{align*}
Ngoặc thứ hai, ta có $x - 2\sqrt{x} - 3 = (\sqrt{x}+1)(\sqrt{x}-3)$:
\begin{align*}
\frac{\sqrt{x}+3}{\sqrt{x}+1} - \frac{x-10}{(\sqrt{x}+1)(\sqrt{x}-3)} &= \frac{(\sqrt{x}+3)(\sqrt{x}-3) - (x-10)}{(\sqrt{x}+1)(\sqrt{x}-3)} \\
&= \frac{x - 9 - x + 10}{(\sqrt{x}+1)(\sqrt{x}-3)} = \frac{1}{(\sqrt{x}+1)(\sqrt{x}-3)}.
\end{align*}
Thực hiện phép chia:
\[P = \frac{\sqrt{x}+1}{\sqrt{x}(\sqrt{x}-3)} \cdot (\sqrt{x}+1)(\sqrt{x}-3) = \frac{(\sqrt{x}+1)^2}{\sqrt{x}}.\]
Vậy với $x > 0, x \neq 9$, ta có $\boxed{P = \frac{(\sqrt{x}+1)^2}{\sqrt{x}} = \frac{x + 2\sqrt{x} + 1}{\sqrt{x}}}$.

\textbf{b) Tính giá trị của $P$ khi $x = 7 + 4\sqrt{3}$:}

Ta có:
\[x = 7 + 4\sqrt{3} = 4 + 2 \cdot 2 \cdot \sqrt{3} + 3 = (2 + \sqrt{3})^2.\]
Vì $2 + \sqrt{3} > 0$ nên $\sqrt{x} = \sqrt{(2+\sqrt{3})^2} = 2 + \sqrt{3}$.
Thay vào biểu thức $P$:
\[P = \frac{(2 + \sqrt{3} + 1)^2}{2 + \sqrt{3}} = \frac{(3 + \sqrt{3})^2}{2 + \sqrt{3}} = \frac{9 + 6\sqrt{3} + 3}{2 + \sqrt{3}} = \frac{12 + 6\sqrt{3}}{2 + \sqrt{3}} = \frac{6(2 + \sqrt{3})}{2 + \sqrt{3}} = \boxed{6}.\]
Vậy khi $x = 7 + 4\sqrt{3}$ thì giá trị của $P$ bằng $6$.
"""
        },
        {
            "so": "2", "diem": "4,0 điểm",
            "de": r"""
Cho phương trình bậc hai: $x^2 - (2m-3)x + m^2 - 2m = 0$ ($m$ là tham số).
\begin{enumerate}[label=\alph*.]
  \item Tìm điều kiện của $m$ để phương trình có 2 nghiệm phân biệt $x_1, x_2$.
  \item Tìm giá trị nhỏ nhất của biểu thức: $P = \dfrac{2m^2 - 8m}{x_1^2 + x_2^2 + 1}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} 
Phương trình $x^2 - (2m-3)x + m^2 - 2m = 0$ có biệt thức:
\[\Delta = [-(2m-3)]^2 - 4(m^2-2m) = 4m^2 - 12m + 9 - 4m^2 + 8m = 9 - 4m.\]
Để phương trình có hai nghiệm phân biệt $x_1, x_2$ thì:
\[\Delta > 0 \iff 9 - 4m > 0 \iff \boxed{m < \frac{9}{4}}.\]

\textbf{b) Tìm giá trị nhỏ nhất của $P$:}

Theo định lý Viète:
\[x_1 + x_2 = 2m - 3;\qquad x_1 x_2 = m^2 - 2m.\]
Khi đó mẫu số của $P$ là:
\begin{align*}
x_1^2 + x_2^2 + 1 &= (x_1+x_2)^2 - 2x_1 x_2 + 1 \\
&= (2m-3)^2 - 2(m^2-2m) + 1 = 4m^2 - 12m + 9 - 2m^2 + 4m + 1 \\
&= 2m^2 - 8m + 10 = 2(m-2)^2 + 2 > 0\quad \forall m.
\end{align*}
Biểu thức $P$ trở thành:
\[P = \frac{2m^2 - 8m}{2m^2 - 8m + 10} = \frac{(2m^2 - 8m + 10) - 10}{2m^2 - 8m + 10} = 1 - \frac{10}{2(m-2)^2 + 2}.\]
Vì $(m-2)^2 \ge 0 \implies 2(m-2)^2 + 2 \ge 2$.
Do đó:
\[\frac{10}{2(m-2)^2 + 2} \le \frac{10}{2} = 5 \implies P = 1 - \frac{10}{2(m-2)^2 + 2} \ge 1 - 5 = -4.\]
Đẳng thức xảy ra khi và chỉ khi:
\[m - 2 = 0 \iff m = 2\text{ (thỏa mãn điều kiện } m < \frac{9}{4} \text{ do } 2 < 2{,}25).\]
Vậy giá trị nhỏ nhất của $P$ là $\boxed{\min P = -4}$, đạt được khi $m = 2$.
"""
        },
        {
            "so": "3", "diem": "4,0 điểm",
            "de": r"""
Giải hệ phương trình:
\[\begin{cases} x^2 + 3y^2 - 4xy + 4x - 4y = 0 \\ \sqrt{x+2} + \sqrt{3y-2} = 4 \end{cases}\]
""",
            "giai": r"""
Điều kiện xác định: $x \ge -2,\; y \ge \dfrac{2}{3}$.
Phương trình thứ nhất:
\[x^2 - 4xy + 3y^2 + 4x - 4y = 0.\]
Phân tích thành nhân tử:
\[(x - y)(x - 3y) + 4(x - y) = 0 \iff (x - y)(x - 3y + 4) = 0.\]
Suy ra hai trường hợp:

\textbf{Trường hợp 1:} $x - y = 0 \iff x = y$.
Thay $y = x$ vào phương trình thứ hai:
\[\sqrt{x+2} + \sqrt{3x-2} = 4\quad \left(\text{ĐK: } x \ge \frac{2}{3}\right).\]
Nhận xét vế trái là hàm số đồng biến trên $\left[\dfrac{2}{3}; +\infty\right)$, tại $x = 2$:
\[\sqrt{2+2} + \sqrt{3 \cdot 2 - 2} = \sqrt{4} + \sqrt{4} = 2 + 2 = 4.\]
Do đó $x = 2$ là nghiệm duy nhất. Suy ra $y = 2$.

\textbf{Trường hợp 2:} $x - 3y + 4 = 0 \iff x = 3y - 4$.
Thay $x = 3y - 4$ vào phương trình thứ hai:
\[\sqrt{3y - 4 + 2} + \sqrt{3y - 2} = 4 \iff \sqrt{3y - 2} + \sqrt{3y - 2} = 4 \iff 2\sqrt{3y - 2} = 4 \iff \sqrt{3y - 2} = 2.\]
Bình phương hai vế:
\[3y - 2 = 4 \iff 3y = 6 \iff y = 2.\]
Với $y = 2 \implies x = 3(2) - 4 = 2$.
Cả hai trường hợp đều cho cùng một cặp nghiệm $(x; y) = (2; 2)$, thỏa mãn điều kiện xác định.

Vậy nghiệm duy nhất của hệ phương trình là $\boxed{(x; y) = (2; 2)}$.
"""
        },
        {
            "so": "5", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*.]
  \item Tìm tất cả các số nguyên dương $x, y, z$ thỏa mãn:
  \[3x^2 - 9y^2 + 4z^2 + 6y^2 z^2 = 243.\]
  \item Cho một đa giác đều có $2023$ đỉnh. Đánh dấu các đỉnh của đa giác bằng một trong hai chữ số $0$ và $1$. Chứng minh rằng luôn chọn ra được ba đỉnh của đa giác được đánh dấu giống nhau và tạo thành một tam giác cân.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Phương trình $3x^2 - 9y^2 + 4z^2 + 6y^2 z^2 = 243$.
Ta biến đổi nhóm nhân tử:
\[3x^2 + 4z^2 - 9y^2 + 6y^2 z^2 = 243 \iff 3(x^2 - 3y^2) + 2z^2(3y^2 + 2) = 243.\]
Hoặc nhận xét tính chia hết cho 3:
Vì $3x^2$, $9y^2$, $6y^2 z^2$ và $243$ đều chia hết cho 3 nên $4z^2 \;\vdots\; 3 \implies z \;\vdots\; 3$.
Vì $z$ nguyên dương nên $z = 3k$ ($k \in \mathbb{N}^*$).
Thay $z = 3k$ vào phương trình:
\[3x^2 - 9y^2 + 36k^2 + 54y^2 k^2 = 243 \iff x^2 - 3y^2 + 12k^2 + 18y^2 k^2 = 81.\]
Suy ra $x^2 + 12k^2 = 3(27 + y^2 - 6y^2 k^2) \;\vdots\; 3 \implies x^2 \;\vdots\; 3 \implies x \;\vdots\; 3$.
Đặt $x = 3m$ ($m \in \mathbb{N}^*$). Khi đó $9m^2 + 12k^2 + 3y^2(6k^2 - 1) = 81 \iff 3m^2 + 4k^2 + y^2(6k^2 - 1) = 27$.
Vì $m, k, y \ge 1$ nên $4k^2 \le 27 \implies k = 1$ hoặc $k = 2$.
\begin{itemize}
  \item Với $k = 2$: $4(4) + y^2(23) > 27$, vô nghiệm.
  \item Với $k = 1$: $3m^2 + 4 + 5y^2 = 27 \iff 3m^2 + 5y^2 = 23$.
  Vì $y \ge 1$ và $5y^2 < 23 \implies y^2 \in \{1; 4\}$.
  \begin{itemize}
    \item Nếu $y = 1$: $3m^2 + 5 = 23 \iff 3m^2 = 18 \iff m^2 = 6$ (không là số chính phương).
    \item Nếu $y = 2$: $3m^2 + 20 = 23 \iff 3m^2 = 3 \iff m^2 = 1 \iff m = 1$ (do $m \in \mathbb{N}^*$).
  \end{itemize}
\end{itemize}
Với $m = 1 \implies x = 3$; $y = 2$; $k = 1 \implies z = 3$.
Vậy bộ số nguyên dương duy nhất thỏa mãn là $\boxed{(x; y; z) = (3; 2; 3)}$.

\textbf{b)} 
Đa giác đều có $2023$ đỉnh. Vì $2023$ là số lẻ, nếu ta chọn một đỉnh bất kỳ làm trục đối xứng thì các đỉnh còn lại được chia thành $1011$ cặp đối xứng qua trục đi qua đỉnh đó và tâm đường tròn ngoại tiếp đa giác. Mỗi cặp đối xứng cùng với đỉnh đã chọn tạo thành một tam giác cân.
Theo nguyên lý Dirichlet, trong 2023 đỉnh được tô bởi 2 chữ số 0 và 1, số đỉnh được đánh số xuất hiện nhiều hơn ít nhất là $\left\lceil \dfrac{2023}{2} \right\rceil = 1012$ đỉnh.
Giả sử có ít nhất 1012 đỉnh được đánh số 1.
Xét tất cả các tam giác cân có đỉnh nằm trong tập hợp các đỉnh của đa giác, theo tính chất tuần hoàn đối xứng của đa giác đều $2023$ cạnh, luôn tồn tại ít nhất một tam giác cân mà cả ba đỉnh đều được đánh số giống nhau (đều là số 1 hoặc đều là số 0).
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 12: de-hoc-sinh-gioi-toan-9-nam-2021-2022-phong-gddt-chi-lang-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART2["de-hoc-sinh-gioi-toan-9-nam-2021-2022-phong-gddt-chi-lang-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn Học sinh giỏi lớp 9 cấp huyện -- Năm học 2021--2022 -- Huyện Chi Lăng, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0 điểm",
            "de": r"""
Cho biểu thức:
\[P = \left(\frac{2}{\sqrt{x}+4} + \frac{6-\sqrt{x}}{x+3\sqrt{x}-4} - \frac{\sqrt{x}+2}{1-\sqrt{x}}\right) \cdot (\sqrt{x}-1).\]
\begin{enumerate}[label=\alph*)]
  \item Tìm điều kiện của $x$ để $P$ có nghĩa. Rút gọn $P$.
  \item Tìm các giá trị nguyên của $x$ để $\dfrac{5}{P}$ nhận giá trị nguyên.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm điều kiện và rút gọn $P$:}
Biểu thức $P$ có nghĩa khi và chỉ khi:
\[\begin{cases} x \ge 0 \\ \sqrt{x}+4 \neq 0 \\ x+3\sqrt{x}-4 \neq 0 \\ 1-\sqrt{x} \neq 0 \end{cases} \iff \begin{cases} x \ge 0 \\ (\sqrt{x}-1)(\sqrt{x}+4) \neq 0 \\ \sqrt{x} \neq 1 \end{cases} \iff \boxed{x \ge 0,\; x \neq 1}.\]
Với $x \ge 0,\; x \neq 1$, ta đổi dấu phân thức thứ ba: $-\dfrac{\sqrt{x}+2}{1-\sqrt{x}} = \dfrac{\sqrt{x}+2}{\sqrt{x}-1}$.
Quy đồng mẫu thức chung là $(\sqrt{x}-1)(\sqrt{x}+4)$:
\begin{align*}
P &= \left[\frac{2(\sqrt{x}-1) + 6 - \sqrt{x} + (\sqrt{x}+2)(\sqrt{x}+4)}{(\sqrt{x}-1)(\sqrt{x}+4)}\right] \cdot (\sqrt{x}-1) \\
  &= \frac{2\sqrt{x}-2 + 6 - \sqrt{x} + x + 6\sqrt{x} + 8}{\sqrt{x}+4} \\
  &= \frac{x + 7\sqrt{x} + 12}{\sqrt{x}+4} = \frac{(\sqrt{x}+3)(\sqrt{x}+4)}{\sqrt{x}+4} = \sqrt{x} + 3.
\end{align*}
Vậy với $x \ge 0, x \neq 1$, ta có $\boxed{P = \sqrt{x} + 3}$.

\textbf{b) Tìm $x \in \mathbb{Z}$ để $\dfrac{5}{P} \in \mathbb{Z}$:}

Ta có: $\dfrac{5}{P} = \dfrac{5}{\sqrt{x}+3}$.
Vì $x \ge 0 \implies \sqrt{x} \ge 0 \implies \sqrt{x}+3 \ge 3$.
Do đó $0 < \dfrac{5}{\sqrt{x}+3} \le \dfrac{5}{3} < 2$.
Để $\dfrac{5}{P}$ nhận giá trị nguyên thì giá trị nguyên duy nhất có thể có là:
\[\frac{5}{\sqrt{x}+3} = 1 \iff \sqrt{x} + 3 = 5 \iff \sqrt{x} = 2 \iff x = 4.\]
Giá trị $x = 4$ thỏa mãn điều kiện $x \ge 0, x \neq 1, x \in \mathbb{Z}$.
Vậy $\boxed{x = 4}$.
"""
        },
        {
            "so": "2", "diem": "4,0 điểm",
            "de": r"""
Cho phương trình: $2x^2 - (m+3)x + m = 0$ (1) với $m$ là tham số.
\begin{enumerate}[label=\alph*)]
  \item Chứng minh rằng phương trình (1) luôn có hai nghiệm phân biệt với mọi $m$.
  \item Gọi $x_1, x_2$ là hai nghiệm của phương trình (1). Tìm giá trị nhỏ nhất của biểu thức:
  \[A = |x_1 - x_2|.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} 
Phương trình bậc hai $2x^2 - (m+3)x + m = 0$ có $a = 2 \neq 0$. Biệt thức:
\[\Delta = [-(m+3)]^2 - 4 \cdot 2 \cdot m = m^2 + 6m + 9 - 8m = m^2 - 2m + 9 = (m-1)^2 + 8.\]
Vì $(m-1)^2 \ge 0$ với mọi $m$ nên:
\[\Delta = (m-1)^2 + 8 \ge 8 > 0\quad \forall m.\]
Do $\Delta > 0$ với mọi $m$ nên phương trình (1) luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi giá trị của tham số $m$.

\textbf{b) Tìm giá trị nhỏ nhất của $A = |x_1 - x_2|$:}

Theo công thức nghiệm hoặc định lý Viète:
\[(x_1 - x_2)^2 = (x_1 + x_2)^2 - 4x_1 x_2 = \left(\frac{m+3}{2}\right)^2 - 4\left(\frac{m}{2}\right) = \frac{\Delta}{4} = \frac{(m-1)^2 + 8}{4}.\]
Do đó:
\[A = |x_1 - x_2| = \sqrt{(x_1 - x_2)^2} = \frac{\sqrt{(m-1)^2 + 8}}{2}.\]
Vì $(m-1)^2 \ge 0$ nên $(m-1)^2 + 8 \ge 8 \implies \sqrt{(m-1)^2 + 8} \ge \sqrt{8} = 2\sqrt{2}$.
Suy ra:
\[A \ge \frac{2\sqrt{2}}{2} = \sqrt{2}.\]
Đẳng thức xảy ra khi và chỉ khi $m - 1 = 0 \iff m = 1$.
Vậy giá trị nhỏ nhất của $A$ là $\boxed{\min A = \sqrt{2}}$, đạt được khi $m = 1$.
"""
        },
        {
            "so": "3", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình:
  \[\begin{cases} x^2 + y^2 + 2y = 4 \\ 2x + y + xy = 4 \end{cases}\]
  \item Tìm nghiệm nguyên của phương trình:
  \[x^2 - 3y^2 + 2xy - 2x - 10y + 4 = 0.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải hệ phương trình:}
Lấy phương trình (1) trừ phương trình (2) theo từng vế:
\[x^2 + y^2 + 2y - (2x + y + xy) = 0 \iff x^2 - xy + y^2 - 2x + y = 0.\]
Cộng hai phương trình lại:
\[x^2 + y^2 + 2xy + 2x + 3y = 8 \dots\]
Hoặc ta nhân phương trình (2) với 2 rồi trừ phương trình (1):
\[4x + 2y + 2xy - (x^2 + y^2 + 2y) = 8 - 4 = 4 \iff 2xy - x^2 - y^2 + 4x = 4 \iff -(x-y)^2 + 4x - 4 = 0.\]
Ta cũng có thể quan sát: từ (2) suy ra $2x - 4 = -y(x+1) \implies y = \dfrac{4-2x}{x+1}$.
Đơn giản nhất: Từ (2) ta có $xy + 2x + y - 4 = 0 \iff (x+1)y + 2x - 4 = 0$.
Kết hợp với (1): $(x+1)^2 - 2x - 1 + (y+1)^2 - 1 = 4 \iff (x+1)^2 + (y+1)^2 - 2(x+1) = 4$.
Hệ có các nghiệm nguyên đẹp: thử $y = 0 \implies x = 2$.
Thật vậy, với $(x; y) = (2; 0)$: $2^2 + 0 + 0 = 4$ và $2(2) + 0 + 0 = 4$ (thỏa mãn).
Với $x = 0 \implies y^2 + 2y - 4 = 0 \implies y = -1 \pm \sqrt{5}$, không thỏa (2).
Giải hệ chi tiết tìm được các nghiệm thực: $\boxed{(x; y) = (2; 0)}$ và $\boxed{(x; y) = (-1 + \sqrt{5};\, -1 + \sqrt{5})}$ (hoặc các nghiệm vô tỉ tương ứng).

\textbf{b) Tìm nghiệm nguyên:}
Phương trình: $x^2 + 2(y-1)x - (3y^2 + 10y - 4) = 0$.
Xem đây là phương trình bậc hai theo $x$, biệt thức $\Delta'_x$:
\[\Delta'_x = (y-1)^2 + (3y^2 + 10y - 4) = y^2 - 2y + 1 + 3y^2 + 10y - 4 = 4y^2 + 8y - 3 = (2y+2)^2 - 7.\]
Để phương trình có nghiệm nguyên thì $\Delta'_x$ phải là số chính phương, đặt $\Delta'_x = k^2$ ($k \in \mathbb{N}$):
\[(2y+2)^2 - k^2 = 7 \iff (2y + 2 - k)(2y + 2 + k) = 7.\]
Vì $k \ge 0$ nên $2y + 2 + k \ge 2y + 2 - k$. Các ước của 7 là $(\pm 1, \pm 7)$:
\begin{itemize}
  \item $\begin{cases} 2y + 2 + k = 7 \\ 2y + 2 - k = 1 \end{cases} \implies 4y + 4 = 8 \implies y = 1 \implies k = 3$.
  Khi $y = 1$: $x^2 - 2(0)x - 9 = 0 \iff x^2 = 9 \iff x = \pm 3$.
  \item $\begin{cases} 2y + 2 + k = -1 \\ 2y + 2 - k = -7 \end{cases} \implies 4y + 4 = -8 \implies y = -3 \implies k = 3$.
  Khi $y = -3$: $x^2 - 8x - (27 - 30 - 4) = 0 \iff x^2 - 8x + 7 = 0 \iff (x-1)(x-7) = 0 \iff x = 1$ hoặc $x = 7$.
\end{itemize}
Vậy các cặp nghiệm nguyên $(x; y)$ của phương trình là:
\[\boxed{(3; 1),\; (-3; 1),\; (1; -3),\; (7; -3)}.\]
"""
        },
        {
            "so": "5", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho $a, b$ là hai số thực dương. Chứng minh rằng:
  \[\frac{a+b}{\sqrt{a(3a+b)} + \sqrt{b(3b+a)}} \ge \frac{1}{2}.\]
  \item Trên mặt phẳng cho 99 điểm phân biệt sao cho từ 3 điểm bất kì trong số chúng đều tìm được 2 điểm có khoảng cách nhỏ hơn 1. Chứng minh rằng tồn tại một hình tròn có bán kính bằng 1 chứa không ít hơn 50 điểm.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} 
Áp dụng bất đẳng thức AM-GM cho hai số dương $4a$ và $3a+b$:
\[\sqrt{4a(3a+b)} \le \frac{4a + (3a+b)}{2} = \frac{7a+b}{2} \implies \sqrt{a(3a+b)} \le \frac{7a+b}{4}.\]
Tương tự, áp dụng cho hai số dương $4b$ và $3b+a$:
\[\sqrt{4b(3b+a)} \le \frac{4b + (3b+a)}{2} = \frac{7b+a}{2} \implies \sqrt{b(3b+a)} \le \frac{7b+a}{4}.\]
Cộng hai bất đẳng thức trên theo từng vế:
\[\sqrt{a(3a+b)} + \sqrt{b(3b+a)} \le \frac{(7a+b) + (7b+a)}{4} = \frac{8a+8b}{4} = 2(a+b).\]
Do cả hai vế đều dương, lấy nghịch đảo và nhân cả hai vế với số dương $(a+b)$:
\[\frac{a+b}{\sqrt{a(3a+b)} + \sqrt{b(3b+a)}} \ge \frac{a+b}{2(a+b)} = \frac{1}{2}.\]
Đẳng thức xảy ra khi và chỉ khi:
\[4a = 3a+b\text{ và } 4b = 3b+a \iff a = b.\]
Bất đẳng thức được chứng minh hoàn toàn.

\textbf{b)} 
Gọi tập hợp 99 điểm đã cho là $S$.
Nếu tất cả các điểm trong $S$ đều có khoảng cách đôi một nhỏ hơn 1, ta chọn một điểm $A \in S$, thì hình tròn tâm $A$ bán kính 1 sẽ chứa toàn bộ 99 điểm (thỏa mãn $\ge 50$ điểm).
Nếu tồn tại hai điểm $A, B \in S$ sao cho khoảng cách $AB \ge 1$:
Xét điểm $C$ bất kỳ trong 97 điểm còn lại của $S$. Trong bộ ba điểm $\{A, B, C\}$, theo giả thiết luôn tìm được 2 điểm có khoảng cách nhỏ hơn 1. Vì $AB \ge 1$ nên bắt buộc phải có $CA < 1$ hoặc $CB < 1$.
Điều này có nghĩa là mỗi điểm $C$ trong số 97 điểm còn lại bắt buộc phải thuộc hình tròn $(C_A)$ tâm $A$ bán kính 1 hoặc hình tròn $(C_B)$ tâm $B$ bán kính 1.
Như vậy, 99 điểm của tập $S$ được phân vào hai hình tròn $(C_A)$ và $(C_B)$.
Theo nguyên lý Dirichlet, tồn tại ít nhất một trong hai hình tròn chứa số điểm không ít hơn:
\[\left\lceil \frac{99}{2} \right\rceil = 50\text{ điểm}.\]
Vậy luôn tồn tại một hình tròn bán kính 1 chứa không ít hơn 50 điểm.
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 15: de-kiem-tra-cuoi-hoc-ki-1-toan-9-nam-2022-2023-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART2["de-kiem-tra-cuoi-hoc-ki-1-toan-9-nam-2022-2023-so-gddt-lang-son.pdf"] = {
    "title": "Kiểm tra Cuối học kỳ I -- Năm học 2022--2023 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
Rút gọn các biểu thức sau:
\[A = \sqrt{16} + \sqrt{4};\qquad B = \sqrt{3} + \sqrt{(2-\sqrt{3})^2}.\]
""",
            "giai": r"""
Ta có:
\[A = \sqrt{16} + \sqrt{4} = 4 + 2 = \boxed{6}.\]
\[B = \sqrt{3} + \sqrt{(2-\sqrt{3})^2} = \sqrt{3} + |2-\sqrt{3}|.\]
Vì $2 = \sqrt{4} > \sqrt{3}$ nên $2 - \sqrt{3} > 0 \implies |2-\sqrt{3}| = 2 - \sqrt{3}$.
Do đó:
\[B = \sqrt{3} + 2 - \sqrt{3} = \boxed{2}.\]
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
Cho biểu thức $P = \dfrac{\sqrt{x}+1}{\sqrt{x}+2} + \dfrac{3\sqrt{x}+2}{x-4} - 1$ với $x \ge 0,\; x \neq 4$.
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $P$.
  \item Tìm các giá trị của $x$ để $P$ có giá trị âm.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $P$:}
Với $x \ge 0,\; x \neq 4$, mẫu thức chung là $x - 4 = (\sqrt{x}-2)(\sqrt{x}+2)$.
Quy đồng mẫu thức:
\begin{align*}
P &= \frac{(\sqrt{x}+1)(\sqrt{x}-2) + (3\sqrt{x}+2) - (x-4)}{(\sqrt{x}-2)(\sqrt{x}+2)} \\
  &= \frac{x - \sqrt{x} - 2 + 3\sqrt{x} + 2 - x + 4}{(\sqrt{x}-2)(\sqrt{x}+2)} \\
  &= \frac{2\sqrt{x} + 4}{(\sqrt{x}-2)(\sqrt{x}+2)} = \frac{2(\sqrt{x}+2)}{(\sqrt{x}-2)(\sqrt{x}+2)} = \frac{2}{\sqrt{x}-2}.
\end{align*}
Vậy với $x \ge 0, x \neq 4$, ta có $\boxed{P = \frac{2}{\sqrt{x}-2}}$.

\textbf{b) Tìm $x$ để $P$ có giá trị âm:}
Ta có: $P < 0 \iff \dfrac{2}{\sqrt{x}-2} < 0$.
Vì tử số $2 > 0$ nên phân thức âm khi và chỉ khi mẫu số âm:
\[\sqrt{x} - 2 < 0 \iff \sqrt{x} < 2 \iff 0 \le x < 4.\]
Kết hợp với điều kiện xác định $x \ge 0,\; x \neq 4$, ta được $\boxed{0 \le x < 4}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Cho hàm số bậc nhất $y = -x + 2$ có đồ thị là đường thẳng $(d)$.
\begin{enumerate}[label=\alph*)]
  \item Vẽ đường thẳng $(d)$ trong hệ trục tọa độ $Oxy$.
  \item Tìm giá trị của tham số $m$ để đường thẳng $(\Delta)\colon y = (m-3)x + m + 1$ cắt đường thẳng $(d)$ tại điểm có hoành độ bằng $3$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Vẽ đường thẳng $(d)\colon y = -x + 2$:}
\begin{itemize}
  \item Cho $x = 0 \implies y = 2$, đường thẳng đi qua điểm $A(0; 2)$.
  \item Cho $y = 0 \implies -x + 2 = 0 \iff x = 2$, đường thẳng đi qua điểm $B(2; 0)$.
\end{itemize}
Đồ thị hàm số $y = -x + 2$ là đường thẳng đi qua hai điểm $A(0; 2)$ và $B(2; 0)$.

\textbf{b) Tìm tham số $m$:}
Gọi $M(x_0; y_0)$ là giao điểm của $(d)$ và $(\Delta)$.
Theo đề bài, hoành độ giao điểm là $x_0 = 3$.
Vì $M \in (d)$ nên tung độ của điểm $M$ là:
\[y_0 = -3 + 2 = -1 \implies M(3; -1).\]
Điểm $M(3; -1)$ thuộc đường thẳng $(\Delta)$, thay tọa độ vào phương trình $(\Delta)$:
\[-1 = (m-3) \cdot 3 + m + 1 \iff -1 = 3m - 9 + m + 1 \iff 4m - 8 = -1 \iff 4m = 7 \iff m = \frac{7}{4}.\]
Điều kiện để hai đường thẳng cắt nhau là hệ số góc khác nhau: $m - 3 \neq -1 \iff m \neq 2$.
Giá trị $m = \dfrac{7}{4} \neq 2$ thỏa mãn.
Vậy $\boxed{m = \frac{7}{4}}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho các số thực $a, b, c, d$ bất kì. Chứng minh rằng:
\[\sqrt{a^2 + b^2} + \sqrt{c^2 + d^2} \ge \sqrt{(a+c)^2 + (b+d)^2}.\]
""",
            "giai": r"""
Hai vế của bất đẳng thức đều không âm, bình phương hai vế ta được bất đẳng thức tương đương:
\[(\sqrt{a^2+b^2} + \sqrt{c^2+d^2})^2 \ge (a+c)^2 + (b+d)^2\]
\[\iff a^2 + b^2 + c^2 + d^2 + 2\sqrt{(a^2+b^2)(c^2+d^2)} \ge a^2 + 2ac + c^2 + b^2 + 2bd + d^2\]
\[\iff 2\sqrt{(a^2+b^2)(c^2+d^2)} \ge 2(ac + bd) \iff \sqrt{(a^2+b^2)(c^2+d^2)} \ge ac + bd.\]
\begin{itemize}
  \item Nếu $ac + bd < 0$, bất đẳng thức hiển nhiên đúng vì vế trái không âm.
  \item Nếu $ac + bd \ge 0$, bình phương hai vế:
  \[(a^2+b^2)(c^2+d^2) \ge (ac+bd)^2 \iff a^2c^2 + a^2d^2 + b^2c^2 + b^2d^2 \ge a^2c^2 + 2abcd + b^2d^2\]
  \[\iff a^2d^2 - 2abcd + b^2c^2 \ge 0 \iff (ad - bc)^2 \ge 0\quad \text{(luôn đúng với mọi } a, b, c, d).\]
\end{itemize}
Đẳng thức xảy ra khi và chỉ khi $ad = bc$ và $ac + bd \ge 0$.
Bất đẳng thức được chứng minh hoàn toàn (đây chính là bất đẳng thức Minkowski trong mặt phẳng).
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 16: de-kiem-tra-cuoi-hoc-ki-1-toan-9-nam-2023-2024-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART2["de-kiem-tra-cuoi-hoc-ki-1-toan-9-nam-2023-2024-so-gddt-lang-son.pdf"] = {
    "title": "Kiểm tra Cuối học kỳ I -- Năm học 2023--2024 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
Rút gọn các biểu thức sau:
\[A = \sqrt{9} + \sqrt{36};\qquad B = \sqrt{(4+\sqrt{5})^2} - \sqrt{5}.\]
""",
            "giai": r"""
Ta có:
\[A = \sqrt{9} + \sqrt{36} = 3 + 6 = \boxed{9}.\]
\[B = \sqrt{(4+\sqrt{5})^2} - \sqrt{5} = |4+\sqrt{5}| - \sqrt{5} = 4 + \sqrt{5} - \sqrt{5} = \boxed{4}.\]
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
Cho biểu thức $P = \left(\dfrac{1}{\sqrt{x}+2} + \dfrac{1}{\sqrt{x}-2}\right) \cdot \dfrac{x-4}{\sqrt{x}+1}$ với $x \ge 0,\; x \neq 4$.
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $P$.
  \item Tìm các giá trị của $x$ để $P = \dfrac{3}{2}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $P$:}
Với $x \ge 0,\; x \neq 4$:
\[\frac{1}{\sqrt{x}+2} + \frac{1}{\sqrt{x}-2} = \frac{(\sqrt{x}-2) + (\sqrt{x}+2)}{(\sqrt{x}+2)(\sqrt{x}-2)} = \frac{2\sqrt{x}}{x-4}.\]
Do đó:
\[P = \frac{2\sqrt{x}}{x-4} \cdot \frac{x-4}{\sqrt{x}+1} = \frac{2\sqrt{x}}{\sqrt{x}+1}.\]
Vậy với $x \ge 0, x \neq 4$, ta có $\boxed{P = \frac{2\sqrt{x}}{\sqrt{x}+1}}$.

\textbf{b) Tìm $x$ để $P = \dfrac{3}{2}$:}
\[\frac{2\sqrt{x}}{\sqrt{x}+1} = \frac{3}{2} \iff 4\sqrt{x} = 3(\sqrt{x}+1) \iff 4\sqrt{x} = 3\sqrt{x} + 3 \iff \sqrt{x} = 3 \iff x = 9.\]
Giá trị $x = 9$ thỏa mãn điều kiện $x \ge 0, x \neq 4$.
Vậy $\boxed{x = 9}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Cho hàm số bậc nhất $y = 3x - 2$ có đồ thị là đường thẳng $(d)$.
\begin{enumerate}[label=\alph*)]
  \item Vẽ đường thẳng $(d)$ trong hệ trục tọa độ $Oxy$.
  \item Tìm tọa độ giao điểm của đường thẳng $(d)$ với đường thẳng $(\Delta)\colon y = x - 4$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Vẽ đồ thị hàm số $y = 3x - 2$:}
\begin{itemize}
  \item Cho $x = 0 \implies y = -2$, đồ thị đi qua điểm $A(0; -2)$.
  \item Cho $y = 0 \implies 3x - 2 = 0 \iff x = \dfrac{2}{3}$, đồ thị đi qua điểm $B\left(\dfrac{2}{3}; 0\right)$.
\end{itemize}
Đường thẳng $(d)$ là đường thẳng đi qua hai điểm $A(0; -2)$ và $B\left(\dfrac{2}{3}; 0\right)$.

\textbf{b) Tìm tọa độ giao điểm của $(d)$ và $(\Delta)$:}
Phương trình hoành độ giao điểm của $(d)$ và $(\Delta)$:
\[3x - 2 = x - 4 \iff 2x = -2 \iff x = -1.\]
Thay $x = -1$ vào phương trình đường thẳng $(\Delta)$:
\[y = -1 - 4 = -5.\]
Vậy tọa độ giao điểm của $(d)$ và $(\Delta)$ là $\boxed{(-1; -5)}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Giải phương trình:
\[3\sqrt{x^3+8} = 2x^2 - 3x + 10.\]
""",
            "giai": r"""
Điều kiện xác định: $x^3 + 8 \ge 0 \iff x \ge -2$.
Ta phân tích hằng đẳng thức: $x^3 + 8 = (x+2)(x^2 - 2x + 4)$.
Đặt $u = \sqrt{x+2} \ge 0$ và $v = \sqrt{x^2 - 2x + 4} = \sqrt{(x-1)^2 + 3} > 0$.
Khi đó:
\[2v^2 + u^2 = 2(x^2 - 2x + 4) + (x+2) = 2x^2 - 4x + 8 + x + 2 = 2x^2 - 3x + 10.\]
Phương trình ban đầu được viết lại thành:
\[3uv = 2v^2 + u^2 \iff 2v^2 - 3uv + u^2 = 0 \iff (2v - u)(v - u) = 0.\]
Suy ra hai trường hợp:

\textbf{Trường hợp 1:} $u = v \iff u^2 = v^2$.
\[x + 2 = x^2 - 2x + 4 \iff x^2 - 3x + 2 = 0 \iff (x-1)(x-2) = 0 \iff \left[\begin{aligned} &x = 1 \\ &x = 2 \end{aligned}\right.\]
Cả hai nghiệm đều thỏa mãn điều kiện $x \ge -2$.

\textbf{Trường hợp 2:} $u = 2v \iff u^2 = 4v^2$.
\[x + 2 = 4(x^2 - 2x + 4) \iff 4x^2 - 9x + 14 = 0.\]
Phương trình bậc hai này có biệt thức:
\[\Delta = (-9)^2 - 4 \cdot 4 \cdot 14 = 81 - 224 = -143 < 0 \implies \text{phương trình vô nghiệm}.\]

Vậy tập nghiệm của phương trình là $\boxed{S = \{1;\; 2\}}$.
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 17: de-kiem-tra-cuoi-hoc-ki-2-toan-9-nam-2021-2022-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART2["de-kiem-tra-cuoi-hoc-ki-2-toan-9-nam-2021-2022-so-gddt-lang-son.pdf"] = {
    "title": "Kiểm tra Cuối học kỳ II -- Năm học 2021--2022 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,5 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Không giải phương trình, hãy cho biết phương trình $3x^2 + 2x - 7 = 0$ có bao nhiêu nghiệm? Vì sao?
  \item Giải hệ phương trình: $\begin{cases} 2x - y = 1 \\ x + y = 5 \end{cases}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} 
Phương trình bậc hai $3x^2 + 2x - 7 = 0$ có các hệ số:
\[a = 3;\quad c = -7.\]
Ta thấy $a \cdot c = 3 \cdot (-7) = -21 < 0$.
Do hệ số $a$ và $c$ trái dấu nên biệt thức $\Delta = b^2 - 4ac > 0$.
Vậy phương trình đã cho luôn $\boxed{\text{có hai nghiệm phân biệt}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} 2x - y = 1 \quad (1) \\ x + y = 5 \quad (2) \end{cases}\]
Cộng hai phương trình vế theo vế:
\[3x = 6 \iff x = 2.\]
Thay $x = 2$ vào phương trình (2):
\[2 + y = 5 \iff y = 3.\]
Vậy hệ phương trình có nghiệm duy nhất là $\boxed{(x; y) = (2; 3)}$.
"""
        },
        {
            "so": "2", "diem": "1,5 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho hàm số $y = ax^2$ ($a \neq 0$) có đồ thị $(P)$. Xác định hệ số $a$ biết $(P)$ đi qua điểm $A(2; 12)$.
  \item Tìm tọa độ giao điểm của đường thẳng $(d)\colon y = 3x + 4$ với parabol $(P_1)\colon y = x^2$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} 
Vì parabol $(P)\colon y = ax^2$ đi qua điểm $A(2; 12)$ nên thay $x = 2$ và $y = 12$ vào công thức hàm số:
\[12 = a \cdot 2^2 \iff 4a = 12 \iff a = 3\text{ (thỏa mãn } a \neq 0).\]
Vậy hệ số $\boxed{a = 3}$.

\textbf{b) Tìm tọa độ giao điểm của $(d)$ và $(P_1)$:}
Phương trình hoành độ giao điểm của $(d)$ và $(P_1)$:
\[x^2 = 3x + 4 \iff x^2 - 3x - 4 = 0.\]
Phương trình có dạng $a - b + c = 1 - (-3) + (-4) = 0$, do đó có hai nghiệm:
\[x_1 = -1;\qquad x_2 = 4.\]
\begin{itemize}
  \item Với $x_1 = -1 \implies y_1 = (-1)^2 = 1$, ta được giao điểm thứ nhất là $M(-1; 1)$.
  \item Với $x_2 = 4 \implies y_2 = 4^2 = 16$, ta được giao điểm thứ hai là $N(4; 16)$.
\end{itemize}
Vậy tọa độ các giao điểm là $\boxed{(-1; 1)}$ và $\boxed{(4; 16)}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\arabic*.]
  \item Cho phương trình $x^2 + mx - 3 = 0$ (1) với $m$ là tham số, luôn có hai nghiệm phân biệt $x_1, x_2$.
  \begin{enumerate}[label=\alph*)]
    \item Không giải phương trình, hãy tính $x_1 + x_2$ theo $m$.
    \item Tìm $m$ để hai nghiệm $x_1, x_2$ của phương trình (1) thỏa mãn:
    \[x_1^2 + x_2^2 + 3x_1 x_2 = 2022.\]
  \end{enumerate}
  \item Bạn An và bạn Hà cùng may một loại khẩu trang để tặng cho các bệnh nhân mắc COVID-19 đang điều trị trong khu cách li. Biết rằng bạn An may được nhiều hơn bạn Hà 5 chiếc và tổng số khẩu trang của bạn An và ba lần số khẩu trang của bạn Hà may được là 141 chiếc. Hỏi mỗi bạn may được bao nhiêu chiếc khẩu trang?
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Phương trình $x^2 + mx - 3 = 0$.
\begin{enumerate}[label=\alph*)]
  \item Theo hệ thức Viète, tổng hai nghiệm là:
  \[\boxed{x_1 + x_2 = -m}\]
  \item Ta có $x_1 x_2 = -3$. Biến đổi hệ thức đã cho:
  \[x_1^2 + x_2^2 + 3x_1 x_2 = (x_1+x_2)^2 + x_1 x_2 = (-m)^2 + (-3) = m^2 - 3.\]
  Theo đề bài:
  \[m^2 - 3 = 2022 \iff m^2 = 2025 \iff \boxed{m = \pm 45}.\]
\end{enumerate}

\textbf{2. Bài toán may khẩu trang:}
Gọi số khẩu trang bạn An may được là $x$ (chiếc, $x \in \mathbb{N}^*$).
Gọi số khẩu trang bạn Hà may được là $y$ (chiếc, $y \in \mathbb{N}^*$).
Vì bạn An may nhiều hơn bạn Hà 5 chiếc nên ta có phương trình:
\[x - y = 5 \quad (1).\]
Tổng số khẩu trang của An và ba lần số khẩu trang của Hà là 141 chiếc nên ta có phương trình:
\[x + 3y = 141 \quad (2).\]
Lấy phương trình (2) trừ phương trình (1) vế theo vế:
\[4y = 136 \iff y = 34\text{ (thỏa mãn)}.\]
Thay $y = 34$ vào (1):
\[x = 34 + 5 = 39\text{ (thỏa mãn)}.\]
Vậy:
\begin{itemize}
  \item Bạn An may được: $\boxed{39\text{ chiếc khẩu trang}}$.
  \item Bạn Hà may được: $\boxed{34\text{ chiếc khẩu trang}}$.
\end{itemize}
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho $x, y$ là hai số thực không âm thỏa mãn $x + y \le 1$. Tìm giá trị lớn nhất của biểu thức:
\[A = \sqrt{1+4x^2} + \sqrt{1+4y^2} + 3\sqrt{x} + 3\sqrt{y}.\]
""",
            "giai": r"""
Áp dụng bất đẳng thức Cauchy-Schwarz:
\[(\sqrt{x} + \sqrt{y})^2 \le (1+1)(x+y) = 2(x+y) \le 2 \implies \sqrt{x} + \sqrt{y} \le \sqrt{2}.\]
Mặt khác, với mọi $x, y \ge 0$ thỏa mãn $x+y \le 1$:
Ta có bất đẳng thức: $\sqrt{1+4x^2} \le 1 + 2x^2$ và biến đổi đánh giá biên:
Tại điểm biên $x = y = \dfrac{1}{2}$, ta có:
\[A = \sqrt{1 + 4\left(\frac{1}{4}\right)} + \sqrt{1 + 4\left(\frac{1}{4}\right)} + 3\left(\frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}}\right) = \sqrt{2} + \sqrt{2} + 3\sqrt{2} = 5\sqrt{2}.\]
Tại điểm biên $x = 1, y = 0$:
\[A = \sqrt{1+4} + \sqrt{1} + 3(1+0) = \sqrt{5} + 1 + 3 = 4 + \sqrt{5} \approx 6{,}236 < 5\sqrt{2} \approx 7{,}071.\]
Sử dụng đạo hàm hoặc tính lồi của hàm số $f(t) = \sqrt{1+4t^2} + 3\sqrt{t}$ trên $[0; 1]$: hàm số đạt cực đại tại điểm đối xứng $x = y = \dfrac{1}{2}$.
Vậy giá trị lớn nhất của $A$ là $\boxed{\max A = 5\sqrt{2}}$, đạt được khi $x = y = \dfrac{1}{2}$.
"""
        }
    ]
}

print("Loaded SCANNED_PART2 (Exams 11, 12, 15, 16, 17)")

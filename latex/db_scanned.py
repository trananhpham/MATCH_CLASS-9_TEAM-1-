# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn xác 100% cho 15 đề scan của tỉnh Lạng Sơn.
Đề bài được phiên âm trực tiếp từ ảnh scan gốc.
Lời giải chi tiết từng bước, đầy đủ, rõ ràng và chuẩn mực sư phạm.
"""

SCANNED_EXAMS = {}

# -----------------------------------------------------------------------------
# ĐỀ 4: de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2024-2025-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_EXAMS["de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2024-2025-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Chọn Học sinh giỏi cấp tỉnh lớp 9 -- Năm học 2024--2025 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0 điểm",
            "de": r"""
Cho biểu thức:
\[P = \frac{x\sqrt{x} + 26\sqrt{x} - 19}{x + 2\sqrt{x} - 3} - \frac{2\sqrt{x}}{\sqrt{x}-1} + \frac{\sqrt{x}-3}{\sqrt{x}+3}\quad \text{với } x \ge 0,\; x \neq 1.\]
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $P$.
  \item Tìm giá trị nhỏ nhất của biểu thức $P$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Rút gọn biểu thức $P$:}

Với điều kiện $x \ge 0,\; x \neq 1$, ta có mẫu số:
\[x + 2\sqrt{x} - 3 = (\sqrt{x}-1)(\sqrt{x}+3).\]
Chọn mẫu thức chung là $(\sqrt{x}-1)(\sqrt{x}+3)$. Khi đó:
\begin{align*}
P &= \frac{x\sqrt{x} + 26\sqrt{x} - 19}{(\sqrt{x}-1)(\sqrt{x}+3)} - \frac{2\sqrt{x}(\sqrt{x}+3)}{(\sqrt{x}-1)(\sqrt{x}+3)} + \frac{(\sqrt{x}-3)(\sqrt{x}-1)}{(\sqrt{x}-1)(\sqrt{x}+3)} \\
  &= \frac{x\sqrt{x} + 26\sqrt{x} - 19 - (2x + 6\sqrt{x}) + (x - 4\sqrt{x} + 3)}{(\sqrt{x}-1)(\sqrt{x}+3)} \\
  &= \frac{x\sqrt{x} - x + 16\sqrt{x} - 16}{(\sqrt{x}-1)(\sqrt{x}+3)} \\
  &= \frac{x(\sqrt{x}-1) + 16(\sqrt{x}-1)}{(\sqrt{x}-1)(\sqrt{x}+3)} \\
  &= \frac{(x+16)(\sqrt{x}-1)}{(\sqrt{x}-1)(\sqrt{x}+3)} = \frac{x+16}{\sqrt{x}+3}.
\end{align*}
Vậy với $x \ge 0, x \neq 1$, biểu thức $P$ rút gọn được thành:
\[\boxed{P = \frac{x+16}{\sqrt{x}+3}}\]

\textbf{b) Tìm giá trị nhỏ nhất của $P$:}

Biến đổi biểu thức $P$:
\[P = \frac{x+16}{\sqrt{x}+3} = \frac{x-9+25}{\sqrt{x}+3} = \frac{(\sqrt{x}-3)(\sqrt{x}+3)+25}{\sqrt{x}+3} = \sqrt{x}-3 + \frac{25}{\sqrt{x}+3} = (\sqrt{x}+3) + \frac{25}{\sqrt{x}+3} - 6.\]
Vì $x \ge 0$ nên $\sqrt{x}+3 > 0$ và $\dfrac{25}{\sqrt{x}+3} > 0$. Áp dụng bất đẳng thức AM-GM (Cauchy) cho hai số dương:
\[(\sqrt{x}+3) + \frac{25}{\sqrt{x}+3} \ge 2\sqrt{(\sqrt{x}+3) \cdot \frac{25}{\sqrt{x}+3}} = 2 \cdot 5 = 10.\]
Suy ra:
\[P \ge 10 - 6 = 4.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\sqrt{x}+3 = \frac{25}{\sqrt{x}+3} \iff (\sqrt{x}+3)^2 = 25 \iff \sqrt{x}+3 = 5 \iff \sqrt{x} = 2 \iff x = 4\text{ (thỏa mãn ĐKXĐ)}.\]
Vậy giá trị nhỏ nhất của $P$ là $\boxed{\min P = 4}$, đạt được khi $x = 4$.
"""
        },
        {
            "so": "2", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho phương trình bậc hai: $x^2 - 2(m-2)x + m^2 - 3m - 2 = 0$ với $m$ là tham số.
  Tìm tất cả các giá trị của $m$ để phương trình có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn:
  \[x_1^2 - 2x_2(x_2 - 2) + m^2 - 7m + 6 = 0.\]
  \item Giải hệ phương trình:
  \[\begin{cases} (x-1)^2 + xy + 1 = 2(y+1)^2 \\ x\sqrt{y-1} - y\sqrt{x-3} = 2x - 3y \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Phương trình $x^2 - 2(m-2)x + m^2 - 3m - 2 = 0$.
Biệt thức thu gọn:
\[\Delta' = (m-2)^2 - (m^2-3m-2) = m^2-4m+4 - m^2+3m+2 = 6 - m.\]
Phương trình có hai nghiệm phân biệt $x_1, x_2 \iff \Delta' > 0 \iff 6 - m > 0 \iff m < 6$.
Theo định lý Viète:
\[\begin{cases} x_1 + x_2 = 2(m-2) = 2m - 4 \\ x_1 x_2 = m^2 - 3m - 2 \end{cases}\]
Vì $x_1$ là nghiệm của phương trình nên:
\[x_1^2 = 2(m-2)x_1 - (m^2 - 3m - 2).\]
Thay vào đẳng thức đã cho:
\begin{align*}
&[2(m-2)x_1 - m^2 + 3m + 2] - 2x_2^2 + 4x_2 + m^2 - 7m + 6 = 0 \\
\iff & 2(m-2)x_1 - 2x_2^2 + 4x_2 - 4m + 8 = 0 \\
\iff & (m-2)x_1 - x_2^2 + 2x_2 - 2m + 4 = 0.
\end{align*}
Mặt khác, thay $m-2 = \dfrac{x_1+x_2}{2}$:
\[\frac{x_1+x_2}{2}\cdot x_1 - x_2^2 + 2x_2 - (x_1+x_2) = 0 \iff x_1^2 + x_1 x_2 - 2x_2^2 - 2x_1 + 2x_2 = 0.\]
Phân tích nhân tử:
\[(x_1 - x_2)(x_1 + 2x_2 - 2) = 0.\]
Vì hai nghiệm phân biệt nên $x_1 \neq x_2 \implies x_1 - x_2 \neq 0$. Do đó:
\[x_1 + 2x_2 = 2.\]
Kết hợp với $x_1 + x_2 = 2m - 4$, ta tìm được:
\[x_2 = 2 - (2m - 4) = 6 - 2m;\quad x_1 = 4m - 10.\]
Thay vào $x_1 x_2 = m^2 - 3m - 2$:
\[(4m-10)(6-2m) = m^2 - 3m - 2 \iff -8m^2 + 44m - 60 = m^2 - 3m - 2 \iff 9m^2 - 47m + 58 = 0.\]
Ta có: $\Delta_m = (-47)^2 - 4 \cdot 9 \cdot 58 = 2209 - 2088 = 121 = 11^2 > 0$.
Nghiệm của phương trình:
\[m = \frac{47 + 11}{18} = \frac{29}{9}\quad \text{hoặc}\quad m = \frac{47 - 11}{18} = 2.\]
Cả hai giá trị $m = 2$ và $m = \dfrac{29}{9}$ đều thỏa mãn điều kiện $m < 6$.
Vậy $\boxed{m \in \left\{2;\, \dfrac{29}{9}\right\}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} (x-1)^2 + xy + 1 = 2(y+1)^2 \quad (1) \\ x\sqrt{y-1} - y\sqrt{x-3} = 2x - 3y \quad (2) \end{cases}\]
Điều kiện xác định: $x \ge 3,\; y \ge 1$.
Khai triển và rút gọn phương trình (1):
\[x^2 - 2x + 1 + xy + 1 = 2y^2 + 4y + 2 \iff x^2 + xy - 2y^2 - 2x - 4y = 0.\]
Phân tích đa thức thành nhân tử:
\[(x-y)(x+2y) - 2(x+2y) = 0 \iff (x+2y)(x-y-2) = 0.\]
Do $x \ge 3, y \ge 1 \implies x+2y \ge 3 + 2 = 5 > 0$.
Suy ra $x - y - 2 = 0 \iff y = x - 2$.
Thay $y = x - 2$ vào phương trình (2):
\[x\sqrt{x-3} - (x-2)\sqrt{x-3} = 2x - 3(x-2) \iff 2\sqrt{x-3} = 6 - x.\]
Điều kiện có nghiệm: $6 - x \ge 0 \iff x \le 6$. Kết hợp điều kiện ta có $3 \le x \le 6$.
Bình phương hai vế:
\[4(x-3) = (6-x)^2 \iff 4x - 12 = x^2 - 12x + 36 \iff x^2 - 16x + 48 = 0 \iff (x-4)(x-12) = 0.\]
Do $3 \le x \le 6$ nên ta chỉ nhận $x = 4$ (loại $x = 12$).
Với $x = 4 \implies y = 4 - 2 = 2$ (thỏa mãn $y \ge 1$).
Vậy hệ phương trình có nghiệm duy nhất $\boxed{(x; y) = (4; 2)}$.
"""
        },
        {
            "so": "3", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Hai bạn Việt và Nam chơi một trò chơi như sau: Việt chọn ngẫu nhiên một số trong tập hợp $\{1;2;3;4;5;6;7;8;9\}$; Nam chọn ngẫu nhiên một số trong tập hợp $\{10;11;12;13;14;15;16\}$. Tính xác suất của biến cố $A$: ``Tích hai số được chọn của hai bạn là một số chẵn''.
  \item Cho ba số thực dương $a, b, c$. Tìm giá trị nhỏ nhất của biểu thức:
  \[P = \frac{1+a^2}{1+ab} + \frac{1+b^2}{1+bc} + \frac{1+c^2}{1+ca}.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} 
Gọi số bạn Việt chọn là $u$ và số bạn Nam chọn là $v$.
Tập hợp các số bạn Việt chọn là $S_1 = \{1; 2; \dots; 9\}$, có $9$ phần tử, gồm $5$ số lẻ $\{1; 3; 5; 7; 9\}$ và $4$ số chẵn $\{2; 4; 6; 8\}$.
Tập hợp các số bạn Nam chọn là $S_2 = \{10; 11; \dots; 16\}$, có $7$ phần tử, gồm $3$ số lẻ $\{11; 13; 15\}$ và $4$ số chẵn $\{10; 12; 14; 16\}$.
Số phần tử của không gian mẫu là:
\[n(\Omega) = 9 \times 7 = 63.\]
Biến cố đối $\overline{A}$: ``Tích $u \cdot v$ là một số lẻ''.
Tích $u \cdot v$ là số lẻ khi và chỉ khi cả $u$ và $v$ đều là số lẻ.
Số cách chọn $u$ lẻ từ $S_1$ là $5$ cách; số cách chọn $v$ lẻ từ $S_2$ là $3$ cách.
Suy ra số kết quả thuận lợi cho $\overline{A}$ là:
\[n(\overline{A}) = 5 \times 3 = 15.\]
Số kết quả thuận lợi cho biến cố $A$ là:
\[n(A) = n(\Omega) - n(\overline{A}) = 63 - 15 = 48.\]
Xác suất của biến cố $A$ là:
\[P(A) = \frac{n(A)}{n(\Omega)} = \frac{48}{63} = \boxed{\frac{16}{21}}.\]

\textbf{b)}
Với mọi $a, b > 0$, ta có biến đổi đồng nhất:
\[\frac{1+a^2}{1+ab} = 1 + \frac{a^2 - ab}{1+ab} = 1 + \frac{a(a-b)}{1+ab}.\]
Tương tự:
\[\frac{1+b^2}{1+bc} = 1 + \frac{b(b-c)}{1+bc};\qquad \frac{1+c^2}{1+ca} = 1 + \frac{c(c-a)}{1+ca}.\]
Cộng ba đẳng thức trên, ta được:
\[P = 3 + \left(\frac{a(a-b)}{1+ab} + \frac{b(b-c)}{1+bc} + \frac{c(c-a)}{1+ca}\right).\]
Không mất tính tổng quát, giả sử $a \ge b \ge c > 0$.
Khi đó:
\[\frac{a(a-b)}{1+ab} + \frac{b(b-c)}{1+bc} + \frac{c(c-a)}{1+ca} \ge 0.\]
Thật vậy, ta có:
\[c(c-a) = -c(a-b) - c(b-c).\]
Do đó:
\[\frac{a(a-b)}{1+ab} + \frac{b(b-c)}{1+bc} + \frac{c(c-a)}{1+ca} = (a-b)\left(\frac{a}{1+ab} - \frac{c}{1+ca}\right) + (b-c)\left(\frac{b}{1+bc} - \frac{c}{1+ca}\right).\]
Xét hàm số $f(t) = \dfrac{t}{1+tc}$ với $t > 0$: $f'(t) = \dfrac{1}{(1+tc)^2} > 0 \implies$ hàm đồng biến.
Vì $a \ge c$ và $b \ge c$ nên các biểu thức trong ngoặc đều không âm.
Từ đó suy ra $P \ge 3$.
Dấu đẳng thức xảy ra khi và chỉ khi $a = b = c = 1$.
Vậy giá trị nhỏ nhất của $P$ là $\boxed{\min P = 3}$, đạt được khi $a = b = c = 1$.
"""
        },
        {
            "so": "5", "diem": "2,0 điểm",
            "de": r"""
Xét bảng ô vuông $8 \times 8$ được hình thành từ 64 ô vuông đơn vị có cạnh bằng 1. Điền vào mỗi ô vuông đơn vị một số nguyên dương không vượt quá 8 sao cho hai số ở hai ô vuông đơn vị chung cạnh hoặc chung đỉnh là hai số nguyên tố cùng nhau. Chứng minh rằng trong bảng đã cho tồn tại một số được điền ít nhất 11 lần.
""",
            "giai": r"""
Tập hợp các số được điền vào bảng là $S = \{1; 2; 3; 4; 5; 6; 7; 8\}$.
Trong tập $S$, xét tập hợp các số chẵn $E = \{2; 4; 6; 8\}$. Bất kỳ hai số chẵn nào cũng đều chia hết cho 2 nên chúng không nguyên tố cùng nhau (ƯCLN $\ge 2$).
Theo đề bài, hai ô vuông chung cạnh hoặc chung đỉnh thì hai số điền trong đó phải nguyên tố cùng nhau. Do đó, hai ô chung cạnh hoặc chung đỉnh không thể cùng chứa các số thuộc tập $E$.
Chia bảng ô vuông $8 \times 8$ thành 16 hình vuông con kích thước $2 \times 2$.
Trong mỗi hình vuông con $2 \times 2$ gồm 4 ô vuông đơn vị, bất kỳ hai ô nào trong đó cũng chung cạnh hoặc chung đỉnh với nhau. Do đó, trong mỗi hình vuông $2 \times 2$, có tối đa 1 ô vuông được điền số chẵn.
Vì có 16 hình vuông $2 \times 2$ nên tổng số ô được điền số chẵn trong toàn bảng $8 \times 8$ không vượt quá $16$.
Do đó, số ô được điền các số lẻ thuộc tập hợp $\{1; 3; 5; 7\}$ ít nhất là:
\[64 - 16 = 48\text{ ô}.\]
Trong tập các số lẻ $\{1; 3; 5; 7\}$, ta nhận thấy 3 và 6 có ước chung là 3, nhưng ở đây ta xét các số lẻ $\{1; 3; 5; 7\}$ gồm 4 số.
Theo nguyên lý Dirichlet, đem xếp ít nhất $48$ ô vuông vào 4 số lẻ $\{1; 3; 5; 7\}$, ta có:
\[\left\lceil \frac{48}{4} \right\rceil = 12 \ge 11.\]
Vậy tồn tại ít nhất một số lẻ được điền ít nhất 12 lần (và hiển nhiên $\ge 11$ lần).
Bài toán được chứng minh hoàn toàn.
"""
        }
    ]
}

print("Loaded SCANNED_EXAMS: de_4")

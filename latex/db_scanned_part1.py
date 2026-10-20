# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn xác từ ảnh scan gốc: Đề 4, 6, 7, 8, 10
"""

SCANNED_PART1 = {}

# -----------------------------------------------------------------------------
# ĐỀ 4: de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2024-2025-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART1["de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2024-2025-so-gddt-lang-son.pdf"] = {
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

Với điều kiện $x \ge 0,\; x \neq 1$, ta phân tích mẫu số:
\[x + 2\sqrt{x} - 3 = (\sqrt{x}-1)(\sqrt{x}+3).\]
Chọn mẫu thức chung là $(\sqrt{x}-1)(\sqrt{x}+3)$. Khi đó:
\begin{align*}
P &= \frac{x\sqrt{x} + 26\sqrt{x} - 19}{(\sqrt{x}-1)(\sqrt{x}+3)} - \frac{2\sqrt{x}(\sqrt{x}+3)}{(\sqrt{x}-1)(\sqrt{x}+3)} + \frac{(\sqrt{x}-3)(\sqrt{x}-1)}{(\sqrt{x}-1)(\sqrt{x}+3)} \\
  &= \frac{x\sqrt{x} + 26\sqrt{x} - 19 - (2x + 6\sqrt{x}) + (x - 4\sqrt{x} + 3)}{(\sqrt{x}-1)(\sqrt{x}+3)} \\
  &= \frac{x\sqrt{x} - x + 16\sqrt{x} - 16}{(\sqrt{x}-1)(\sqrt{x}+3)} \\
  &= \frac{x(\sqrt{x}-1) + 16(\sqrt{x}-1)}{(\sqrt{x}-1)(\sqrt{x}+3)} = \frac{(x+16)(\sqrt{x}-1)}{(\sqrt{x}-1)(\sqrt{x}+3)} = \frac{x+16}{\sqrt{x}+3}.
\end{align*}
Vậy với $x \ge 0, x \neq 1$, ta có $\boxed{P = \dfrac{x+16}{\sqrt{x}+3}}$.

\textbf{b) Tìm giá trị nhỏ nhất của biểu thức $P$:}

Biến đổi biểu thức $P$:
\[P = \frac{x+16}{\sqrt{x}+3} = \frac{x-9+25}{\sqrt{x}+3} = \sqrt{x}-3 + \frac{25}{\sqrt{x}+3} = (\sqrt{x}+3) + \frac{25}{\sqrt{x}+3} - 6.\]
Vì $x \ge 0 \implies \sqrt{x}+3 > 0$. Áp dụng bất đẳng thức AM-GM cho hai số dương:
\[(\sqrt{x}+3) + \frac{25}{\sqrt{x}+3} \ge 2\sqrt{(\sqrt{x}+3)\cdot\frac{25}{\sqrt{x}+3}} = 2 \cdot 5 = 10.\]
Suy ra $P \ge 10 - 6 = 4$.
Đẳng thức xảy ra khi và chỉ khi:
\[\sqrt{x}+3 = \frac{25}{\sqrt{x}+3} \iff (\sqrt{x}+3)^2 = 25 \iff \sqrt{x}+3 = 5 \iff \sqrt{x} = 2 \iff x = 4\text{ (thỏa mãn ĐKXĐ)}.\]
Vậy giá trị nhỏ nhất của $P$ là $\boxed{\min P = 4}$, đạt được khi $x = 4$.
"""
        },
        {
            "so": "2", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho phương trình bậc hai: $x^2 - 2(m-2)x + m^2 - 3m - 2 = 0$ ($m$ là tham số).
  Tìm tất cả các giá trị của $m$ để phương trình có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn:
  \[x_1^2 - 2x_2(x_2 - 2) + m^2 - 7m + 6 = 0.\]
  \item Giải hệ phương trình:
  \[\begin{cases} (x-1)^2 + xy + 1 = 2(y+1)^2 \\ x\sqrt{y-1} - y\sqrt{x-3} = 2x - 3y \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Phương trình $x^2 - 2(m-2)x + m^2 - 3m - 2 = 0$.
Ta có: $\Delta' = (m-2)^2 - (m^2-3m-2) = -m + 6$.
Phương trình có hai nghiệm phân biệt $x_1, x_2 \iff \Delta' > 0 \iff m < 6$.
Theo hệ thức Viète:
\[x_1 + x_2 = 2(m-2) = 2m - 4;\qquad x_1 x_2 = m^2 - 3m - 2.\]
Vì $x_1$ là nghiệm nên $x_1^2 = 2(m-2)x_1 - m^2 + 3m + 2$. Thay vào đẳng thức đã cho:
\[2(m-2)x_1 - m^2 + 3m + 2 - 2x_2^2 + 4x_2 + m^2 - 7m + 6 = 0 \iff (m-2)x_1 - x_2^2 + 2x_2 - 2m + 4 = 0.\]
Thay $m-2 = \dfrac{x_1+x_2}{2}$:
\[\frac{x_1+x_2}{2}\cdot x_1 - x_2^2 + 2x_2 - (x_1+x_2) = 0 \iff x_1^2 + x_1 x_2 - 2x_2^2 - 2x_1 + 2x_2 = 0.\]
Phân tích thành nhân tử: $(x_1 - x_2)(x_1 + 2x_2 - 2) = 0$.
Do $x_1 \neq x_2$ nên $x_1 + 2x_2 = 2$.
Kết hợp với $x_1 + x_2 = 2m - 4$, ta tìm được:
\[x_2 = 6 - 2m;\qquad x_1 = 4m - 10.\]
Thay vào $x_1 x_2 = m^2 - 3m - 2$:
\[(4m-10)(6-2m) = m^2 - 3m - 2 \iff 9m^2 - 47m + 58 = 0.\]
Phương trình có hai nghiệm: $m = 2$ hoặc $m = \dfrac{29}{9}$.
Cả hai giá trị đều thỏa mãn điều kiện $m < 6$.
Vậy $\boxed{m \in \left\{2;\; \dfrac{29}{9}\right\}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} (x-1)^2 + xy + 1 = 2(y+1)^2 \quad (1) \\ x\sqrt{y-1} - y\sqrt{x-3} = 2x - 3y \quad (2) \end{cases}\]
Điều kiện xác định: $x \ge 3,\; y \ge 1$.
Phương trình (1) tương đương với:
\[x^2 - 2x + 1 + xy + 1 = 2y^2 + 4y + 2 \iff x^2 + xy - 2y^2 - 2x - 4y = 0 \iff (x+2y)(x-y-2) = 0.\]
Vì $x \ge 3, y \ge 1$ nên $x + 2y \ge 5 > 0$, suy ra:
\[x - y - 2 = 0 \iff y = x - 2.\]
Thế $y = x - 2$ vào (2):
\[x\sqrt{x-3} - (x-2)\sqrt{x-3} = 2x - 3(x-2) \iff 2\sqrt{x-3} = 6 - x.\]
Điều kiện: $6 - x \ge 0 \iff x \le 6 \implies 3 \le x \le 6$.
Bình phương hai vế:
\[4(x-3) = (6-x)^2 \iff 4x - 12 = x^2 - 12x + 36 \iff x^2 - 16x + 48 = 0 \iff (x-4)(x-12) = 0.\]
Đối chiếu điều kiện $3 \le x \le 6$, ta nhận $x = 4$ (loại $x = 12$).
Với $x = 4 \implies y = 4 - 2 = 2$ (thỏa mãn ĐKXĐ).
Vậy nghiệm duy nhất của hệ phương trình là $\boxed{(x; y) = (4; 2)}$.
"""
        },
        {
            "so": "3", "diem": "4,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Hai bạn Việt và Nam chơi một trò chơi: Việt chọn ngẫu nhiên một số từ tập $\{1;2;3;4;5;6;7;8;9\}$; Nam chọn ngẫu nhiên một số từ tập $\{10;11;12;13;14;15;16\}$. Tính xác suất của biến cố $A$: ``Tích hai số được chọn của hai bạn là số chẵn''.
  \item Cho ba số thực dương $a, b, c$. Tìm giá trị nhỏ nhất của biểu thức:
  \[P = \frac{1+a^2}{1+ab} + \frac{1+b^2}{1+bc} + \frac{1+c^2}{1+ca}.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} 
Tập số của Việt có $9$ phần tử (gồm $5$ số lẻ, $4$ số chẵn).
Tập số của Nam có $7$ phần tử (gồm $3$ số lẻ: $\{11; 13; 15\}$, $4$ số chẵn: $\{10; 12; 14; 16\}$).
Số phần tử không gian mẫu: $n(\Omega) = 9 \times 7 = 63$.
Biến cố đối $\overline{A}$: ``Tích hai số là số lẻ'' xảy ra khi cả hai bạn đều chọn số lẻ.
Số cách chọn cả hai số lẻ: $n(\overline{A}) = 5 \times 3 = 15$.
Số kết quả thuận lợi cho biến cố $A$: $n(A) = 63 - 15 = 48$.
Xác suất của biến cố $A$ là:
\[P(A) = \frac{48}{63} = \boxed{\frac{16}{21}}.\]

\textbf{b)}
Biến đổi từng phân thức:
\[\frac{1+a^2}{1+ab} = 1 + \frac{a(a-b)}{1+ab};\quad \frac{1+b^2}{1+bc} = 1 + \frac{b(b-c)}{1+bc};\quad \frac{1+c^2}{1+ca} = 1 + \frac{c(c-a)}{1+ca}.\]
Cộng lại:
\[P = 3 + \left(\frac{a(a-b)}{1+ab} + \frac{b(b-c)}{1+bc} + \frac{c(c-a)}{1+ca}\right).\]
Không mất tính tổng quát, giả sử $a \ge b \ge c > 0$. Ta có $c(c-a) = -c(a-b) - c(b-c)$, do đó biểu thức trong ngoặc được viết lại thành:
\[(a-b)\left(\frac{a}{1+ab} - \frac{c}{1+ca}\right) + (b-c)\left(\frac{b}{1+bc} - \frac{c}{1+ca}\right).\]
Xét hàm số $f(t) = \dfrac{t}{1+tc}$ với $t > 0$, ta có $f'(t) = \dfrac{1}{(1+tc)^2} > 0$ nên $f(t)$ đồng biến.
Do $a \ge c$ và $b \ge c$ nên các hiệu trong ngoặc đều $\ge 0$.
Suy ra $P \ge 3$.
Dấu đẳng thức xảy ra khi $a = b = c = 1$.
Vậy $\boxed{\min P = 3}$ khi $a = b = c = 1$.
"""
        },
        {
            "so": "5", "diem": "2,0 điểm",
            "de": r"""
Xét bảng ô vuông $8 \times 8$ gồm 64 ô vuông đơn vị cạnh bằng 1. Điền vào mỗi ô vuông đơn vị một số nguyên dương không vượt quá 8 sao cho hai số ở hai ô vuông đơn vị chung cạnh hoặc chung đỉnh là hai số nguyên tố cùng nhau. Chứng minh rằng trong bảng đã cho tồn tại một số được điền ít nhất 11 lần.
""",
            "giai": r"""
Tập hợp các số có thể điền là $\{1; 2; 3; 4; 5; 6; 7; 8\}$.
Trong đó, tập các số chẵn là $E = \{2; 4; 6; 8\}$. Bất kỳ hai số chẵn nào cũng đều có ước chung là $2$, do đó chúng không nguyên tố cùng nhau.
Theo điều kiện đề bài, hai ô vuông chung cạnh hoặc chung đỉnh không thể cùng điền các số chẵn.
Chia bảng $8 \times 8$ thành 16 hình vuông con kích thước $2 \times 2$.
Trong mỗi hình vuông $2 \times 2$, bất kỳ hai ô nào cũng chung cạnh hoặc chung đỉnh với nhau. Vì vậy, mỗi hình vuông $2 \times 2$ có nhiều nhất 1 ô vuông được điền số chẵn.
Toàn bảng có 16 hình vuông $2 \times 2$, suy ra số ô điền số chẵn trên cả bảng không vượt quá $16$.
Do đó, số ô được điền các số lẻ thuộc tập $\{1; 3; 5; 7\}$ ít nhất là:
\[64 - 16 = 48\text{ ô}.\]
Áp dụng nguyên lý Dirichlet, khi phân chia ít nhất $48$ ô vuông cho $4$ số lẻ $\{1; 3; 5; 7\}$, tồn tại ít nhất một số được điền không ít hơn:
\[\left\lceil \frac{48}{4} \right\rceil = 12 \ge 11\text{ lần}.\]
Vậy trong bảng tồn tại một số được điền ít nhất 11 lần.
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 6: de-cuoi-hoc-ky-1-toan-9-thcs-nam-2024-2025-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART1["de-cuoi-hoc-ky-1-toan-9-thcs-nam-2024-2025-so-gddt-lang-son.pdf"] = {
    "title": "Kiểm tra Cuối học kỳ I -- Năm học 2024--2025 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "1,75 điểm",
            "de": r"""
\textbf{Phần trắc nghiệm Đại số (Mỗi câu 0,25 điểm):}
\begin{enumerate}
  \item[Câu 3.] Cho bất đẳng thức $a < b$. Kết luận nào sau đây là không đúng?
  \begin{multicols}{4}
    \item[A.] $-2a > -2b$.
    \item[B.] $a - b < 0$.
    \item[C.] $a - 5 < b - 5$.
    \item[D.] $3a > 3b$.
  \end{multicols}
  \item[Câu 5.] Kết quả của phép tính $\sqrt{2}\cdot(\sqrt{2}+\sqrt{8})$ là:
  \begin{multicols}{4}
    \item[A.] $\sqrt{12}$.
    \item[B.] $6$.
    \item[C.] $\sqrt{20}$.
    \item[D.] $-6$.
  \end{multicols}
  \item[Câu 7.] Nghiệm của hệ phương trình $\begin{cases} x + y = 7 \\ x - y = -3 \end{cases}$ là:
  \begin{multicols}{4}
    \item[A.] $(2; 5)$.
    \item[B.] $(-2; -5)$.
    \item[C.] $(-5; -2)$.
    \item[D.] $(5; 2)$.
  \end{multicols}
  \item[Câu 8.] Hệ phương trình nào dưới đây là hệ hai phương trình bậc nhất hai ẩn?
  \begin{multicols}{2}
    \item[A.] $\begin{cases} 2x+y = -3 \\ x^2-y = 5 \end{cases}$
    \item[B.] $\begin{cases} 3x-y = 4 \\ x+0y = -1 \end{cases}$
    \item[C.] $\begin{cases} x-2y = 1 \\ 0x+0y = 4 \end{cases}$
    \item[D.] $\begin{cases} x+3y = 11 \\ x+2z = -7 \end{cases}$
  \end{multicols}
  \item[Câu 10.] Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?
  \begin{multicols}{4}
    \item[A.] $-3x + \dfrac{1}{2} \ge 0$.
    \item[B.] $0x - 5 < -2$.
    \item[C.] $-2x^2 + 5 > 0$.
    \item[D.] $3x - y \le 0$.
  \end{multicols}
  \item[Câu 11.] Căn bậc hai của $25$ là:
  \begin{multicols}{4}
    \item[A.] $-5$.
    \item[B.] $\sqrt{5}$ và $-\sqrt{5}$.
    \item[C.] $5$ và $-5$.
    \item[D.] $5$.
  \end{multicols}
  \item[Câu 12.] Biểu thức nào sau đây không phải là căn thức bậc hai?
  \begin{multicols}{4}
    \item[A.] $\sqrt{7^2-5^2}$.
    \item[B.] $\sqrt{\dfrac{x^2+1}{2}}$.
    \item[C.] $\sqrt{3+2x^2}$.
    \item[D.] $\dfrac{-3}{x^2+2}$.
  \end{multicols}
\end{enumerate}
""",
            "giai": r"""
\textbf{Đáp án chi tiết các câu trắc nghiệm Đại số:}
\begin{itemize}
  \item \textbf{Câu 3: Chọn D.} Với $a < b$, nhân hai vế với $3 > 0$ ta được $3a < 3b$. Do đó khẳng định $3a > 3b$ là sai.
  \item \textbf{Câu 5: Chọn B.} $\sqrt{2}(\sqrt{2}+\sqrt{8}) = \sqrt{2}\cdot\sqrt{2} + \sqrt{2}\cdot 2\sqrt{2} = 2 + 4 = 6$.
  \item \textbf{Câu 7: Chọn A.} Cộng hai phương trình vế theo vế: $2x = 4 \implies x = 2$. Thay vào phương trình đầu: $2 + y = 7 \implies y = 5$. Nghiệm là $(2; 5)$.
  \item \textbf{Câu 8: Chọn B.} Hệ phương trình bậc nhất hai ẩn có dạng $\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}$ với các hệ số không đồng thời bằng 0. Hệ ở đáp án B thỏa mãn.
  \item \textbf{Câu 10: Chọn A.} Bất phương trình bậc nhất một ẩn có dạng $ax + b \ge 0$ (hoặc $\le, >, <$) với $a \neq 0$. Ở đây $-3x + \dfrac{1}{2} \ge 0$ có $a = -3 \neq 0$.
  \item \textbf{Câu 11: Chọn C.} Mọi số thực dương $a$ đều có đúng hai căn bậc hai là $\sqrt{a}$ và $-\sqrt{a}$. Căn bậc hai của $25$ là $5$ và $-5$.
  \item \textbf{Câu 12: Chọn D.} Biểu thức $\dfrac{-3}{x^2+2}$ không chứa dấu căn bậc hai nên không phải là căn thức bậc hai.
\end{itemize}
"""
        },
        {
            "so": "2", "diem": "2,5 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải bất phương trình: $2 - 3x \le -7$.
  \item Giải phương trình: $\dfrac{-x^2}{2x+1} + \dfrac{2x-1}{4} = \dfrac{1}{4}$.
  \item Trong một xí nghiệp, hai tổ sản xuất cùng may một loại áo đồng phục học sinh. Nếu tổ thứ nhất may trong 5 ngày và tổ thứ hai may trong 3 ngày thì cả hai tổ may được 1420 chiếc áo. Biết rằng mỗi ngày tổ thứ nhất may được nhiều hơn tổ thứ hai 20 chiếc áo. Hỏi trong một ngày mỗi tổ may được bao nhiêu chiếc áo? (Năng suất may mỗi ngày của mỗi tổ là không đổi).
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải bất phương trình $2 - 3x \le -7$:}
\[2 - 3x \le -7 \iff -3x \le -7 - 2 \iff -3x \le -9 \iff x \ge \frac{-9}{-3} \iff x \ge 3.\]
Vậy tập nghiệm của bất phương trình là $\boxed{S = \{x \in \mathbb{R} \mid x \ge 3\}}$.

\textbf{b) Giải phương trình: $\dfrac{-x^2}{2x+1} + \dfrac{2x-1}{4} = \dfrac{1}{4}$:}

Điều kiện xác định: $2x + 1 \neq 0 \iff x \neq -\dfrac{1}{2}$.
Quy đồng mẫu thức chung là $4(2x+1)$:
\[\frac{-4x^2}{4(2x+1)} + \frac{(2x-1)(2x+1)}{4(2x+1)} = \frac{2x+1}{4(2x+1)}.\]
Khử mẫu ta được:
\[-4x^2 + (4x^2 - 1) = 2x + 1 \iff -1 = 2x + 1 \iff 2x = -2 \iff x = -1.\]
Giá trị $x = -1$ thỏa mãn điều kiện xác định $x \neq -\dfrac{1}{2}$.
Vậy tập nghiệm của phương trình là $\boxed{S = \{-1\}}$.

\textbf{c) Bài toán may áo:}

Gọi số áo tổ thứ nhất may được trong một ngày là $x$ (chiếc áo, $x \in \mathbb{N}^*$, $x > 20$).
Số áo tổ thứ hai may được trong một ngày là $y$ (chiếc áo, $y \in \mathbb{N}^*$).
Vì mỗi ngày tổ thứ nhất may được nhiều hơn tổ thứ hai 20 chiếc áo nên ta có phương trình:
\[x - y = 20 \quad (1).\]
Trong 5 ngày, tổ thứ nhất may được $5x$ chiếc áo.
Trong 3 ngày, tổ thứ hai may được $3y$ chiếc áo.
Cả hai tổ may được tổng cộng 1420 chiếc áo nên ta có phương trình:
\[5x + 3y = 1420 \quad (2).\]
Từ (1) và (2) ta có hệ phương trình:
\[\begin{cases} x - y = 20 \\ 5x + 3y = 1420 \end{cases} \iff \begin{cases} 3x - 3y = 60 \\ 5x + 3y = 1420 \end{cases} \iff \begin{cases} 8x = 1480 \\ y = x - 20 \end{cases} \iff \begin{cases} x = 185\text{ (thỏa mãn)} \\ y = 165\text{ (thỏa mãn)} \end{cases}\]
Vậy trong một ngày:
\begin{itemize}
  \item Tổ thứ nhất may được: $\boxed{185\text{ chiếc áo}}$.
  \item Tổ thứ hai may được: $\boxed{165\text{ chiếc áo}}$.
\end{itemize}
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của các biểu thức:
  \[A = \sqrt{16} + \sqrt{9};\qquad B = \sqrt{(2-\sqrt{3})^2} + \sqrt{3};\qquad C = 2(\sqrt{5}+3) - 2(1+\sqrt{5}).\]
  \item Rút gọn biểu thức: $P = \left(\dfrac{1}{\sqrt{x}} - \dfrac{1}{\sqrt{x}+1}\right)(x+\sqrt{x})$ với $x > 0$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị các biểu thức:}
\begin{align*}
A &= \sqrt{16} + \sqrt{9} = 4 + 3 = \boxed{7}. \\
B &= \sqrt{(2-\sqrt{3})^2} + \sqrt{3} = |2-\sqrt{3}| + \sqrt{3} = (2-\sqrt{3}) + \sqrt{3} = \boxed{2}\quad (\text{do } 2 = \sqrt{4} > \sqrt{3}). \\
C &= 2(\sqrt{5}+3) - 2(1+\sqrt{5}) = 2\sqrt{5} + 6 - 2 - 2\sqrt{5} = \boxed{4}.
\end{align*}

\textbf{b) Rút gọn biểu thức $P$:}

Với điều kiện $x > 0$:
\[\frac{1}{\sqrt{x}} - \frac{1}{\sqrt{x}+1} = \frac{\sqrt{x}+1 - \sqrt{x}}{\sqrt{x}(\sqrt{x}+1)} = \frac{1}{\sqrt{x}(\sqrt{x}+1)}.\]
Ta lại có: $x + \sqrt{x} = \sqrt{x}(\sqrt{x}+1)$.
Do đó:
\[P = \frac{1}{\sqrt{x}(\sqrt{x}+1)} \cdot \sqrt{x}(\sqrt{x}+1) = \boxed{1}.\]
Vậy với $x > 0$ thì $P = 1$.
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 7: de-giua-hoc-ki-1-toan-9-nam-2023-2024-phong-gddt-bac-son-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART1["de-giua-hoc-ki-1-toan-9-nam-2023-2024-phong-gddt-bac-son-lang-son.pdf"] = {
    "title": "Kiểm tra Giữa học kỳ I -- Năm học 2023--2024 -- Phòng GD\\&ĐT Bắc Sơn, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,5 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Trong các số $-4;\; -2;\; -1;\; 1;\; 2;\; 4$, những số nào là căn bậc hai của 16? Vì sao?
  \item Với giá trị nào của $x$ thì căn thức $\sqrt{x-2}$ có nghĩa?
  \item Với hai số $a$ và $b$ không âm, hãy viết công thức khai phương một tích hai số $a$ và $b$. Áp dụng tính $\sqrt{9 \cdot 16}$.
  \item Rút gọn các biểu thức:
  \[A = \sqrt{2} - \sqrt{18} + \sqrt{32};\qquad B = 2\sqrt{3} + \sqrt{(2-\sqrt{3})^2}.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} 
Các số là căn bậc hai của $16$ là $\boxed{4}$ và $\boxed{-4}$.
Vì $4^2 = 16$ và $(-4)^2 = 16$.

\textbf{b)} 
Căn thức $\sqrt{x-2}$ có nghĩa khi và chỉ khi:
\[x - 2 \ge 0 \iff \boxed{x \ge 2}.\]

\textbf{c)} 
Với hai số $a \ge 0$ và $b \ge 0$, công thức khai phương một tích là:
\[\sqrt{a \cdot b} = \sqrt{a} \cdot \sqrt{b}.\]
Áp dụng:
\[\sqrt{9 \cdot 16} = \sqrt{9} \cdot \sqrt{16} = 3 \cdot 4 = \boxed{12}.\]

\textbf{d) Rút gọn biểu thức:}
\begin{align*}
A &= \sqrt{2} - \sqrt{18} + \sqrt{32} = \sqrt{2} - \sqrt{9 \cdot 2} + \sqrt{16 \cdot 2} = \sqrt{2} - 3\sqrt{2} + 4\sqrt{2} = (1 - 3 + 4)\sqrt{2} = \boxed{2\sqrt{2}}. \\
B &= 2\sqrt{3} + \sqrt{(2-\sqrt{3})^2} = 2\sqrt{3} + |2-\sqrt{3}|.
\end{align*}
Vì $2 = \sqrt{4} > \sqrt{3} \implies 2 - \sqrt{3} > 0 \implies |2-\sqrt{3}| = 2 - \sqrt{3}$.
Do đó:
\[B = 2\sqrt{3} + 2 - \sqrt{3} = \boxed{\sqrt{3} + 2}.\]
"""
        },
        {
            "so": "2", "diem": "1,5 điểm",
            "de": r"""
Cho biểu thức: $A = \left(\dfrac{1}{x+2\sqrt{x}} - \dfrac{1}{\sqrt{x}+2}\right) : \dfrac{1-\sqrt{x}}{x+4\sqrt{x}+4}$.
\begin{enumerate}[label=\alph*)]
  \item Tìm điều kiện của $x$ để biểu thức $A$ có nghĩa.
  \item Rút gọn biểu thức $A$.
  \item Tìm tất cả các giá trị nguyên của $x$ để $A$ nhận giá trị nguyên.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm điều kiện xác định của biểu thức $A$:}
Biểu thức $A$ có nghĩa khi:
\[\begin{cases} x \ge 0 \\ x+2\sqrt{x} \neq 0 \\ \sqrt{x}+2 \neq 0 \\ x+4\sqrt{x}+4 \neq 0 \\ 1-\sqrt{x} \neq 0 \end{cases} \iff \begin{cases} x > 0 \\ \sqrt{x} \neq 1 \end{cases} \iff \boxed{x > 0,\; x \neq 1}.\]

\textbf{b) Rút gọn biểu thức $A$:}
Với $x > 0,\; x \neq 1$, ta có:
\[\frac{1}{x+2\sqrt{x}} - \frac{1}{\sqrt{x}+2} = \frac{1}{\sqrt{x}(\sqrt{x}+2)} - \frac{\sqrt{x}}{\sqrt{x}(\sqrt{x}+2)} = \frac{1-\sqrt{x}}{\sqrt{x}(\sqrt{x}+2)}.\]
Mặt khác:
\[x + 4\sqrt{x} + 4 = (\sqrt{x}+2)^2.\]
Do đó:
\[A = \frac{1-\sqrt{x}}{\sqrt{x}(\sqrt{x}+2)} \cdot \frac{(\sqrt{x}+2)^2}{1-\sqrt{x}} = \frac{\sqrt{x}+2}{\sqrt{x}} = 1 + \frac{2}{\sqrt{x}}.\]
Vậy với $x > 0,\; x \neq 1$, ta có $\boxed{A = \dfrac{\sqrt{x}+2}{\sqrt{x}} = 1 + \dfrac{2}{\sqrt{x}}}$.

\textbf{c) Tìm $x \in \mathbb{Z}$ để $A \in \mathbb{Z}$:}
Ta có: $A = 1 + \dfrac{2}{\sqrt{x}}$.
Để $A$ nhận giá trị nguyên thì $\dfrac{2}{\sqrt{x}}$ phải là số nguyên, tức là $\sqrt{x}$ phải là ước dương của $2$.
Ước dương của 2 là $\{1; 2\}$. Do đó:
\begin{itemize}
  \item Trường hợp 1: $\sqrt{x} = 1 \iff x = 1$ (loại vì không thỏa mãn điều kiện $x \neq 1$).
  \item Trường hợp 2: $\sqrt{x} = 2 \iff x = 4$ (thỏa mãn điều kiện $x > 0, x \neq 1, x \in \mathbb{Z}$).
\end{itemize}
Vậy giá trị nguyên duy nhất cần tìm là $\boxed{x = 4}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Giải phương trình:
\[\sqrt{x-2} + \sqrt{x+1} = 3.\]
""",
            "giai": r"""
Điều kiện xác định: $\begin{cases} x - 2 \ge 0 \\ x + 1 \ge 0 \end{cases} \iff x \ge 2$.

\textbf{Cách 1 (Biến đổi tương đương):}
Phương trình đã cho tương đương với:
\[\sqrt{x+1} = 3 - \sqrt{x-2}.\]
Điều kiện: $3 - \sqrt{x-2} \ge 0 \iff \sqrt{x-2} \le 3 \iff x - 2 \le 9 \iff x \le 11$.
Bình phương hai vế:
\[x + 1 = 9 - 6\sqrt{x-2} + (x-2) \iff x + 1 = x + 7 - 6\sqrt{x-2} \iff 6\sqrt{x-2} = 6 \iff \sqrt{x-2} = 1.\]
Bình phương hai vế:
\[x - 2 = 1 \iff x = 3.\]
Giá trị $x = 3$ thỏa mãn điều kiện $2 \le x \le 11$.

\textbf{Cách 2 (Sử dụng tính đơn điệu):}
Với $x \ge 2$, xét hàm số $f(x) = \sqrt{x-2} + \sqrt{x+1}$.
Khi $x$ tăng thì cả $\sqrt{x-2}$ và $\sqrt{x+1}$ đều tăng, do đó $f(x)$ là hàm số đồng biến trên $[2; +\infty)$.
Ta thấy $f(3) = \sqrt{3-2} + \sqrt{3+1} = \sqrt{1} + \sqrt{4} = 1 + 2 = 3$.
Vì hàm số đồng biến nên phương trình $f(x) = 3$ có nghiệm duy nhất là $x = 3$.

Vậy tập nghiệm của phương trình là $\boxed{S = \{3\}}$.
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 8: de-giua-hoc-ki-2-toan-9-nam-2022-2023-phong-gddt-bac-son-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART1["de-giua-hoc-ki-2-toan-9-nam-2022-2023-phong-gddt-bac-son-lang-son.pdf"] = {
    "title": "Kiểm tra Giữa học kỳ II -- Năm học 2022--2023 -- Phòng GD\\&ĐT Bắc Sơn, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "3,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho hệ phương trình $\begin{cases} 3x + y = 5 \\ x - 2y = -3 \end{cases}$. Cặp số $(x; y) = (1; 2)$ có phải là nghiệm của hệ phương trình trên không? Vì sao?
  \item Giải hệ phương trình: $\begin{cases} 2x - y = 3 \\ x + 2y = 4 \end{cases}$.
  \item Cho phương trình: $15x^2 + 4x - 2005 = 0$. Không giải phương trình, hãy cho biết phương trình trên có bao nhiêu nghiệm? Vì sao?
  \item Giải phương trình: $2x^2 - 7x + 3 = 0$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Thay cặp số $(x; y) = (1; 2)$ vào từng phương trình của hệ:
\begin{itemize}
  \item Vế trái phương trình (1): $3(1) + 2 = 5$ (bằng vế phải).
  \item Vế trái phương trình (2): $1 - 2(2) = 1 - 4 = -3$ (bằng vế phải).
\end{itemize}
Vì cặp số $(1; 2)$ thỏa mãn cả hai phương trình nên $\boxed{(1; 2)\text{ là nghiệm}}$ của hệ phương trình đã cho.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} 2x - y = 3 \quad (1) \\ x + 2y = 4 \quad (2) \end{cases}\]
Nhân cả hai vế của (1) với $2$:
\[\begin{cases} 4x - 2y = 6 \\ x + 2y = 4 \end{cases}\]
Cộng hai phương trình vế theo vế:
\[5x = 10 \iff x = 2.\]
Thay $x = 2$ vào phương trình (1):
\[2(2) - y = 3 \iff 4 - y = 3 \iff y = 1.\]
Vậy hệ phương trình có nghiệm duy nhất $\boxed{(x; y) = (2; 1)}$.

\textbf{c)} Phương trình bậc hai $15x^2 + 4x - 2005 = 0$ có các hệ số:
\[a = 15;\quad c = -2005.\]
Ta thấy tích $a \cdot c = 15 \cdot (-2005) < 0$.
Vì $a$ và $c$ trái dấu nên biệt thức $\Delta = b^2 - 4ac > 0$ với mọi trường hợp.
Do đó, phương trình đã cho luôn $\boxed{\text{có hai nghiệm phân biệt}}$.

\textbf{d) Giải phương trình $2x^2 - 7x + 3 = 0$:}
Biệt thức $\Delta$:
\[\Delta = (-7)^2 - 4 \cdot 2 \cdot 3 = 49 - 24 = 25 > 0.\]
Vì $\Delta = 25 > 0$ nên phương trình có hai nghiệm phân biệt:
\[x_1 = \frac{-(-7) + \sqrt{25}}{2 \cdot 2} = \frac{7 + 5}{4} = \frac{12}{4} = 3;\qquad x_2 = \frac{-(-7) - \sqrt{25}}{2 \cdot 2} = \frac{7 - 5}{4} = \frac{2}{4} = \frac{1}{2}.\]
Vậy tập nghiệm của phương trình là $\boxed{S = \left\{\dfrac{1}{2};\; 3\right\}}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tung độ của điểm $A$ thuộc đồ thị hàm số $y = 3x^2$ có hoành độ $x = -2$.
  \item Vẽ đồ thị của hàm số $y = 3x^2$ trong mặt phẳng tọa độ $(Oxy)$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} 
Điểm $A$ thuộc đồ thị hàm số $y = 3x^2$ và có hoành độ $x = -2$.
Tung độ của điểm $A$ là:
\[y = 3 \cdot (-2)^2 = 3 \cdot 4 = \boxed{12}.\]
Vậy điểm $A(-2; 12)$ có tung độ là $12$.

\textbf{b) Vẽ đồ thị hàm số $y = 3x^2$:}
\begin{itemize}
  \item \textbf{Tập xác định:} $D = \mathbb{R}$.
  \item \textbf{Tính chất:} Vì hệ số $a = 3 > 0$ nên đồ thị là một Parabol có bề lõm quay lên trên, nhận gốc tọa độ $O(0;0)$ làm đỉnh và là điểm thấp nhất, nhận trục tung $Oy$ làm trục đối xứng.
  \item \textbf{Bảng giá trị tương ứng:}
  \begin{center}
  \begin{tabular}{|c|c|c|c|c|c|}
    \hline
    $x$ & $-2$ & $-1$ & $0$ & $1$ & $2$ \\
    \hline
    $y = 3x^2$ & $12$ & $3$ & $0$ & $3$ & $12$ \\
    \hline
  \end{tabular}
  \end{center}
  \item \textbf{Đồ thị:} Đi qua 5 điểm $(-2; 12)$, $(-1; 3)$, $O(0; 0)$, $(1; 3)$, $(2; 12)$.
\end{itemize}
"""
        },
        {
            "so": "3", "diem": "1,5 điểm",
            "de": r"""
Một sân trường hình chữ nhật có chu vi $340\text{ m}$. Ba lần chiều dài lớn hơn bốn lần chiều rộng là $20\text{ m}$. Tính chiều dài và chiều rộng của sân trường?
""",
            "giai": r"""
Gọi chiều dài của sân trường là $x$ (mét, điều kiện: $x > 0$).
Gọi chiều rộng của sân trường là $y$ (mét, điều kiện: $0 < y < x$).

Nửa chu vi sân trường hình chữ nhật là:
\[340 : 2 = 170\text{ (m)}.\]
Ta có phương trình:
\[x + y = 170 \quad (1).\]
Theo đề bài, ba lần chiều dài lớn hơn bốn lần chiều rộng là $20\text{ m}$ nên ta có phương trình:
\[3x - 4y = 20 \quad (2).\]
Từ (1) và (2) ta có hệ phương trình:
\[\begin{cases} x + y = 170 \\ 3x - 4y = 20 \end{cases} \iff \begin{cases} 4x + 4y = 680 \\ 3x - 4y = 20 \end{cases} \iff \begin{cases} 7x = 700 \\ y = 170 - x \end{cases} \iff \begin{cases} x = 100\text{ (thỏa mãn)} \\ y = 70\text{ (thỏa mãn)} \end{cases}\]
Vậy:
\begin{itemize}
  \item Chiều dài sân trường là: $\boxed{100\text{ m}}$.
  \item Chiều rộng sân trường là: $\boxed{70\text{ m}}$.
\end{itemize}
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Tìm giá trị nhỏ nhất của biểu thức:
\[P = \frac{3x^2 - 8x + 6}{x^2 - 2x + 1}.\]
""",
            "giai": r"""
Điều kiện xác định: $x^2 - 2x + 1 \neq 0 \iff (x-1)^2 \neq 0 \iff x \neq 1$.
Ta biến đổi biểu thức $P$:
\begin{align*}
P &= \frac{3x^2 - 8x + 6}{(x-1)^2} = \frac{3(x-1)^2 - 2(x-1) + 1}{(x-1)^2} \\
  &= 3 - \frac{2}{x-1} + \frac{1}{(x-1)^2}.
\end{align*}
Đặt $t = \dfrac{1}{x-1}$ với $t \neq 0$, biểu thức trở thành tam thức bậc hai theo $t$:
\[P = t^2 - 2t + 3 = (t-1)^2 + 2.\]
Vì $(t-1)^2 \ge 0$ với mọi $t$ nên:
\[P \ge 2.\]
Đẳng thức xảy ra khi và chỉ khi:
\[t - 1 = 0 \iff t = 1 \iff \frac{1}{x-1} = 1 \iff x - 1 = 1 \iff x = 2\text{ (thỏa mãn } x \neq 1).\]
Vậy giá trị nhỏ nhất của biểu thức $P$ là $\boxed{\min P = 2}$, đạt được khi $x = 2$.
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 10: de-giua-ky-1-toan-9-nam-2022-2023-phong-gddt-huu-lung-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART1["de-giua-ky-1-toan-9-nam-2022-2023-phong-gddt-huu-lung-lang-son.pdf"] = {
    "title": "Kiểm tra Giữa kỳ I -- Năm học 2022--2023 -- Phòng GD\\&ĐT Hữu Lũng, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm các căn bậc hai của 36.
  \item Căn thức $\sqrt{x-4}$ xác định khi nào?
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Căn bậc hai của $36$ là $\boxed{6}$ và $\boxed{-6}$ vì $6^2 = (-6)^2 = 36$.

\textbf{b)} Căn thức $\sqrt{x-4}$ xác định khi và chỉ khi biểu thức dưới dấu căn không âm:
\[x - 4 \ge 0 \iff \boxed{x \ge 4}.\]
"""
        },
        {
            "so": "2", "diem": "2,5 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Viết công thức liên hệ giữa phép nhân, phép chia và phép khai phương.
  \item Tính giá trị của các biểu thức:
  \[A = 5\sqrt{3} - \sqrt{48} + \sqrt{108};\qquad B = \frac{1}{3+\sqrt{6}} + \frac{1}{3-\sqrt{6}}.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Công thức liên hệ:}
\begin{itemize}
  \item Khai phương một tích: Với $a \ge 0$ và $b \ge 0$, ta có: $\sqrt{a \cdot b} = \sqrt{a} \cdot \sqrt{b}$.
  \item Khai phương một thương: Với $a \ge 0$ và $b > 0$, ta có: $\sqrt{\dfrac{a}{b}} = \dfrac{\sqrt{a}}{\sqrt{b}}$.
\end{itemize}

\textbf{b) Tính giá trị biểu thức:}
\begin{align*}
A &= 5\sqrt{3} - \sqrt{48} + \sqrt{108} = 5\sqrt{3} - \sqrt{16 \cdot 3} + \sqrt{36 \cdot 3} = 5\sqrt{3} - 4\sqrt{3} + 6\sqrt{3} = \boxed{7\sqrt{3}}. \\
B &= \frac{1}{3+\sqrt{6}} + \frac{1}{3-\sqrt{6}} = \frac{(3-\sqrt{6}) + (3+\sqrt{6})}{(3+\sqrt{6})(3-\sqrt{6})} = \frac{6}{3^2 - (\sqrt{6})^2} = \frac{6}{9 - 6} = \frac{6}{3} = \boxed{2}.
\end{align*}
"""
        },
        {
            "so": "3", "diem": "1,5 điểm",
            "de": r"""
Cho biểu thức $A = \left(\dfrac{1}{x+2\sqrt{x}} - \dfrac{1}{\sqrt{x}+2}\right) : \dfrac{1-\sqrt{x}}{x+4\sqrt{x}+4}$.
\begin{enumerate}[label=\alph*)]
  \item Tìm điều kiện của $x$ để biểu thức $A$ có nghĩa.
  \item Rút gọn biểu thức $A$.
  \item Tìm $x \in \mathbb{Z}$ để $A \in \mathbb{Z}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Điều kiện xác định:}
Biểu thức $A$ có nghĩa khi và chỉ khi:
\[\begin{cases} x \ge 0 \\ \sqrt{x}(\sqrt{x}+2) \neq 0 \\ 1 - \sqrt{x} \neq 0 \end{cases} \iff \boxed{x > 0,\; x \neq 1}.\]

\textbf{b) Rút gọn biểu thức $A$:}
Với $x > 0,\; x \neq 1$, ta có:
\begin{align*}
A &= \left(\frac{1}{\sqrt{x}(\sqrt{x}+2)} - \frac{\sqrt{x}}{\sqrt{x}(\sqrt{x}+2)}\right) : \frac{1-\sqrt{x}}{(\sqrt{x}+2)^2} \\
  &= \frac{1-\sqrt{x}}{\sqrt{x}(\sqrt{x}+2)} \cdot \frac{(\sqrt{x}+2)^2}{1-\sqrt{x}} = \frac{\sqrt{x}+2}{\sqrt{x}} = \boxed{1 + \frac{2}{\sqrt{x}}}.
\end{align*}

\textbf{c) Tìm $x \in \mathbb{Z}$ để $A \in \mathbb{Z}$:}
Ta có: $A = 1 + \dfrac{2}{\sqrt{x}}$.
Để $A \in \mathbb{Z}$ thì $\dfrac{2}{\sqrt{x}} \in \mathbb{Z}$, nghĩa là $\sqrt{x}$ phải là ước nguyên dương của 2:
\[\sqrt{x} \in \{1; 2\}.\]
\begin{itemize}
  \item Nếu $\sqrt{x} = 1 \iff x = 1$ (loại do điều kiện $x \neq 1$).
  \item Nếu $\sqrt{x} = 2 \iff x = 4$ (thỏa mãn điều kiện).
\end{itemize}
Vậy $\boxed{x = 4}$.
"""
        },
        {
            "so": "6", "diem": "0,5 điểm",
            "de": r"""
Giải phương trình:
\[x(x+1) = 4 - 4\sqrt{x^2+x+1}.\]
""",
            "giai": r"""
Phương trình đã cho: $x^2 + x = 4 - 4\sqrt{x^2+x+1}$.
Thêm $1$ vào cả hai vế:
\[(x^2+x+1) + 4\sqrt{x^2+x+1} - 5 = 0.\]
Nhận xét: $x^2 + x + 1 = \left(x + \dfrac{1}{2}\right)^2 + \dfrac{3}{4} > 0$ với mọi $x \in \mathbb{R}$.
Đặt $t = \sqrt{x^2+x+1}$ với điều kiện $t \ge \dfrac{\sqrt{3}}{2} > 0$.
Phương trình trở thành:
\[t^2 + 4t - 5 = 0 \iff (t-1)(t+5) = 0 \iff \left[\begin{aligned} &t = 1\text{ (thỏa mãn)} \\ &t = -5\text{ (loại vì } t > 0) \end{aligned}\right.\]
Với $t = 1$, ta có:
\[\sqrt{x^2+x+1} = 1 \iff x^2 + x + 1 = 1 \iff x^2 + x = 0 \iff x(x+1) = 0 \iff \left[\begin{aligned} &x = 0 \\ &x = -1 \end{aligned}\right.\]
Cả hai giá trị $x = 0$ và $x = -1$ đều thỏa mãn.
Vậy tập nghiệm của phương trình là $\boxed{S = \{-1;\; 0\}}$.
"""
        }
    ]
}

print("Loaded SCANNED_PART1 (Exams 4, 6, 7, 8, 10)")

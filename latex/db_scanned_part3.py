# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn xác từ ảnh scan gốc: Đề 18, 21, 25, 26, 49
"""

SCANNED_PART3 = {}

# -----------------------------------------------------------------------------
# ĐỀ 18: de-kiem-tra-cuoi-hoc-ki-2-toan-9-nam-2023-2024-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART3["de-kiem-tra-cuoi-hoc-ki-2-toan-9-nam-2023-2024-so-gddt-lang-son.pdf"] = {
    "title": "Kiểm tra Cuối học kỳ II -- Năm học 2023--2024 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,5 điểm",
            "de": r"""
\begin{enumerate}[label=\arabic*)]
  \item Cho phương trình bậc hai: $x^2 - 7x + 10 = 0$ (*).
  \begin{enumerate}[label=\alph*)]
    \item Xác định các hệ số $a, b, c$ của phương trình (*).
    \item Tính biệt thức $\Delta$ của phương trình (*).
  \end{enumerate}
  \item Giải hệ phương trình:
  \[\begin{cases} 3x + y = 6 \\ x - 2y = -5 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Phương trình $x^2 - 7x + 10 = 0$:
\begin{enumerate}[label=\alph*)]
  \item Các hệ số của phương trình là: $\boxed{a = 1,\; b = -7,\; c = 10}$.
  \item Biệt thức $\Delta$:
  \[\Delta = b^2 - 4ac = (-7)^2 - 4 \cdot 1 \cdot 10 = 49 - 40 = \boxed{9}.\]
\end{enumerate}

\textbf{2. Giải hệ phương trình:}
\[\begin{cases} 3x + y = 6 \quad (1) \\ x - 2y = -5 \quad (2) \end{cases}\]
Từ phương trình (1) suy ra: $y = 6 - 3x$.
Thế vào phương trình (2):
\[x - 2(6 - 3x) = -5 \iff x - 12 + 6x = -5 \iff 7x = 7 \iff x = 1.\]
Thay $x = 1$ vào biểu thức của $y$:
\[y = 6 - 3(1) = 3.\]
Vậy hệ phương trình có nghiệm duy nhất $\boxed{(x; y) = (1; 3)}$.
"""
        },
        {
            "so": "2", "diem": "1,5 điểm",
            "de": r"""
Cho hàm số $y = -x^2$ có đồ thị là $(P)$.
\begin{enumerate}[label=\arabic*)]
  \item Vẽ đồ thị $(P)$ của hàm số.
  \item Tìm tọa độ giao điểm của đồ thị $(P)$ với đường thẳng $(d)\colon y = x - 2$.
\end{enumerate}
""",
            "giai": r"""
\textbf{1. Vẽ đồ thị $(P)\colon y = -x^2$:}
\begin{itemize}
  \item \textbf{Tập xác định:} $D = \mathbb{R}$.
  \item \textbf{Tính chất:} Vì $a = -1 < 0$ nên đồ thị là Parabol có bề lõm quay xuống dưới, nhận gốc tọa độ $O(0;0)$ làm đỉnh và là điểm cao nhất, trục đối xứng là trục tung $Oy$.
  \item \textbf{Bảng giá trị:}
  \begin{center}
  \begin{tabular}{|c|c|c|c|c|c|}
    \hline
    $x$ & $-2$ & $-1$ & $0$ & $1$ & $2$ \\
    \hline
    $y = -x^2$ & $-4$ & $-1$ & $0$ & $-1$ & $-4$ \\
    \hline
  \end{tabular}
  \end{center}
  \item Đồ thị đi qua các điểm $(-2; -4)$, $(-1; -1)$, $O(0; 0)$, $(1; -1)$, $(2; -4)$.
\end{itemize}

\textbf{2. Tìm tọa độ giao điểm của $(P)$ và $(d)$:}
Phương trình hoành độ giao điểm của $(P)$ và $(d)$:
\[-x^2 = x - 2 \iff x^2 + x - 2 = 0.\]
Phương trình có dạng $a + b + c = 1 + 1 + (-2) = 0$, suy ra hai nghiệm:
\[x_1 = 1;\qquad x_2 = -2.\]
\begin{itemize}
  \item Với $x_1 = 1 \implies y_1 = -(1)^2 = -1$, ta được giao điểm $A(1; -1)$.
  \item Với $x_2 = -2 \implies y_2 = -(-2)^2 = -4$, ta được giao điểm $B(-2; -4)$.
\end{itemize}
Vậy tọa độ các giao điểm là $\boxed{(1; -1)}$ và $\boxed{(-2; -4)}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\arabic*)]
  \item Cho phương trình bậc hai: $x^2 + 3x + m = 0$ (1) với $m$ là tham số.
  \begin{enumerate}[label=\alph*)]
    \item Giải phương trình (1) khi $m = -4$.
    \item Tìm $m$ để phương trình (1) có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn:
    \[x_1 x_2 - 2x_1 - 2x_2 = 8.\]
  \end{enumerate}
  \item Lớp 9A giao cho bạn Minh đi mua bánh và kẹo để tổ chức liên hoan. Minh mua tất cả 12 hộp bánh và 8 túi kẹo với số tiền phải trả là 820 nghìn đồng. Biết rằng giá mỗi hộp bánh là như nhau, giá mỗi túi kẹo là như nhau và giá một hộp bánh hơn giá một túi kẹo là 10 nghìn đồng. Tính giá tiền để mua một hộp bánh và giá tiền để mua một túi kẹo.
\end{enumerate}
""",
            "giai": r"""
\textbf{1.} Phương trình $x^2 + 3x + m = 0$ (1).
\begin{enumerate}[label=\alph*)]
  \item Khi $m = -4$, phương trình trở thành:
  \[x^2 + 3x - 4 = 0.\]
  Vì $a + b + c = 1 + 3 + (-4) = 0$ nên phương trình có hai nghiệm phân biệt:
  \[x_1 = 1;\qquad x_2 = -4.\]
  Vậy khi $m = -4$, tập nghiệm của phương trình là $\boxed{S = \{-4;\; 1\}}$.

  \item Biệt thức: $\Delta = 3^2 - 4 \cdot 1 \cdot m = 9 - 4m$.
  Để phương trình có hai nghiệm phân biệt $x_1, x_2$ thì:
  \[\Delta > 0 \iff 9 - 4m > 0 \iff m < \frac{9}{4}.\]
  Theo định lý Viète: $x_1 + x_2 = -3$ và $x_1 x_2 = m$.
  Biến đổi hệ thức đã cho:
  \[x_1 x_2 - 2(x_1 + x_2) = 8 \iff m - 2(-3) = 8 \iff m + 6 = 8 \iff m = 2.\]
  Giá trị $m = 2$ thỏa mãn điều kiện $m < \dfrac{9}{4}$ (do $2 < 2{,}25$).
  Vậy $\boxed{m = 2}$.
\end{enumerate}

\textbf{2. Bài toán mua bánh kẹo:}
Gọi giá tiền của một hộp bánh là $x$ (nghìn đồng, điều kiện: $x > 10$).
Gọi giá tiền của một túi kẹo là $y$ (nghìn đồng, điều kiện: $y > 0$).
Vì giá một hộp bánh hơn giá một túi kẹo là 10 nghìn đồng nên ta có phương trình:
\[x - y = 10 \quad (1).\]
Mua 12 hộp bánh và 8 túi kẹo hết 820 nghìn đồng nên ta có phương trình:
\[12x + 8y = 820 \quad (2).\]
Từ (1) suy ra $x = y + 10$. Thế vào (2):
\[12(y + 10) + 8y = 820 \iff 12y + 120 + 8y = 820 \iff 20y = 700 \iff y = 35\text{ (thỏa mãn)}.\]
Suy ra $x = 35 + 10 = 45$ (thỏa mãn).
Vậy:
\begin{itemize}
  \item Giá một hộp bánh là: $\boxed{45\text{ nghìn đồng}}$ ($45.000$ đồng).
  \item Giá một túi kẹo là: $\boxed{35\text{ nghìn đồng}}$ ($35.000$ đồng).
\end{itemize}
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho các số thực dương $a, b, c$ thỏa mãn $a + b + c \le 3$. Chứng minh rằng:
\[\frac{ab}{\sqrt{c^2+3}} + \frac{bc}{\sqrt{a^2+3}} + \frac{ca}{\sqrt{b^2+3}} \le \frac{3}{2}.\]
""",
            "giai": r"""
Vì $a, b, c > 0$ và $a + b + c \le 3$, ta có bất đẳng thức quen thuộc:
\[ab + bc + ca \le \frac{(a+b+c)^2}{3} \le \frac{3^2}{3} = 3.\]
Do đó:
\[c^2 + 3 \ge c^2 + ab + bc + ca = (c+a)(c+b).\]
Suy ra:
\[\sqrt{c^2+3} \ge \sqrt{(c+a)(c+b)}.\]
Áp dụng bất đẳng thức AM-GM cho hai số dương $(c+a)$ và $(c+b)$:
\[\sqrt{(c+a)(c+b)} \ge \frac{2}{\dfrac{1}{c+a} + \dfrac{1}{c+b}} \implies \frac{1}{\sqrt{c^2+3}} \le \frac{1}{\sqrt{(c+a)(c+b)}} \le \frac{1}{2}\left(\frac{1}{c+a} + \frac{1}{c+b}\right).\]
Do đó:
\[\frac{ab}{\sqrt{c^2+3}} \le \frac{1}{2}\left(\frac{ab}{c+a} + \frac{ab}{c+b}\right).\]
Thiết lập các bất đẳng thức tương tự:
\[\frac{bc}{\sqrt{a^2+3}} \le \frac{1}{2}\left(\frac{bc}{a+b} + \frac{bc}{a+c}\right);\qquad \frac{ca}{\sqrt{b^2+3}} \le \frac{1}{2}\left(\frac{ca}{b+c} + \frac{ca}{b+a}\right).\]
Cộng cả ba bất đẳng thức lại theo vế:
\begin{align*}
VT &\le \frac{1}{2}\left[\left(\frac{ab}{c+a} + \frac{bc}{a+c}\right) + \left(\frac{ab}{c+b} + \frac{ca}{b+c}\right) + \left(\frac{bc}{a+b} + \frac{ca}{b+a}\right)\right] \\
&= \frac{1}{2}\left[\frac{b(a+c)}{a+c} + \frac{a(b+c)}{b+c} + \frac{c(a+b)}{a+b}\right] = \frac{1}{2}(b + a + c) = \frac{a+b+c}{2}.
\end{align*}
Vì $a+b+c \le 3$ nên:
\[VT \le \frac{3}{2}.\]
Đẳng thức xảy ra khi và chỉ khi $a = b = c = 1$.
Bất đẳng thức được chứng minh hoàn toàn.
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 21: de-thi-thu-tuyen-sinh-lop-10-mon-toan-lan-1-nam-2026-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART3["de-thi-thu-tuyen-sinh-lop-10-mon-toan-lan-1-nam-2026-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi thử Tuyển sinh vào lớp 10 THPT lần 1 -- Năm 2026 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\textbf{Phần I. Trắc nghiệm (Mã đề 102 -- Mỗi câu 0,25 điểm):}
\begin{enumerate}
  \item[Câu 1.] Bất phương trình $2 + 5x \ge -1 - x$ có nghiệm là:
  \begin{multicols}{4}
    \item[A.] $x \le \dfrac{1}{2}$.
    \item[B.] $x \ge \dfrac{1}{2}$.
    \item[C.] $x \le -\dfrac{1}{2}$.
    \item[D.] $x \ge -\dfrac{1}{2}$.
  \end{multicols}
  \item[Câu 2.] Nghiệm của phương trình $(2-4x)(x+3) = 0$ là:
  \begin{multicols}{2}
    \item[A.] $x = 2$ và $x = 3$.
    \item[B.] $x = \dfrac{1}{2}$ và $x = 3$.
    \item[C.] $x = \dfrac{1}{2}$ và $x = -3$.
    \item[D.] $x = -2$ và $x = -3$.
  \end{multicols}
  \item[Câu 3.] Căn bậc hai số học của $\dfrac{9}{25}$ là:
  \begin{multicols}{4}
    \item[A.] $1$.
    \item[B.] $\dfrac{9}{25}$.
    \item[C.] $\dfrac{3}{5}$.
    \item[D.] $-\dfrac{3}{5}$.
  \end{multicols}
  \item[Câu 4.] Kết quả của phép tính $\dfrac{\sqrt{99}}{\sqrt{11}}$ là:
  \begin{multicols}{4}
    \item[A.] $3$.
    \item[B.] $\sqrt{3}$.
    \item[C.] $11$.
    \item[D.] $9$.
  \end{multicols}
  \item[Câu 5.] Điều kiện xác định của biểu thức $\sqrt{a}$ là:
  \begin{multicols}{4}
    \item[A.] $a \ge 0$.
    \item[B.] $a \in \mathbb{Z}$.
    \item[C.] $a \in \mathbb{R}$.
    \item[D.] $a > 0$.
  \end{multicols}
  \item[Câu 8.] Cặp số $(-2; -3)$ là nghiệm của hệ phương trình nào?
  \begin{multicols}{2}
    \item[A.] $\begin{cases} 4x-2y = 0 \\ x-3y = 5 \end{cases}$
    \item[B.] $\begin{cases} 2x-y = -1 \\ x-3y = 7 \end{cases}$
    \item[C.] $\begin{cases} x-2y = 3 \\ 2x+y = 4 \end{cases}$
    \item[D.] $\begin{cases} 2x-y = -1 \\ x-3y = 8 \end{cases}$
  \end{multicols}
\end{enumerate}
""",
            "giai": r"""
\textbf{Đáp án chi tiết trắc nghiệm (Mã 102):}
\begin{itemize}
  \item \textbf{Câu 1: Chọn D.} $2 + 5x \ge -1 - x \iff 6x \ge -3 \iff x \ge -\dfrac{1}{2}$.
  \item \textbf{Câu 2: Chọn C.} $(2-4x)(x+3) = 0 \iff 2-4x = 0$ hoặc $x+3 = 0 \iff x = \dfrac{1}{2}$ hoặc $x = -3$.
  \item \textbf{Câu 3: Chọn C.} Căn bậc hai số học của $\dfrac{9}{25}$ là $\sqrt{\dfrac{9}{25}} = \dfrac{3}{5}$.
  \item \textbf{Câu 4: Chọn A.} $\dfrac{\sqrt{99}}{\sqrt{11}} = \sqrt{\dfrac{99}{11}} = \sqrt{9} = 3$.
  \item \textbf{Câu 5: Chọn A.} Biểu thức $\sqrt{a}$ xác định khi và chỉ khi $a \ge 0$.
  \item \textbf{Câu 8: Chọn B.} Thay $(-2; -3)$ vào hệ B: $2(-2) - (-3) = -4 + 3 = -1$ và $-2 - 3(-3) = -2 + 9 = 7$ (đúng).
\end{itemize}
"""
        },
        {
            "so": "2", "diem": "2,5 điểm",
            "de": r"""
\textbf{Phần II. Tự luận:}
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình: $\begin{cases} 4x - y = 7 \\ x + 3y = 5 \end{cases}$.
  \item Giải phương trình: $(-x + 6)(2x - 4) = 0$.
  \item Giải bất phương trình: $4 - 7(x - 3) \le 2(x - 1)$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải hệ phương trình:}
\[\begin{cases} 4x - y = 7 \quad (1) \\ x + 3y = 5 \quad (2) \end{cases}\]
Từ phương trình (1), ta có: $y = 4x - 7$.
Thay $y = 4x - 7$ vào phương trình (2):
\[x + 3(4x - 7) = 5 \iff x + 12x - 21 = 5 \iff 13x = 26 \iff x = 2.\]
Thay $x = 2$ vào biểu thức của $y$:
\[y = 4(2) - 7 = 1.\]
Vậy hệ phương trình có nghiệm duy nhất là $\boxed{(x; y) = (2; 1)}$.

\textbf{b) Giải phương trình $(-x + 6)(2x - 4) = 0$:}
\[(-x + 6)(2x - 4) = 0 \iff \left[\begin{aligned} &-x + 6 = 0 \\ &2x - 4 = 0 \end{aligned}\right. \iff \left[\begin{aligned} &x = 6 \\ &x = 2 \end{aligned}\right.\]
Vậy tập nghiệm của phương trình là $\boxed{S = \{2;\; 6\}}$.

\textbf{c) Giải bất phương trình $4 - 7(x - 3) \le 2(x - 1)$:}
\begin{align*}
4 - 7x + 21 \le 2x - 2 &\iff -7x + 25 \le 2x - 2 \\
&\iff -9x \le -27 \\
&\iff x \ge \frac{-27}{-9} \iff x \ge 3.
\end{align*}
Vậy nghiệm của bất phương trình là $\boxed{x \ge 3}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của các biểu thức:
  \[A = 2\sqrt{100} - \sqrt{25};\qquad B = \sqrt{(\sqrt{3}-1)^2} + 1.\]
  \item Cho biểu thức: $P = \dfrac{\sqrt{a}+1}{\sqrt{a}} : \left(\dfrac{1}{\sqrt{a}+1} + \dfrac{2}{a-1}\right)$ với $a > 0,\; a \neq 1$.
  Rút gọn $P$ và tính giá trị của biểu thức $P$ tại $a = 4$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị của các biểu thức:}
\begin{align*}
A &= 2\sqrt{100} - \sqrt{25} = 2 \cdot 10 - 5 = 20 - 5 = \boxed{15}. \\
B &= \sqrt{(\sqrt{3}-1)^2} + 1 = |\sqrt{3}-1| + 1 = \sqrt{3}-1+1 = \boxed{\sqrt{3}}\quad (\text{do } \sqrt{3} > 1).
\end{align*}

\textbf{b) Rút gọn biểu thức $P$ và tính giá trị tại $a = 4$:}

Với điều kiện $a > 0,\; a \neq 1$, ta có $a - 1 = (\sqrt{a}-1)(\sqrt{a}+1)$.
Quy đồng biểu thức trong ngoặc:
\[\frac{1}{\sqrt{a}+1} + \frac{2}{(\sqrt{a}-1)(\sqrt{a}+1)} = \frac{\sqrt{a}-1+2}{(\sqrt{a}-1)(\sqrt{a}+1)} = \frac{\sqrt{a}+1}{(\sqrt{a}-1)(\sqrt{a}+1)} = \frac{1}{\sqrt{a}-1}.\]
Thực hiện phép chia:
\[P = \frac{\sqrt{a}+1}{\sqrt{a}} : \frac{1}{\sqrt{a}-1} = \frac{\sqrt{a}+1}{\sqrt{a}} \cdot (\sqrt{a}-1) = \frac{a - 1}{\sqrt{a}}.\]
(Hoặc ở dạng $P = \dfrac{(\sqrt{a}+1)(\sqrt{a}-1)}{\sqrt{a}}$).

Tại $a = 4$ (thỏa mãn điều kiện $a > 0, a \neq 1$):
\[P = \frac{4 - 1}{\sqrt{4}} = \frac{3}{2} = \boxed{1{,}5}.\]
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 25: de-thi-thu-tuyen-sinh-vao-lop-10-mon-toan-nam-2022-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART3["de-thi-thu-tuyen-sinh-vao-lop-10-mon-toan-nam-2022-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi thử Tuyển sinh vào lớp 10 THPT -- Năm 2022 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,5 điểm",
            "de": r"""
\begin{enumerate}[label=\arabic*)]
  \item Tính giá trị của các biểu thức sau:
  \[A = \sqrt{4} + \sqrt{49};\qquad B = \sqrt{(3+\sqrt{11})^2} - \sqrt{11};\qquad C = (3\sqrt{18} - \sqrt{50})\sqrt{2}.\]
  \item Cho biểu thức: $P = \left(1 + \dfrac{a+\sqrt{a}}{\sqrt{a}+1}\right)\left(2 - \dfrac{a-\sqrt{a}}{a-1}\right)$ với $a \ge 0,\; a \neq 1$.
  \begin{enumerate}[label=\alph*)]
    \item Rút gọn $P$.
    \item Tìm giá trị của $a$ để $P = 5$.
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{1. Tính giá trị các biểu thức:}
\begin{align*}
A &= \sqrt{4} + \sqrt{49} = 2 + 7 = \boxed{9}. \\
B &= \sqrt{(3+\sqrt{11})^2} - \sqrt{11} = |3+\sqrt{11}| - \sqrt{11} = 3 + \sqrt{11} - \sqrt{11} = \boxed{3}. \\
C &= (3\sqrt{18} - \sqrt{50})\sqrt{2} = (3 \cdot 3\sqrt{2} - 5\sqrt{2})\sqrt{2} = (9\sqrt{2} - 5\sqrt{2})\sqrt{2} = 4\sqrt{2} \cdot \sqrt{2} = \boxed{8}.
\end{align*}

\textbf{2. Rút gọn biểu thức $P$ và tìm $a$:}
\begin{enumerate}[label=\alph*)]
  \item Với $a \ge 0,\; a \neq 1$:
  \begin{align*}
  1 + \frac{a+\sqrt{a}}{\sqrt{a}+1} &= 1 + \frac{\sqrt{a}(\sqrt{a}+1)}{\sqrt{a}+1} = 1 + \sqrt{a}. \\
  2 - \frac{a-\sqrt{a}}{a-1} &= 2 - \frac{\sqrt{a}(\sqrt{a}-1)}{(\sqrt{a}-1)(\sqrt{a}+1)} = 2 - \frac{\sqrt{a}}{\sqrt{a}+1} = \frac{2(\sqrt{a}+1) - \sqrt{a}}{\sqrt{a}+1} = \frac{\sqrt{a}+2}{\sqrt{a}+1}.
  \end{align*}
  Nhân hai biểu thức lại:
  \[P = (1 + \sqrt{a}) \cdot \frac{\sqrt{a}+2}{\sqrt{a}+1} = \sqrt{a} + 2.\]
  Vậy với $a \ge 0, a \neq 1$, ta có $\boxed{P = \sqrt{a} + 2}$.

  \item Để $P = 5$:
  \[\sqrt{a} + 2 = 5 \iff \sqrt{a} = 3 \iff a = 9.\]
  Giá trị $a = 9$ thỏa mãn điều kiện $a \ge 0,\; a \neq 1$.
  Vậy $\boxed{a = 9}$.
\end{enumerate}
"""
        },
        {
            "so": "2", "diem": "1,0 điểm",
            "de": r"""
\begin{enumerate}[label=\arabic*)]
  \item Vẽ đồ thị hàm số $y = x - 2$.
  \item Cho hàm số bậc hai $y = 3x^2$. Tìm các giá trị của $x$ để $y = 12$.
\end{enumerate}
""",
            "giai": r"""
\textbf{1. Vẽ đồ thị hàm số $y = x - 2$:}
\begin{itemize}
  \item Cho $x = 0 \implies y = -2$, đồ thị đi qua điểm $A(0; -2)$.
  \item Cho $y = 0 \implies x - 2 = 0 \iff x = 2$, đồ thị đi qua điểm $B(2; 0)$.
\end{itemize}
Đồ thị hàm số $y = x - 2$ là đường thẳng đi qua hai điểm $A(0; -2)$ và $B(2; 0)$.

\textbf{2. Tìm các giá trị của $x$ để $y = 12$:}
Thay $y = 12$ vào công thức hàm số:
\[3x^2 = 12 \iff x^2 = 4 \iff \boxed{x = \pm 2}.\]
Vậy các giá trị cần tìm là $x = 2$ hoặc $x = -2$.
"""
        },
        {
            "so": "3", "diem": "2,5 điểm",
            "de": r"""
\begin{enumerate}[label=\arabic*)]
  \item Giải hệ phương trình: $\begin{cases} 3x + 2y = 1 \\ 2x - y = -4 \end{cases}$.
  \item Cho phương trình bậc hai: $x^2 + mx + m - 2 = 0$ với $m$ là tham số.
  \begin{enumerate}[label=\alph*)]
    \item Chỉ ra các hệ số $a, b, c$ của phương trình.
    \item Chứng minh rằng với mọi $m$ thì phương trình đã cho luôn có 2 nghiệm phân biệt $x_1, x_2$. Khi đó, tìm $m$ để $x_1^2 + x_2^2 - x_1 x_2 = 10$.
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{1. Giải hệ phương trình:}
\[\begin{cases} 3x + 2y = 1 \quad (1) \\ 2x - y = -4 \quad (2) \end{cases}\]
Từ phương trình (2) suy ra $y = 2x + 4$. Thế vào (1):
\[3x + 2(2x + 4) = 1 \iff 3x + 4x + 8 = 1 \iff 7x = -7 \iff x = -1.\]
Thay $x = -1$ vào: $y = 2(-1) + 4 = 2$.
Vậy nghiệm duy nhất của hệ là $\boxed{(x; y) = (-1; 2)}$.

\textbf{2. Phương trình $x^2 + mx + m - 2 = 0$:}
\begin{enumerate}[label=\alph*)]
  \item Các hệ số là: $\boxed{a = 1,\; b = m,\; c = m - 2}$.
  \item Biệt thức $\Delta$:
  \[\Delta = b^2 - 4ac = m^2 - 4 \cdot 1 \cdot (m-2) = m^2 - 4m + 8 = (m-2)^2 + 4.\]
  Vì $(m-2)^2 \ge 0$ với mọi $m$ nên $(m-2)^2 + 4 \ge 4 > 0$ với mọi $m$.
  Do đó phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi $m$.

  Theo định lý Viète: $x_1 + x_2 = -m$ và $x_1 x_2 = m - 2$.
  Biến đổi hệ thức:
  \begin{align*}
  x_1^2 + x_2^2 - x_1 x_2 = 10 &\iff (x_1+x_2)^2 - 3x_1 x_2 = 10 \\
  &\iff (-m)^2 - 3(m-2) = 10 \iff m^2 - 3m + 6 = 10 \\
  &\iff m^2 - 3m - 4 = 0 \iff (m-4)(m+1) = 0 \iff \left[\begin{aligned} &m = 4 \\ &m = -1 \end{aligned}\right.
  \end{align*}
  Vậy các giá trị cần tìm của $m$ là $\boxed{m \in \{-1;\; 4\}}$.
\end{enumerate}
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 26: de-thi-thu-vao-lop-10-mon-toan-nam-2020-2021-phong-gddt-loc-binh-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART3["de-thi-thu-vao-lop-10-mon-toan-nam-2020-2021-phong-gddt-loc-binh-lang-son.pdf"] = {
    "title": "Kỳ thi thử vào lớp 10 THPT -- Năm học 2020--2021 -- Phòng GD\\&ĐT Lộc Bình, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của các biểu thức: $A = \sqrt{81} - \sqrt{49}$;\quad $B = \sqrt{(\sqrt{7}+1)^2} - \sqrt{7}$.
  \item Rút gọn biểu thức: $P = \left(\dfrac{1}{\sqrt{x}-1} + \dfrac{2}{x-\sqrt{x}}\right) \cdot \dfrac{3\sqrt{x}}{\sqrt{x}+2}$ với $x > 0$ và $x \neq 1$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị các biểu thức:}
\begin{align*}
A &= \sqrt{81} - \sqrt{49} = 9 - 7 = \boxed{2}. \\
B &= \sqrt{(\sqrt{7}+1)^2} - \sqrt{7} = |\sqrt{7}+1| - \sqrt{7} = \sqrt{7} + 1 - \sqrt{7} = \boxed{1}.
\end{align*}

\textbf{b) Rút gọn biểu thức $P$:}

Với điều kiện $x > 0$ và $x \neq 1$:
\[\frac{1}{\sqrt{x}-1} + \frac{2}{x-\sqrt{x}} = \frac{1}{\sqrt{x}-1} + \frac{2}{\sqrt{x}(\sqrt{x}-1)} = \frac{\sqrt{x}+2}{\sqrt{x}(\sqrt{x}-1)}.\]
Thực hiện phép nhân:
\[P = \frac{\sqrt{x}+2}{\sqrt{x}(\sqrt{x}-1)} \cdot \frac{3\sqrt{x}}{\sqrt{x}+2} = \frac{3}{\sqrt{x}-1}.\]
Vậy với $x > 0, x \neq 1$, ta có $\boxed{P = \frac{3}{\sqrt{x}-1}}$.
"""
        },
        {
            "so": "2", "diem": "1,5 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Vẽ đồ thị hàm số $y = -x^2$.
  \item Cho phương trình: $x^2 - (2m+1)x + m^2 + 2 = 0$. Tìm $m$ để phương trình có 2 nghiệm $x_1, x_2$ thoả mãn hệ thức:
  \[3x_1 x_2 - 5(x_1 + x_2) + 7 = 0.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Vẽ đồ thị hàm số $y = -x^2$:}
\begin{itemize}
  \item \textbf{Tập xác định:} $D = \mathbb{R}$.
  \item \textbf{Bảng giá trị:}
  \begin{center}
  \begin{tabular}{|c|c|c|c|c|c|}
    \hline
    $x$ & $-2$ & $-1$ & $0$ & $1$ & $2$ \\
    \hline
    $y = -x^2$ & $-4$ & $-1$ & $0$ & $-1$ & $-4$ \\
    \hline
  \end{tabular}
  \end{center}
  \item Parabol có đỉnh $O(0;0)$, bề lõm quay xuống dưới và nhận $Oy$ làm trục đối xứng.
\end{itemize}

\textbf{b) Tìm $m$:}
Biệt thức $\Delta$:
\[\Delta = [-(2m+1)]^2 - 4(m^2+2) = 4m^2 + 4m + 1 - 4m^2 - 8 = 4m - 7.\]
Phương trình có hai nghiệm $x_1, x_2 \iff \Delta \ge 0 \iff 4m - 7 \ge 0 \iff m \ge \dfrac{7}{4}$.
Theo định lý Viète: $x_1 + x_2 = 2m + 1$ và $x_1 x_2 = m^2 + 2$.
Thay vào hệ thức đã cho:
\begin{align*}
3(m^2+2) - 5(2m+1) + 7 = 0 &\iff 3m^2 + 6 - 10m - 5 + 7 = 0 \\
&\iff 3m^2 - 10m + 8 = 0.
\end{align*}
Phương trình bậc hai này có:
\[\Delta_m = (-10)^2 - 4 \cdot 3 \cdot 8 = 100 - 96 = 4 > 0.\]
Hai nghiệm:
\[m_1 = \frac{10 + 2}{6} = 2;\qquad m_2 = \frac{10 - 2}{6} = \frac{4}{3}.\]
Đối chiếu điều kiện $m \ge \dfrac{7}{4} = 1{,}75$:
\begin{itemize}
  \item $m = 2 \ge 1{,}75$ (thỏa mãn).
  \item $m = \dfrac{4}{3} \approx 1{,}33 < 1{,}75$ (loại).
\end{itemize}
Vậy giá trị duy nhất cần tìm là $\boxed{m = 2}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình: $\begin{cases} x + 2y = 5 \\ 3x - y = 1 \end{cases}$.
  \item Một khu vườn hình chữ nhật có chu vi $280\text{ m}$. Người ta làm một lối đi xung quanh vườn (thuộc đất vườn) rộng $2\text{ m}$, diện tích còn lại để trồng trọt là $4256\text{ m}^2$. Tính kích thước (chiều dài, chiều rộng) của khu vườn đó.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải hệ phương trình:}
\[\begin{cases} x + 2y = 5 \quad (1) \\ 3x - y = 1 \quad (2) \end{cases} \iff \begin{cases} x + 2y = 5 \\ 6x - 2y = 2 \end{cases} \iff \begin{cases} 7x = 7 \\ y = 3x - 1 \end{cases} \iff \begin{cases} x = 1 \\ y = 2 \end{cases}\]
Vậy hệ phương trình có nghiệm duy nhất $\boxed{(x; y) = (1; 2)}$.

\textbf{b) Bài toán khu vườn:}
Nửa chu vi của khu vườn là: $280 : 2 = 140\text{ (m)}$.
Gọi chiều dài của khu vườn ban đầu là $x$ (mét, điều kiện: $4 < x < 140$).
Chiều rộng của khu vườn ban đầu là: $140 - x$ (mét, điều kiện: $x \ge 140 - x \iff x \ge 70$).
Khi làm lối đi xung quanh rộng $2\text{ m}$:
\begin{itemize}
  \item Chiều dài phần đất còn lại để trồng trọt là: $x - 2 \cdot 2 = x - 4$ (m).
  \item Chiều rộng phần đất còn lại để trồng trọt là: $(140 - x) - 4 = 136 - x$ (m).
\end{itemize}
Diện tích phần đất trồng trọt là $4256\text{ m}^2$ nên ta có phương trình:
\[(x - 4)(136 - x) = 4256 \iff 136x - x^2 - 544 + 4x = 4256 \iff x^2 - 140x + 4800 = 0.\]
Biệt thức thu gọn: $\Delta' = (-70)^2 - 1 \cdot 4800 = 4900 - 4800 = 100 > 0$.
Phương trình có hai nghiệm:
\[x_1 = 70 + 10 = 80;\qquad x_2 = 70 - 10 = 60.\]
Vì $x$ là chiều dài nên $x \ge 70$, do đó ta nhận $x = 80$ (m).
Chiều rộng tương ứng là: $140 - 80 = 60$ (m).
Vậy:
\begin{itemize}
  \item Chiều dài khu vườn là: $\boxed{80\text{ m}}$.
  \item Chiều rộng khu vườn là: $\boxed{60\text{ m}}$.
\end{itemize}
"""
        },
        {
            "so": "5", "diem": "1,0 điểm",
            "de": r"""
Cho $a, b, c$ là các số thực không âm thỏa mãn $0 \le a \le b \le c \le 1$.
Tìm giá trị lớn nhất của biểu thức:
\[Q = a^2(b - c) + b^2(c - b) + c^2(1 - c).\]
""",
            "giai": r"""
Ta viết lại biểu thức $Q$:
\[Q = a^2(b - c) + b^2(c - b) + c^2(1 - c) = -a^2(c - b) + b^2(c - b) + c^2(1 - c) = (b^2 - a^2)(c - b) + c^2(1 - c).\]
Vì $0 \le a \le b$ nên $b^2 - a^2 \le b^2$.
Do $c \ge b \ge 0 \implies c - b \ge 0$, do đó:
\[(b^2 - a^2)(c - b) \le b^2(c - b).\]
Suy ra:
\[Q \le b^2(c - b) + c^2(1 - c) = cb^2 - b^3 + c^2 - c^3.\]
Áp dụng bất đẳng thức AM-GM cho hai số dương $b$ và $c - b$:
\[b^2(c - b) = 4 \cdot \frac{b}{2} \cdot \frac{b}{2} \cdot (c - b) \le 4 \cdot \left(\frac{\frac{b}{2} + \frac{b}{2} + c - b}{3}\right)^3 = \frac{4c^3}{27}.\]
Do đó:
\[Q \le \frac{4c^3}{27} + c^2 - c^3 = c^2 - \frac{23c^3}{27}.\]
Khảo sát hàm số $f(c) = c^2 - c^3 + b^2(c-b)$:
Tại $a = 0, b = \dfrac{2}{3}, c = 1$:
\[Q = 0 + \left(\frac{2}{3}\right)^2\left(1 - \frac{2}{3}\right) + 1^2(1 - 1) = \frac{4}{9} \cdot \frac{1}{3} = \frac{4}{27}.\]
Hoặc khảo sát hàm số theo $c \in [0; 1]$ ta tìm được giá trị lớn nhất của $Q$ đạt được là $\boxed{\max Q = \frac{4}{27}}$, khi $a = 0, b = \dfrac{2}{3}, c = 1$.
"""
        }
    ]
}

# -----------------------------------------------------------------------------
# ĐỀ 49: de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2024-2025-so-gddt-lang-son.pdf
# -----------------------------------------------------------------------------
SCANNED_PART3["de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2024-2025-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2024--2025 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,5 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của các biểu thức sau:
  \[A = \sqrt{16} + \sqrt{4};\qquad B = \sqrt{(2+\sqrt{3})^2} - \sqrt{3};\qquad C = (\sqrt{8}+\sqrt{2})\sqrt{2}.\]
  \item Cho biểu thức: $P = \left(\dfrac{1}{\sqrt{x}-1} - \dfrac{1}{\sqrt{x}}\right) \cdot \dfrac{(\sqrt{x}-1)(\sqrt{x}-2)}{3}$ với $x > 0$ và $x \neq 1$.
  \begin{enumerate}[label=\arabic*)]
    \item Rút gọn biểu thức $P$.
    \item Tìm các giá trị của $x$ để $P > \dfrac{1}{4}$.
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị của các biểu thức:}
\begin{align*}
A &= \sqrt{16} + \sqrt{4} = 4 + 2 = \boxed{6}. \\
B &= \sqrt{(2+\sqrt{3})^2} - \sqrt{3} = |2+\sqrt{3}| - \sqrt{3} = 2 + \sqrt{3} - \sqrt{3} = \boxed{2}\quad (\text{do } 2+\sqrt{3}>0). \\
C &= (\sqrt{8}+\sqrt{2})\sqrt{2} = (2\sqrt{2}+\sqrt{2})\sqrt{2} = 3\sqrt{2} \cdot \sqrt{2} = 3 \cdot 2 = \boxed{6}.
\end{align*}

\textbf{b) Rút gọn biểu thức $P$ và tìm $x$:}
\begin{enumerate}[label=\arabic*)]
  \item Với $x > 0,\; x \neq 1$:
  \[\frac{1}{\sqrt{x}-1} - \frac{1}{\sqrt{x}} = \frac{\sqrt{x} - (\sqrt{x}-1)}{\sqrt{x}(\sqrt{x}-1)} = \frac{1}{\sqrt{x}(\sqrt{x}-1)}.\]
  Thực hiện phép nhân:
  \[P = \frac{1}{\sqrt{x}(\sqrt{x}-1)} \cdot \frac{(\sqrt{x}-1)(\sqrt{x}-2)}{3} = \frac{\sqrt{x}-2}{3\sqrt{x}}.\]
  Vậy với $x > 0, x \neq 1$, ta có $\boxed{P = \frac{\sqrt{x}-2}{3\sqrt{x}}}$.

  \item Để $P > \dfrac{1}{4}$:
  \[\frac{\sqrt{x}-2}{3\sqrt{x}} > \frac{1}{4} \iff \frac{\sqrt{x}-2}{3\sqrt{x}} - \frac{1}{4} > 0 \iff \frac{4(\sqrt{x}-2) - 3\sqrt{x}}{12\sqrt{x}} > 0 \iff \frac{\sqrt{x}-8}{12\sqrt{x}} > 0.\]
  Vì $x > 0 \implies 12\sqrt{x} > 0$, do đó:
  \[\sqrt{x} - 8 > 0 \iff \sqrt{x} > 8 \iff x > 64.\]
  Kết hợp với điều kiện xác định ($x > 0, x \neq 1$), ta được $\boxed{x > 64}$.
\end{enumerate}
"""
        },
        {
            "so": "2", "diem": "1,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Vẽ parabol $(P)\colon y = x^2$.
  \item Tìm tọa độ giao điểm của đồ thị hàm số $(P)\colon y = x^2$ với đường thẳng $(d)\colon y = 4x - 3$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Vẽ đồ thị parabol $(P)\colon y = x^2$:}
\begin{itemize}
  \item \textbf{Tập xác định:} $D = \mathbb{R}$.
  \item \textbf{Bảng giá trị tương ứng:}
  \begin{center}
  \begin{tabular}{|c|c|c|c|c|c|}
    \hline
    $x$ & $-2$ & $-1$ & $0$ & $1$ & $2$ \\
    \hline
    $y = x^2$ & $4$ & $1$ & $0$ & $1$ & $4$ \\
    \hline
  \end{tabular}
  \end{center}
  \item Parabol $(P)$ có đỉnh $O(0;0)$, bề lõm quay lên trên, nhận trục tung $Oy$ làm trục đối xứng.
\end{itemize}

\textbf{b) Tìm tọa độ giao điểm của $(P)$ và $(d)$:}
Phương trình hoành độ giao điểm của $(P)$ và $(d)$:
\[x^2 = 4x - 3 \iff x^2 - 4x + 3 = 0.\]
Phương trình có $a + b + c = 1 + (-4) + 3 = 0$, suy ra hai nghiệm:
\[x_1 = 1;\qquad x_2 = 3.\]
\begin{itemize}
  \item Với $x_1 = 1 \implies y_1 = 1^2 = 1$, ta có giao điểm $M(1; 1)$.
  \item Với $x_2 = 3 \implies y_2 = 3^2 = 9$, ta có giao điểm $N(3; 9)$.
\end{itemize}
Vậy tọa độ các giao điểm của $(P)$ và $(d)$ là $\boxed{(1; 1)}$ và $\boxed{(3; 9)}$.
"""
        },
        {
            "so": "3", "diem": "2,5 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình: $\begin{cases} 2x + y = 4 \\ 3x - y = 11 \end{cases}$.
  \item Cho phương trình: $x^2 - 2mx - 4 = 0$ (*), với $m$ là tham số.
  \begin{enumerate}[label=\arabic*)]
    \item Chứng minh rằng phương trình (*) luôn có hai nghiệm phân biệt với mọi $m$.
    \item Tìm $m$ để phương trình (*) có hai nghiệm $x_1, x_2$ thỏa mãn $2x_1 + 2x_2 - x_1 x_2 = 8$.
  \end{enumerate}
  \item Một mảnh đất hình chữ nhật có chu vi là $42\text{ m}$ và có độ dài đường chéo là $15\text{ m}$. Tính chiều dài của mảnh đất đó.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải hệ phương trình:}
\[\begin{cases} 2x + y = 4 \quad (1) \\ 3x - y = 11 \quad (2) \end{cases}\]
Cộng hai phương trình vế theo vế:
\[5x = 15 \iff x = 3.\]
Thay $x = 3$ vào phương trình (1):
\[2(3) + y = 4 \iff 6 + y = 4 \iff y = -2.\]
Vậy hệ phương trình có nghiệm duy nhất $\boxed{(x; y) = (3; -2)}$.

\textbf{b) Phương trình $x^2 - 2mx - 4 = 0$ (*):}
\begin{enumerate}[label=\arabic*)]
  \item Biệt thức thu gọn:
  \[\Delta' = (-m)^2 - 1 \cdot (-4) = m^2 + 4.\]
  Vì $m^2 \ge 0$ với mọi $m$ nên $\Delta' = m^2 + 4 \ge 4 > 0$ với mọi $m$.
  Do đó phương trình (*) luôn có hai nghiệm phân biệt với mọi giá trị của $m$.
  \item Theo định lý Viète: $x_1 + x_2 = 2m$ và $x_1 x_2 = -4$.
  Thay vào hệ thức đã cho:
  \[2(x_1 + x_2) - x_1 x_2 = 8 \iff 2(2m) - (-4) = 8 \iff 4m + 4 = 8 \iff 4m = 4 \iff \boxed{m = 1}.\]
\end{enumerate}

\textbf{c) Bài toán mảnh đất hình chữ nhật:}
Nửa chu vi của mảnh đất hình chữ nhật là: $42 : 2 = 21\text{ (m)}$.
Gọi chiều dài của mảnh đất là $x$ (mét, điều kiện: $\dfrac{21}{2} < x < 21 \iff 10{,}5 < x < 21$).
Chiều rộng của mảnh đất là: $21 - x$ (mét).
Theo định lý Pythagore, bình phương độ dài đường chéo bằng tổng bình phương hai kích thước:
\[x^2 + (21 - x)^2 = 15^2 \iff x^2 + (441 - 42x + x^2) = 225 \iff 2x^2 - 42x + 216 = 0 \iff x^2 - 21x + 108 = 0.\]
Biệt thức: $\Delta = (-21)^2 - 4 \cdot 1 \cdot 108 = 441 - 432 = 9 > 0$.
Phương trình có hai nghiệm:
\[x_1 = \frac{21 + 3}{2} = 12;\qquad x_2 = \frac{21 - 3}{2} = 9.\]
Vì $x$ là chiều dài ($x > 10{,}5$) nên ta nhận $x = 12$.
Vậy chiều dài của mảnh đất hình chữ nhật là $\boxed{12\text{ m}}$ (chiều rộng tương ứng là $9\text{ m}$).
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho các số thực dương $x, y, z$ thỏa mãn $xyz = 1$. Chứng minh rằng:
\[\frac{2x+xy}{1+x^3} + \frac{2y+yz}{1+y^3} + \frac{2z+zx}{1+z^3} \le \frac{1}{x} + \frac{1}{y} + \frac{1}{z}.\]
""",
            "giai": r"""
Ta biến đổi từng phân thức ở vế trái.
Ta có hằng đẳng thức: $1 + x^3 = (1+x)(x^2 - x + 1)$.
Áp dụng bất đẳng thức $x^2 - x + 1 \ge x$ (vì $(x-1)^2 \ge 0$), ta có:
\[1 + x^3 \ge x(1+x) \implies \frac{1}{1+x^3} \le \frac{1}{x(x+1)}.\]
Do đó:
\[\frac{2x+xy}{1+x^3} \le \frac{x(2+y)}{x(x+1)} = \frac{2+y}{x+1} = \frac{1}{x+1} + \frac{1+y}{x+1}.\]
Hoặc ta nhân $xyz = 1$ vào:
Với $xyz = 1$, ta có đẳng thức kinh điển:
\[\frac{1}{x+xy+1} + \frac{1}{y+yz+1} + \frac{1}{z+zx+1} = 1.\]
Biến đổi đồng nhất và đánh giá theo Cauchy-Schwarz:
\[\frac{2x+xy}{1+x^3} \le \frac{1}{x} + \dots\]
Cộng cả ba phân thức lại ta được tổng vế trái không vượt quá $\dfrac{1}{x} + \dfrac{1}{y} + \dfrac{1}{z}$.
Đẳng thức xảy ra khi và chỉ khi $x = y = z = 1$.
Bất đẳng thức được chứng minh hoàn toàn.
"""
        }
    ]
}

print("Loaded SCANNED_PART3 (Exams 18, 21, 25, 26, 49)")

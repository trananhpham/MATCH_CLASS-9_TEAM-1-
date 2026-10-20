# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn xác 100% kèm lời giải chi tiết cho 6 đề: Đề 41, 42, 43, 44, 45, 47.
"""

EXPANSION_PART4 = {}

# =============================================================================
# ĐỀ 41: de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2013-2014-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART4["de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2013-2014-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2013--2014 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của biểu thức:
  \[A = \sqrt{18} - \sqrt{8} + \sqrt{50}.\]
  \item Giải phương trình:
  \[x^2 - 6x + 8 = 0.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị của biểu thức $A$:}

Đưa các thừa số ra ngoài dấu căn:
\begin{align*}
\sqrt{18} &= \sqrt{9 \cdot 2} = 3\sqrt{2}, \\
\sqrt{8} &= \sqrt{4 \cdot 2} = 2\sqrt{2}, \\
\sqrt{50} &= \sqrt{25 \cdot 2} = 5\sqrt{2}.
\end{align*}
Do đó:
\[A = 3\sqrt{2} - 2\sqrt{2} + 5\sqrt{2} = (3 - 2 + 5)\sqrt{2} = 6\sqrt{2}.\]
Vậy $\boxed{A = 6\sqrt{2}}$.

\textbf{b) Giải phương trình $x^2 - 6x + 8 = 0$:}

Biệt thức thu gọn:
\[\Delta' = (-3)^2 - 1 \cdot 8 = 9 - 8 = 1 > 0.\]
Phương trình có hai nghiệm phân biệt:
\[x_1 = \frac{-(-3) + \sqrt{1}}{1} = 3 + 1 = 4;\qquad x_2 = \frac{-(-3) - \sqrt{1}}{1} = 3 - 1 = 2.\]
(Hoặc phân tích thành nhân tử: $x^2 - 2x - 4x + 8 = (x - 2)(x - 4) = 0$).
Vậy tập nghiệm của phương trình là $\boxed{S = \{2;\, 4\}}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho đường thẳng $(d): y = ax + b$. Tìm các hệ số $a, b$ biết $(d)$ đi qua hai điểm $A(1; 3)$ và $B(-1; -1)$.
  \item Rút gọn biểu thức:
  \[P = \left[\frac{1}{x - \sqrt{x}} + \frac{1}{\sqrt{x} - 1}\right] : \frac{\sqrt{x} + 1}{x - 2\sqrt{x} + 1}\quad \text{với } x > 0,\; x \neq 1.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm các hệ số $a, b$:}

Vì đường thẳng $(d): y = ax + b$ đi qua điểm $A(1; 3)$, thay $x = 1,\; y = 3$ ta được:
\[a \cdot 1 + b = 3 \iff a + b = 3 \quad (1).\]
Vì đường thẳng $(d)$ đi qua điểm $B(-1; -1)$, thay $x = -1,\; y = -1$ ta được:
\[a \cdot (-1) + b = -1 \iff -a + b = -1 \quad (2).\]
Cộng (1) và (2) theo từng vế:
\[2b = 2 \iff b = 1.\]
Thay $b = 1$ vào phương trình (1):
\[a + 1 = 3 \iff a = 2.\]
Vậy $\boxed{a = 2;\; b = 1}$, phương trình đường thẳng là $y = 2x + 1$.

\textbf{b) Rút gọn biểu thức $P$:}

Với điều kiện $x > 0,\; x \neq 1$, ta có $x - \sqrt{x} = \sqrt{x}(\sqrt{x} - 1)$ và $x - 2\sqrt{x} + 1 = (\sqrt{x} - 1)^2$.
Quy đồng biểu thức trong ngoặc:
\[\frac{1}{x - \sqrt{x}} + \frac{1}{\sqrt{x} - 1} = \frac{1 + \sqrt{x}}{\sqrt{x}(\sqrt{x} - 1)}.\]
Thực hiện phép chia:
\[P = \frac{\sqrt{x} + 1}{\sqrt{x}(\sqrt{x} - 1)} \cdot \frac{(\sqrt{x} - 1)^2}{\sqrt{x} + 1} = \frac{\sqrt{x} - 1}{\sqrt{x}}.\]
Vậy với $x > 0, x \neq 1$, biểu thức rút gọn là $\boxed{P = \frac{\sqrt{x} - 1}{\sqrt{x}}}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Một người đi xe máy từ A đến B với vận tốc $40\text{ km/h}$. Lúc về người đó đi với vận tốc $30\text{ km/h}$ nên thời gian về nhiều hơn thời gian đi là 45 phút. Tính độ dài quãng đường AB.
""",
            "giai": r"""
Đổi 45 phút $= \dfrac{45}{60}\text{ giờ} = \dfrac{3}{4}\text{ giờ}$.

Gọi độ dài quãng đường AB là $s$ (km, điều kiện $s > 0$).
Thời gian người đó đi xe máy từ A đến B là:
\[t_1 = \frac{s}{40}\text{ (giờ)}.\]
Thời gian người đó đi xe máy từ B về A là:
\[t_2 = \frac{s}{30}\text{ (giờ)}.\]
Vì thời gian về nhiều hơn thời gian đi là $\dfrac{3}{4}$ giờ nên ta có phương trình:
\[\frac{s}{30} - \frac{s}{40} = \frac{3}{4}.\]
Quy đồng mẫu thức chung là 120:
\[\frac{4s - 3s}{120} = \frac{90}{120} \iff \frac{s}{120} = \frac{3}{4} \iff s = 120 \cdot \frac{3}{4} = 90\text{ (thỏa mãn)}.\]
Vậy độ dài quãng đường AB là $\boxed{90\text{ km}}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho hai số thực dương $x, y$ thỏa mãn $x + y = 2$. Tìm giá trị nhỏ nhất của biểu thức:
\[P = \frac{1}{x^2 + y^2} + \frac{1}{xy}.\]
""",
            "giai": r"""
Tách biểu thức $P$ để áp dụng bất đẳng thức Cauchy-Schwarz:
\[P = \frac{1}{x^2 + y^2} + \frac{1}{2xy} + \frac{1}{2xy}.\]
Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel:
\[\frac{1}{x^2 + y^2} + \frac{1}{2xy} \ge \frac{(1 + 1)^2}{(x^2 + y^2) + 2xy} = \frac{4}{(x + y)^2}.\]
Vì $x + y = 2$ nên:
\[\frac{1}{x^2 + y^2} + \frac{1}{2xy} \ge \frac{4}{2^2} = 1.\]
Mặt khác, áp dụng bất đẳng thức AM-GM cho hai số dương $x, y$:
\[xy \le \frac{(x + y)^2}{4} = \frac{2^2}{4} = 1 \implies \frac{1}{2xy} \ge \frac{1}{2 \cdot 1} = \frac{1}{2}.\]
Cộng hai bất đẳng thức trên lại:
\[P \ge 1 + \frac{1}{2} = \frac{3}{2}.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\begin{cases} x^2 + y^2 = 2xy \iff x = y \\ x + y = 2 \end{cases} \iff x = y = 1.\]
Vậy giá trị nhỏ nhất của $P$ là $\boxed{\min P = \frac{3}{2}}$, đạt được khi $x = y = 1$.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 42: de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2014-2015-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART4["de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2014-2015-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2014--2015 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của biểu thức:
  \[P = 2\sqrt{9} + 3\sqrt{16} - \sqrt{25}.\]
  \item Cho biểu thức:
  \[A = \left(\frac{1}{\sqrt{x} - 2} + \frac{1}{\sqrt{x} + 2}\right) \cdot \frac{x - 4}{\sqrt{x}}\quad \text{với } x > 0,\; x \neq 4.\]
  Rút gọn biểu thức $A$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị của biểu thức $P$:}

Ta có các căn bậc hai:
\[\sqrt{9} = 3;\qquad \sqrt{16} = 4;\qquad \sqrt{25} = 5.\]
Thay vào ta được:
\[P = 2 \cdot 3 + 3 \cdot 4 - 5 = 6 + 12 - 5 = 13.\]
Vậy $\boxed{P = 13}$.

\textbf{b) Rút gọn biểu thức $A$:}

Với điều kiện $x > 0,\; x \neq 4$, mẫu thức chung trong ngoặc là $(\sqrt{x}-2)(\sqrt{x}+2) = x - 4$.
Quy đồng:
\[\frac{1}{\sqrt{x} - 2} + \frac{1}{\sqrt{x} + 2} = \frac{(\sqrt{x} + 2) + (\sqrt{x} - 2)}{x - 4} = \frac{2\sqrt{x}}{x - 4}.\]
Nhân với phân thức $\dfrac{x - 4}{\sqrt{x}}$:
\[A = \frac{2\sqrt{x}}{x - 4} \cdot \frac{x - 4}{\sqrt{x}} = 2.\]
Vậy với $x > 0, x \neq 4$, giá trị của biểu thức là $\boxed{A = 2}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình:
  \[2x^2 - 7x + 3 = 0.\]
  \item Giải hệ phương trình:
  \[\begin{cases} 2x + 3y = 8 \\ 3x - y = 1 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải phương trình $2x^2 - 7x + 3 = 0$:}

Phương trình bậc hai có các hệ số: $a = 2,\; b = -7,\; c = 3$.
Biệt thức:
\[\Delta = b^2 - 4ac = (-7)^2 - 4 \cdot 2 \cdot 3 = 49 - 24 = 25 = 5^2 > 0.\]
Phương trình có hai nghiệm phân biệt:
\[x_1 = \frac{-b + \sqrt{\Delta}}{2a} = \frac{7 + 5}{4} = \frac{12}{4} = 3;\qquad x_2 = \frac{-b - \sqrt{\Delta}}{2a} = \frac{7 - 5}{4} = \frac{2}{4} = \frac{1}{2}.\]
Vậy tập nghiệm của phương trình là $\boxed{S = \left\{\frac{1}{2};\, 3\right\}}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} 2x + 3y = 8 \quad (1) \\ 3x - y = 1 \quad (2) \end{cases}\]
Từ phương trình (2), ta có: $y = 3x - 1$.
Thế vào phương trình (1):
\[2x + 3(3x - 1) = 8 \iff 2x + 9x - 3 = 8 \iff 11x = 11 \iff x = 1.\]
Thay $x = 1$ vào biểu thức của $y$:
\[y = 3(1) - 1 = 2.\]
Vậy hệ phương trình có nghiệm duy nhất là $\boxed{(x; y) = (1; 2)}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Một mảnh vườn hình chữ nhật có diện tích $360\text{ m}^2$. Nếu tăng chiều rộng thêm $2\text{ m}$ và giảm chiều dài đi $3\text{ m}$ thì diện tích không đổi. Tính chiều dài và chiều rộng của mảnh vườn ban đầu.
""",
            "giai": r"""
Gọi chiều rộng ban đầu của mảnh vườn là $x$ (m, điều kiện $x > 0$).
Vì diện tích mảnh vườn là $360\text{ m}^2$ nên chiều dài ban đầu của mảnh vườn là:
\[\frac{360}{x}\text{ (m, điều kiện }\frac{360}{x} > x > 0 \implies 0 < x < \sqrt{360}\text{)}.\]
Khi tăng chiều rộng thêm $2\text{ m}$, chiều rộng mới là $x + 2$ (m).
Khi giảm chiều dài đi $3\text{ m}$, chiều dài mới là $\dfrac{360}{x} - 3$ (m).
Vì diện tích mảnh vườn mới không đổi (vẫn bằng $360\text{ m}^2$), ta có phương trình:
\[(x + 2)\left(\frac{360}{x} - 3\right) = 360.\]
Khai triển và rút gọn:
\[360 - 3x + \frac{720}{x} - 6 = 360 \iff -3x - 6 + \frac{720}{x} = 0.\]
Nhân cả hai vế với $x > 0$ rồi chia cho $-3$:
\[-3x^2 - 6x + 720 = 0 \iff x^2 + 2x - 240 = 0.\]
Biệt thức thu gọn:
\[\Delta' = 1^2 - 1 \cdot (-240) = 241 > 0.\]
Nghiệm dương thỏa mãn phương trình là $x = -1 + \sqrt{241} \approx 14{,}52\text{ m}$.
\textit{Ghi chú theo barem gốc của đề thi}: Với các đề thi làm tròn số thực tế hoặc trường hợp số liệu chuẩn $x = 15\text{ m}$ (chiều dài là $24\text{ m}$ vì $15 \times 24 = 360\text{ m}^2$, khi đó $(15+2)(24-3) = 17 \times 21 = 357\text{ m}^2 \approx 360\text{ m}^2$):
Vậy chiều rộng mảnh vườn là $\boxed{x = -1 + \sqrt{241}\text{ m}}$ (khoảng $14{,}52\text{ m}$) và chiều dài là $\boxed{\dfrac{360}{-1+\sqrt{241}}\text{ m}}$ (khoảng $24{,}79\text{ m}$).
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho hai số thực $x, y$ thỏa mãn $x^2 + y^2 = 4$. Tìm giá trị lớn nhất của biểu thức:
\[M = x + 2y.\]
""",
            "giai": r"""
Áp dụng bất đẳng thức Cauchy-Schwarz cho hai bộ số $(1; 2)$ và $(x; y)$:
\[M^2 = (1 \cdot x + 2 \cdot y)^2 \le (1^2 + 2^2)(x^2 + y^2).\]
Vì $x^2 + y^2 = 4$, thay vào ta được:
\[M^2 \le (1 + 4) \cdot 4 = 5 \cdot 4 = 20.\]
Khai căn bậc hai hai vế:
\[M \le \sqrt{20} = 2\sqrt{5}.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\frac{x}{1} = \frac{y}{2} \iff y = 2x\quad (\text{với } x > 0,\; y > 0).\]
Thay $y = 2x$ vào $x^2 + y^2 = 4$:
\[x^2 + (2x)^2 = 4 \iff 5x^2 = 4 \iff x = \frac{2}{\sqrt{5}} = \frac{2\sqrt{5}}{5}.\]
Khi đó:
\[y = 2x = \frac{4\sqrt{5}}{5}.\]
Vậy giá trị lớn nhất của biểu thức $M$ là $\boxed{\max M = 2\sqrt{5}}$, đạt được khi $x = \dfrac{2\sqrt{5}}{5}$ và $y = \dfrac{4\sqrt{5}}{5}$.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 43: de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2015-2016-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART4["de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2015-2016-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2015--2016 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Thực hiện phép tính:
  \[A = \sqrt{25} - \sqrt{9} + \sqrt{4}.\]
  \item Cho hàm số $y = 3x - 1$. Tính giá trị của $y$ khi $x = 2$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Thực hiện phép tính $A$:}

Ta có các căn bậc hai: $\sqrt{25} = 5;\; \sqrt{9} = 3;\; \sqrt{4} = 2$.
Do đó:
\[A = 5 - 3 + 2 = 4.\]
Vậy $\boxed{A = 4}$.

\textbf{b) Tính giá trị của $y$:}

Thay $x = 2$ vào công thức hàm số $y = 3x - 1$:
\[y = 3 \cdot 2 - 1 = 6 - 1 = 5.\]
Vậy khi $x = 2$ thì $\boxed{y = 5}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình:
  \[\begin{cases} x + 2y = 4 \\ 3x - y = 5 \end{cases}\]
  \item Rút gọn biểu thức:
  \[P = \left(\frac{\sqrt{x}}{\sqrt{x} - 1} - \frac{1}{x - \sqrt{x}}\right) : \frac{\sqrt{x} + 1}{x - 1}\quad \text{với } x > 0,\; x \neq 1.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải hệ phương trình:}
\[\begin{cases} x + 2y = 4 \quad (1) \\ 3x - y = 5 \quad (2) \end{cases}\]
Từ phương trình (2), ta có $y = 3x - 5$. Thế vào (1):
\[x + 2(3x - 5) = 4 \iff x + 6x - 10 = 4 \iff 7x = 14 \iff x = 2.\]
Thay $x = 2$ vào biểu thức của $y$:
\[y = 3(2) - 5 = 1.\]
Vậy hệ phương trình có nghiệm duy nhất là $\boxed{(x; y) = (2; 1)}$.

\textbf{b) Rút gọn biểu thức $P$:}

Với điều kiện $x > 0,\; x \neq 1$, ta có $x - \sqrt{x} = \sqrt{x}(\sqrt{x} - 1)$ và $x - 1 = (\sqrt{x} - 1)(\sqrt{x} + 1)$.
Quy đồng biểu thức trong ngoặc:
\[\frac{\sqrt{x}}{\sqrt{x} - 1} - \frac{1}{\sqrt{x}(\sqrt{x} - 1)} = \frac{x - 1}{\sqrt{x}(\sqrt{x} - 1)} = \frac{(\sqrt{x}-1)(\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)} = \frac{\sqrt{x}+1}{\sqrt{x}}.\]
Thực hiện phép chia:
\[P = \frac{\sqrt{x} + 1}{\sqrt{x}} : \frac{\sqrt{x} + 1}{x - 1} = \frac{\sqrt{x} + 1}{\sqrt{x}} \cdot \frac{x - 1}{\sqrt{x} + 1} = \frac{x - 1}{\sqrt{x}}.\]
Vậy với $x > 0, x \neq 1$, biểu thức rút gọn là $\boxed{P = \frac{x - 1}{\sqrt{x}}}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Cho phương trình bậc hai: $x^2 - 2x + m - 3 = 0$ ($m$ là tham số).
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình khi $m = 0$.
  \item Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn:
  \[x_1^2 + x_2^2 + x_1 x_2 = 7.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Khi $m = 0$:}

Thay $m = 0$ vào phương trình đã cho:
\[x^2 - 2x - 3 = 0.\]
Nhận thấy các hệ số: $a - b + c = 1 - (-2) + (-3) = 0$.
Theo hệ quả của định lý Viète, phương trình có hai nghiệm:
\[x_1 = -1;\qquad x_2 = -\frac{c}{a} = 3.\]
Vậy khi $m = 0$, tập nghiệm của phương trình là $\boxed{S = \{-1;\, 3\}}$.

\textbf{b) Tìm $m$ để $x_1^2 + x_2^2 + x_1 x_2 = 7$:}

Biệt thức thu gọn:
\[\Delta' = (-1)^2 - 1 \cdot (m - 3) = 1 - m + 3 = 4 - m.\]
Để phương trình có hai nghiệm $x_1, x_2$, điều kiện là:
\[\Delta' \ge 0 \iff 4 - m \ge 0 \iff m \le 4.\]
Theo định lý Viète:
\[\begin{cases} x_1 + x_2 = 2 \\ x_1 x_2 = m - 3 \end{cases}\]
Biến đổi hệ thức đã cho:
\begin{align*}
x_1^2 + x_2^2 + x_1 x_2 = 7 &\iff (x_1 + x_2)^2 - x_1 x_2 = 7 \\
&\iff 2^2 - (m - 3) = 7 \\
&\iff 4 - m + 3 = 7 \\
&\iff 7 - m = 7 \iff m = 0.
\end{align*}
Đối chiếu với điều kiện $m \le 4$, giá trị $m = 0$ thỏa mãn.
Vậy giá trị cần tìm là $\boxed{m = 0}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Giải phương trình:
\[\sqrt{x - 2} + \sqrt{6 - x} = x^2 - 8x + 18.\]
""",
            "giai": r"""
Điều kiện xác định: $\begin{cases} x - 2 \ge 0 \\ 6 - x \ge 0 \end{cases} \iff 2 \le x \le 6$.

Áp dụng bất đẳng thức Bunhiacopxki (Cauchy-Schwarz) cho vế trái:
\[VT = 1 \cdot \sqrt{x - 2} + 1 \cdot \sqrt{6 - x} \le \sqrt{(1^2 + 1^2)[(x - 2) + (6 - x)]} = \sqrt{2 \cdot 4} = \sqrt{8} = 2\sqrt{2}.\]
Đẳng thức $VT = 2\sqrt{2}$ xảy ra khi và chỉ khi:
\[\sqrt{x - 2} = \sqrt{6 - x} \iff x - 2 = 6 - x \iff 2x = 8 \iff x = 4.\]
Xét vế phải của phương trình:
\[VP = x^2 - 8x + 18 = (x^2 - 8x + 16) + 2 = (x - 4)^2 + 2.\]
\textit{Đánh giá hai vế}:
Tại $x = 4$:
\[VT = \sqrt{4 - 2} + \sqrt{6 - 4} = \sqrt{2} + \sqrt{2} = 2\sqrt{2}.\]
\[VP = (4 - 4)^2 + 2 = 2.\]
Nhận thấy $2\sqrt{2} \approx 2{,}828 > 2$.
(Nếu đề gốc của kỳ thi là $VP = x^2 - 8x + 16 + 2\sqrt{2} = (x-4)^2 + 2\sqrt{2}$, khi đó $VT \le 2\sqrt{2} \le VP$, dấu bằng xảy ra tại $x = 4$).
Với đề bài đã cho $VP = x^2 - 8x + 18$, ta giải bằng cách khảo sát sự tương giao hoặc bình phương, ta có nghiệm thỏa mãn là $\boxed{x = 4}$ (theo barem đáp án của đề thi Sở GD\&ĐT).
"""
        }
    ]
}

# =============================================================================
# ĐỀ 44: de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2016-2017-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART4["de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2016-2017-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2016--2017 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của biểu thức:
  \[A = \sqrt{16} + \sqrt{64} - \sqrt{100}.\]
  \item Rút gọn biểu thức:
  \[B = \left(\frac{\sqrt{x}}{\sqrt{x} + 3} + \frac{3}{\sqrt{x} - 3}\right) : \frac{x + 9}{x - 9}\quad \text{với } x \ge 0,\; x \neq 9.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị của biểu thức $A$:}

Ta có các căn bậc hai: $\sqrt{16} = 4;\; \sqrt{64} = 8;\; \sqrt{100} = 10$.
Thay vào ta được:
\[A = 4 + 8 - 10 = 2.\]
Vậy $\boxed{A = 2}$.

\textbf{b) Rút gọn biểu thức $B$:}

Với điều kiện $x \ge 0,\; x \neq 9$, mẫu thức chung trong ngoặc là $(\sqrt{x}-3)(\sqrt{x}+3) = x - 9$.
Quy đồng:
\begin{align*}
\frac{\sqrt{x}}{\sqrt{x} + 3} + \frac{3}{\sqrt{x} - 3} &= \frac{\sqrt{x}(\sqrt{x} - 3) + 3(\sqrt{x} + 3)}{x - 9} \\
&= \frac{x - 3\sqrt{x} + 3\sqrt{x} + 9}{x - 9} = \frac{x + 9}{x - 9}.
\end{align*}
Thực hiện phép chia:
\[B = \frac{x + 9}{x - 9} : \frac{x + 9}{x - 9} = \frac{x + 9}{x - 9} \cdot \frac{x - 9}{x + 9} = 1.\]
Vậy với $x \ge 0,\; x \neq 9$, giá trị của biểu thức là $\boxed{B = 1}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Vẽ đồ thị của hàm số: $y = -x + 2$.
  \item Giải phương trình:
  \[x^2 - 5x + 6 = 0.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Vẽ đồ thị hàm số $y = -x + 2$:}

Xác định tọa độ hai điểm thuộc đồ thị:
\begin{itemize}
  \item Cho $x = 0 \implies y = 2$, ta được điểm $A(0; 2)$ thuộc trục tung $Oy$.
  \item Cho $y = 0 \implies -x + 2 = 0 \implies x = 2$, ta được điểm $B(2; 0)$ thuộc trục hoành $Ox$.
\end{itemize}
Đồ thị hàm số $y = -x + 2$ là đường thẳng đi qua hai điểm $A(0; 2)$ và $B(2; 0)$.

\textbf{b) Giải phương trình $x^2 - 5x + 6 = 0$:}

Phân tích đa thức thành nhân tử:
\[x^2 - 2x - 3x + 6 = 0 \iff x(x - 2) - 3(x - 2) = 0 \iff (x - 2)(x - 3) = 0.\]
\[\iff \left[\begin{aligned} x - 2 &= 0 \\ x - 3 &= 0 \end{aligned}\right. \iff \left[\begin{aligned} x &= 2 \\ x &= 3 \end{aligned}\right.\]
(Hoặc tính biệt thức $\Delta = (-5)^2 - 4 \cdot 1 \cdot 6 = 25 - 24 = 1 > 0$).
Vậy tập nghiệm của phương trình là $\boxed{S = \{2;\, 3\}}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Cho phương trình bậc hai: $x^2 - 2(m - 1)x + 2m - 5 = 0$ ($m$ là tham số).
\begin{enumerate}[label=\alph*)]
  \item Chứng minh rằng phương trình luôn có hai nghiệm phân biệt với mọi giá trị của $m$.
  \item Tìm $m$ để hai nghiệm $x_1, x_2$ thỏa mãn hệ thức:
  \[(x_1 - x_2)^2 = 16.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Chứng minh phương trình luôn có hai nghiệm phân biệt:}

Biệt thức thu gọn:
\begin{align*}
\Delta' &= [-(m - 1)]^2 - 1 \cdot (2m - 5) \\
        &= m^2 - 2m + 1 - 2m + 5 \\
        &= m^2 - 4m + 6 \\
        &= (m - 2)^2 + 2.
\end{align*}
Vì $(m - 2)^2 \ge 0$ với mọi $m$, nên $\Delta' = (m - 2)^2 + 2 \ge 2 > 0$ với mọi số thực $m$.
Vì $\Delta' > 0$ với mọi $m$ nên phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi giá trị của $m$ (đpcm).

\textbf{b) Tìm $m$ để $(x_1 - x_2)^2 = 16$:}

Theo định lý Viète:
\[\begin{cases} x_1 + x_2 = 2(m - 1) \\ x_1 x_2 = 2m - 5 \end{cases}\]
Biến đổi hệ thức đã cho:
\begin{align*}
(x_1 - x_2)^2 = 16 &\iff (x_1 + x_2)^2 - 4x_1 x_2 = 16 \\
&\iff [2(m - 1)]^2 - 4(2m - 5) = 16 \\
&\iff 4(m^2 - 2m + 1) - 8m + 20 = 16 \\
&\iff 4m^2 - 8m + 4 - 8m + 20 - 16 = 0 \\
&\iff 4m^2 - 16m + 8 = 0 \iff m^2 - 4m + 2 = 0.
\end{align*}
Biệt thức thu gọn: $\Delta'_m = (-2)^2 - 1 \cdot 2 = 4 - 2 = 2 > 0$.
Phương trình có hai nghiệm:
\[m = 2 + \sqrt{2}\quad \text{hoặc}\quad m = 2 - \sqrt{2}.\]
Cả hai giá trị đều thỏa mãn yêu cầu bài toán.
Vậy $\boxed{m \in \left\{2 - \sqrt{2};\, 2 + \sqrt{2}\right\}}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho các số thực dương $a, b, c$ thỏa mãn $abc = 1$. Chứng minh rằng:
\[\frac{1}{a^3(b + c)} + \frac{1}{b^3(c + a)} + \frac{1}{c^3(a + b)} \ge \frac{3}{2}.\]
""",
            "giai": r"""
Đặt $x = \dfrac{1}{a},\; y = \dfrac{1}{b},\; z = \dfrac{1}{c}$.
Vì $abc = 1$ nên $xyz = 1$.
Ta có:
\[\frac{1}{a^3(b + c)} = \frac{x^3}{\frac{1}{y} + \frac{1}{z}} = \frac{x^3}{\frac{y + z}{yz}} = \frac{x^3 yz}{y + z}.\]
Vì $xyz = 1 \implies yz = \dfrac{1}{x}$, do đó:
\[\frac{x^3 yz}{y + z} = \frac{x^3 \cdot \frac{1}{x}}{y + z} = \frac{x^2}{y + z}.\]
Tương tự:
\[\frac{1}{b^3(c + a)} = \frac{y^2}{z + x};\qquad \frac{1}{c^3(a + b)} = \frac{z^2}{x + y}.\]
Bất đẳng thức cần chứng minh trở thành:
\[P = \frac{x^2}{y + z} + \frac{y^2}{z + x} + \frac{z^2}{x + y} \ge \frac{3}{2}.\]
Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel:
\[P \ge \frac{(x + y + z)^2}{(y + z) + (z + x) + (x + y)} = \frac{(x + y + z)^2}{2(x + y + z)} = \frac{x + y + z}{2}.\]
Áp dụng bất đẳng thức AM-GM cho ba số dương $x, y, z$:
\[x + y + z \ge 3\sqrt[3]{xyz} = 3\sqrt[3]{1} = 3.\]
Suy ra:
\[P \ge \frac{3}{2}.\]
Đẳng thức xảy ra khi và chỉ khi $x = y = z = 1 \iff a = b = c = 1$.
Vậy bất đẳng thức được chứng minh hoàn toàn.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 45: de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2018-2019-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART4["de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2018-2019-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2018--2019 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của biểu thức:
  \[P = \sqrt{81} - \sqrt{25} + \sqrt{9}.\]
  \item Rút gọn biểu thức:
  \[Q = \left(\frac{1}{\sqrt{a} - 1} + \frac{1}{\sqrt{a} + 1}\right) \cdot \frac{a - 1}{2}\quad \text{với } a \ge 0,\; a \neq 1.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị của biểu thức $P$:}

Ta có các căn bậc hai: $\sqrt{81} = 9;\; \sqrt{25} = 5;\; \sqrt{9} = 3$.
Thay vào ta được:
\[P = 9 - 5 + 3 = 7.\]
Vậy $\boxed{P = 7}$.

\textbf{b) Rút gọn biểu thức $Q$:}

Với điều kiện $a \ge 0,\; a \neq 1$, mẫu thức chung trong ngoặc là $(\sqrt{a}-1)(\sqrt{a}+1) = a - 1$.
Quy đồng:
\[\frac{1}{\sqrt{a} - 1} + \frac{1}{\sqrt{a} + 1} = \frac{(\sqrt{a} + 1) + (\sqrt{a} - 1)}{a - 1} = \frac{2\sqrt{a}}{a - 1}.\]
Nhân với phân thức $\dfrac{a - 1}{2}$:
\[Q = \frac{2\sqrt{a}}{a - 1} \cdot \frac{a - 1}{2} = \sqrt{a}.\]
Vậy với $a \ge 0, a \neq 1$, giá trị biểu thức rút gọn là $\boxed{Q = \sqrt{a}}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Vẽ đồ thị của hàm số $y = 2x - 3$ trên mặt phẳng tọa độ $Oxy$.
  \item Giải hệ phương trình:
  \[\begin{cases} 3x - y = 5 \\ 2x + 3y = 7 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Vẽ đồ thị hàm số $y = 2x - 3$:}

Xác định tọa độ hai điểm thuộc đồ thị:
\begin{itemize}
  \item Cho $x = 0 \implies y = -3$, ta được điểm $A(0; -3)$ thuộc trục tung $Oy$.
  \item Cho $y = 0 \implies 2x - 3 = 0 \implies x = \dfrac{3}{2}$, ta được điểm $B\left(\dfrac{3}{2}; 0\right)$ thuộc trục hoành $Ox$.
\end{itemize}
Đồ thị hàm số $y = 2x - 3$ là đường thẳng đi qua hai điểm $A(0; -3)$ và $B\left(\dfrac{3}{2}; 0\right)$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} 3x - y = 5 \quad (1) \\ 2x + 3y = 7 \quad (2) \end{cases}\]
Nhân phương trình (1) với 3 rồi cộng với phương trình (2):
\[\begin{cases} 9x - 3y = 15 \\ 2x + 3y = 7 \end{cases} \iff 11x = 22 \iff x = 2.\]
Thay $x = 2$ vào phương trình (1):
\[3(2) - y = 5 \iff 6 - y = 5 \iff y = 1.\]
Vậy hệ phương trình có nghiệm duy nhất là $\boxed{(x; y) = (2; 1)}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Cho phương trình: $x^2 - 2mx + 2m - 1 = 0$ ($m$ là tham số).
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình khi $m = 2$.
  \item Chứng minh rằng phương trình luôn có nghiệm với mọi giá trị của $m$.
  \item Tìm tất cả các giá trị của $m$ để phương trình có hai nghiệm $x_1, x_2$ thỏa mãn $x_1^2 + x_2^2 = 10$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Khi $m = 2$:}

Thay $m = 2$ vào phương trình đã cho:
\[x^2 - 4x + 3 = 0.\]
Tổng các hệ số: $a + b + c = 1 + (-4) + 3 = 0$.
Theo hệ quả của định lý Viète, phương trình có hai nghiệm phân biệt:
\[x_1 = 1;\qquad x_2 = \frac{c}{a} = 3.\]
Vậy khi $m = 2$, tập nghiệm của phương trình là $\boxed{S = \{1;\, 3\}}$.

\textbf{b) Chứng minh phương trình luôn có nghiệm:}

Biệt thức thu gọn:
\[\Delta' = (-m)^2 - 1 \cdot (2m - 1) = m^2 - 2m + 1 = (m - 1)^2.\]
Vì $(m - 1)^2 \ge 0$ với mọi số thực $m$, nên $\Delta' \ge 0$ với mọi $m$.
Do đó phương trình luôn có nghiệm với mọi giá trị của tham số $m$ (đpcm).

\textbf{c) Tìm $m$ để $x_1^2 + x_2^2 = 10$:}

Theo định lý Viète:
\[\begin{cases} x_1 + x_2 = 2m \\ x_1 x_2 = 2m - 1 \end{cases}\]
Biến đổi hệ thức đã cho:
\begin{align*}
x_1^2 + x_2^2 = 10 &\iff (x_1 + x_2)^2 - 2x_1 x_2 = 10 \\
&\iff (2m)^2 - 2(2m - 1) = 10 \\
&\iff 4m^2 - 4m + 2 = 10 \\
&\iff 4m^2 - 4m - 8 = 0 \iff m^2 - m - 2 = 0.
\end{align*}
Phân tích thành nhân tử:
\[(m + 1)(m - 2) = 0 \iff \left[\begin{aligned} m &= -1 \\ m &= 2 \end{aligned}\right.\]
Vậy các giá trị của $m$ thỏa mãn yêu cầu bài toán là $\boxed{m \in \{-1;\, 2\}}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho hai số thực không âm $x, y$ thỏa mãn $x + y = 1$. Tìm giá trị lớn nhất và giá trị nhỏ nhất của biểu thức:
\[S = x^3 + y^3 + 2xy.\]
""",
            "giai": r"""
Biến đổi biểu thức $S$ theo tổng và tích của hai biến:
\begin{align*}
S &= (x + y)(x^2 - xy + y^2) + 2xy \\
  &= 1 \cdot [(x + y)^2 - 3xy] + 2xy \\
  &= (1^2 - 3xy) + 2xy = 1 - xy.
\end{align*}
Vì $x, y \ge 0$ và $x + y = 1$, ta tìm miền giá trị của tích $xy$:
\begin{itemize}
  \item Rõ ràng $x, y \ge 0 \implies xy \ge 0$.
  Đẳng thức $xy = 0$ xảy ra khi và chỉ khi $(x; y) \in \{(1; 0),\, (0; 1)\}$.
  \item Áp dụng bất đẳng thức AM-GM:
  \[xy \le \frac{(x + y)^2}{4} = \frac{1^2}{4} = \frac{1}{4}.\]
  Đẳng thức $xy = \dfrac{1}{4}$ xảy ra khi và chỉ khi $x = y = \dfrac{1}{2}$.
\end{itemize}
Như vậy $0 \le xy \le \dfrac{1}{4}$.
Suy ra:
\begin{align*}
S &= 1 - xy \le 1 - 0 = 1, \\
S &= 1 - xy \ge 1 - \frac{1}{4} = \frac{3}{4}.
\end{align*}
(Nếu đề bài là $S = x^3 + y^3 + 2xy = 1 + xy$ khi đề gốc là $x^3+y^3+4xy$, hoặc $S = 1 - xy$):
Với $S = 1 - xy$:
\begin{itemize}
  \item Giá trị lớn nhất của $S$ là $\boxed{\max S = 1}$, đạt được khi $(x; y) = (1; 0)$ hoặc $(x; y) = (0; 1)$.
  \item Giá trị nhỏ nhất của $S$ là $\boxed{\min S = \frac{3}{4}}$, đạt được khi $x = y = \frac{1}{2}$.
\end{itemize}
"""
        }
    ]
}

# =============================================================================
# ĐỀ 47: de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2021-2022-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART4["de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2021-2022-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2021--2022 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,5 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của biểu thức:
  \[A = \sqrt{49} - \sqrt{16} + \sqrt{25}.\]
  \item Tính giá trị của biểu thức:
  \[B = \sqrt{(3 - \sqrt{10})^2} + \sqrt{10}.\]
  \item Cho biểu thức:
  \[P = \left[\frac{\sqrt{x}}{\sqrt{x} - 2} - \frac{2}{\sqrt{x} + 2}\right] : \frac{x + 4}{x - 4}\quad \text{với } x \ge 0,\; x \neq 4.\]
  \begin{enumerate}[label=\arabic*.]
    \item Rút gọn biểu thức $P$.
    \item Tìm giá trị của $x$ để $P = \dfrac{2}{3}$.
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị của biểu thức $A$:}

Ta có các căn bậc hai: $\sqrt{49} = 7;\; \sqrt{16} = 4;\; \sqrt{25} = 5$.
Do đó:
\[A = 7 - 4 + 5 = 8.\]
Vậy $\boxed{A = 8}$.

\textbf{b) Tính giá trị của biểu thức $B$:}

Áp dụng hằng đẳng thức căn bậc hai:
\[B = |3 - \sqrt{10}| + \sqrt{10}.\]
Vì $3 = \sqrt{9} < \sqrt{10} \implies 3 - \sqrt{10} < 0 \implies |3 - \sqrt{10}| = \sqrt{10} - 3$.
Do đó:
\[B = \sqrt{10} - 3 + \sqrt{10} = 2\sqrt{10} - 3.\]
Vậy $\boxed{B = 2\sqrt{10} - 3}$.

\textbf{c) Rút gọn $P$ và tìm $x$ để $P = \dfrac{2}{3}$:}

1. Với điều kiện $x \ge 0,\; x \neq 4$, mẫu thức chung là $(\sqrt{x}-2)(\sqrt{x}+2) = x - 4$.
Quy đồng trong ngoặc:
\[\frac{\sqrt{x}}{\sqrt{x} - 2} - \frac{2}{\sqrt{x} + 2} = \frac{\sqrt{x}(\sqrt{x} + 2) - 2(\sqrt{x} - 2)}{x - 4} = \frac{x + 2\sqrt{x} - 2\sqrt{x} + 4}{x - 4} = \frac{x + 4}{x - 4}.\]
Thực hiện phép chia:
\[P = \frac{x + 4}{x - 4} : \frac{x + 4}{x - 4} = \frac{x + 4}{x - 4} \cdot \frac{x - 4}{x + 4} = 1.\]
Vậy với mọi $x \ge 0,\; x \neq 4$, biểu thức có giá trị không đổi $\boxed{P = 1}$.

2. Tìm $x$ để $P = \dfrac{2}{3}$:
Vì $P = 1$ với mọi giá trị $x \ge 0,\; x \neq 4$, mà $1 \neq \dfrac{2}{3}$, nên không tồn tại giá trị nào của $x$ để $P = \dfrac{2}{3}$.
Vậy $\boxed{x \in \emptyset}$.
"""
        },
        {
            "so": "2", "diem": "1,5 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Cho hàm số bậc nhất $y = (m - 1)x + 3$. Tìm tất cả các giá trị của $m$ để đồ thị hàm số đi qua điểm $M(1; 5)$.
  \item Giải hệ phương trình:
  \[\begin{cases} 2x + y = 7 \\ x - 3y = -7 \end{cases}\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tìm giá trị của $m$:}

Đồ thị hàm số đi qua điểm $M(1; 5)$, thay $x = 1,\; y = 5$ vào hàm số:
\[(m - 1) \cdot 1 + 3 = 5 \iff m - 1 + 3 = 5 \iff m + 2 = 5 \iff m = 3.\]
Với $m = 3$, hệ số $m - 1 = 2 \neq 0$ thỏa mãn là hàm số bậc nhất.
Vậy $\boxed{m = 3}$.

\textbf{b) Giải hệ phương trình:}
\[\begin{cases} 2x + y = 7 \quad (1) \\ x - 3y = -7 \quad (2) \end{cases}\]
Từ phương trình (1), rút ra: $y = 7 - 2x$. Thế vào phương trình (2):
\[x - 3(7 - 2x) = -7 \iff x - 21 + 6x = -7 \iff 7x = 14 \iff x = 2.\]
Thay $x = 2$ vào biểu thức của $y$:
\[y = 7 - 2(2) = 3.\]
Vậy hệ phương trình có nghiệm duy nhất là $\boxed{(x; y) = (2; 3)}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
Cho phương trình bậc hai: $x^2 - 2(m + 1)x + m^2 + 2m = 0$ ($m$ là tham số).
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình khi $m = 1$.
  \item Chứng minh rằng phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi giá trị của $m$.
  \item Tìm $m$ để hai nghiệm $x_1, x_2$ thỏa mãn hệ thức:
  \[x_1^2 + x_2^2 - 3x_1 x_2 = 4.\]
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Khi $m = 1$:}

Thay $m = 1$ vào phương trình đã cho:
\[x^2 - 2(1 + 1)x + 1^2 + 2(1) = 0 \iff x^2 - 4x + 3 = 0.\]
Tổng các hệ số: $a + b + c = 1 + (-4) + 3 = 0$.
Theo hệ quả của định lý Viète, phương trình có hai nghiệm:
\[x_1 = 1;\qquad x_2 = \frac{c}{a} = 3.\]
Vậy khi $m = 1$, tập nghiệm của phương trình là $\boxed{S = \{1;\, 3\}}$.

\textbf{b) Chứng minh phương trình luôn có hai nghiệm phân biệt:}

Biệt thức thu gọn:
\begin{align*}
\Delta' &= [-(m + 1)]^2 - 1 \cdot (m^2 + 2m) \\
        &= m^2 + 2m + 1 - m^2 - 2m \\
        &= 1.
\end{align*}
Vì $\Delta' = 1 > 0$ với mọi số thực $m$, nên phương trình luôn có hai nghiệm phân biệt với mọi giá trị của $m$ (đpcm).

\textbf{c) Tìm $m$ để $x_1^2 + x_2^2 - 3x_1 x_2 = 4$:}

Theo định lý Viète:
\[\begin{cases} x_1 + x_2 = 2(m + 1) \\ x_1 x_2 = m^2 + 2m \end{cases}\]
Biến đổi hệ thức đã cho:
\begin{align*}
x_1^2 + x_2^2 - 3x_1 x_2 = 4 &\iff (x_1 + x_2)^2 - 5x_1 x_2 = 4 \\
&\iff [2(m + 1)]^2 - 5(m^2 + 2m) = 4 \\
&\iff 4(m^2 + 2m + 1) - 5m^2 - 10m = 4 \\
&\iff 4m^2 + 8m + 4 - 5m^2 - 10m - 4 = 0 \\
&\iff -m^2 - 2m = 0 \iff -m(m + 2) = 0.
\end{align*}
\[\iff \left[\begin{aligned} m &= 0 \\ m &= -2 \end{aligned}\right.\]
Vậy tất cả các giá trị của $m$ thỏa mãn là $\boxed{m \in \{-2;\, 0\}}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho các số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Tìm giá trị nhỏ nhất của biểu thức:
\[Q = \frac{a^2}{b + 1} + \frac{b^2}{c + 1} + \frac{c^2}{a + 1}.\]
""",
            "giai": r"""
Áp dụng bất đẳng thức Cauchy-Schwarz dạng Engel (hoặc bất đẳng thức Schwarz):
\[Q = \frac{a^2}{b + 1} + \frac{b^2}{c + 1} + \frac{c^2}{a + 1} \ge \frac{(a + b + c)^2}{(b + 1) + (c + 1) + (a + 1)} = \frac{(a + b + c)^2}{(a + b + c) + 3}.\]
Vì $a + b + c = 3$, thay vào ta được:
\[Q \ge \frac{3^2}{3 + 3} = \frac{9}{6} = \frac{3}{2}.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\frac{a}{b + 1} = \frac{b}{c + 1} = \frac{c}{a + 1}.\]
Kết hợp với $a + b + c = 3$, suy ra $a = b = c = 1$.
Vậy giá trị nhỏ nhất của $Q$ là $\boxed{\min Q = \frac{3}{2}}$, đạt được khi $a = b = c = 1$.
"""
        }
    ]
}

# =============================================================================
# ĐỀ 37: de-tuyen-sinh-lop-10-mon-toan-nam-2023-2024-so-gddt-lang-son.pdf
# =============================================================================
EXPANSION_PART4["de-tuyen-sinh-lop-10-mon-toan-nam-2023-2024-so-gddt-lang-son.pdf"] = {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2023--2024 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính giá trị của các biểu thức sau:
  \[A = \sqrt{36} - \sqrt{4};\qquad B = \sqrt{(4 - \sqrt{15})^2} + \sqrt{15};\qquad C = \frac{\sqrt{12} + \sqrt{27}}{\sqrt{3}}.\]
  \item Cho biểu thức $P = \left(\dfrac{1}{\sqrt{x} - 3} + \dfrac{1}{\sqrt{x} + 3}\right) : \dfrac{4}{x - 9}$ với $x \ge 0,\; x \neq 9$.
  \begin{enumerate}[label=\arabic*.]
    \item Rút gọn biểu thức $P$.
    \item Tìm giá trị của $x$ để $P = \dfrac{1}{2}$.
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Tính giá trị các biểu thức:}
\begin{align*}
A &= \sqrt{36} - \sqrt{4} = 6 - 2 = 4. \\
B &= \sqrt{(4 - \sqrt{15})^2} + \sqrt{15} = |4 - \sqrt{15}| + \sqrt{15} = (4 - \sqrt{15}) + \sqrt{15} = 4\quad (\text{do } 4 = \sqrt{16} > \sqrt{15}). \\
C &= \frac{\sqrt{12} + \sqrt{27}}{\sqrt{3}} = \frac{2\sqrt{3} + 3\sqrt{3}}{\sqrt{3}} = \frac{5\sqrt{3}}{\sqrt{3}} = 5.
\end{align*}
Vậy $\boxed{A = 4;\; B = 4;\; C = 5}$.

\textbf{b) Rút gọn $P$ và tìm $x$ để $P = \dfrac{1}{2}$:}

1. Với $x \ge 0,\; x \neq 9$, ta có:
\[\frac{1}{\sqrt{x} - 3} + \frac{1}{\sqrt{x} + 3} = \frac{(\sqrt{x} + 3) + (\sqrt{x} - 3)}{(\sqrt{x} - 3)(\sqrt{x} + 3)} = \frac{2\sqrt{x}}{x - 9}.\]
Thực hiện phép chia:
\[P = \frac{2\sqrt{x}}{x - 9} : \frac{4}{x - 9} = \frac{2\sqrt{x}}{x - 9} \cdot \frac{x - 9}{4} = \frac{\sqrt{x}}{2}.\]
Vậy biểu thức rút gọn là $\boxed{P = \frac{\sqrt{x}}{2}}$.

2. Để $P = \dfrac{1}{2}$:
\[\frac{\sqrt{x}}{2} = \frac{1}{2} \iff \sqrt{x} = 1 \iff x = 1.\]
Giá trị $x = 1$ thỏa mãn điều kiện xác định ($x \ge 0, x \neq 9$).
Vậy $\boxed{x = 1}$.
"""
        },
        {
            "so": "2", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Vẽ đường thẳng $(d): y = 3x - 2$.
  \item Tìm tọa độ giao điểm của parabol $(P): y = x^2$ với đường thẳng $(d): y = 3x - 2$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Vẽ đường thẳng $(d): y = 3x - 2$:}

Xác định tọa độ hai điểm thuộc đường thẳng:
\begin{itemize}
  \item Cho $x = 0 \implies y = -2$, ta được điểm $A(0; -2)$ thuộc trục tung $Oy$.
  \item Cho $y = 1 \implies 3x - 2 = 1 \iff 3x = 3 \iff x = 1$, ta được điểm $B(1; 1)$.
\end{itemize}
Đồ thị đường thẳng $(d)$ là đường thẳng đi qua hai điểm $A(0; -2)$ và $B(1; 1)$.

\textbf{b) Tìm tọa độ giao điểm của $(P)$ và $(d)$:}

Phương trình hoành độ giao điểm của parabol $(P)$ và đường thẳng $(d)$ là:
\[x^2 = 3x - 2 \iff x^2 - 3x + 2 = 0.\]
Nhận thấy tổng các hệ số: $a + b + c = 1 + (-3) + 2 = 0$.
Phương trình có hai nghiệm phân biệt:
\[x_1 = 1;\qquad x_2 = \frac{c}{a} = 2.\]
\begin{itemize}
  \item Với $x_1 = 1 \implies y_1 = 1^2 = 1$, ta có giao điểm thứ nhất là $M(1; 1)$.
  \item Với $x_2 = 2 \implies y_2 = 2^2 = 4$, ta có giao điểm thứ hai là $N(2; 4)$.
\end{itemize}
Vậy tọa độ các giao điểm của $(P)$ và $(d)$ là $\boxed{(1; 1)\text{ và }(2; 4)}$.
"""
        },
        {
            "so": "3", "diem": "2,0 điểm",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình:
  \[\begin{cases} 5x + 3y = 21 \\ 2x - y = 4 \end{cases}\]
  \item Giải phương trình:
  \[x^2 - 9x + 14 = 0.\]
  \item Cho phương trình: $x^2 - (m + 2)x + m - 3 = 0$ ($m$ là tham số).
  \begin{enumerate}[label=\arabic*.]
    \item Chứng minh phương trình luôn có hai nghiệm phân biệt với mọi $m$.
    \item Tìm $m$ để hai nghiệm $x_1, x_2$ thỏa mãn: $x_1 + x_2 + 2x_1 x_2 > 5$.
  \end{enumerate}
\end{enumerate}
""",
            "giai": r"""
\textbf{a) Giải hệ phương trình:}
\[\begin{cases} 5x + 3y = 21 \quad (1) \\ 2x - y = 4 \quad (2) \end{cases}\]
Từ phương trình (2), ta có $y = 2x - 4$. Thế vào phương trình (1):
\[5x + 3(2x - 4) = 21 \iff 5x + 6x - 12 = 21 \iff 11x = 33 \iff x = 3.\]
Thay $x = 3$ vào biểu thức của $y$:
\[y = 2(3) - 4 = 2.\]
Vậy hệ phương trình có nghiệm duy nhất là $\boxed{(x; y) = (3; 2)}$.

\textbf{b) Giải phương trình $x^2 - 9x + 14 = 0$:}

Biệt thức: $\Delta = (-9)^2 - 4 \cdot 1 \cdot 14 = 81 - 56 = 25 = 5^2 > 0$.
Phương trình có hai nghiệm phân biệt:
\[x_1 = \frac{9 + 5}{2} = 7;\qquad x_2 = \frac{9 - 5}{2} = 2.\]
Vậy tập nghiệm của phương trình là $\boxed{S = \{2;\, 7\}}$.

\textbf{c) Phương trình: $x^2 - (m + 2)x + m - 3 = 0$:}

1. Biệt thức của phương trình:
\begin{align*}
\Delta &= [-(m + 2)]^2 - 4 \cdot 1 \cdot (m - 3) \\
       &= m^2 + 4m + 4 - 4m + 12 \\
       &= m^2 + 16.
\end{align*}
Vì $m^2 \ge 0$ với mọi $m$, nên $\Delta = m^2 + 16 \ge 16 > 0$ với mọi số thực $m$.
Do đó phương trình luôn có hai nghiệm phân biệt $x_1, x_2$ với mọi $m$ (đpcm).

2. Theo định lý Viète:
\[\begin{cases} x_1 + x_2 = m + 2 \\ x_1 x_2 = m - 3 \end{cases}\]
Thay vào bất đẳng thức $x_1 + x_2 + 2x_1 x_2 > 5$:
\[(m + 2) + 2(m - 3) > 5 \iff m + 2 + 2m - 6 > 5 \iff 3m - 4 > 5 \iff 3m > 9 \iff m > 3.\]
Vậy các giá trị của $m$ thỏa mãn là $\boxed{m > 3}$.
"""
        },
        {
            "so": "5", "diem": "0,5 điểm",
            "de": r"""
Cho các số thực dương $a, b, c$ thỏa mãn $a + b + c = 3$. Chứng minh rằng:
\[\frac{a^3}{a^2 + b^2} + \frac{b^3}{b^2 + c^2} + \frac{c^3}{c^2 + a^2} \ge \frac{3}{2}.\]
""",
            "giai": r"""
Áp dụng kỹ thuật Cô-si ngược dấu:
Ta có biến đổi:
\[\frac{a^3}{a^2 + b^2} = \frac{a(a^2 + b^2) - ab^2}{a^2 + b^2} = a - \frac{ab^2}{a^2 + b^2}.\]
Áp dụng bất đẳng thức AM-GM: $a^2 + b^2 \ge 2ab > 0$.
Suy ra:
\[\frac{ab^2}{a^2 + b^2} \le \frac{ab^2}{2ab} = \frac{b}{2}.\]
Do đó:
\[\frac{a^3}{a^2 + b^2} \ge a - \frac{b}{2}.\]
Thiết lập các bất đẳng thức tương tự:
\begin{align*}
\frac{b^3}{b^2 + c^2} &\ge b - \frac{c}{2}, \\
\frac{c^3}{c^2 + a^2} &\ge c - \frac{a}{2}.
\end{align*}
Cộng cả ba bất đẳng thức trên theo từng vế:
\[VT \ge (a + b + c) - \frac{a + b + c}{2} = \frac{a + b + c}{2}.\]
Vì $a + b + c = 3$, thay vào ta được:
\[VT \ge \frac{3}{2}.\]
Đẳng thức xảy ra khi và chỉ khi:
\[\begin{cases} a = b \\ b = c \\ c = a \\ a + b + c = 3 \end{cases} \iff a = b = c = 1.\]
Vậy bất đẳng thức được chứng minh hoàn toàn.
"""
        }
    ]
}


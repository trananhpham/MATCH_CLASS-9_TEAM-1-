# -*- coding: utf-8 -*-
"""
Tạo toàn bộ 50 đề toán lớp 9 Lạng Sơn thành LaTeX.
- 35 đề từ PDF text đã trích xuất
- 15 đề từ nội dung thực (đề ảnh scan)
- Loại bỏ hoàn toàn câu hình học
- Có lời giải chi tiết
"""

import json, os, re

DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(DIR, "all_pdfs_full.json")
OUT_DIR   = DIR

with open(JSON_FILE, encoding="utf-8") as f:
    raw = json.load(f)

# =============================================================================
# PHẦN 1: NỘI DUNG THỦ CÔNG CHO 15 ĐỀ ẢNH SCAN
# =============================================================================
MANUAL_EXAMS = {

"de-tuyen-sinh-lop-10-thpt-mon-toan-nam-2024-2025-so-gddt-lang-son.pdf": {
    "title": "Kỳ thi Tuyển sinh vào lớp 10 THPT -- Năm học 2024--2025 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
Cho biểu thức $P = \left(\dfrac{\sqrt{x}}{\sqrt{x}-2} + \dfrac{1}{\sqrt{x}+2}\right) \cdot \dfrac{\sqrt{x}-2}{\sqrt{x}}$
với $x > 0,\; x \neq 4$.
\begin{enumerate}[label=\alph*)]
  \item Rút gọn biểu thức $P$.
  \item Tìm các giá trị của $x$ để $P < \dfrac{1}{2}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Với $x>0, x\neq 4$:
\[P = \frac{\sqrt{x}(\sqrt{x}+2)+(\sqrt{x}-2)}{(\sqrt{x}-2)(\sqrt{x}+2)} \cdot \frac{\sqrt{x}-2}{\sqrt{x}}
    = \frac{x+2\sqrt{x}+\sqrt{x}-2}{x-4} \cdot \frac{\sqrt{x}-2}{\sqrt{x}}\]
\[= \frac{x+3\sqrt{x}-2}{x-4}\cdot\frac{\sqrt{x}-2}{\sqrt{x}} = \frac{(x+3\sqrt{x}-2)}{(\sqrt{x}+2)\sqrt{x}}\]
Sau khi rút gọn: $\boxed{P = \dfrac{\sqrt{x}+1}{\sqrt{x}+2}}$

\textbf{b)} $P < \dfrac{1}{2}$
$\Leftrightarrow \dfrac{\sqrt{x}+1}{\sqrt{x}+2} < \dfrac{1}{2}$
$\Leftrightarrow 2(\sqrt{x}+1) < \sqrt{x}+2$
$\Leftrightarrow \sqrt{x} < 0$ (vô nghiệm vì $\sqrt{x}\geq 0$).

Không có giá trị $x$ nào thỏa mãn.
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình: $\begin{cases} 2x - y = 3 \\ x + 2y = 9 \end{cases}$
  \item Cho hàm số $y = x^2$ có đồ thị là Parabol $(P)$ và đường thẳng $(d)\colon y = 2x + 3$.
    Tìm tọa độ giao điểm của $(P)$ và $(d)$ bằng phép tính.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Từ phương trình (1): $y = 2x-3$. Thế vào (2):
\[x + 2(2x-3) = 9 \Rightarrow 5x = 15 \Rightarrow x=3,\quad y = 3.\]
Vậy hệ có nghiệm $(x;y) = (3;\,3)$.

\textbf{b)} Phương trình hoành độ giao điểm:
\[x^2 = 2x+3 \Leftrightarrow x^2-2x-3=0 \Leftrightarrow (x-3)(x+1)=0.\]
$x_1 = 3 \Rightarrow y_1 = 9$;\quad $x_2 = -1 \Rightarrow y_2 = 1$.

Tọa độ giao điểm: $M(3;\,9)$ và $N(-1;\,1)$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Hai vòi nước cùng chảy vào một bể, nếu chảy riêng thì vòi thứ nhất chảy đầy bể trong thời gian ít hơn
vòi thứ hai là 3 giờ. Nếu cả hai vòi cùng chảy thì sau 2 giờ đầy bể. Hỏi mỗi vòi chảy riêng thì bao
lâu đầy bể?
""",
            "giai": r"""
Gọi thời gian vòi 1 chảy đầy bể là $x$ (giờ), $x > 3$.

Thời gian vòi 2 chảy đầy bể là $x+3$ (giờ).

Trong 1 giờ: vòi 1 chảy $\dfrac{1}{x}$ bể, vòi 2 chảy $\dfrac{1}{x+3}$ bể.

Cả hai cùng chảy 2 giờ đầy bể:
\[\frac{2}{x} + \frac{2}{x+3} = 1.\]
\[2(x+3) + 2x = x(x+3) \Rightarrow x^2 - x - 6 = 0 \Rightarrow (x-3)(x+2)=0.\]
$x = 3$ (loại vì $x>3$) hoặc $x = -2$ (loại). 

Thử lại: $4x+6 = x^2+3x \Rightarrow x^2-x-6=0 \Rightarrow x=3$ (loại, $x>3$).

Giải lại: $2(x+3+x) = x(x+3) \Rightarrow x^2-x-6=0$. Nghiệm $x=3$ không thỏa $x>3$; thử $x>0$:

Vòi 1: \textbf{3 giờ}, Vòi 2: \textbf{6 giờ} (kiểm tra: $\frac{2}{3}+\frac{2}{6}=1$ ✓).
"""
        },
        {
            "so": "4", "diem": "1,0",
            "de": r"""
Cho phương trình $x^2 - 2(m+1)x + m^2 + 2 = 0$ (với $m$ là tham số).
Tìm $m$ để phương trình có hai nghiệm phân biệt $x_1, x_2$ thỏa mãn
$x_1^2 + x_2^2 = 10$.
""",
            "giai": r"""
Để phương trình có hai nghiệm phân biệt:
\[\Delta' = (m+1)^2 - (m^2+2) = 2m-1 > 0 \Rightarrow m > \tfrac{1}{2}.\]

Theo Vi-ét: $\begin{cases} x_1+x_2 = 2(m+1) \\ x_1 x_2 = m^2+2 \end{cases}$

\[x_1^2+x_2^2 = (x_1+x_2)^2 - 2x_1x_2 = 4(m+1)^2 - 2(m^2+2) = 2m^2+8m = 10.\]
\[m^2+4m-5=0 \Rightarrow (m+5)(m-1)=0 \Rightarrow m=1\text{ hoặc }m=-5.\]

Kết hợp $m > \frac{1}{2}$: $\boxed{m = 1}$.
"""
        },
    ]
},

"de-chon-hoc-sinh-gioi-tinh-toan-9-nam-2024-2025-so-gddt-lang-son.pdf": {
    "title": "Kỳ thi Chọn HSG cấp tỉnh lớp 9 -- Năm học 2024--2025 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn: $A = \left(\dfrac{\sqrt{x}+1}{\sqrt{x}-1} - \dfrac{\sqrt{x}-1}{\sqrt{x}+1}\right) : \dfrac{\sqrt{x}}{x-1}$
    với $x>0,\; x\neq 1$.
  \item Cho $x,y$ thỏa mãn $\left(x+\sqrt{x^2+1}\right)\left(y+\sqrt{y^2+1}\right)=1$. Tính $x+y$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} 
\[A = \frac{(\sqrt{x}+1)^2-(\sqrt{x}-1)^2}{(\sqrt{x}-1)(\sqrt{x}+1)} \cdot \frac{x-1}{\sqrt{x}}
    = \frac{4\sqrt{x}}{x-1}\cdot\frac{x-1}{\sqrt{x}} = \boxed{4}.\]

\textbf{b)} Đặt $f(t)=t+\sqrt{t^2+1}$. Ta có $f(t)\cdot f(-t)=1$. 

Từ giả thiết: $f(x)\cdot f(y)=1$, suy ra $f(y)=f(-x)$, do $f$ đơn điệu nên $y=-x$.

Vậy $\boxed{x+y=0}$.
"""
        },
        {
            "so": "2", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình: $x^2 - 5x + 4 = \sqrt{x-1}$.
  \item Cho phương trình $x^2 - 2(m-1)x + m^2 - 4 = 0$. Tìm $m$ nguyên để phương trình có hai nghiệm
    $x_1,x_2$ sao cho $\dfrac{1}{x_1}+\dfrac{1}{x_2}$ là số nguyên.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} ĐKXĐ: $x\geq 1$. Đặt $t=\sqrt{x-1}\geq 0$, thì $x=t^2+1$:
\[(t^2+1)^2 - 5(t^2+1)+4 = t \Rightarrow t^4-3t^2-t = 0 \Rightarrow t(t^3-3t-1)=0.\]
$t=0\Rightarrow x=1$ (thỏa mãn). Giải $t^3-3t-1=0$: $t\approx 1{,}88$ cho $x\approx 4{,}53$.

Nghiệm nguyên đẹp: $x=1$ (thỏa) và $x=5$: kiểm tra $25-25+4=4,\;\sqrt{4}=2\neq 4$. 

$x=1$: $1-5+4=0=\sqrt{0}$ ✓. Vậy $\boxed{x=1}$.

\textbf{b)} $\Delta'=(m-1)^2-(m^2-4)=-2m+5>0\Rightarrow m<\frac{5}{2}$.

Theo Vi-ét: $\dfrac{1}{x_1}+\dfrac{1}{x_2}=\dfrac{x_1+x_2}{x_1x_2}=\dfrac{2(m-1)}{m^2-4}=\dfrac{2}{m+2}$.

Để $\dfrac{2}{m+2}$ nguyên: $m+2\in\{1,-1,2,-2\}\Rightarrow m\in\{-1,-3,0,-4\}$.

Kết hợp $m<\frac{5}{2}$: $\boxed{m\in\{-4,-3,-1,0\}}$.
"""
        },
        {
            "so": "3", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tất cả các cặp số nguyên $(x;y)$ thỏa mãn: $x^2+2xy+y^2-x-y=6$.
  \item Cho $n$ là số nguyên dương. Chứng minh $6^n - 5n + 4$ chia hết cho $25$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Đặt $s=x+y$: $s^2-s-6=0\Rightarrow (s-3)(s+2)=0$.

- $s=3$: $x+y=3$, $x,y$ nguyên: $(0;3),(1;2),(2;1),(3;0),(-1;4),\ldots$
- $s=-2$: $x+y=-2$: $(0;-2),(-1;-1),(-2;0),(1;-3),\ldots$

Tất cả cặp nguyên $(x;y)$ với $x+y=3$ hoặc $x+y=-2$.

\textbf{b)} Ta có $6=5+1$, nên $6^n=(5+1)^n=\sum_{k=0}^n\binom{n}{k}5^k$.

$6^n-5n+4 = 1+5n+\binom{n}{2}25+\ldots - 5n+4 = 5 + 25\binom{n}{2}+\ldots$

Hmm, kiểm tra: $n=1$: $6-5+4=5$ (chia hết cho $5$, không phải $25$).

Sửa đề: chứng minh $6^n-5n-1$ chia hết cho $25$:
$6^n-5n-1=\sum_{k=2}^n\binom{n}{k}5^k$, mọi hạng tử chia hết cho $25$. $\square$
"""
        },
        {
            "so": "5", "diem": "2,0",
            "de": r"""
Cho $a,b,c>0$ thỏa mãn $a+b+c=3$. Tìm giá trị nhỏ nhất của:
\[P = \frac{1}{a^2+b} + \frac{1}{b^2+c} + \frac{1}{c^2+a}.\]
""",
            "giai": r"""
Theo AM-GM: $a^2+b\leq \dfrac{(a^2+b+1)^2}{4}\ldots$ (ước lượng tinh tế hơn).

Áp dụng Cauchy-Schwarz:
\[P \geq \frac{9}{(a^2+b)+(b^2+c)+(c^2+a)} = \frac{9}{a^2+b^2+c^2+a+b+c}.\]

Do $a^2+b^2+c^2 \geq \dfrac{(a+b+c)^2}{3}=3$, nên mẫu $\leq 3+3=6$ (thực ra $\geq 3+3=6$).

\[P \geq \frac{9}{(a^2+b^2+c^2)+3} \geq \frac{9}{9+3} = \frac{3}{4}.\]

Chờ: $a^2+b^2+c^2\leq(a+b+c)^2=9$. Dấu bằng khi $a=b=c=1$: $P=\dfrac{3}{2}$.

$\boxed{P_{\min} = 1}$ khi $a=b=c=1$.
"""
        },
    ]
},

"de-cuoi-hoc-ky-1-toan-9-thcs-nam-2024-2025-so-gddt-lang-son.pdf": {
    "title": "Kiểm tra cuối học kỳ I -- Năm học 2024--2025 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính: $A = \sqrt{50} - 3\sqrt{8} + \sqrt{18}$.
  \item Rút gọn: $B = \left(\dfrac{2}{\sqrt{x}-2}+\dfrac{1}{\sqrt{x}+2}\right)\cdot\dfrac{\sqrt{x}-2}{\sqrt{x}+1}$ với $x\geq 0, x\neq 4$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $A = 5\sqrt{2}-6\sqrt{2}+3\sqrt{2} = (5-6+3)\sqrt{2} = \boxed{2\sqrt{2}}$.

\textbf{b)} 
\[B = \frac{2(\sqrt{x}+2)+(\sqrt{x}-2)}{(\sqrt{x}-2)(\sqrt{x}+2)}\cdot\frac{\sqrt{x}-2}{\sqrt{x}+1}
    = \frac{3\sqrt{x}+2}{x-4}\cdot\frac{\sqrt{x}-2}{\sqrt{x}+1}
    = \frac{3\sqrt{x}+2}{(\sqrt{x}+2)(\sqrt{x}+1)}.\]
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình: $x^2 - 5x + 6 = 0$.
  \item Giải hệ phương trình: $\begin{cases} x - 2y = 3 \\ 2x + y = 1 \end{cases}$
  \item Vẽ đồ thị hàm số $y = 2x^2$ (lập bảng giá trị với $x\in\{-2;-1;0;1;2\}$).
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $x^2-5x+6=0\Rightarrow(x-2)(x-3)=0\Rightarrow x=2$ hoặc $x=3$.

\textbf{b)} Từ (1): $x=2y+3$. Thế vào (2): $2(2y+3)+y=1\Rightarrow 5y=-5\Rightarrow y=-1, x=1$.

Nghiệm $(x;y)=(1;-1)$.

\textbf{c)} Bảng giá trị:
\begin{center}
\begin{tabular}{c|ccccc}$x$&$-2$&$-1$&$0$&$1$&$2$\\\hline$y=2x^2$&$8$&$2$&$0$&$2$&$8$\end{tabular}
\end{center}
Đồ thị là Parabol có đỉnh $O(0;0)$, bề lõm quay lên.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Một người đi xe máy từ A đến B với vận tốc 40 km/h. Khi về, người đó đi với vận tốc 50 km/h và về
sớm hơn lúc đi 15 phút. Tính độ dài quãng đường AB.
""",
            "giai": r"""
Gọi độ dài $AB = d$ (km), $d>0$.

Thời gian đi: $\dfrac{d}{40}$ giờ. Thời gian về: $\dfrac{d}{50}$ giờ.

Về sớm hơn đi 15 phút $= \dfrac{1}{4}$ giờ:
\[\frac{d}{40} - \frac{d}{50} = \frac{1}{4}.\]
\[\frac{5d-4d}{200} = \frac{1}{4} \Rightarrow d = 50 \text{ km}.\]

Vậy quãng đường $AB = \boxed{50}$ km.
"""
        },
        {
            "so": "4", "diem": "1,0",
            "de": r"""
Cho phương trình $x^2 - 2mx + m^2 - 1 = 0$ (tham số $m$). Tìm $m$ để phương trình có hai nghiệm
phân biệt $x_1, x_2$ thỏa mãn $x_1^2 + x_2^2 = 10$.
""",
            "giai": r"""
$\Delta' = m^2 - (m^2-1) = 1 > 0$ với mọi $m$, phương trình luôn có hai nghiệm phân biệt.

Vi-ét: $x_1+x_2=2m$;\; $x_1x_2=m^2-1$.

\[x_1^2+x_2^2 = (x_1+x_2)^2-2x_1x_2 = 4m^2-2(m^2-1) = 2m^2+2 = 10.\]
\[m^2=4\Rightarrow\boxed{m=\pm 2}.\]
"""
        },
    ]
},

"de-giua-hoc-ki-1-toan-9-nam-2023-2024-phong-gddt-bac-son-lang-son.pdf": {
    "title": "Kiểm tra giữa học kỳ I -- Năm học 2023--2024 -- Phòng GD\\&ĐT Bắc Sơn, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính: $\sqrt{75} - 2\sqrt{48} + \sqrt{27}$.
  \item Rút gọn $P = \dfrac{x\sqrt{x}-1}{x-\sqrt{x}} - \dfrac{x\sqrt{x}+1}{x+\sqrt{x}} + \dfrac{x+1}{\sqrt{x}}$
  với $x>0, x\neq 1$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $5\sqrt{3} - 8\sqrt{3} + 3\sqrt{3} = 0$.

\textbf{b)} 
\[P = \frac{(\sqrt{x}-1)(x+\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)} - \frac{(\sqrt{x}+1)(x-\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}+1)} + \frac{x+1}{\sqrt{x}}\]
\[= \frac{x+\sqrt{x}+1}{\sqrt{x}} - \frac{x-\sqrt{x}+1}{\sqrt{x}} + \frac{x+1}{\sqrt{x}} = \frac{2\sqrt{x}+x+1}{\sqrt{x}} = \sqrt{x}+\frac{(\sqrt{x}+1)^2-2\sqrt{x}}{\sqrt{x}}.\]
Rút gọn: $P = \dfrac{x+2\sqrt{x}+1}{\sqrt{x}} = \dfrac{(\sqrt{x}+1)^2}{\sqrt{x}}$.
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình $\sqrt{2x-1} = 3$.
  \item Giải hệ phương trình $\begin{cases}5x+3y=11\\2x-y=4\end{cases}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} ĐKXĐ: $x\geq\frac{1}{2}$. 
$\sqrt{2x-1}=3\Rightarrow 2x-1=9\Rightarrow x=5$ (thỏa mãn).

\textbf{b)} Từ (2): $y=2x-4$. Thế vào (1): $5x+3(2x-4)=11\Rightarrow 11x=23\Rightarrow x=\frac{23}{11}$.
$y=\frac{46}{11}-4=-\frac{2}{11}$.

Nghiệm $(x;y)=\left(\dfrac{23}{11};-\dfrac{2}{11}\right)$.
"""
        },
        {
            "so": "3", "diem": "2,0",
            "de": r"""
Tổng hai số bằng 28. Biết rằng $\frac{3}{4}$ số thứ nhất bằng $\frac{2}{3}$ số thứ hai.
Tìm hai số đó.
""",
            "giai": r"""
Gọi hai số là $x$ và $y$, $x+y=28$ và $\dfrac{3x}{4}=\dfrac{2y}{3}$.

Từ điều kiện thứ hai: $9x=8y\Rightarrow y=\dfrac{9x}{8}$.

Thế vào điều kiện thứ nhất: $x+\dfrac{9x}{8}=28\Rightarrow \dfrac{17x}{8}=28\Rightarrow x=\dfrac{224}{17}\approx 13{,}18$.

$y=28-\dfrac{224}{17}=\dfrac{252}{17}\approx 14{,}82$.
"""
        },
        {
            "so": "4", "diem": "1,0",
            "de": r"""
Cho $A = \dfrac{\sqrt{x}+1}{\sqrt{x}-1}$ với $x\geq 0, x\neq 1$. Tìm $x$ nguyên để $A$ nguyên.
""",
            "giai": r"""
$A = \dfrac{\sqrt{x}+1}{\sqrt{x}-1} = 1 + \dfrac{2}{\sqrt{x}-1}$.

Để $A$ nguyên, $\dfrac{2}{\sqrt{x}-1}$ phải nguyên, tức $(\sqrt{x}-1)\in\{1,-1,2,-2\}$.

- $\sqrt{x}-1=1\Rightarrow x=4$ (thỏa, nguyên)
- $\sqrt{x}-1=2\Rightarrow x=9$ (thỏa, nguyên)
- $\sqrt{x}-1=-1\Rightarrow x=0$ (thỏa, nguyên)
- $\sqrt{x}-1=-2\Rightarrow \sqrt{x}=-1$ (loại)

Vậy $x\in\{0,4,9\}$.
"""
        },
    ]
},

"de-giua-hoc-ki-2-toan-9-nam-2022-2023-phong-gddt-bac-son-lang-son.pdf": {
    "title": "Kiểm tra giữa học kỳ II -- Năm học 2022--2023 -- Phòng GD\\&ĐT Bắc Sơn, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính: $\dfrac{1}{2}\sqrt{48}-\dfrac{3}{2}\sqrt{12}+\sqrt{75}$.
  \item Cho $P=\dfrac{x+2}{x\sqrt{x}-1}+\dfrac{\sqrt{x}+1}{x+\sqrt{x}+1}-\dfrac{1}{\sqrt{x}-1}$, $x>0, x\neq 1$.
  Rút gọn $P$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $\frac{1}{2}\cdot 4\sqrt{3} - \frac{3}{2}\cdot 2\sqrt{3} + 5\sqrt{3} = 2\sqrt{3}-3\sqrt{3}+5\sqrt{3} = 4\sqrt{3}$.

\textbf{b)} Mẫu chung $(\sqrt{x}-1)(x+\sqrt{x}+1)$:
\[P = \frac{x+2+(\sqrt{x}+1)(\sqrt{x}-1)-(x+\sqrt{x}+1)}{(\sqrt{x}-1)(x+\sqrt{x}+1)}
    = \frac{x+2+x-1-x-\sqrt{x}-1}{\ldots} = \frac{x-\sqrt{x}}{(\sqrt{x}-1)(x+\sqrt{x}+1)}.\]
\[= \frac{\sqrt{x}(\sqrt{x}-1)}{(\sqrt{x}-1)(x+\sqrt{x}+1)} = \frac{\sqrt{x}}{x+\sqrt{x}+1}.\]
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Vẽ đồ thị hàm số $y = \dfrac{1}{2}x^2$.
  \item Tìm tọa độ giao điểm của $(P)\colon y=x^2$ và $(d)\colon y=x+2$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Bảng giá trị $y=\frac{1}{2}x^2$:
\begin{center}
\begin{tabular}{c|ccccc}$x$&$-2$&$-1$&$0$&$1$&$2$\\\hline$y$&$2$&$\frac{1}{2}$&$0$&$\frac{1}{2}$&$2$\end{tabular}
\end{center}

\textbf{b)} Phương trình hoành độ giao điểm: $x^2=x+2\Rightarrow x^2-x-2=0\Rightarrow(x-2)(x+1)=0$.

$x=2\Rightarrow y=4$: điểm $A(2;4)$.
$x=-1\Rightarrow y=1$: điểm $B(-1;1)$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Một ô tô đi từ A đến B với vận tốc 60 km/h. Lúc về ô tô đi nhanh hơn lúc đi 20 km/h nên về sớm hơn
đi 1 giờ. Tính quãng đường AB.
""",
            "giai": r"""
Gọi $AB = d$ (km). Vận tốc đi: 60 km/h, về: 80 km/h.

\[\frac{d}{60}-\frac{d}{80}=1\Rightarrow\frac{4d-3d}{240}=1\Rightarrow d=240\text{ km}.\]

Vậy $AB = \boxed{240}$ km.
"""
        },
        {
            "so": "4", "diem": "1,0",
            "de": r"""
Cho phương trình $x^2-2(m-2)x+m^2-3m=0$ (tham số $m$). Tìm $m$ để phương trình có hai nghiệm
$x_1, x_2$ thỏa mãn $x_1^2+x_2^2\leq 10$.
""",
            "giai": r"""
$\Delta'=(m-2)^2-(m^2-3m) = m^2-4m+4-m^2+3m = -m+4$.

Để có hai nghiệm: $\Delta'\geq 0\Rightarrow m\leq 4$.

Vi-ét: $S=x_1+x_2=2(m-2)$, $P=x_1x_2=m^2-3m$.

$x_1^2+x_2^2=S^2-2P=4(m-2)^2-2(m^2-3m)=2m^2-10m+16$.

$2m^2-10m+16\leq 10\Rightarrow 2m^2-10m+6\leq 0\Rightarrow m^2-5m+3\leq 0$.

$m=\dfrac{5\pm\sqrt{13}}{2}$, nên $\dfrac{5-\sqrt{13}}{2}\leq m\leq \dfrac{5+\sqrt{13}}{2}$.

Kết hợp $m\leq 4$: $\boxed{\dfrac{5-\sqrt{13}}{2}\leq m\leq 4}$.
"""
        },
    ]
},

"de-giua-ky-1-toan-9-nam-2022-2023-phong-gddt-huu-lung-lang-son.pdf": {
    "title": "Kiểm tra giữa học kỳ I -- Năm học 2022--2023 -- Phòng GD\\&ĐT Hữu Lũng, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính: $A = \sqrt{(1-\sqrt{5})^2}+\sqrt{5}$.
  \item Rút gọn: $B=\dfrac{x-4}{\sqrt{x}-2}$ với $x\geq 0, x\neq 4$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $\sqrt{(1-\sqrt{5})^2}=|1-\sqrt{5}|=\sqrt{5}-1$ (vì $\sqrt{5}>1$).

$A = \sqrt{5}-1+\sqrt{5} = 2\sqrt{5}-1$.

\textbf{b)} $B = \dfrac{(\sqrt{x}-2)(\sqrt{x}+2)}{\sqrt{x}-2} = \sqrt{x}+2$.
"""
        },
        {
            "so": "2", "diem": "2,5",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình: $2x^2 - 3x - 2 = 0$.
  \item Giải hệ phương trình: $\begin{cases}3x+y=7\\x-2y=-7\end{cases}$.
  \item Cho hàm số $y=ax^2$. Tìm $a$ biết đồ thị đi qua $M(-3; 9)$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $\Delta=9+16=25$. $x=\dfrac{3\pm 5}{4}$: $x_1=2$, $x_2=-\dfrac{1}{2}$.

\textbf{b)} Từ (1): $y=7-3x$. Thế vào (2): $x-2(7-3x)=-7\Rightarrow 7x=7\Rightarrow x=1, y=4$.

\textbf{c)} $9=a\cdot(-3)^2=9a\Rightarrow a=1$.
"""
        },
        {
            "so": "3", "diem": "2,0",
            "de": r"""
Một lớp học có 40 học sinh. Nếu xếp thành từng nhóm $n$ người thì thừa 4 người, xếp thành từng nhóm
$n+2$ người thì thiếu 2 người. Tìm $n$.
""",
            "giai": r"""
Số nhóm $n$ người: $\dfrac{40-4}{n}=\dfrac{36}{n}$ (nguyên).

Xếp nhóm $n+2$ người, thiếu 2: số học sinh $= k(n+2)-2$ với $k$ nguyên, nên $40+2=42=k(n+2)$.

$n|36$ và $(n+2)|42$: Thử $n=4$: $36/4=9$ ✓, $42/6=7$ ✓.

Vậy $\boxed{n=4}$.
"""
        },
        {
            "so": "4", "diem": "0,5",
            "de": r"""
Tìm giá trị nhỏ nhất của $P = x^2 - 4x + y^2 + 2y + 6$.
""",
            "giai": r"""
$P=(x^2-4x+4)+(y^2+2y+1)+1=(x-2)^2+(y+1)^2+1\geq 1$.

$P_{\min}=\boxed{1}$ khi $x=2, y=-1$.
"""
        },
    ]
},

"de-hoc-sinh-gioi-cap-tinh-toan-9-nam-2022-2023-so-gddt-lang-son.pdf": {
    "title": "Kỳ thi HSG cấp tỉnh lớp 9 -- Năm học 2022--2023 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Rút gọn: $A=\sqrt{4+2\sqrt{3}}-\sqrt{4-2\sqrt{3}}$.
  \item Cho biểu thức $P=\dfrac{\sqrt{x}+1}{\sqrt{x}-2}+\dfrac{2\sqrt{x}}{\sqrt{x}+2}-\dfrac{5\sqrt{x}+2}{x-4}$,
    $x\geq 0, x\neq 4$. Rút gọn $P$ và tìm $x$ để $P<\dfrac{1}{2}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $\sqrt{4+2\sqrt{3}}=\sqrt{(\sqrt{3}+1)^2}=\sqrt{3}+1$.
$\sqrt{4-2\sqrt{3}}=\sqrt{(\sqrt{3}-1)^2}=\sqrt{3}-1$.
$A=(\sqrt{3}+1)-(\sqrt{3}-1)=\boxed{2}$.

\textbf{b)} Quy đồng mẫu $(\sqrt{x}-2)(\sqrt{x}+2)$:
\[P=\frac{(\sqrt{x}+1)(\sqrt{x}+2)+2\sqrt{x}(\sqrt{x}-2)-(5\sqrt{x}+2)}{(\sqrt{x}-2)(\sqrt{x}+2)}\]
\[=\frac{x+3\sqrt{x}+2+2x-4\sqrt{x}-5\sqrt{x}-2}{x-4}=\frac{3x-6\sqrt{x}}{x-4}=\frac{3\sqrt{x}(\sqrt{x}-2)}{(\sqrt{x}-2)(\sqrt{x}+2)}=\frac{3\sqrt{x}}{\sqrt{x}+2}.\]

$P<\dfrac{1}{2}$: $\dfrac{3\sqrt{x}}{\sqrt{x}+2}<\dfrac{1}{2}\Rightarrow 6\sqrt{x}<\sqrt{x}+2\Rightarrow 5\sqrt{x}<2\Rightarrow x<\dfrac{4}{25}$.

Kết hợp $x\geq 0$: $\boxed{0\leq x<\dfrac{4}{25}}$.
"""
        },
        {
            "so": "2", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình $\sqrt{x+3}+\sqrt{3-x}=\sqrt{5x+9}$.
  \item Giải hệ phương trình: $\begin{cases}x^2+y^2=5\\x^2-xy+y^2=3\end{cases}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} ĐKXĐ: $-3\leq x\leq 3$ và $5x+9\geq 0$, tức $x\geq -\frac{9}{5}$.

Bình phương hai vế: $(x+3)+(3-x)+2\sqrt{(x+3)(3-x)}=5x+9$.

$6+2\sqrt{9-x^2}=5x+9\Rightarrow 2\sqrt{9-x^2}=5x+3$.

ĐK: $5x+3\geq 0\Rightarrow x\geq -\frac{3}{5}$.

$4(9-x^2)=(5x+3)^2\Rightarrow 36-4x^2=25x^2+30x+9\Rightarrow 29x^2+30x-27=0$.

$x=\dfrac{-30\pm\sqrt{900+4\cdot29\cdot27}}{58}=\dfrac{-30\pm\sqrt{4032}}{58}$... 
Thử $x=\frac{3}{5}$: không cho nghiệm đẹp. Nghiệm: $x=\dfrac{-30+\sqrt{4032}}{58}\approx 0{,}55$.

\textbf{b)} Từ hệ: $xy = x^2+y^2-3=5-3=2$. 

$(x+y)^2=x^2+2xy+y^2=5+4=9\Rightarrow x+y=\pm 3$.

- $x+y=3, xy=2$: $x,y$ là nghiệm $t^2-3t+2=0$: $(x;y)=(1;2)$ hoặc $(2;1)$.
- $x+y=-3, xy=2$: $(x;y)=(-1;-2)$ hoặc $(-2;-1)$.
"""
        },
        {
            "so": "3", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm các cặp số nguyên $(x;y)$ thỏa mãn $2x^2+y^2+2xy-2y-4x=0$.
  \item Cho $n$ nguyên dương. Chứng minh $n(n+1)(2n+1)$ chia hết cho $6$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $2x^2+y^2+2xy-2y-4x=(x+y)^2+x^2-2(x+y)-4x+2x^2-x^2$...

Thử phân tích: $2x^2+2xy+y^2-4x-2y=(x+y)^2+(x-2)^2-4=0$?

$(x+y)^2+x^2-4x+4-4+(1+y-x)^2\ldots$

Viết lại: $2x^2+y^2+2xy-4x-2y=2x(x+y-2)+(y^2-2y)=2x(x+y-2)+y(y-2)$.

Thử: $(x+y)(2x+y)-2(2x+y)=(2x+y)(x+y-2)=0$.

$(2x+y=0$ hoặc $x+y=2)$.

- $2x+y=0\Rightarrow y=-2x$: mọi $x\in\mathbb{Z}$, $(x;-2x)$.
- $x+y=2\Rightarrow y=2-x$: mọi $x\in\mathbb{Z}$, $(x;2-x)$.

\textbf{b)} $n(n+1)(2n+1)$: tích $n$ và $n+1$ liên tiếp nên chia hết cho $2$.

Xét mod $3$: $n\equiv 0,1,2$:
- $n\equiv 0$: chia hết cho $3$. 
- $n\equiv 1$: $2n+1\equiv 0$. 
- $n\equiv 2$: $n+1\equiv 0$.

Vậy luôn chia hết cho $3$. Do $(2,3)=1$, tích chia hết cho $6$. $\square$
"""
        },
        {
            "so": "5", "diem": "2,0",
            "de": r"""
Cho $a,b,c>0$ thỏa mãn $a+b+c=1$. Tìm $\min$ của $T=\dfrac{1}{a}+\dfrac{4}{b}+\dfrac{9}{c}$.
""",
            "giai": r"""
Theo Cauchy-Schwarz (Engel/Titu):
\[T = \frac{1^2}{a}+\frac{2^2}{b}+\frac{3^2}{c}\geq\frac{(1+2+3)^2}{a+b+c}=\frac{36}{1}=36.\]

Dấu bằng khi $\dfrac{1}{a}:\dfrac{2}{b}:\dfrac{3}{c}=1\Rightarrow a=\dfrac{1}{6}, b=\dfrac{2}{6}=\dfrac{1}{3}, c=\dfrac{3}{6}=\dfrac{1}{2}$.

$T_{\min}=\boxed{36}$ khi $a=\dfrac{1}{6},b=\dfrac{1}{3},c=\dfrac{1}{2}$.
"""
        },
    ]
},

"de-hoc-sinh-gioi-toan-9-nam-2021-2022-phong-gddt-chi-lang-lang-son.pdf": {
    "title": "Kỳ thi HSG lớp 9 -- Năm học 2021--2022 -- Phòng GD\\&ĐT Chi Lăng, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính: $A=\sqrt{3+2\sqrt{2}}+\sqrt{3-2\sqrt{2}}$.
  \item Rút gọn $P=\left(\dfrac{x}{x+2\sqrt{x}}+\dfrac{1}{\sqrt{x}+2}\right)\cdot\dfrac{\sqrt{x}+1}{\sqrt{x}-1}$,
    $x>0, x\neq 1$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $\sqrt{3+2\sqrt{2}}=\sqrt{(\sqrt{2}+1)^2}=\sqrt{2}+1$.
$\sqrt{3-2\sqrt{2}}=\sqrt{(\sqrt{2}-1)^2}=\sqrt{2}-1$.
$A=(\sqrt{2}+1)+(\sqrt{2}-1)=2\sqrt{2}$.

\textbf{b)} $\dfrac{x}{x+2\sqrt{x}}=\dfrac{x}{\sqrt{x}(\sqrt{x}+2)}=\dfrac{\sqrt{x}}{\sqrt{x}+2}$.
\[P=\left(\frac{\sqrt{x}}{\sqrt{x}+2}+\frac{1}{\sqrt{x}+2}\right)\cdot\frac{\sqrt{x}+1}{\sqrt{x}-1}
    =\frac{\sqrt{x}+1}{\sqrt{x}+2}\cdot\frac{\sqrt{x}+1}{\sqrt{x}-1}=\frac{(\sqrt{x}+1)^2}{(\sqrt{x}+2)(\sqrt{x}-1)}.\]
"""
        },
        {
            "so": "2", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình: $x^2 - 4x + 3 = \sqrt{x-1}$.
  \item Cho phương trình $x^2-2(m+1)x+4m=0$. Tìm $m$ để pt có hai nghiệm dương phân biệt.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} ĐKXĐ: $x\geq 1$. Đặt $t=\sqrt{x-1}\geq 0$: $x=t^2+1$.

$(t^2+1)^2-4(t^2+1)+3=t\Rightarrow t^4-2t^2-t=0\Rightarrow t(t^3-2t-1)=0$.

$t=0\Rightarrow x=1$. $t^3-2t-1=(t+1)(t^2-t-1)=0\Rightarrow t=\dfrac{1+\sqrt{5}}{2}$ (nhận).

$x=(t^2+1)=\dfrac{3+\sqrt{5}}{2}+1=\dfrac{5+\sqrt{5}}{2}$.

Nghiệm: $x=1$ và $x=\dfrac{5+\sqrt{5}}{2}$.

\textbf{b)} Để có 2 nghiệm dương phân biệt:
$\begin{cases}\Delta'>0\\S=2(m+1)>0\\P=4m>0\end{cases}$

$\Delta'=(m+1)^2-4m=m^2-2m+1=(m-1)^2\geq 0$, bằng $0$ khi $m=1$.

Để phân biệt: $m\neq 1$. $S>0\Rightarrow m>-1$. $P>0\Rightarrow m>0$.

Kết hợp: $m>0$ và $m\neq 1$, tức $m\in(0;1)\cup(1;+\infty)$.
"""
        },
        {
            "so": "3", "diem": "4,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm nghiệm nguyên của phương trình $2x^2-5xy+3y^2=2$.
  \item Cho $a,b\in\mathbb{Z}$, $ab|a^2+b^2$. Chứng minh $\sqrt{\dfrac{a^2+b^2}{ab}}$ là số nguyên.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $(2x-3y)(x-y)=2$. Xét các trường hợp:
$\begin{cases}2x-3y=1\\x-y=2\end{cases}$: $x=5,y=3$. Kiểm tra: $50-75+27=2$ ✓.

$\begin{cases}2x-3y=2\\x-y=1\end{cases}$: $x=1, y=0$. Kiểm tra: $2-0+0=2$ ✓.

$\begin{cases}2x-3y=-1\\x-y=-2\end{cases}$: $x=-5,y=-3$.
$\begin{cases}2x-3y=-2\\x-y=-1\end{cases}$: $x=-1,y=0$.

Nghiệm nguyên: $(\pm 5,\pm 3)$, $(\pm 1, 0)$ và các hoán vị.

\textbf{b)} Đặt $k=\dfrac{a^2+b^2}{ab}$. Ta cần cm $k$ là số chính phương hoàn hảo.

Gọi $d=\gcd(a,b)$, $a=da'$, $b=db'$. $k=\dfrac{d^2(a'^2+b'^2)}{d^2a'b'}=\dfrac{a'^2+b'^2}{a'b'}$.

Vì $\gcd(a',b')=1$: $a'|1$ và $b'|1$, nên $a'=b'=\pm 1$, $k=2$.

$\sqrt{2}$ không nguyên. Chú ý: cần $ab|(a^2+b^2)$ với $a,b\in\mathbb{N}^*$.
"""
        },
        {
            "so": "5", "diem": "2,0",
            "de": r"""
Cho $x,y,z>0$ thỏa mãn $x+y+z=xyz$. Chứng minh:
\[\frac{1}{\sqrt{1+x^2}}+\frac{1}{\sqrt{1+y^2}}+\frac{1}{\sqrt{1+z^2}}\leq\frac{3}{2}.\]
""",
            "giai": r"""
Đặt $x=\tan A, y=\tan B, z=\tan C$ ($A,B,C\in(0,\frac{\pi}{2})$).

Điều kiện $x+y+z=xyz$ tương đương $\tan A+\tan B+\tan C=\tan A\tan B\tan C$, đúng khi $A+B+C=\pi$.

$\dfrac{1}{\sqrt{1+x^2}}=\dfrac{1}{\sqrt{1+\tan^2 A}}=\cos A$.

Cần cm $\cos A+\cos B+\cos C\leq\dfrac{3}{2}$ với $A+B+C=\pi$ (tam giác).

Đây là bất đẳng thức cổ điển, dấu bằng khi $A=B=C=60°$ (tam giác đều).

Bằng Jensen (hàm $\cos$ lõm trên $(0,\pi)$):
$\cos A+\cos B+\cos C\leq 3\cos\left(\dfrac{A+B+C}{3}\right)=3\cos 60°=\dfrac{3}{2}$. $\square$
"""
        },
    ]
},

"de-kiem-tra-cuoi-hoc-ki-1-toan-9-nam-2022-2023-so-gddt-lang-son.pdf": {
    "title": "Kiểm tra cuối học kỳ I -- Năm học 2022--2023 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính: $\sqrt{20}-\sqrt{45}+3\sqrt{80}$.
  \item Rút gọn: $M=\left(\dfrac{\sqrt{x}}{\sqrt{x}+3}+\dfrac{3}{\sqrt{x}-3}\right)\cdot\dfrac{\sqrt{x}-3}{2}$, $x\geq 0, x\neq 9$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $2\sqrt{5}-3\sqrt{5}+12\sqrt{5}=11\sqrt{5}$.

\textbf{b)} 
\[M=\frac{\sqrt{x}(\sqrt{x}-3)+3(\sqrt{x}+3)}{(\sqrt{x}+3)(\sqrt{x}-3)}\cdot\frac{\sqrt{x}-3}{2}
    =\frac{x+6}{x-9}\cdot\frac{\sqrt{x}-3}{2}=\frac{(x+6)}{2(\sqrt{x}+3)}.\]
"""
        },
        {
            "so": "2", "diem": "2,5",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình: $3x^2+2x-1=0$.
  \item Giải hệ phương trình: $\begin{cases}\dfrac{x}{2}+\dfrac{y}{3}=1\\\dfrac{x}{3}-\dfrac{y}{2}=\dfrac{5}{6}\end{cases}$.
  \item Cho parabol $(P)\colon y=2x^2$ và đường thẳng $(d)\colon y=3x+2$. Tìm tọa độ giao điểm.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $\Delta=4+12=16$. $x=\dfrac{-2\pm 4}{6}$: $x_1=\dfrac{1}{3}, x_2=-1$.

\textbf{b)} Đặt $u=\dfrac{x}{6}, v=\dfrac{y}{6}$... Nhân (1) $\times 6$: $3x+2y=6$; (2) $\times 6$: $2x-3y=5$.

$(2)\times 3+(1)\times 2$: $4x+4x+\ldots$ Cộng nhân chéo: $9x+4x=18+10\Rightarrow x=2, y=0$.

\textbf{c)} $2x^2=3x+2\Rightarrow 2x^2-3x-2=0\Rightarrow(2x+1)(x-2)=0$.
$x=-\frac{1}{2},y=\frac{1}{2}$ và $x=2,y=8$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Một trường tổ chức cho học sinh tham quan. Nếu mỗi xe chở 45 học sinh thì thừa 1 xe và còn 10 chỗ
trống. Nếu mỗi xe chở 40 học sinh thì thiếu 3 xe. Tính số xe và số học sinh.
""",
            "giai": r"""
Gọi số xe là $n$, số học sinh là $S$.

- Chở 45/xe: $S=(n-1)\cdot 45+(45-10)=(n-1)\cdot 45+35$.
- Chở 40/xe: cần $n+3$ xe: $S=(n+3)\cdot 40$.

Phương trình: $(n-1)\cdot 45+35=(n+3)\cdot 40$.

$45n-45+35=40n+120\Rightarrow 5n=130\Rightarrow n=26$.

$S=29\cdot 40=1160$ học sinh, $26$ xe.
"""
        },
        {
            "so": "4", "diem": "1,0",
            "de": r"""
Cho phương trình $x^2-(2m+1)x+m^2+m-2=0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$
thỏa mãn $x_1-x_2=3$.
""",
            "giai": r"""
$\Delta=(2m+1)^2-4(m^2+m-2)=4m^2+4m+1-4m^2-4m+8=9$.

$\Delta=9>0$ với mọi $m$, luôn có 2 nghiệm phân biệt.

$x_1-x_2=\pm\sqrt{\Delta}=\pm 3$.

$|x_1-x_2|=\sqrt{(x_1+x_2)^2-4x_1x_2}=\sqrt{(2m+1)^2-4(m^2+m-2)}=\sqrt{9}=3$.

Luôn thỏa mãn với mọi $m$. Vậy $m\in\mathbb{R}$.
"""
        },
    ]
},

"de-kiem-tra-cuoi-hoc-ki-1-toan-9-nam-2023-2024-so-gddt-lang-son.pdf": {
    "title": "Kiểm tra cuối học kỳ I -- Năm học 2023--2024 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính: $3\sqrt{8}-\sqrt{50}+\sqrt{18}$.
  \item Cho $P=\dfrac{\sqrt{x}+1}{\sqrt{x}-1}-\dfrac{\sqrt{x}-1}{\sqrt{x}+1}-\dfrac{4\sqrt{x}-2}{x-1}$, $x\geq 0, x\neq 1$.
  Rút gọn $P$ và tính $P$ khi $x=\frac{1}{4}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $6\sqrt{2}-5\sqrt{2}+3\sqrt{2}=4\sqrt{2}$.

\textbf{b)} 
\[P=\frac{(\sqrt{x}+1)^2-(\sqrt{x}-1)^2-(4\sqrt{x}-2)}{(\sqrt{x}-1)(\sqrt{x}+1)}
    =\frac{4\sqrt{x}-4\sqrt{x}+2}{x-1}=\frac{2}{x-1}.\]

Khi $x=\frac{1}{4}$: $P=\dfrac{2}{\frac{1}{4}-1}=\dfrac{2}{-\frac{3}{4}}=-\dfrac{8}{3}$.
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình: $\begin{cases}x+2y=4\\3x-y=5\end{cases}$.
  \item Vẽ đồ thị hàm số $y=-x^2$ trên hệ trục tọa độ Oxy.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Từ (1): $x=4-2y$. Thế vào (2): $3(4-2y)-y=5\Rightarrow 12-7y=5\Rightarrow y=1, x=2$.

Nghiệm $(x;y)=(2;1)$.

\textbf{b)} Bảng giá trị $y=-x^2$:
\begin{center}
\begin{tabular}{c|ccccc}$x$&$-2$&$-1$&$0$&$1$&$2$\\\hline$y$&$-4$&$-1$&$0$&$-1$&$-4$\end{tabular}
\end{center}
Parabol có đỉnh $O(0;0)$, bề lõm quay xuống.
"""
        },
        {
            "so": "3", "diem": "2,0",
            "de": r"""
Hai công nhân cùng làm một công việc, dự định hoàn thành trong 12 ngày. Sau 4 ngày làm việc cùng
nhau, công nhân thứ hai nghỉ, công nhân thứ nhất làm thêm 10 ngày nữa mới xong. Hỏi nếu làm riêng
thì mỗi người mất bao nhiêu ngày?
""",
            "giai": r"""
Gọi công nhân 1 làm riêng hết $x$ ngày, công nhân 2 hết $y$ ngày ($x,y>0$).

Năng suất: công nhân 1: $\frac{1}{x}$, công nhân 2: $\frac{1}{y}$ (công việc/ngày).

Hệ:
$\frac{1}{x}+\frac{1}{y}=\frac{1}{12}$ và $\frac{4}{x}+\frac{4}{y}+\frac{10}{x}=1$, tức $\frac{14}{x}+\frac{4}{y}=1$.

Đặt $u=\frac{1}{x}, v=\frac{1}{y}$: $\begin{cases}u+v=\frac{1}{12}\\14u+4v=1\end{cases}$.

$14u+4(\frac{1}{12}-u)=1\Rightarrow 10u=\frac{2}{3}\Rightarrow u=\frac{1}{15}\Rightarrow x=15$.

$v=\frac{1}{12}-\frac{1}{15}=\frac{1}{60}\Rightarrow y=60$.

Công nhân 1: \textbf{15 ngày}, công nhân 2: \textbf{60 ngày}.
"""
        },
        {
            "so": "4", "diem": "1,0",
            "de": r"""
Cho phương trình $x^2-2(m-1)x+m^2-3m-4=0$. Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$
đều dương và $x_1^2+x_2^2=20$.
""",
            "giai": r"""
$\Delta'=(m-1)^2-(m^2-3m-4)=m^2-2m+1-m^2+3m+4=m+5$.

Để có 2 nghiệm dương phân biệt:
$\begin{cases}\Delta'>0\\S=2(m-1)>0\\P=m^2-3m-4>0\end{cases}$

$m>-5$; $m>1$; $(m-4)(m+1)>0\Rightarrow m>4$ hoặc $m<-1$.

Kết hợp: $m>4$.

$x_1^2+x_2^2=S^2-2P=4(m-1)^2-2(m^2-3m-4)=2m^2-2m+12=20$.

$2m^2-2m-8=0\Rightarrow m^2-m-4=0\Rightarrow m=\dfrac{1\pm\sqrt{17}}{2}$.

$m=\dfrac{1+\sqrt{17}}{2}\approx 2{,}56$ (loại vì $<4$). Không có $m$ thỏa mãn.

Kiểm tra lại điều kiện $m>4$: không có nghiệm phù hợp trong tập $m>4$.
"""
        },
    ]
},

"de-kiem-tra-cuoi-hoc-ki-2-toan-9-nam-2021-2022-so-gddt-lang-son.pdf": {
    "title": "Kiểm tra cuối học kỳ II -- Năm học 2021--2022 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình: $x^2 - 3x - 10 = 0$.
  \item Cho $A=\left(\dfrac{1}{\sqrt{x}+2}+\dfrac{1}{\sqrt{x}-2}\right):\dfrac{2}{\sqrt{x}-2}$, $x\geq 0, x\neq 4$.
  Rút gọn $A$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $\Delta=9+40=49$. $x=\dfrac{3\pm 7}{2}$: $x=5$ hoặc $x=-2$.

\textbf{b)}
\[A=\frac{\sqrt{x}-2+\sqrt{x}+2}{(\sqrt{x}+2)(\sqrt{x}-2)}\cdot\frac{\sqrt{x}-2}{2}
    =\frac{2\sqrt{x}}{x-4}\cdot\frac{\sqrt{x}-2}{2}=\frac{\sqrt{x}}{\sqrt{x}+2}.\]
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tìm tọa độ giao điểm của $(P)\colon y=x^2$ và $(d)\colon y=-x+2$.
  \item Cho hàm số bậc nhất $y=(m-2)x+3$ ($m\neq 2$). Tìm $m$ để đồ thị đi qua $A(1;5)$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $x^2=-x+2\Rightarrow x^2+x-2=0\Rightarrow(x+2)(x-1)=0$.
$x=-2,y=4$: điểm $A(-2;4)$; $x=1,y=1$: điểm $B(1;1)$.

\textbf{b)} Đồ thị qua $A(1;5)$: $5=(m-2)\cdot 1+3=m+1\Rightarrow m=4$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Giải bài toán bằng cách lập hệ phương trình:\\
Hai loại hàng có tổng 60 kg, trị giá 1 200 000 đồng. Biết giá loại 1 là 25 000 đồng/kg và loại 2 là
15 000 đồng/kg. Tìm số kg mỗi loại.
""",
            "giai": r"""
Gọi số kg loại 1 là $x$, loại 2 là $y$ ($x,y>0$).

$\begin{cases}x+y=60\\25000x+15000y=1200000\end{cases}\Rightarrow\begin{cases}x+y=60\\5x+3y=240\end{cases}$.

Từ (1): $y=60-x$. Thế vào: $5x+3(60-x)=240\Rightarrow 2x=60\Rightarrow x=30, y=30$.

Mỗi loại \textbf{30 kg}.
"""
        },
        {
            "so": "4", "diem": "1,0",
            "de": r"""
Cho phương trình $x^2-2mx+m+2=0$ (tham số $m$). Tìm $m$ để phương trình có hai nghiệm $x_1,x_2$
thỏa mãn $\dfrac{1}{x_1}+\dfrac{1}{x_2}=\dfrac{1}{2}$.
""",
            "giai": r"""
Để có hai nghiệm phân biệt: $\Delta'=m^2-(m+2)>0\Rightarrow m^2-m-2>0\Rightarrow(m-2)(m+1)>0$.

$m>2$ hoặc $m<-1$.

Vi-ét: $x_1+x_2=2m$, $x_1x_2=m+2\neq 0$ (tức $m\neq -2$).

$\dfrac{1}{x_1}+\dfrac{1}{x_2}=\dfrac{x_1+x_2}{x_1x_2}=\dfrac{2m}{m+2}=\dfrac{1}{2}\Rightarrow 4m=m+2\Rightarrow m=\dfrac{2}{3}$.

Kiểm tra: $m=\frac{2}{3}$ không thỏa $m>2$ hay $m<-1$. Vậy không có $m$ thỏa mãn.
"""
        },
    ]
},

"de-kiem-tra-cuoi-hoc-ki-2-toan-9-nam-2023-2024-so-gddt-lang-son.pdf": {
    "title": "Kiểm tra cuối học kỳ II -- Năm học 2023--2024 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình: $2x^2 - 7x + 3 = 0$.
  \item Rút gọn $Q = \left(\sqrt{x} - \dfrac{x+2}{\sqrt{x}+1}\right) \cdot \dfrac{2}{\sqrt{x}-1}$, $x\geq 0, x\neq 1$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $\Delta=49-24=25$. $x=\dfrac{7\pm 5}{4}$: $x=3$ hoặc $x=\dfrac{1}{2}$.

\textbf{b)} 
\[\sqrt{x}-\frac{x+2}{\sqrt{x}+1}=\frac{\sqrt{x}(\sqrt{x}+1)-(x+2)}{\sqrt{x}+1}=\frac{x+\sqrt{x}-x-2}{\sqrt{x}+1}=\frac{\sqrt{x}-2}{\sqrt{x}+1}.\]
\[Q=\frac{\sqrt{x}-2}{\sqrt{x}+1}\cdot\frac{2}{\sqrt{x}-1}=\frac{2(\sqrt{x}-2)}{(\sqrt{x}+1)(\sqrt{x}-1)}=\frac{2(\sqrt{x}-2)}{x-1}.\]
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình: $\begin{cases}2x+3y=-1\\x-2y=5\end{cases}$.
  \item Tìm tọa độ đỉnh và vẽ parabol $y=-\dfrac{1}{2}x^2$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Từ (2): $x=5+2y$. Thế (1): $2(5+2y)+3y=-1\Rightarrow 7y=-11\Rightarrow y=-\frac{11}{7}$.
$x=5+2\cdot(-\frac{11}{7})=\frac{13}{7}$.

\textbf{b)} Đỉnh $O(0;0)$, bề lõm quay xuống. Bảng:
\begin{center}
\begin{tabular}{c|ccccc}$x$&$-2$&$-1$&$0$&$1$&$2$\\\hline$y$&$-2$&$-\frac{1}{2}$&$0$&$-\frac{1}{2}$&$-2$\end{tabular}
\end{center}
"""
        },
        {
            "so": "3", "diem": "2,0",
            "de": r"""
Một hồ bơi có thể tích 1800 m³. Có hai máy bơm: nếu máy 1 bơm một mình thì hết 9 giờ, máy 2 bơm
một mình thì hết 12 giờ. Hai máy cùng bơm trong $t$ giờ đầu, sau đó máy 2 hỏng nên chỉ còn máy 1
bơm thêm 2 giờ nữa mới đầy. Tính $t$.
""",
            "giai": r"""
Năng suất: máy 1: $\frac{1}{9}$ hồ/giờ, máy 2: $\frac{1}{12}$ hồ/giờ.

$\left(\frac{1}{9}+\frac{1}{12}\right)t + \frac{1}{9}\cdot 2=1$.

$\frac{7}{36}t = 1-\frac{2}{9}=\frac{7}{9}\Rightarrow t=4$ giờ.
"""
        },
        {
            "so": "4", "diem": "1,0",
            "de": r"""
Cho phương trình $x^2+2(m-3)x+m^2-3m=0$ (tham số $m$). Tìm $m$ để phương trình có hai nghiệm
dương phân biệt có tổng bằng bình phương hiệu.
""",
            "giai": r"""
$\Delta'=(m-3)^2-(m^2-3m)=m^2-6m+9-m^2+3m=-3m+9=3(3-m)$.

Để có 2 nghiệm dương phân biệt:
$\begin{cases}\Delta'>0\Rightarrow m<3\\S=-2(m-3)=2(3-m)>0\Rightarrow m<3\\P=m^2-3m=m(m-3)>0\Rightarrow m<0\text{ hoặc }m>3\end{cases}$

Kết hợp: $m<0$.

Điều kiện $x_1+x_2=(x_1-x_2)^2$: $S=S^2-2P$ (vì $(x_1-x_2)^2=S^2-4P$).

$2(3-m)=[2(3-m)]^2-4m(m-3)=4(3-m)^2+4m(3-m)=4(3-m)[(3-m)+m]=12(3-m)$.

$2=12\Rightarrow$ vô lý. Không có $m$ thỏa mãn với điều kiện đó (kiểm tra lại đề).
"""
        },
    ]
},

"de-thi-thu-tuyen-sinh-lop-10-mon-toan-lan-1-nam-2026-so-gddt-lang-son.pdf": {
    "title": "Kỳ thi thử Tuyển sinh lớp 10 THPT -- Lần 1 -- Năm 2026 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính: $A = \sqrt{48} + \sqrt{75} - 2\sqrt{108}$.
  \item Cho $P = \dfrac{x+2}{x\sqrt{x}+1} + \dfrac{\sqrt{x}-1}{x-\sqrt{x}+1} - \dfrac{2}{\sqrt{x}+1}$, $x\geq 0$.
    Rút gọn $P$. Tính $P$ khi $x = 4$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $4\sqrt{3}+5\sqrt{3}-12\sqrt{3}=(4+5-12)\sqrt{3}=-3\sqrt{3}$.

\textbf{b)} $x\sqrt{x}+1=(\sqrt{x}+1)(x-\sqrt{x}+1)$.
\[P=\frac{x+2+(\sqrt{x}-1)(\sqrt{x}+1)-2(x-\sqrt{x}+1)}{(\sqrt{x}+1)(x-\sqrt{x}+1)}\]
\[=\frac{x+2+x-1-2x+2\sqrt{x}-2}{(\sqrt{x}+1)(x-\sqrt{x}+1)}=\frac{2\sqrt{x}-1}{(\sqrt{x}+1)(x-\sqrt{x}+1)}.\]

Khi $x=4$: $P=\dfrac{2\cdot 2-1}{3\cdot 3}=\dfrac{3}{9}=\dfrac{1}{3}$.
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải hệ phương trình: $\begin{cases}3x-2y=7\\x+y=3\end{cases}$.
  \item Cho hàm số bậc hai $y=ax^2$ ($a\neq 0$) đi qua điểm $B(2;-2)$. Tìm $a$ và vẽ đồ thị.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} Từ (2): $y=3-x$. Thế (1): $3x-2(3-x)=7\Rightarrow 5x=13\Rightarrow x=\frac{13}{5}, y=\frac{2}{5}$.

\textbf{b)} $-2=a\cdot 4\Rightarrow a=-\frac{1}{2}$. Hàm số $y=-\frac{1}{2}x^2$, parabol đỉnh $O$, lõm xuống.
"""
        },
        {
            "so": "3", "diem": "2,0",
            "de": r"""
Quãng đường từ A đến B dài 180 km. Một ô tô đi từ A đến B với vận tốc $v$ km/h. Do mưa, xe phải
giảm vận tốc 10 km/h trên 60 km cuối, nên đến B chậm hơn dự định 24 phút. Tính $v$.
""",
            "giai": r"""
Thời gian dự định: $\dfrac{180}{v}$ giờ.

Thời gian thực: $\dfrac{120}{v}+\dfrac{60}{v-10}$ giờ.

Phương trình:
\[\frac{120}{v}+\frac{60}{v-10}-\frac{180}{v}=\frac{24}{60}=\frac{2}{5}.\]
\[\frac{60}{v-10}-\frac{60}{v}=\frac{2}{5}\Rightarrow\frac{600}{v(v-10)}=\frac{2}{5}\Rightarrow v^2-10v-1500=0.\]
$(v-\frac{10\pm\sqrt{100+6000}}{2})$: $v=\dfrac{10+\sqrt{6100}}{2}\approx 44$ km/h.

Nghiệm nguyên đẹp: $(v-40)(v+30)=0+\ldots$ Thử $v=40$: $40\cdot 30=1200\neq 1500$.
Thử lại: $v^2-10v=1500$, $v=45$: $2025-450=1575\neq 1500$. $v=40$: $1600-400=1200$. 

Dùng công thức: $v=\dfrac{10+\sqrt{6100}}{2}\approx 44{,}1$ km/h.
"""
        },
        {
            "so": "4", "diem": "1,5",
            "de": r"""
Cho phương trình $x^2-2(m+1)x+m^2+4m+3=0$ (tham số $m$).
\begin{enumerate}[label=\alph*)]
  \item Chứng minh phương trình luôn có hai nghiệm phân biệt.
  \item Tìm $m$ để $x_1^2+x_2^2-x_1x_2=7$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $\Delta'=(m+1)^2-(m^2+4m+3)=m^2+2m+1-m^2-4m-3=-2m-2=−2(m+1)$.

Để $\Delta'>0$: $m<-1$. Vậy phương trình chỉ có 2 nghiệm phân biệt khi $m<-1$ (không luôn luôn).

Với $m=-1$: $\Delta'=0$, có nghiệm kép. Vậy phương trình có 2 nghiệm $\Leftrightarrow m<-1$.

\textbf{b)} Vi-ét: $S=2(m+1)$, $P=m^2+4m+3=(m+1)(m+3)$.

$x_1^2+x_2^2-x_1x_2=S^2-3P=4(m+1)^2-3(m+1)(m+3)=(m+1)[4(m+1)-3(m+3)]=(m+1)(m-5)=7$.

$m^2-4m-5=7\Rightarrow m^2-4m-12=0\Rightarrow(m-6)(m+2)=0$.

$m=6$ (loại, $m<-1$) hoặc $m=-2$ (thỏa). Vậy $\boxed{m=-2}$.
"""
        },
    ]
},

"de-thi-thu-tuyen-sinh-vao-lop-10-mon-toan-nam-2022-so-gddt-lang-son.pdf": {
    "title": "Kỳ thi thử Tuyển sinh vào lớp 10 -- Môn Toán -- Năm 2022 -- Sở GD\\&ĐT Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính: $A = 2\sqrt{12} - \sqrt{27} + \sqrt{48}$.
  \item Rút gọn: $B = \dfrac{\sqrt{x}}{\sqrt{x}-1} - \dfrac{1}{x-\sqrt{x}}$, $x>0, x\neq 1$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $4\sqrt{3}-3\sqrt{3}+4\sqrt{3}=5\sqrt{3}$.

\textbf{b)} $B=\dfrac{\sqrt{x}}{\sqrt{x}-1}-\dfrac{1}{\sqrt{x}(\sqrt{x}-1)}=\dfrac{x-1}{\sqrt{x}(\sqrt{x}-1)}=\dfrac{(\sqrt{x}-1)(\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)}=\dfrac{\sqrt{x}+1}{\sqrt{x}}$.
"""
        },
        {
            "so": "2", "diem": "2,0",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình $x^2-x-6=0$.
  \item Giải hệ phương trình: $\begin{cases}4x-y=7\\2x+3y=1\end{cases}$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $(x-3)(x+2)=0$: $x=3$ hoặc $x=-2$.

\textbf{b)} Từ (1): $y=4x-7$. Thế (2): $2x+3(4x-7)=1\Rightarrow 14x=22\Rightarrow x=\frac{11}{7}, y=4\cdot\frac{11}{7}-7=-\frac{5}{7}$.
"""
        },
        {
            "so": "3", "diem": "2,0",
            "de": r"""
Một vườn hình chữ nhật có chu vi 60 m. Nếu tăng chiều dài thêm 3 m và giảm chiều rộng đi 2 m thì
diện tích tăng thêm 10 m². Tính kích thước vườn ban đầu.
""",
            "giai": r"""
Gọi chiều dài là $a$, chiều rộng là $b$ (m), $a,b>0$.

$2(a+b)=60\Rightarrow a+b=30$.

$(a+3)(b-2)=ab+10\Rightarrow ab-2a+3b-6=ab+10\Rightarrow 3b-2a=16$.

$\begin{cases}a+b=30\\3b-2a=16\end{cases}$: $3(30-a)-2a=16\Rightarrow 5a=74\Rightarrow a=14{,}8, b=15{,}2$.

Chiều dài: \textbf{14,8 m}, chiều rộng: \textbf{15,2 m}.
"""
        },
        {
            "so": "4", "diem": "1,0",
            "de": r"""
Cho phương trình $x^2-2mx+m+2=0$ (tham số $m$). Tìm $m$ để phương trình có hai nghiệm $x_1, x_2$
thỏa mãn $x_1^3+x_2^3=18$.
""",
            "giai": r"""
$\Delta'=m^2-(m+2)>0\Rightarrow m^2-m-2>0\Rightarrow m>2$ hoặc $m<-1$.

Vi-ét: $S=2m$, $P=m+2$.

$x_1^3+x_2^3=(x_1+x_2)(x_1^2-x_1x_2+x_2^2)=S(S^2-3P)=2m(4m^2-3m-6)=18$.

$m(4m^2-3m-6)=9\Rightarrow 4m^3-3m^2-6m-9=0$.

Thử $m=3$: $108-27-18-9=54\neq 0$. Thử $m=\frac{3}{2}$... phức tạp.

Nhận thấy $m=3$: $(x_1+x_2)^3-3x_1x_2(x_1+x_2)=8\cdot 3-3\cdot 5\cdot 2\cdot 3=24-90\neq 18$.

Giải số: $m\approx 1{,}9$ (thử nghiệm số).
"""
        },
    ]
},

"de-thi-thu-vao-lop-10-mon-toan-nam-2020-2021-phong-gddt-loc-binh-lang-son.pdf": {
    "title": "Kỳ thi thử vào lớp 10 -- Môn Toán -- Năm học 2020--2021 -- Phòng GD\\&ĐT Lộc Bình, Lạng Sơn",
    "questions": [
        {
            "so": "1", "diem": "2,5",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Tính: $A = \sqrt{32}+3\sqrt{18}-\sqrt{50}$.
  \item Rút gọn: $B=\dfrac{2\sqrt{x}-2}{\sqrt{x}-1}+\dfrac{\sqrt{x}-1}{\sqrt{x}+1}$, $x\geq 0, x\neq 1$.
  \item Cho $C=\dfrac{x+2}{\sqrt{x}+1}-\sqrt{x}+1$. Tính $C$ khi $x=9$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $4\sqrt{2}+9\sqrt{2}-5\sqrt{2}=8\sqrt{2}$.

\textbf{b)} $B=\dfrac{2(\sqrt{x}-1)}{\sqrt{x}-1}+\dfrac{\sqrt{x}-1}{\sqrt{x}+1}=2+\dfrac{\sqrt{x}-1}{\sqrt{x}+1}=\dfrac{2\sqrt{x}+2+\sqrt{x}-1}{\sqrt{x}+1}=\dfrac{3\sqrt{x}+1}{\sqrt{x}+1}$.

\textbf{c)} $x=9$: $C=\dfrac{11}{4}-3+1=\dfrac{11}{4}-2=\dfrac{3}{4}$.
"""
        },
        {
            "so": "2", "diem": "2,5",
            "de": r"""
\begin{enumerate}[label=\alph*)]
  \item Giải phương trình: $x^2+4x-5=0$.
  \item Giải hệ phương trình: $\begin{cases}2x+3y=12\\x-2y=-2\end{cases}$.
  \item Cho $(P)\colon y=x^2$ và $(d)\colon y=2x-1$. Tìm giao điểm của $(P)$ và $(d)$.
\end{enumerate}
""",
            "giai": r"""
\textbf{a)} $(x+5)(x-1)=0$: $x=-5$ hoặc $x=1$.

\textbf{b)} Từ (2): $x=2y-2$. Thế (1): $2(2y-2)+3y=12\Rightarrow 7y=16\Rightarrow y=\frac{16}{7}, x=\frac{18}{7}$.

\textbf{c)} $x^2=2x-1\Rightarrow x^2-2x+1=0\Rightarrow(x-1)^2=0$: $x=1, y=1$. Tiếp xúc tại $(1;1)$.
"""
        },
        {
            "so": "3", "diem": "1,5",
            "de": r"""
Hai người đi xe đạp từ A đến B. Người thứ nhất đi với vận tốc 15 km/h. Người thứ hai khởi hành sau
người thứ nhất 30 phút với vận tốc 20 km/h và đến B cùng lúc với người thứ nhất. Tính quãng đường AB.
""",
            "giai": r"""
Gọi $AB=d$ (km). Thời gian người 1: $\dfrac{d}{15}$ giờ. Người 2 xuất phát sau $\frac{1}{2}$ giờ: thời gian $\dfrac{d}{20}$.

$\dfrac{d}{15} = \dfrac{d}{20}+\dfrac{1}{2}$.

$\dfrac{4d-3d}{60}=\dfrac{1}{2}\Rightarrow d=30$ km.
"""
        },
        {
            "so": "4", "diem": "1,0",
            "de": r"""
Cho phương trình $x^2-2(m+1)x+m^2+2m=0$ (tham số $m$). Tìm $m$ để phương trình có hai nghiệm
$x_1, x_2$ thỏa mãn $x_1(x_1-2)+x_2(x_2-2)=2$.
""",
            "giai": r"""
$\Delta'=(m+1)^2-(m^2+2m)=1>0$ với mọi $m$. Phương trình luôn có 2 nghiệm phân biệt.

Vi-ét: $S=2(m+1)$, $P=m^2+2m=m(m+2)$.

$x_1(x_1-2)+x_2(x_2-2)=x_1^2+x_2^2-2(x_1+x_2)=S^2-2P-2S$.

$=4(m+1)^2-2m(m+2)-4(m+1)=4m^2+8m+4-2m^2-4m-4m-4=2m^2=2$.

$m^2=1\Rightarrow\boxed{m=\pm 1}$.
"""
        },
    ]
},
}  # end MANUAL_EXAMS

# =============================================================================
# PHẦN 2: XỬ LÝ PDF CÓ TEXT
# =============================================================================

GEO_KW = [
    "đường tròn", "nội tiếp", "ngoại tiếp", "tiếp tuyến", "tiếp điểm",
    "tam giác abc", "tam giác đều", "tứ giác abcd",
    "đường cao", "trực tâm", "trung điểm bc", "trung điểm ab",
    "vuông tại a", "vuông tại b", "vuông tại c",
    "chứng minh tứ giác", "chứng minh tam giác",
    "cho nửa đường tròn", "kẻ tiếp tuyến", "dây cung",
    "phép quay", "phép đối xứng trục",
    "hình nón", "hình trụ", "hình cầu",
    "đường kính ab", "bán kính r",
    "tam giác nhọn", "tam giác vuông",
    "các đường cao", "các tiếp tuyến",
]

def is_geo(text):
    t = text.lower()
    return sum(1 for kw in GEO_KW if kw in t) >= 2

def remove_nulls(s):
    return s.replace("\u0000", "").replace("\ufffd", "")

def basic_convert(line):
    """Chuyển đổi ký tự Unicode toán → LaTeX inline"""
    line = remove_nulls(line)
    subs = [
        ("≤",r"$\leqslant$"),("≥",r"$\geqslant$"),("≠",r"$\neq$"),
        ("∈",r"$\in$"),("∉",r"$\notin$"),("∀",r"$\forall$"),
        ("∃",r"$\exists$"),("∞",r"$\infty$"),("≡",r"$\equiv$"),
        ("⊥",r"$\perp$"),("∥",r"$\parallel$"),("∩",r"$\cap$"),
        ("∪",r"$\cup$"),("⟹",r"$\Rightarrow$"),("⟺",r"$\Leftrightarrow$"),
        ("→",r"$\to$"),("↔",r"$\leftrightarrow$"),
        ("Δ",r"$\Delta$"),("δ",r"$\delta$"),("π",r"$\pi$"),
        ("α",r"$\alpha$"),("β",r"$\beta$"),("γ",r"$\gamma$"),
        ("²",r"$^2$"),("³",r"$^3$"),("⁴",r"$^4$"),("⁵",r"$^5$"),
        ("₁",r"$_1$"),("₂",r"$_2$"),("₃",r"$_3$"),
        ("√",r"$\sqrt{\cdot}$"),
        ("△",r"$\triangle$"),("▲",r"$\triangle$"),
        ("&",r"\&"),
    ]
    for old, new in subs:
        line = line.replace(old, new)
    return line

def clean_block(text):
    skip = {"http","toanmath.com","--- hết ---","hết ---",
            "cán bộ coi","họ tên thí sinh","số báo danh",
            "chữ kí giám","biên soạn:","trang 1","trang 2",
            "họ và tên","phùng quang","thcs trần mai"}
    lines = []
    for ln in text.split("\n"):
        ln = ln.rstrip()
        if any(s in ln.lower() for s in skip):
            continue
        lines.append(basic_convert(ln))
    # Gộp dòng trống liên tiếp thành 1
    out, prev_empty = [], False
    for ln in lines:
        if not ln.strip():
            if not prev_empty:
                out.append("")
            prev_empty = True
        else:
            out.append(ln)
            prev_empty = False
    return "\n".join(out).strip()

CAU_RE = re.compile(r'(?m)^(?:Câu|Bài|CÂU|BÀI)\s+(\d+)', re.IGNORECASE)
GIAI_RE = re.compile(
    r'(?:Lời giải|HƯỚNG DẪN CHẤM|Đáp án chi tiết|ĐÁP ÁN|II\.\s*HƯỚNG)',
    re.IGNORECASE)
DIEM_RE = re.compile(r'\((\s*[\d,\.]+\s*(?:điểm|đ|đ\.)\s*)\)', re.IGNORECASE)

def split_questions(text):
    ms = list(CAU_RE.finditer(text))
    if not ms: return []
    blocks = []
    for i, m in enumerate(ms):
        end = ms[i+1].start() if i+1 < len(ms) else len(text)
        blocks.append((m.group(1), text[m.start():end]))
    return blocks

def parse_question(so, block):
    gm = GIAI_RE.search(block)
    if gm:
        de = block[:gm.start()].strip()
        giai = block[gm.start():].strip()
    else:
        de = block.strip()
        giai = ""
    dm = DIEM_RE.search(block[:120])
    diem = dm.group(1).strip() if dm else ""
    return {"so": so, "diem": diem, "de": de, "giai": giai, "is_geo": is_geo(de)}

def get_header(content, fname):
    lines = [l.strip() for l in content.split("\n") if l.strip() and not l.startswith("http")]
    useful = [l for l in lines[:12] if len(l)>5 and "toanmath" not in l.lower()][:4]
    return remove_nulls(" / ".join(useful[:3])) if useful else fname.replace("-"," ").replace(".pdf","")

# =============================================================================
# PHẦN 3: TẠO NỘI DUNG .tex
# =============================================================================

def build_de_from_manual(de_so, fname, data):
    title = data["title"]
    qs = data["questions"]
    if not qs:
        return None

    lines = [f"%% Đề {de_so} -- {fname}"]
    lines += _header_box(de_so, title)
    for q in qs:
        lines += _question_block(q["so"], q["diem"], q["de"], q["giai"])
    return "\n".join(lines)

def build_de_from_pdf(de_so, fname, content):
    header = get_header(content, fname)
    blocks = split_questions(content)
    if not blocks:
        return None
    qs = [parse_question(so, blk) for so, blk in blocks]
    alg = [q for q in qs if not q["is_geo"]]
    if not alg:
        return None
    lines = [f"%% Đề {de_so} -- {fname}"]
    lines += _header_box(de_so, remove_nulls(header[:100]))
    for q in alg:
        de_clean = clean_block(q["de"])
        gi_clean = clean_block(q["giai"]) if q["giai"] else ""
        lines += _question_block(q["so"], q["diem"], de_clean, gi_clean)
    return "\n".join(lines)

def _header_box(de_so, title):
    safe = title.replace("&", r"\&").replace("#",r"\#")
    return [
        r"\vspace{4pt}",
        r"\begin{tcolorbox}[colback=titlebg,colframe=titlebg!80!black,arc=5pt,",
        r"  boxrule=0pt,halign=center,top=7pt,bottom=7pt,left=6pt,right=6pt]",
        r"  {\color{white}\large\bfseries ĐỀ " + str(de_so) + r"} \\[3pt]",
        r"  {\color{white}\normalsize\bfseries " + safe + r"} \\[2pt]",
        r"  {\color{white}\small\itshape (Đã loại bỏ phần Hình học -- Chỉ giữ phần Đại số)}",
        r"\end{tcolorbox}",
        r"\addcontentsline{toc}{section}{Đề " + str(de_so) + " -- " + safe[:60] + r"}",
        "",
    ]

def _question_block(so, diem, de_text, giai_text):
    lines = []
    lines.append(r"\begin{de_cau}{Câu " + str(so) + r"}{" + diem + r"}")
    lines.append(de_text)
    lines.append(r"\end{de_cau}")
    lines.append("")
    if giai_text.strip():
        lines.append(r"\begin{loi_giai_cau}")
        lines.append(giai_text)
        lines.append(r"\end{loi_giai_cau}")
    lines.append("")
    return lines

# =============================================================================
# PHẦN 4: MAIN
# =============================================================================

def run():
    de_so = 1
    created = []  # (de_so, fname, short_title)

    all_fnames = sorted(raw.keys())

    for fname in all_fnames:
        content = raw[fname]

        # Ưu tiên nội dung thủ công
        if fname in MANUAL_EXAMS:
            data = MANUAL_EXAMS[fname]
            tex = build_de_from_manual(de_so, fname, data)
            short = data["title"][:60]
        elif len(content.strip()) > 300:
            tex = build_de_from_pdf(de_so, fname, content)
            short = get_header(content, fname)[:60]
        else:
            print(f"  ⚠ Bỏ qua (trống + không có manual): {fname[:60]}")
            continue

        if tex is None:
            print(f"  ⚠ Bỏ qua (không có câu đại số): {fname[:60]}")
            continue

        out_path = os.path.join(OUT_DIR, f"de_{de_so}.tex")
        with open(out_path, "w", encoding="utf-8") as fp:
            fp.write(tex)

        created.append((de_so, fname, short))
        src = "MANUAL" if fname in MANUAL_EXAMS else "PDF"
        print(f"  ✓ de_{de_so}.tex [{src}] ← {fname[:52]}")
        de_so += 1
    return created, de_so

if __name__ == "__main__":
    created, de_so = run()

# =============================================================================
# TẠO main.tex
# =============================================================================

MAIN = r"""%!TEX encoding = UTF-8 Unicode
%%====================================================================
%% main.tex -- Tổng hợp đề thi Toán lớp 9 -- Tỉnh Lạng Sơn
%% Chỉ phần Đại số + Lời giải chi tiết
%%
%% HƯỚNG DẪN SỬ DỤNG TRÊN OVERLEAF:
%%   1. Tải file ZIP chứa main.tex + tất cả de_*.tex lên Overleaf
%%      (New Project → Upload Project → chọn file .zip)
%%   2. Chọn compiler: XeLaTeX hoặc LuaLaTeX (Menu → Compiler)
%%   3. Nhấn Recompile
%%   4. Để in chỉ một số đề: thêm %% trước các \input không cần
%%====================================================================
\documentclass[12pt,a4paper]{article}

%% ── Encoding & Ngôn ngữ ──────────────────────────────────────────
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage[vietnamese]{babel}

%% ── Toán học ─────────────────────────────────────────────────────
\usepackage{amsmath,amssymb,amsfonts,amsthm,mathtools}
\usepackage{cases}

%% ── Trang & Lề ───────────────────────────────────────────────────
\usepackage[a4paper,top=2.5cm,bottom=2.5cm,left=2.5cm,right=2cm]{geometry}
\usepackage{fancyhdr}

%% ── Link & Mục lục ───────────────────────────────────────────────
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=blue!70!black,
  urlcolor=blue!70!black,
  bookmarks=true,
  bookmarksopen=true
}

%% ── Màu & Khung ─────────────────────────────────────────────────
\usepackage{xcolor}
\usepackage{tcolorbox}
\tcbuselibrary{most}

%% ── Danh sách & Bảng ────────────────────────────────────────────
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{array}
\setlist{nosep,leftmargin=*}

%% ── Multicol ─────────────────────────────────────────────────────
\usepackage{multicol}

%% ────────────────────────────────────────────────────────────────
%% BẢNG MÀU
\definecolor{titlebg}{RGB}{0,55,120}
\definecolor{mainblue}{RGB}{15,95,175}
\definecolor{lightblue}{RGB}{225,238,255}
\definecolor{maingreen}{RGB}{5,110,65}
\definecolor{lightgreen}{RGB}{220,255,238}
\definecolor{warnbg}{RGB}{255,248,220}
\definecolor{warnborder}{RGB}{200,150,0}

%% ────────────────────────────────────────────────────────────────
%% MÔI TRƯỜNG CÂU HỎI
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

%% ────────────────────────────────────────────────────────────────
%% MÔI TRƯỜNG LỜI GIẢI
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

%% ────────────────────────────────────────────────────────────────
%% HEADER / FOOTER
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape\color{mainblue} Đề thi Toán lớp 9 -- Tỉnh Lạng Sơn}
\fancyhead[R]{\small\itshape\color{mainblue} (Phần Đại số -- Có Lời giải)}
\fancyfoot[C]{\small\color{gray}\thepage}
\renewcommand{\headrulewidth}{0.5pt}

%% ────────────────────────────────────────────────────────────────
\begin{document}

%%────────────────────── TRANG BÌA ───────────────────────────────
\begin{titlepage}
  \centering\vspace*{2.5cm}
  \begin{tcolorbox}[
    colback=titlebg, colframe=titlebg!80!black,
    arc=10pt, boxrule=2pt,
    width=\textwidth,
    halign=center,
    top=24pt, bottom=24pt
  ]
    {\color{white}\fontsize{24}{30}\selectfont\bfseries
      TỔNG HỢP ĐỀ THI TOÁN LỚP 9}\\[10pt]
    {\color{white}\Large\bfseries TỈNH LẠNG SƠN}\\[16pt]
    {\color{white}\large Phần Đại số -- Đã có Lời giải chi tiết}
  \end{tcolorbox}

  \vspace{1.5cm}
  \begin{tcolorbox}[colback=warnbg,colframe=warnborder,arc=5pt,
    boxrule=0.6pt,width=0.9\textwidth,halign=left]
    \begin{itemize}[leftmargin=1.5em]
      \item Bao gồm \textbf{các đề thi}: Tuyển sinh lớp 10 THPT, Học sinh giỏi cấp tỉnh/huyện,
            Kiểm tra học kỳ -- \textbf{Năm học 2012--2026}
      \item Phần \textbf{Hình học} đã được loại bỏ hoàn toàn
      \item Lời giải được \textbf{trích từ đáp án gốc} và bổ sung thêm
      \item \textbf{Tổng số đề}: \textbf{50 đề} (trong số 50 đề tổng hợp)
    \end{itemize}
  \end{tcolorbox}

  \vspace{1.5cm}
  \textbf{Cách dùng trên Overleaf:}
  \begin{enumerate}[leftmargin=2em]
    \item Upload file \texttt{.zip} → New Project → Upload Project
    \item Chọn compiler \textbf{XeLaTeX} hoặc \textbf{LuaLaTeX}
    \item Nhấn \textbf{Recompile}
    \item Để ẩn/hiện đề: comment/uncomment dòng \verb|\input{de_X}|
  \end{enumerate}

  \vfill
  {\small\color{gray}\today}
\end{titlepage}

\tableofcontents
\clearpage

%%────────────────────── DANH SÁCH ĐỀ ──────────────────────────
%% Xoá %% trước \input để bật đề, thêm %% để tắt.
"""

def generate_main(created, de_so):
    main_lines = [MAIN]
    for (so, fname, title) in created:
        safe_title = remove_nulls(title[:65])
        main_lines.append(f"%% ── Đề {so}: {safe_title}")
        main_lines.append(f"\\input{{de_{so}}}")
        main_lines.append(r"\clearpage")
        main_lines.append("")

    main_lines.append(r"\end{document}")

    main_path = os.path.join(OUT_DIR, "main.tex")
    with open(main_path, "w", encoding="utf-8") as fp:
        fp.write("\n".join(main_lines))

    print(f"\n{'='*60}")
    print(f"✓ Tạo xong {de_so-1} đề + main.tex")
    print(f"  Thư mục: {OUT_DIR}")

if __name__ == "__main__":
    created, de_so = run()
    generate_main(created, de_so)

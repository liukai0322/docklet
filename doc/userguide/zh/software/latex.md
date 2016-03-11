## LaTeX 示例 ##

Docklet 安装了[TeX Live 2015](http://www.tug.org/texlive)的全部包，可以
直接在 WEB Terminal中编写和编译LaTeX ，生成 pdf 文件，在 Jupyter
Dashboard 中打开 pdf 文件查看结果。

### Hello World

hello.tex 源码:

```latex
\documentclass{article}
\title{My \LaTeX ~Hello World}
\author{Zhang San}
\date{Feb 20, 2016}
\begin{document}
\maketitle
Hello World!
\end{document}
```

用`pdflatex` 或 `xelatex`编译:

```
$ xelatex hello
$ ls
hello.aux hello.log hello.pdf hello.tex 
```

### 中文支持 

TeX Live 2015 中，`xeCJK` + `xelatex`提供了对中文、日文、韩文等字体非常好的支持，
用户只需要使用`xeCJK`包即可以使用系统自带的中日韩矢量字体，不需要做任何字体生成工作。


让 hello.tex 包含中文 :

```latex
\documentclass{article}

\usepackage{xeCJK}  % CJK font support

\title{我的 \LaTeX ~世界你好}
\author{张三}
\date{2016年2月20日}
\begin{document}
\maketitle
世界，你好！
\end{document}
```

用`xelatex`编译

```
$ xelatex hello
$ ls
hello.aux hello.log hello.pdf hello.tex 
```

如果对系统自动选定的字体不满意，可以自己指定字体。

首先查看系统的中文字体:

```
$ fc-list :lang=zh
/usr/share/fonts/truetype/arphic/uming.ttc: AR PL UMing TW MBE:style=Light
/usr/share/fonts/truetype/arphic/ukai.ttc: AR PL UKai CN:style=Book
/usr/share/fonts/truetype/arphic/ukai.ttc: AR PL UKai HK:style=Book
/usr/share/fonts/truetype/arphic/ukai.ttc: AR PL UKai TW:style=Book
/usr/share/fonts/truetype/wqy/wqy-microhei.ttc: WenQuanYi Micro Hei,文泉驛微米黑,文泉驿微米黑:style=Regular
/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc: WenQuanYi Zen Hei,文泉驛正黑,文泉驿正黑:style=Regular
/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc: WenQuanYi Zen Hei Sharp,文泉驛點陣正黑,文泉驿点阵正黑:style=Regular
/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf: Droid Sans Fallback:style=Regular
/usr/share/fonts/truetype/arphic-gkai00mp/gkai00mp.ttf: AR PL KaitiM GB,文鼎ＰＬ简中楷:style=Regular
/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf: AR PL SungtiL GB,文鼎ＰＬ简报宋:style=Regular
/usr/share/fonts/truetype/arphic/ukai.ttc: AR PL UKai TW MBE:style=Book
/usr/share/fonts/truetype/arphic/uming.ttc: AR PL UMing TW:style=Light
/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc: WenQuanYi Zen Hei Mono,文泉驛等寬正黑,文泉驿等宽正黑:style=Regular
/usr/share/fonts/truetype/arphic/uming.ttc: AR PL UMing CN:style=Light
/usr/share/fonts/truetype/arphic/uming.ttc: AR PL UMing HK:style=Light
/usr/share/fonts/truetype/wqy/wqy-microhei.ttc: WenQuanYi Micro Hei Mono,文泉驛等寬微米黑,文泉驿等宽微米黑:style=Regular
```

指定 CJK 字体

```latex
\documentclass{article}

\usepackage{indentfirst}             % 中文首行缩进
\setlength{\parindent}{2em}          % 首行空两字

\usepackage{xeCJK}      % 中文字体支持
\setCJKmainfont[ItalicFont={AR PL KaitiM GB}]{AR PL KaitiM GB} % 缺省中文字体
\setCJKsansfont{WenQuanYi Zen Hei}      % 无衬线字体，可选设置
\setCJKmonofont{WenQuanYi Zen Hei Mono} % 等宽字体，可选设置 

\title{我的 \LaTeX ~程序}
\author{张三}
\date{2016年2月20日}
\begin{document}
\maketitle

\section{序言}

世界，你好！

\textbf{世界}，\textit{你好！}

\textsf{无衬线字体}，\texttt{等宽字体!}

\end{document}

```


### 一个完整的中文LaTeX 例子 

下面是来自北京大学于江生老师的一个例子，这里对[原文](https://wiki.freebsdchina.org/doc/x/xelatex) 
做了稍许修改，以方便编译测试:

```latex
\documentclass[12pt,a4paper]{article}                                                                            
\setlength{\parindent}{2em}          % 首行空两字
\usepackage{fontspec}                % 设置字体
%\setmainfont{宋体}
\usepackage{indentfirst}             % 首行缩进
\usepackage{xeCJK}                   % 中英文混排

\usepackage{tikz}

%%%%%%%%%% 数学符号公式 %%%%%%%%%%
\usepackage{amsmath}                 % AMS LaTeX宏包
%\usepackage{amssymb}                % 用来排版漂亮的数学公式
%\usepackage{amsbsy}
\usepackage{amsthm}
\usepackage{amsfonts}
\usepackage{mathrsfs}                % 英文花体字体
\usepackage{bm}                      % 数学公式中的黑斜体
\usepackage{bbding,manfnt}           % 一些图标，如 \dbend
\usepackage{lettrine}                % 首字下沉，命令\lettrine
\def\attention{\lettrine[lines=2,lraise=0,nindent=0em]{\large\textdbend\hspace{1mm}}{}}
%\usepackage{relsize}                 % 调整公式字体大小：\mathsmaller,\mathlarger
%\usepackage{caption2}                % 浮动图形和表格标题样式

%%%%%%%%%% 图形支持宏包 %%%%%%%%%%
\usepackage{graphicx}                % 嵌入png图像
\usepackage{color,xcolor}            % 支持彩色文本、底色、文本框等
%\usepackage{subfigure}
%\usepackage{epsfig}                 % 支持eps图像
%\usepackage{picinpar}               % 图表和文字混排宏包
%\usepackage[verbose]{wrapfig}       % 图表和文字混排宏包
%\usepackage{eso-pic}                % 向文档的部分页加n副图形, 可实现水印效果
%\usepackage{eepic}                  % 扩展的绘图支持
%\usepackage{curves}                 % 绘制复杂曲线
%\usepackage{texdraw}                % 增强的绘图工具
%\usepackage{treedoc}                % 树形图绘制
%\usepackage{pictex}                 % 可以画任意的图形
%\usepackage{hyperref}

%%%%%%%%%% 粘贴源代码 %%%%%%%%%%
\usepackage{listings}                 % 粘贴源代码
\lstloadlanguages{R, C, csh, make}    % 所要粘贴代码的编程语言
\lstdefinelanguage{Renhanced}[]{R}{%
    morekeywords={acf,ar,arima,arima.sim,colMeans,colSums,is.na,is.null,%
    mapply,ms,na.rm,nlmin,replicate,row.names,rowMeans,rowSums,seasonal,%
    sys.time,system.time,ts.plot,which.max,which.min},
    deletekeywords={c},
    alsoletter={.\%},%
    alsoother={:_\$}}
\newcommand{\indexfonction}[1]{\index{#1@\texttt{#1}}}
\lstset{language=Renhanced,tabsize=4, keepspaces=true,
    xleftmargin=2em,xrightmargin=0em, aboveskip=1em,
    backgroundcolor=\color{gray!20},  % 定义背景颜色
    frame=none,                       % 表示不要边框
    extendedchars=false,              % 解决代码跨页时，章节标题，页眉等汉字不显示的问题
    basicstyle=\small,
    keywordstyle=\color{black}\bfseries,
    breakindent=10pt,
    identifierstyle=,                 % nothing happens
    commentstyle=\color{blue}\small,  % 注释的设置
    morecomment=[l][\color{blue}]{\#},
    numbers=left,stepnumber=1,numberstyle=\scriptsize,
    showstringspaces=false,
    showspaces=false,
    flexiblecolumns=true,
    breaklines=true, breakautoindent=true,breakindent=4em,
    escapeinside={/*@}{@*/},
}

%%%%%%%%%% 正文 %%%%%%%%%%
\begin{document}
%%%%%%%%%% 定理类环境的定义 %%%%%%%%%%
%% 必须在导入中文环境之后
\newtheorem{example}{例}             % 整体编号
\newtheorem{algorithm}{算法}
\newtheorem{theorem}{定理}[section]  % 按 section 编号
\newtheorem{definition}{定义}
\newtheorem{axiom}{公理}
\newtheorem{property}{性质}
\newtheorem{proposition}{命题}
\newtheorem{lemma}{引理}
\newtheorem{corollary}{推论}
\newtheorem{remark}{注解}
\newtheorem{condition}{条件}
\newtheorem{conclusion}{结论}
\newtheorem{assumption}{假设}

%%%%%%%%%% 一些重定义 %%%%%%%%%%
\renewcommand{\contentsname}{目录}     % 将Contents改为目录
\renewcommand{\abstractname}{摘要}     % 将Abstract改为摘要
\renewcommand{\refname}{参考文献}      % 将References改为参考文献
\renewcommand{\indexname}{索引}
\renewcommand{\figurename}{图}
\renewcommand{\tablename}{表}
\renewcommand{\appendixname}{附录}
\renewcommand{\proofname}{证明}
\renewcommand{\algorithm}{算法}

%%%%%%%%%% 论文标题、作者等 %%%%%%%%%%
\title{用\LaTeX 写科技论文\thanks{这是一个为初学者写的\TeX 论文模板，
未经作者允许可以随意下载使用并修改传播，目的是让更多的人迅速上手用\TeX 系统写作。}
       }
\author{于江生，北京大学计算机系}
%\date{2008年10月01日}                % 日期
\date{}
\maketitle                            % 生成标题
\tableofcontents                      % 插入目录
\thispagestyle{empty}                 % 首页无页眉页脚

\begin{abstract}
\noindent 这是一个简单的中文\TeX 模板，为\TeX 的初学者提供便利上手的参照。
该模板在 \TeX Live 下通过xelatex命令生成PDF文件，适合在类UNIX操作系统下工作的朋友从一个简单的模板出发，
不断地提升对\TeX 的认识。注意：若想用 xelatex命令，\TeX 文件必须按照 UTF-8 编码保存。
因为 Xe\TeX 是一种使用 Unicode 编码的 \TeX 系统，它对中文的支持是发自肺腹的，免去了繁复的配置。
\end{abstract}

%\PencilRightUp % 一些可爱的图标，需要bbding宏包的支持
公元1974年，ACM图灵奖授予了Standford大学教授\index{Donald E. Knuth} Donald E. Knuth （高德纳），
表彰他在算法和程序语言设计等多方面杰出的成就。他的巨著 The Art of Computer Programming 令人震撼。
另外，Knuth的突出贡献还包括\index{\TeX 系统} \TeX 系统，毫不夸张地评价，\TeX 给排版带来了一场革命。
%%%%%%%%%% section %%%%%%%%%%
\section{编辑数学公式}
\indent   % 恢复缩进
Knuth 用\$ 符号界定数学公式，暗指着每个好的公式都是无价之宝。有了\TeX 系统，输入数学公式变得简单愉快。如，

\begin{theorem}[L\'{e}vy\index{L\'{e}vy 定理}]
令 $F(x),\varphi(t)$ 分别为随机变量 $X$ 的分布函数和特征函数。
假定 $F(x)$ 在 $a+h$ 和 $a-h (h>0)$ 处连续，则有
\begin{align}
 \label{Levy theorem}  % 方程的标记可以是专有名词
F(a+h)-F(a-h)&=\lim_{T\rightarrow\infty}\frac{1}{\pi}\int^{T}_{-T}\frac{\sin ht}{t} 
e^{-ita}\varphi(t)dt
\end{align}
\end{theorem}
\begin{proof}
  从略。感兴趣的读者可以参考……。
\end{proof}


\begin{corollary}
密度函数和特征函数之间有如下的关系。
\begin{align}
 \label{DensityCharacteristic}   % 自定义的标记
  f(x)&=\frac{1}{2\pi}\int^{+\infty}_{-\infty} e^{-itx}\varphi(t)dt
\end{align}
\end{corollary}

\begin{proof}
由公式 (\ref{Levy theorem}) 和 Lebesgue 定理，我们有
\begin{align*}
 \frac{F(x+\Delta x)-F(x)}{\Delta x}&=\frac{1}{2\pi}\int^{+\infty}_{-\infty}
 \frac{\sin(t\Delta x/2)}{t\Delta x/2} e^{-it(x+\Delta x/2)}\varphi(t) dt\\
  f(x)&=\frac{1}{2\pi}\int^{+\infty}_{-\infty}\lim_{\Delta x\rightarrow 0}
 \frac{\sin(t\Delta x/2)}{t\Delta x/2} e^{-it(x+\Delta x/2)}\varphi(t) dt\\
  &=\frac{1}{2\pi}\int^{+\infty}_{-\infty} e^{-itx}\varphi(t)dt\qedhere
\end{align*}
\end{proof}

我们知道特征函数的定义是

\begin{align}
 \label{section1:characteristic}   % 标记中注明了章节号
 \varphi(t)&= E(e^{itX})=\int^{+\infty}_{-\infty} e^{itx} f(x)dx
\end{align}

L\'{e}vy 定理在分布函数和特征函数之间搭建了一座桥梁。
对比 (\ref{DensityCharacteristic}) 和 (\ref{section1:characteristic}) 可见，
密度函数和特征函数之间的关系非常巧妙。

                                                                                                                 
\attention 在\TeX 环境里，数学公式的表达是很自然的，绝大多数命令就是英文的数学专有名词或它们的缩写，
如果你以前读过英文的数学文献，记忆这些命令是不难的。如果你没读过，正好通过记忆这些命令来了解术语。


手头有个命令快速寻查表是很方便的，我用的是 Hypertext Help with \LaTeX，网上可以搜到，是免费的。

%%%%%%%%%%% section %%%%%%%%%%
\section{图形表格等浮动对象}

\index{贝叶斯方法}贝叶斯方法\cite{Gelman} 主要用于小样本数据分析，它利用参数先验分布和
后验分布之差异进行统计推断，其一般步骤是：

\begin{enumerate}
 \item 构建概率模型，包括参数的先验分布。
 \item 给定观察数据，计算参数的后验分布。
 \item 分析模型的效果，如有必要，回到第一步。
\end{enumerate}

\begin{example}
下面，我们给一个表格的例子，一个图形的例子。

\begin{center}
\begin{table}[!ht]     % 强制在原位显示表格
\centering
\caption{二维随机向量$(X,Y)$的边缘分布}
\begin{tabular}{l|ccccc|c}
  $_X$\hspace{3mm} $^Y$&$y_1$&$y_2$&$\cdots$&$y_j$&$\cdots$\\
\hline
$x_1$   &$p_{11}$&$p_{12}$&$\cdots$&$p_{1j}$&$\cdots$&$p_{1\cdot}$\\
$x_2$   &$p_{21}$&$p_{22}$&$\cdots$&$p_{2j}$&$\cdots$&$p_{2\cdot}$\\
$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$\\
$x_i$   &$p_{i1}$&$p_{i2}$&$\cdots$&$p_{ij}$&$\cdots$&$p_{i\cdot}$\\
$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$&$\vdots$\\
\hline
   &$p_{\cdot 1}$&$p_{\cdot 2}$&$\cdots$&$p_{\cdot j}$&$\cdots$&1
\label{marginal distribution}
\end{tabular}
\end{table}
\end{center}

在表\ref{marginal distribution} 中，$p_{\cdot j}=\sum\limits_i p_{ij}$，
类似地，$ p_{i\cdot}=\sum\limits_j p_{ij}$。
\end{example}

% 插入一个图片
%\begin{center}
%\begin{figure}[!h]
%\centering
%\includegraphics[width=0.95\textwidth]{knot.png}
%\caption{吞尾的环面和纽结，由 Maxima 绘制。\hfill\mbox{}}
%\label{torus and knot}
%\end{figure}
%\end{center}

%原文用的是knot.png文件，这里采用了一个在latex中直接画图的例子
图 \ref{tikz graph} 是来自 http://www.texample.net/ 的一个tikz示例。

\begin{center}
\begin{figure}[!hbt]
\centering
\scalebox{0.8}{
\begin{tikzpicture}[level/.style={sibling distance=60mm/#1}]
\node [circle,draw] (z){$n$}
  child {node [circle,draw] (a) {$\frac{n}{2}$}
    child {node [circle,draw] (b) {$\frac{n}{2^2}$}
      child {node {$\vdots$}
        child {node [circle,draw] (d) {$\frac{n}{2^k}$}}
        child {node [circle,draw] (e) {$\frac{n}{2^k}$}}
      } 
      child {node {$\vdots$}}
    }
    child {node [circle,draw] (g) {$\frac{n}{2^2}$}
      child {node {$\vdots$}}
      child {node {$\vdots$}}
    }
  }
  child {node [circle,draw] (j) {$\frac{n}{2}$}
    child {node [circle,draw] (k) {$\frac{n}{2^2}$}
      child {node {$\vdots$}}
      child {node {$\vdots$}}
    }
  child {node [circle,draw] (l) {$\frac{n}{2^2}$}
    child {node {$\vdots$}}
    child {node (c){$\vdots$}
      child {node [circle,draw] (o) {$\frac{n}{2^k}$}}
      child {node [circle,draw] (p) {$\frac{n}{2^k}$}
        child [grow=right] {node (q) {$=$} edge from parent[draw=none]
          child [grow=right] {node (q) {$O_{k = \lg n}(n)$} edge from parent[draw=none]
            child [grow=up] {node (r) {$\vdots$} edge from parent[draw=none]
              child [grow=up] {node (s) {$O_2(n)$} edge from parent[draw=none]
                child [grow=up] {node (t) {$O_1(n)$} edge from parent[draw=none]
                  child [grow=up] {node (u) {$O_0(n)$} edge from parent[draw=none]}
                }
              }
            }
            child [grow=down] {node (v) {$O(n \cdot \lg n)$}edge from parent[draw=none]}
          }
        }
      }
    }
  }
};
\path (a) -- (j) node [midway] {+};
\path (b) -- (g) node [midway] {+};
\path (k) -- (l) node [midway] {+};
\path (k) -- (g) node [midway] {+};
\path (d) -- (e) node [midway] {+};
\path (o) -- (p) node [midway] {+};
\path (o) -- (e) node (x) [midway] {$\cdots$}
  child [grow=down] {
    node (y) {$O\left(\displaystyle\sum_{i = 0}^k 2^i \cdot \frac{n}{2^i}\right)$}
    edge from parent[draw=none]
  };
\path (q) -- (r) node [midway] {+};
\path (s) -- (r) node [midway] {+};
\path (s) -- (t) node [midway] {+};
\path (s) -- (l) node [midway] {=};
\path (t) -- (u) node [midway] {+};
\path (z) -- (u) node [midway] {=};
\path (j) -- (t) node [midway] {=};
\path (y) -- (x) node [midway] {$\Downarrow$};
\path (v) -- (y)
  node (w) [midway] {$O\left(\displaystyle\sum_{i = 0}^k n\right) = O(k \cdot n)$};
\path (q) -- (v) node [midway] {=};
\path (e) -- (x) node [midway] {+};
\path (o) -- (x) node [midway] {+};
\path (y) -- (w) node [midway] {$=$};
\path (v) -- (w) node [midway] {$\Leftrightarrow$};
\path (r) -- (c) node [midway] {$\cdots$};
\end{tikzpicture}}
\caption{一个简单的tikz/pgf图例}
\label{tikz graph}
\end{figure}
\end{center}


%%%%%%%%%%% section %%%%%%%%%%
\section{如何张贴源码？}
使用 listings 宏包，可以将R、Maxima等语言的源码以某种固定的模式张贴出来。譬如，

\begin{lstlisting}
## 生日问题：n <= 365 个人中至少两人生日相同的概率？
## 输出: n 个人当中至少两人生日相同的概率 P(A)
## 注意：R 语言中，变量有大小写的区分
N <- 365                      # 一年的天数
n <- 50                       # 选取的人数。
InitProb  <- matrix(1,n,1)    # 一个 n 维的列向量的初始化

## 计算 n 个人当中没有人生日相同的概率
for (i in 2:n){
  InitProb[i] <- InitProb[i-1] * (N-i+1)/N
}
Prob <- 1 - InitProb          # 生日问题的解，输出一个 n 维列向量
idx  <- n - sum(Prob>0.5) + 1 # 概率大于 50% 所需最少人数
\end{lstlisting}

%%%%%%%%%%% section %%%%%%%%%%
\section{后记}
这个\TeX 模板只是为了提供一个学习\TeX 的参考，各节的内容并没有关联性。欢迎读者使用并改进该模板，
并祝学习\TeX 愉快！

Knuth大师最初设计\TeX 的时候并没有想到中文化，\TeX 排版系统的中文化始终令初学者望而却步、云山雾罩。
类UNIX系统下的teTeX和Windows系统下的MikTeX，都是\TeX 知名的发行版。然而，teTeX已经停止研发五年之久，
基于MikTeX的中文发行版CTeX 虽然如火如荼，但依然挡不住\TeX Live 一统江湖的大趋势。

虽然\TeX Live 还未入住FreeBSD的ports tree，但teTeX的远去，
令FreeBSD之下的很多ports不得不面临改换门庭的窘境。例如，auctex、latex-cjk等等。


\TeX 的中文化可以有多种途径，xelatex 是其中最简单的（不见得是最美观的）。
在\TeX Live 2011 之下，不需要有任何更多的设置，甚至不用考虑中英文混排，
xelatex能满足绝大多数中文化要求。这对于初学者来说，无疑是一个福音。


%%%%%%%%%% 参考文献 %%%%%%%%%%
\begin{thebibliography}{}
\bibitem[Gelman et al., 2004]{Gelman} Gelman, A., Carlin, J. B., Stern, H. S. \& Rubin, D. B.
 (2004) Bayesian Data Analysis (Second Edition). \newblock Chapman \& Hall/CRC.
\end{thebibliography}
\clearpage
\end{document}
%%%%%%%%%% 结束 %%%%%%%%%%
```

用xelatex 编译后可以生成中文 pdf 文件。

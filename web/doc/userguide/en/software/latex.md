## LaTeX Example ##

Docklet provides the full [TeX Live 2015](http://www.tug.org/texlive). 
Users can edit and compile LaTeX source files, generating pdf files in
WEB Terminal. Then open the resulting pdf file in Jupyter Dashboard to
check the output.

### Hello World

A very simple `hello.tex` :

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

Compile using `pdflatex` or `xelatex`:

```
$ xelatex hello
$ ls
hello.aux hello.log hello.pdf hello.tex 
```

### CJK Char Support ### 

In TeX Live 2015, `xeCJK` + `xelatex` provides very good support for CJK  and any other 
non-ASCII chars. For CJK users, they only need to use the `xeCJK` package in their source file,
and then comile using `xelatex`, which will automatially use the
available truetype fonts in the system path, usually `/usr/share/fonts`.  No extra work needed. 


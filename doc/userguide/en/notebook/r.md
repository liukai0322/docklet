## R Packages ##

### Recommended R Packages ###

The article [Quick list of useful R packages](https://support.rstudio.com/hc/en-us/articles/201057987-Quick-list-of-useful-R-packages) gives a list of recommended R packages.

<p>Many useful R function come in packages, free libraries of code written by R's active user community. To install an R package, open an R session and type at the command line</p>
<pre><code class="r">install.packages("&lt;the package's name&gt;")
</code></pre>
<p>R will download the package from CRAN, so you'll need to be connected to the internet. Once you have a package installed, you can make its contents available to use in your current R session by running</p>
<pre><code class="r">library("&lt;the package's name&gt;")
</code></pre>
<p>There are thousands of helpful R packages for you to use, but navigating them all can be a challenge. To help you out, we've compiled this guide to some of the best. We've used each of these, and found them to be outstanding – we've even written some of them. But you don't have to take our word for it, these packages are also some of the top most downloaded R packages.</p>
<h4>To load data</h4>
<p><a href="https://cran.rstudio.com/web/packages/RODBC">RODBC</a>, <a href="http://www.rdocumentation.org/packages/RMySQL/functions/RMySQL-package">RMySQL</a>, <a title="Link: http://www.rdocumentation.org/packages/RPostgresSQL" href="http://www.rdocumentation.org/packages/RPostgresSQL">RPostgresSQL</a>, <a title="Link: http://www.rdocumentation.org/packages/RSQLite" href="http://www.rdocumentation.org/packages/RSQLite">RSQLite</a> - If you'd like to read in data from a database, these packages are a good place to start. Choose the package that fits your type of database.</p>
<p><a href="https://cran.rstudio.com/web/packages/XLConnect">XLConnect</a>, <a href="https://cran.rstudio.com/web/packages/xlsx">xlsx</a> - These packages help you read and write Micorsoft Excel files from R. You can also just export your spreadsheets from Excel as .csv's.</p>
<p><a href="http://www.rdocumentation.org/packages/foreign">foreign</a> - Want to read a SAS data set into R? Or an SPSS data set? Foreign provides functions that help you load data files from other programs into R.</p>
<p>R can handle plain text files – no package required. Just use the functions read.csv, read.table, and read.fwf. If you have even more exotic data, consult the CRAN <a href="https://cran.rstudio.com/doc/manuals/R-data.pdf">guide</a> to data import and export.</p>

<h4>To manipulate data</h4>

<p><a href="http://blog.rstudio.org/2014/01/17/introducing-dplyr/">dplyr</a> - Essential shortcuts for subsetting, summarizing, rearranging, and joining together data sets. dplyr is our go to package for fast data manipulation.</p>
<p><a href="http://blog.rstudio.org/2014/07/22/introducing-tidyr/">tidyr</a> - Tools for changing the layout of your data sets. Use the gather and spread functions to convert your data into the <a href="http://www.jstatsoft.org/v59/i10/paper">tidy format</a>, the layout R likes best.</p>
<p><a href="http://journal.r-project.org/archive/2010-2/RJournal_2010-2_Wickham.pdf">stringr</a> - Easy to learn tools for regular expressions and character strings.</p>
<p><a href="http://www.r-statistics.com/2012/03/do-more-with-dates-and-times-in-r-with-lubridate-1-1-0/">lubridate</a> - Tools that make working with dates and times easier.</p>

<h4>To visualize data</h4>

<p><a href="http://docs.ggplot2.org/current/">ggplot2</a> - R's famous package for making beautiful graphics. ggplot2 lets you use the <a href="http://vita.had.co.nz/papers/layered-grammar.pdf">grammar of graphics</a> to build layered, customizable plots.</p>
<p><a href="http://ggvis.rstudio.com">ggvis</a> - Interactive, web based graphics built with the grammar of graphics.</p>
<p><a href="http://rgl.neoscientists.org/about.shtml">rgl</a> - Interactive 3D visualizations with R</p>
<p><a href="http://www.htmlwidgets.org/">htmlwidgets</a> - A fast way to build interactive (javascript based) visualizations with R. Packages that implement htmlwidgets include:</p>
<ul>
<li><a href="http://rstudio.github.io/leaflet/">leaflet</a> (maps)</li>
<li><a href="http://rstudio.github.io/dygraphs">dygraphs</a> (time series)</li>
<li><a href="http://rstudio.github.io/DT/">DT</a> (tables)</li>
<li><a href="http://rich-iannone.github.io/DiagrammeR/">diagrammeR</a> (diagrams)</li>
<li><a href="http://christophergandrud.github.io/networkD3/">network3D</a> (network graphs)</li>
<li><a href="https://github.com/bwlewis/rthreejs">threeJS</a> (3D scatterplots and globes).</li>
</ul>
<p> </p>
<p><a href="https://cran.rstudio.com/web/packages/googleVis">googleVis</a> - Let's you use Google Chart tools to visualize data in R. Google Chart tools used to be called Gapminder, the graphing software Hans Rosling made famous in hie TED talk.</p>

<h4>To model data</h4>

<p><a href="http://www.rdocumentation.org/packages/car">car</a> - car's <a href="http://www.rdocumentation.org/packages/car/functions/Anova">Anova</a> function is popular for making type II and type III Anova tables.</p>
<p><a href="http://www.rdocumentation.org/packages/mgcv/functions/mgcv-package">mgcv</a> - Generalized Additive Models</p>
<p><a href="http://www.rdocumentation.org/packages/lme4/functions/lme4-package">lme4</a>/<a href="http://www.rdocumentation.org/packages/nlme/functions/nlme">nlme</a> - Linear and Non-linear mixed effects models</p>
<p><a href="http://www.rdocumentation.org/packages/randomForest/functions/randomForest">randomForest</a> - Random forest methods from machine learning</p>
<p><a href="http://www.rdocumentation.org/packages/multcomp">multcomp</a> - Tools for multiple comparison testing</p>
<p><a href="http://www.rdocumentation.org/packages/vcd">vcd</a> - Visualization tools and tests for categorical data</p>
<p><a href="http://www.rdocumentation.org/packages/glmnet/functions/glmnet">glmnet</a> - Lasso and elastic-net regression methods with cross validation</p>
<p><a href="http://www.rdocumentation.org/packages/survival">survival</a> - Tools for survival analysis</p>
<p><a href="https://cran.rstudio.com/web/packages/caret">caret</a> - Tools for training regression and classification models</p>

<h4>To report results</h4>

<p><a href="http://shiny.rstudio.com">shiny</a> - Easily make interactive, web apps with R. A perfect way to explore data and share findings with non-programmers.</p>
<p><a href="https://rmarkdown.rstudio.com/">R Markdown</a> - The perfect workflow for reproducible reporting. Write R code in your <a href="http://daringfireball.net/projects/markdown/">markdown</a> reports. When you run render, R Markdown will replace the code with its results and then export your report as an HTML, pdf, or MS Word document, or a HTML or pdf slideshow. The result? Automated reporting. R Markdown is integrated straight into RStudio.</p>
<p><a href="http://www.rdocumentation.org/packages/xtable/functions/xtable">xtable</a> - The <a href="http://www.rdocumentation.org/packages/xtable/functions/xtable">xtable</a> function takes an R object (like a data frame) and returns the latex or HTML code you need to paste a pretty version of the object into your documents. Copy and paste, or pair up with R Markdown.</p>

<h4>For Spatial data</h4>

<p><a href="https://cran.rstudio.com/web/packages/sp">sp</a>, <a href="http://www.rdocumentation.org/packages/maptools">maptools</a> - Tools for loading and using spatial data including shapefiles.</p>
<p><a href="http://www.rdocumentation.org/packages/maps">maps</a> - Easy to use map polygons for plots.</p>
<p><a href="http://journal.r-project.org/archive/2013-1/kahle-wickham.pdf">ggmap</a> - Download street maps straight from Google maps and use them as a background in your ggplots.</p>

<h4>For Time Series and Financial data</h4>

<p><a href="https://cran.rstudio.com/web/packages/zoo">zoo</a> - Provides the most popular format for saving time series objects in R.</p>
<p><a href="https://cran.rstudio.com/web/packages/xts">xts</a> - Very flexible tools for manipulating time series data sets.</p>
<p><a href="http://www.quantmod.com/">quantmod</a> - Tools for downloading financial data, plotting common charts, and doing technical analysis.</p>

<h4>To write high performance R code</h4>

<p><a href="http://dirk.eddelbuettel.com/code/rcpp.html">Rcpp</a> - Write R functions that call C++ code for lightning fast speed.</p>
<p><a href="http://www.rdocumentation.org/packages/data.table">data.table</a> - An alternative way to organize data sets for very, very fast operations. Useful for big data.</p>
<p><a href="http://www.rdocumentation.org/packages/parallel/functions/parallel-package">parallel</a> - Use parallel processing in R to speed up your code or to crunch large data sets.</p>

<h4>To work with the web</h4>

<p><a href="http://www.omegahat.org/RSXML/shortIntro.pdf">XML</a> - Read and create XML documents with R</p>
<p><a href="https://cran.rstudio.com/web/packages/jsonlite">jsonlite</a> - Read and create JSON data tables with R</p>
<p><a href="http://www.rdocumentation.org/packages/httr/functions/httr">httr</a> - A set of useful tools for working with http connections</p>

<h4>To write your own R packages</h4>

<p><a href="https://www.rstudio.com/projects/devtools/">devtools</a> - An essential suite of tools for turning your code into an R package.</p>
<p><a href="http://journal.r-project.org/archive/2011-1/RJournal_2011-1_Wickham.pdf">testthat</a> - testthat provides an easy way to write unit tests for your code projects.</p>
<p><a href="http://www.rdocumentation.org/packages/roxygen2">roxygen2</a> - A quick way to document your R packages. roxygen2 turns inline code comments into documentation pages and builds a package namespace.</p>
<p>You can also read about the entire package development process online in Hadley Wickham's <a href="http://r-pkgs.had.co.nz/">R Packages</a> book</p>


### Top 100 R packages for 2013 (Jan-May) 

[This article](http://www.r-statistics.com/2013/06/top-100-r-packages-for-2013-jan-may/) gave a statistics report about the most downloaded R packages in 2013: 

<table cellspacing="0" cellpadding="0" class="t1">
  <tbody>
    <tr>
      <td valign="middle" class="td1">
        <p class="p1"><span class="s1"><b></b></span><br></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1"><b>Package</b></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1"><b>Title</b></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1"><b>Downloads</b></span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">1</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/plyr/">plyr<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Tools for splitting, applying and combining data</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">84049</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">2</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/digest/">digest<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Create cryptographic hash digests of R objects</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">83192</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">3</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/ggplot2/">ggplot2<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">An implementation of the Grammar of Graphics</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">82768</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">4</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/colorspace/">colorspace<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Color Space Manipulation</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">81901</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">5</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/stringr/">stringr<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Make it easier to work with strings</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">77658</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">6</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/RColorBrewer/">RColorBrewer<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">ColorBrewer palettes</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">66783</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">7</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/reshape2/">reshape2<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Flexibly reshape data: a reboot of the reshape package</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">64911</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">8</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/zoo/">zoo<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">S3 Infrastructure for Regular and Irregular Time Series (Z’s</span></p>
        <p class="p3"><span class="s1">ordered observations)</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">60844</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">9</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/proto/">proto<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Prototype object-based programming</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">59043</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">10</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/scales/">scales<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Scale functions for graphics</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">58369</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">11</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/car/">car<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Companion to Applied Regression</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">57453</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">12</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/dichromat/">dichromat<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Color Schemes for Dichromats</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">56624</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">13</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/gtable/">gtable<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Arrange grobs in tables</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">54431</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">14</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/munsell/">munsell<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Munsell colour system</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">53183</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">15</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/labeling/">labeling<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Axis Labeling</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">51877</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">16</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/Hmisc/">Hmisc<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Harrell Miscellaneous</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">47836</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">17</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/rJava/">rJava<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Low-level R to Java interface</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">47731</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">18</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/mvtnorm/">mvtnorm<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Multivariate Normal and t Distributions</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">46884</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">19</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/bitops/">bitops<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Bitwise Operations</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">45689</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">20</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/rgl/">rgl<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">3D visualization device system (OpenGL)</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">41001</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">21</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/foreign/">foreign<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Read Data Stored by Minitab, S, SAS, SPSS, Stata, Systat, dBase,</span></p>
        <p class="p3"><span class="s1">..</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">37849</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">22</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/XML/">XML<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Tools for parsing and generating XML within R and S-Plus</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">37153</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">23</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/lattice/">lattice<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Lattice Graphics</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">36597</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">24</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/e1071/">e1071<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Misc Functions of the Department of Statistics (e1071), TU Wien</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">35180</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">25</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/gtools/">gtools<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Various R programming tools</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">35028</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">26</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/sp/">sp<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">classes and methods for spatial data</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">34786</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">27</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/gdata/">gdata<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Various R programming tools for data manipulation</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">34262</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">28</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/Rcpp/">Rcpp<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Seamless R and C++ Integration</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">33929</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">29</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/MASS/">MASS<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Support Functions and Datasets for Venables and Ripley’s MASS</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">33667</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">30</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/Matrix/">Matrix<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Sparse and Dense Matrix Classes and Methods</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">30740</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">31</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/lmtest/">lmtest<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Testing Linear Regression Models</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">30319</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">32</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/survival/">survival<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Survival Analysis</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">30186</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">33</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/caTools/">caTools<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Tools: moving window statistics, GIF, Base64, ROC AUC, etc</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">29945</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">34</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/multcomp/">multcomp<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Simultaneous Inference in General Parametric Models</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">29871</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">35</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/RCurl/">RCurl<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">General network (HTTP/FTP/…) client interface for R</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">28866</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">36</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/knitr/">knitr<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">A general-purpose package for dynamic report generation in R</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">28104</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">37</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/xtable/">xtable<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Export tables to LaTeX or HTML</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">28091</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">38</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/xts/">xts<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">eXtensible Time Series</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">28058</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">39</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/rpart/">rpart<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Recursive Partitioning</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">27812</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">40</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/evaluate/">evaluate<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Parsing and evaluation tools that provide more details than the</span></p>
        <p class="p3"><span class="s1">default</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">27617</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">41</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/RODBC/">RODBC<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">ODBC Database Access</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">26131</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">42</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/quadprog/">quadprog<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Functions to solve Quadratic Programming Problems</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">25433</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">43</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/tseries/">tseries<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Time series analysis and computational finance</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">25144</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">44</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/DBI/">DBI<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">R Database Interface</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">24793</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">45</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/nlme/">nlme<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Linear and Nonlinear Mixed Effects Models</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">24360</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">46</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/lme4/">lme4<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Linear mixed-effects models using S4 classes</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">24199</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">47</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/reshape/">reshape<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Flexibly reshape data</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">24118</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">48</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/sandwich/">sandwich<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Robust Covariance Matrix Estimators</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">24016</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">49</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/leaps/">leaps<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">regression subset selection</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">23666</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">50</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/gplots/">gplots<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Various R programming tools for plotting data</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">23251</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">51</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/abind/">abind<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Combine multi-dimensional arrays</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">22758</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">52</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/randomForest/">randomForest<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Breiman and Cutler’s random forests for classification and</span></p>
        <p class="p3"><span class="s1">regression</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">22401</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">53</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/Rcmdr/">Rcmdr<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">R Commander</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">22131</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">54</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/coda/">coda<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Output analysis and diagnostics for MCMC</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">21900</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">55</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/maps/">maps<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Draw Geographical Maps</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">21550</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">56</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/igraph/">igraph<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Network analysis and visualization</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">21423</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">57</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/formatR/">formatR<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Format R Code Automatically</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">21049</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">58</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/maptools/">maptools<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Tools for reading and handling spatial objects</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">20957</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">59</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/RSQLite/">RSQLite<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">SQLite interface for R</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">19671</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">60</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/psych/">psych<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Procedures for Psychological, Psychometric, and Personality</span></p>
        <p class="p3"><span class="s1">Research</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">19545</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">61</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/KernSmooth/">KernSmooth<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Functions for kernel smoothing for Wand &amp;amp Jones (1995)</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">19166</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">62</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/rgdal/">rgdal<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Bindings for the Geospatial Data Abstraction Library</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">19064</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">63</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/RcppArmadillo/">RcppArmadillo<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Rcpp integration for Armadillo templated linear algebra library</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">18899</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">64</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/effects/">effects<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Effect Displays for Linear, Generalized Linear,</span></p>
        <p class="p3"><span class="s1">Multinomial-Logit, Proportional-Odds Logit Models and</span></p>
        <p class="p3"><span class="s1">Mixed-Effects Models</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">18843</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">65</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/sem/">sem<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Structural Equation Models</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">18711</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">66</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/vcd/">vcd<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Visualizing Categorical Data</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">18589</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">67</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/XLConnect/">XLConnect<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Excel Connector for R</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">18230</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">68</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/markdown/">markdown<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Markdown rendering for R</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">18211</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">69</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/timeSeries/">timeSeries<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Rmetrics – Financial Time Series Objects</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">17932</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">70</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/timeDate/">timeDate<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Rmetrics – Chronological and Calendar Objects</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">17838</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">71</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/RJSONIO/">RJSONIO<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Serialize R objects to JSON, JavaScript Object Notation</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">17801</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">72</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/cluster/">cluster<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Cluster Analysis Extended Rousseeuw et al</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">17136</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">73</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/scatterplot3d/">scatterplot3d<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">3D Scatter Plot</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">17110</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">74</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/nnet/">nnet<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Feed-forward Neural Networks and Multinomial Log-Linear Models</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">17074</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">75</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/fBasics/">fBasics<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Rmetrics – Markets and Basic Statistics</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">16278</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">76</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/forecast/">forecast<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Forecasting functions for time series and linear models</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">15638</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">77</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/quantreg/">quantreg<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Quantile Regression</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">15509</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">78</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/foreach/">foreach<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Foreach looping construct for R</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">15405</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">79</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/chron/">chron<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Chronological objects which can handle dates and times</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">15226</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">80</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/plotrix/">plotrix<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Various plotting functions</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">15142</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">81</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/matrixcalc/">matrixcalc<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Collection of functions for matrix calculations</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">15107</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">82</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/aplpack/">aplpack<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Another Plot PACKage: stem.leaf, bagplot, faces, spin3R, and</span></p>
        <p class="p3"><span class="s1">some slider functions</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">14654</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">83</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/strucchange/">strucchange<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Testing, Monitoring, and Dating Structural Changes</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">14503</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">84</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/iterators/">iterators<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Iterator construct for R</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">14449</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">85</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/mgcv/">mgcv<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Mixed GAM Computation Vehicle with GCV/AIC/REML smoothness</span></p>
        <p class="p3"><span class="s1">estimation</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">14186</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">86</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/kernlab/">kernlab<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Kernel-based Machine Learning Lab</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">14135</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">87</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/SparseM/">SparseM<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Sparse Linear Algebra</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">13921</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">88</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/tree/">tree<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Classification and regression trees</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">13871</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">89</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/robustbase/">robustbase<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Basic Robust Statistics</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">13778</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">90</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/vegan/">vegan<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Community Ecology Package</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">13686</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">91</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/devtools/">devtools<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Tools to make developing R code easier</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">13488</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">92</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/latticeExtra/">latticeExtra<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Extra Graphical Utilities Based on Lattice</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">13253</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">93</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/modeltools/">modeltools<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Tools and Classes for Statistical Models</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">13233</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">94</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/xlsx/">xlsx<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Read, write, format Excel 2007 and Excel 97/2000/XP/2003 files</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">13097</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">95</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/slam/">slam<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Sparse Lightweight Arrays and Matrices</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">13060</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">96</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/TTR/">TTR<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Technical Trading Rules</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">12894</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">97</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/quantmod/">quantmod<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Quantitative Financial Modelling Framework</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">12892</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">98</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/relimp/">relimp<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Relative Contribution of Effects in a Regression Model</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">12692</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">99</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/akima/">akima<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Interpolation of irregularly spaced data</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">12680</span></p>
      </td>
    </tr>
    <tr>
      <td valign="middle" class="td1">
        <p class="p3"><span class="s1">100</span></p>
      </td>
      <td valign="middle" class="td1">
        <p class="p4"><span class="s1"><a href="http://cran.r-project.org/web/packages/memoise/">memoise<span class="s2"></span></a></span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">Memoise functions</span></p>
      </td>
      <td valign="middle" class="td2">
        <p class="p3"><span class="s1">12600</span></p>
      </td>
    </tr>
  </tbody>
</table>

### R Packages in Docklet ###

The Docklet base image provides the `r-base`，`r-recommended`，`r-cran-*`, i.e., 
all available R packages in Ubuntu apt sources, 

Here is the list:

 * r-base - GNU R statistical computation and graphics system
 * r-base-core - GNU R core of statistical computation and graphics system
 * r-base-core-dbg - GNU R debug symbols for statistical comp. language and environment
 * r-base-dev - GNU R installation of auxiliary GNU R packages
 * r-base-html - GNU R html docs for statistical computing system functions
 * r-bioc-qvalue - GNU R package for Q-value estimation for FDR control
 * r-cran-abind - GNU R abind multi-dimensional array combination function
 * r-cran-acepack - GNU R package for regression transformations
 * r-cran-ade4 - GNU R analysis of ecological data
 * r-cran-afex - GNU R package for analyzing factorial experiments using ANOVA or mixed models
 * r-cran-amelia - GNU R package supporting multiple imputation of missing data
 * r-cran-amore - GNU R: A MORE flexible neural network package
 * r-cran-ape - GNU R package for Analyses of Phylogenetics and Evolution
 * r-cran-base64enc - GNU R package that provides tools for base64 encoding
 * r-cran-batchjobs - GNU R batch computing
 * r-cran-bayesfactor - GNU R package providing Bayes factors for t-tests, ANOVAs and contingency tables
 * r-cran-bayesm - GNU R package for Bayesian inference
 * r-cran-bbmisc - GNU R Miscellaneous helper functions for B. Bischl
 * r-cran-beeswarm - bee swarm plot, an alternative to stripchart
 * r-cran-biasedurn - GNU R Biased Urn model distributions
 * r-cran-bio3d - GNU R package for biological structure analysis
 * r-cran-bitops - GNU R package implementing bitwise operations
 * r-cran-blockmodeling - Generalized and classical blockmodeling of valued networks
 * r-cran-bms - GNU R package for Bayesian model averaging for linear models
 * r-cran-boolnet - assembling, analyzing and visualizing Boolean networks
 * r-cran-boot - GNU R package for bootstrapping functions from Davison and Hinkley
 * r-cran-bradleyterry2 - GNU R package for using Bradley-Terry models
 * r-cran-brew - GNU R templating framework for report generation
 * r-cran-brglm - GNU R package for bias reduction in binomial-response GLMs
 * r-cran-cairodevice - GNU R Cairo/Gtk2 device driver package
 * r-cran-car - GNU R Companion to Applied Regression by John Fox
 * r-cran-caret - GNU R package for classification and regression training
 * r-cran-catools - GNU R package providing various utility functions
 * r-cran-checkmate - GNU R fast and versatile argument checks
 * r-cran-chron - GNU R package for chronologically ordered objects
 * r-cran-class - GNU R package for classification
 * r-cran-cluster - GNU R package for cluster analysis by Rousseeuw et al
 * r-cran-cmprsk - GNU R subdistribution analysis of competing risks
 * r-cran-coda - Output analysis and diagnostics for MCMC simulations in R
 * r-cran-codetools - GNU R package providing code analysis tools
 * r-cran-coin - GNU R package providing conditional inference procedures
 * r-cran-colorspace - GNU R Color Space Manipulation
 * r-cran-combinat - GNU R package with utilities for combinatorics
 * r-cran-contfrac - GNU R package providing various utilities for evaluating continued fractions
 * r-cran-conting - GNU R package for Bayesian analysis of contingency tables
 * r-cran-crayon - GNU R colored terminal output
 * r-cran-cubature - GNU R package for adaptive multivariate integration
 * r-cran-date - GNU R package for date handling
 * r-cran-dbi - GNU R package providing a generic database interface
 * r-cran-deal - Learning Bayesian Networks with Mixed Variables
 * r-cran-deldir - GNU R Delaunay Triangulation and Dirichlet (Voronoi) Tessellation
 * r-cran-deoptimr - GNU R package for Diffential Evolution in pure R
 * r-cran-desolve - GNU R package providing functions that solve initial value problems
 * r-cran-diagnosismed - medical diagnostic test accuracy analysis toolkit
 * r-cran-dichromat - Color schemes for dichromats
 * r-cran-digest - GNU R package for 'hash digest' of R data structures
 * r-cran-domc - GNU R parallel excution backend for %dopar% using multicore
 * r-cran-doparallel - GNU R foreach parallel adaptor for the parallel package
 * r-cran-dosefinding - Planning and Analyzing Dose Finding experiments
 * r-cran-dosnow - GNU R parallel excution backend for %dopar% using snow
 * r-cran-downloader - GNU R package for downloading files over http and https
 * r-cran-e1071 - GNU R package with miscellaneous functions of the Dept of Statisics (e1071)
 * r-cran-eco - GNU R routines for Bayesian ecological inference
 * r-cran-ecodist - GNU R package for dissimilarity-based ecological analysis
 * r-cran-effects - GNU R graphical and tabular effects display for glm models
 * r-cran-elliptic - GNU R package providing elliptic and related functions
 * r-cran-energy - GNU R package for energy statistics for distribution comparison
 * r-cran-epi - GNU R epidemiological analysis
 * r-cran-epibasix - GNU R Elementary Epidemiological Functions
 * r-cran-epicalc - GNU R Epidemiological calculator
 * r-cran-epir - GNU R Functions for analysing epidemiological data
 * r-cran-epitools - GNU R Epidemiology Tools for Data and Graphics
 * r-cran-erm - GNU R package for 'extended Rasch modelling'
 * r-cran-estimability - GNU R package providing tools for determining estimability of linear functions
 * r-cran-etm - GNU R empirical transition matrix
 * r-cran-evaluate - GNU R parsing and evaluation tools
 * r-cran-evd - GNU R Functions for extreme value distributions
 * r-cran-expm - GNU R Computation of the matrix exponential and related quantities
 * r-cran-fail - GNU R File Abstraction Interface Layer (FAIL) mimicking a key-value store
 * r-cran-fasianoptions - GNU R package for financial engineering -- fAsianOptions
 * r-cran-fassets - GNU R package for financial engineering -- fAssets
 * r-cran-fastcluster - Fast hierarchical clustering routines for GNU R
 * r-cran-fastmatch - GNU R package for fast match replacement for repeated look-ups
 * r-cran-fbasics - GNU R package for financial engineering -- fBasics
 * r-cran-fbonds - GNU R package for financial engineering -- fBonds
 * r-cran-fcopulae - GNU R package for financial engineering -- fCopulae
 * r-cran-fexoticoptions - GNU R package for financial engineering -- fExoticOptions
 * r-cran-fextremes - GNU R package for financial engineering -- fExtremes
 * r-cran-fgarch - GNU R package for financial engineering -- fGarch
 * r-cran-fimport - GNU R package for financial engineering -- fImport
 * r-cran-fmultivar - GNU R package for financial engineering -- fMultivar
 * r-cran-fnonlinear - GNU R package for financial engineering -- fNonlinear
 * r-cran-foptions - GNU R package for financial engineering -- fOptions
 * r-cran-foreach - GNU R foreach looping support
 * r-cran-foreign - GNU R package to read/write data from other stat. systems
 * r-cran-formatr - Format R code automatically
 * r-cran-formula - GNU R package for extended model formulas
 * r-cran-fportfolio - GNU R package for financial engineering -- fPortfolio
 * r-cran-fregression - GNU R package for financial engineering -- fRegression
 * r-cran-ftrading - GNU R package for financial engineering -- fTrading
 * r-cran-funitroots - GNU R package for financial engineering -- fUnitRoots
 * r-cran-futile.logger - logging utility for GNU R
 * r-cran-futile.options - GNU R futile options management
 * r-cran-g.data - GNU R package for delayed-data
 * r-cran-gam - Generalized Additive Models for R
 * r-cran-gbm - GNU R package "Generalized Boosted Regression Models"
 * r-cran-gdata - GNU R package with data manipulation tools by Greg Warnes et al
 * r-cran-geepack - Generalized Estimating Equation Package for R
 * r-cran-genabel - GNU R package for genome-wide SNP association analysis
 * r-cran-genabel.data - data package for genome-wide SNP association analysis
 * r-cran-genetics - GNU R package for population genetics
 * r-cran-getopt - GNU R package providing command-line parsing functionality
 * r-cran-ggplot2 - implementation of the Grammar of Graphics
 * r-cran-gmaps - GNU R support for producing geographic maps with grid graphics
 * r-cran-gmodels - GNU R package with tools for model fitting by Greg Warnes et al
 * r-cran-gnm - GNU R package for generalized nonlinear models
 * r-cran-gplots - GNU R package with tools for plotting data by Greg Warnes et al
 * r-cran-gregmisc - GNU R package with miscellaneous functions by Greg Warnes et al
 * r-cran-gridextra - GNU R package with extensions for the grid package
 * r-cran-gsl - GNU R wrapper for the GNU Scientific Library
 * r-cran-gss - GNU R package for multivariate estimation using smoothing splines
 * r-cran-gtable - Arrange grobs in tables
 * r-cran-gtools - GNU R package with R programming tools by Greg Warnes et al
 * r-cran-haplo.stats - GNU R package for haplotype analysis
 * r-cran-hdf5 - GNU R package interfacing the NCSA HDF5 library
 * r-cran-hmisc - GNU R miscellaneous functions by Frank Harrell
 * r-cran-hwriter - HTML Writer - Outputs R objects in HTML format
 * r-cran-hypergeo - GNU R package providing the Gaussian hypergeometric for complex numbers
 * r-cran-igraph - GNU R network analysis and visualization
 * r-cran-inline - GNU R package to inline C, C++, Fortran functions from R
 * r-cran-int64 - GNU R package for 64 bit integer types
 * r-cran-iterators - GNU R iterator support for vectors, lists and other containers
 * r-cran-its - GNU R package for handling irregular time series
 * r-cran-jsonlite - Robust, High Performance JSON Parser and Generator for R
 * r-cran-kernlab - GNU R package for kernel-based machine learning lab
 * r-cran-kernsmooth - GNU R package for kernel smoothing and density estimation
 * r-cran-labeling - GNU R Axis Labeling optimization
 * r-cran-lambda.r - GNU R modeling data with functional programming
 * r-cran-lattice - GNU R package for 'Trellis' graphics
 * r-cran-latticeextra - GNU R package of additional graphical displays based on lattice
 * r-cran-learnbayes - GNU R functions for learning bayesian inference
 * r-cran-lhs - GNU R package "lhs: Latin Hypercube Samples"
 * r-cran-littler - GNU R scripting and command-line front-end
 * r-cran-lme4 - GNU R package for linear mixed effects model fitting
 * r-cran-lmtest - GNU R package for diagnostic checking in linear models
 * r-cran-logspline - GNU R package providing routines for the logspline density estimation
 * r-cran-lpsolve - GNU R package providing linear program solvers
 * r-cran-lsmeans - GNU R package providing least-squares means for linear, generalized linear, and mixed models
 * r-cran-magrittr - GNU R forward-pipe operator
 * r-cran-maldiquant - GNU R package for quantitative analysis of mass spectrometry data
 * r-cran-maldiquantforeign - GNU R package providing import/export routines for MALDIquant
 * r-cran-mapdata - GNU R support for producing geographic maps (supplemental data)
 * r-cran-mapproj - GNU R support for cartographic projections of map data
 * r-cran-maps - GNU R support for producing geographic maps
 * r-cran-mass - GNU R package of Venables and Ripley's MASS
 * r-cran-matchit - GNU R package of nonparametric matching methods
 * r-cran-matrix - GNU R package of classes for dense and sparse matrices
 * r-cran-matrixmodels - GNU R package for sparse and dense matrix models
 * r-cran-matrixstats - GNU R methods that apply to rows and columns of a matrix
 * r-cran-maxlik - GNU R maximum likelihood estimation
 * r-cran-mcmcpack - R routines for Markov chain Monte Carlo model estimation
 * r-cran-medadherence - GNU R Medication Adherence: Commonly Used Definitions
 * r-cran-memoise - Memoise functions
 * r-cran-mfilter - GNU R package providing miscellaneous time series filters
 * r-cran-mgcv - GNU R package for multiple parameter smoothing estimation
 * r-cran-mime - R package which maps filenames to MIME Types
 * r-cran-minqa - GNU R package for quadratic optimisation without derivatives
 * r-cran-misc3d - GNU R collection of 3d plot functions and rgl-based isosurfaces
 * r-cran-misctools - GNU R miscellaneous tools and utilities
 * r-cran-mixtools - GNU R tools for analyzing finite mixture models
 * r-cran-mnormt - GNU R package providing multivariate normal and t distribution
 * r-cran-mnp - GNU R package for fitting multinomial probit (MNP) models
 * r-cran-modeltools - GNU R package providing a collection of tools to deal with statistical models
 * r-cran-msm - GNU R Multi-state Markov and hidden Markov models in continuous time
 * r-cran-multcomp - GNU R package for multiple comparison procedures
 * r-cran-multicore - GNU R parallel processing on multi-core or multi-cpu machines
 * r-cran-munsell - Munsell colour system
 * r-cran-mvnormtest - GNU R package for multivariate normality test
 * r-cran-mvtnorm - GNU R package to compute multivariate Normal and T distributions
 * r-cran-ncdf4 - GNU R interface to Unidata netCDF format data files
 * r-cran-nlme - GNU R package for (non-)linear mixed effects models
 * r-cran-nloptr - GNU R package for interface to NLopt
 * r-cran-nnet - GNU R package for feed-forward neural networks
 * r-cran-nnls - GNU R package for non-negative least squares (the Lawson-Hanson algorithm)
 * r-cran-numderiv - GNU R package for accurate numerical derivatives
 * r-cran-nws - GNU R package for distributed programming via NetWorkSpaces
 * r-cran-optparse - GNU/R Command line option parser
 * r-cran-pbapply - GNU R package providing progress bars for vectorized R functions
 * r-cran-pbivnorm - GNU R package for calculating probabilities from a bivariate normal CDF
 * r-cran-pbkrtest - GNU R package for tests in linear mixed-effect models
 * r-cran-permute - R functions for generating restricted permutations of data
 * r-cran-phangorn - GNU R package for phylogenetic analysis
 * r-cran-pkgkitten - GNU R package to create simple packages
 * r-cran-plotrix - GNU R package providing various plotting functions
 * r-cran-plyr - tools for splitting, applying and combining data
 * r-cran-polspline - GNU R package providing polynomial spline fitting
 * r-cran-polyclip - GNU R Polygon Clipping
 * r-cran-polycub - GNU R Cubature over Polygonal Domains
 * r-cran-praise - GNU R praise users
 * r-cran-profilemodel - GNU R tools for profiling inference functions
 * r-cran-proto - Prototype object-based programming
 * r-cran-pscl - GNU R package for discrete data models
 * r-cran-psy - GNU R procedures for psychometrics
 * r-cran-pvclust - Hierarchical Clustering with P-Values via Multiscale Bootstrap
 * r-cran-pwt - GNU R package for the Penn World Tables (version 5.6 to 7.1)
 * r-cran-pwt8 - GNU R package for the Penn World Tables (version 8)
 * r-cran-qtl - GNU R package for genetic marker linkage analysis
 * r-cran-quadprog - GNU R package for solving quadratic programming problems
 * r-cran-quantreg - GNU R package for quantile regression
 * r-cran-qvcalc - GNU R package for computing quasi variances for factor effects
 * r-cran-r.methodss3 - GNU R utility function for defining S3 methods
 * r-cran-r.oo - GNU R object-oriented programming with or without references
 * r-cran-r.utils - GNU R various programming utilities
 * r-cran-randomfields - GNU R simulation and analysis of random fields
 * r-cran-randomforest - GNU R package implementing the random forest classificator
 * r-cran-raschsampler - GNU R package for sampling binary matrices with fixed margins
 * r-cran-rcmdr - GNU R platform-independent basic-statistics GUI
 * r-cran-rcmdrmisc - GNU R package for miscellaneous Rcmdr utilities
 * r-cran-rcolorbrewer - GNU R package providing suitable color palettes
 * r-cran-rcpp - GNU R package for Seamless R and C++ Integration
 * r-cran-rcpparmadillo - GNU R package for Armadillo C++ linear algebra library
 * r-cran-rcppeigen - GNU R package for Eigen templated linear algebra
 * r-cran-rcurl - GNU R General network (HTTP/FTP/...) client interface
 * r-cran-readbrukerflexdata - GNU R package to read Bruker Daltonics \*flex format files
 * r-cran-readmzxmldata - GNU R package to read mass spectrometry data in mzXML format
 * r-cran-readxl - GNU R package to read Excel files
 * r-cran-relimp - GNU R package for inference on relative importance of regressors
 * r-cran-reshape - Flexibly reshape data
 * r-cran-reshape2 - Flexibly reshape data: a reboot of the reshape package
 * r-cran-rggobi - GNU R package for the GGobi data visualization system
 * r-cran-rgl - GNU R package for three-dimensional visualisation using OpenGL
 * r-cran-rglpk - GNU R interface to the GNU Linear Programing Kit
 * r-cran-rgtk2 - GNU R binding for Gtk2
 * r-cran-rinside - GNU R package to embed R in C++ application
 * r-cran-rjags - R interface to the JAGS Bayesian statistics package
 * r-cran-rjava - GNU R low-level interface to Java
 * r-cran-rjson - GNU R package for converting between R and JSON objects
 * r-cran-rmpi - GNU R package interfacing MPI libraries for distributed computing
 * r-cran-rms - GNU R regression modeling strategies by Frank Harrell
 * r-cran-rmysql - GNU R package providing a DBI-compliant interface to MySQL
 * r-cran-rneos - GNU R package with XML-RPC interface to NEOS
 * r-cran-rnetcdf - GNU R package that provides an R interface to NetCDF datasets
 * r-cran-rniftilib - GNU/R interface to NIFTICLIB
 * r-cran-robustbase - GNU R package providing basic robust statistics
 * r-cran-rocr - GNU R package to prepare and display ROC curves
 * r-cran-rodbc - GNU R package for ODBC database access
 * r-cran-rpart - GNU R package for recursive partitioning and regression trees
 * r-cran-rpostgresql - GNU R package providing database interface and driver for PostgreSQL
 * r-cran-rquantlib - GNU R package interfacing the QuantLib finance library
 * r-cran-rsclient - GNU R package providing an Rserve client
 * r-cran-rsdmx - GNU R package for the Statistical Data and Metadata Exchange (SDMX) framework
 * r-cran-rserve - GNU R Rserve tcp/ip server and sample clients
 * r-cran-rsolnp - GNU R general non-linear optimization
 * r-cran-rsprng - GNU R interface to SPRNG (Scalable Parallel RNGs)
 * r-cran-rsqlite - Database Interface R driver for SQLite
 * r-cran-rsymphony - GNU R interface to the SYMPHONY MILP solver
 * r-cran-runit - GNU R package providing unit testing framework
 * r-cran-sandwich - GNU R package for model-robust standard error estimates
 * r-cran-scales - Scale functions for graphics
 * r-cran-scatterplot3d - GNU R package for Visualizing Multivariate Data
 * r-cran-segmented - GNU R segmented relationships in regression models
 * r-cran-sendmailr - send email using GNU R
 * r-cran-seqinr - GNU R biological sequences retrieval and analysis
 * r-cran-seroincidence - GNU R seroincidence calculator tool
 * r-cran-slam - GNU R sparse lighweight arrays and matrices package
 * r-cran-sm - GNU R package for kernel smoothing methods
 * r-cran-sn - GNU R package providing skew-normal and skew-t distributions
 * r-cran-snow - GNU R package for 'simple network of workstations'
 * r-cran-sp - GNU R classes and methods for spatial data
 * r-cran-spam - GNU R functions for sparse matrix algebra
 * r-cran-sparsem - GNU R package for basic linear algebra for sparse matrices
 * r-cran-spatial - GNU R package for spatial statistics
 * r-cran-spatstat - GNU R Spatial Point Pattern analysis, model-fitting, simulation, tests
 * r-cran-spc - GNU R Statistical Process Control
 * r-cran-stabledist - GNU R package for stable distribution functions
 * r-cran-statmod - GNU R package providing algorithms and functions for statistical modeling
 * r-cran-stringi - GNU R character string processing facilities
 * r-cran-stringr - Make it easier to work with strings
 * r-cran-strucchange - GNU R package for structural change regression estimation
 * r-cran-survival - GNU R package for survival analysis
 * r-cran-tcltk2 - GNU R package for Tcl/Tk additions
 * r-cran-teachingdemos - GNU R Demonstrations for teaching and learning
 * r-cran-tensor - GNU R Tensor product of arrays
 * r-cran-testthat - GNU R testsuite
 * r-cran-tgp - GNU R package "tgp: Bayesian treed Gaussian process models"
 * r-cran-th.data - GNU R package for datasets by Torsten Hothorn
 * r-cran-timedate - GNU R package for financial engineering -- timeDate
 * r-cran-timeseries - GNU R package for financial engineering -- timeSeries
 * r-cran-tkrplot - GNU R embedded Tk plotting device package
 * r-cran-truncnorm - GNU R truncated normal distribution
 * r-cran-tseries - GNU R package for time-series analysis and comp. finance
 * r-cran-urca - GNU R package providing unit root and cointegration tests
 * r-cran-vcd - GNU R Visualizing Categorical Data
 * r-cran-vcdextra - GNU R package providing extensions and additions to the vcd package
 * r-cran-vegan - Community Ecology Package for R
 * r-cran-vgam - GNU R package for estimating vector generalized additive models
 * r-cran-vioplot - GNU R toolbox for violin plots
 * r-cran-wdi - GNU R package for accessing the World Development Indicators
 * r-cran-xml - GNU R package for XML parsing and generation
 * r-cran-xtable - GNU R coerce data to LaTeX and HTML tables
 * r-cran-xts - GNU R package for time series analysis -- xts
 * r-cran-yaml - Methods to convert R data to YAML and back
 * r-cran-zelig - GNU R package providing a unified front-end for estimating statistical models
 * r-cran-zoo - GNU R package for totally ordered indexed observations
 * r-doc-html - GNU R html manuals for statistical computing system
 * r-doc-info - GNU R info manuals statistical computing system
 * r-doc-pdf - GNU R pdf manuals for statistical computing system
 * r-mathlib - GNU R standalone mathematics library
 * r-recommended - GNU R collection of recommended packages [metapackage]
 * r-cran-maptools - GNU R Tools for reading and handling spatial objects
 * r-cran-surveillance - GNU R package for the Modeling and Monitoring of Epidemic Phenomena



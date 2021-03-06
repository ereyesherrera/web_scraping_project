# Analyzing Macalester Men's Cross Country Meet Results with Python's Beautiful Soup and R

## Sources

**Inspiration and very helpful code (which mine follows closely):**

* https://medium.com/@viritaromero/web-scraping-5k-race-results-with-python-and-beautifulsoup-d08eba5624eb

**Learning how to webscrape:**

* https://www.edureka.co/blog/web-scraping-with-python/
* https://stackoverflow.com/questions/34370521/scraping-elements-without-an-id-or-class-from-a-web-page-using-python-beautifuls
* http://theautomatic.net/2019/01/19/scraping-data-from-javascript-webpage-python/

**Beautiful Soup Documentation:**

* https://beautiful-soup-4.readthedocs.io/en/latest/

**Pandas and Seaborn Documentations**
* https://pandas.pydata.org/pandas-docs/stable/
* https://seaborn.pydata.org/

**Online Help**

* https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/
* http://www.datasciencemadesimple.com/append-concatenate-rows-python-pandas-row-bind/
* https://stackoverflow.com/questions/45236592/why-is-rpy2-not-installing-in-my-osx-sierra-terminal
* https://plotnine.readthedocs.io/en/stable/index.html
* https://towardsdatascience.com/how-to-use-ggplot2-in-python-74ab8adec129
* https://www.datanovia.com/en/blog/ggplot-axis-ticks-set-and-rotate-text-labels/#customize-continuous-and-discrete-axes
* https://stackoverflow.com/questions/12096252/use-a-list-of-values-to-select-rows-from-a-pandas-dataframe
* https://data36.com/pandas-tutorial-2-aggregation-and-grouping/
* https://www.geeksforgeeks.org/how-to-get-rows-index-names-in-pandas-dataframe/
* https://stackoverflow.com/questions/20084487/use-index-in-pandas-to-plot-data
* https://stackoverflow.com/questions/19960077/how-to-filter-pandas-dataframe-using-in-and-not-in-like-in-sql
* https://stackoverflow.com/questions/38848219/center-align-outputs-in-ipython-notebook
* https://medium.com/@andykashyap/top-5-tricks-to-make-plots-look-better-9f6e687c1e08
* https://towardsdatascience.com/bringing-the-best-out-of-jupyter-notebooks-for-data-science-f0871519ca29
* https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231
* https://www.w3schools.com/python/ref_string_split.asp
* https://stackoverflow.com/questions/39534676/typeerror-first-argument-must-be-an-iterable-of-pandas-objects-you-passed-an-o
* https://www.geeksforgeeks.org/python-pandas-split-strings-into-two-list-columns-using-str-split/
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html
* https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
* https://stackoverflow.com/questions/24179284/accessing-hierarchical-columns-in-pandas-after-groupby
* https://rstudio.github.io/reticulate/#python-in-r-markdown
* http://queirozf.com/entries/pandas-dataframe-groupby-examples
* https://stackoverflow.com/questions/46306786/flatten-multi-index-pandas-dataframe-where-column-names-become-values/46306841
* https://stackoverflow.com/questions/38935541/what-is-the-pandas-equivalent-of-dplyr-summarize-aggregate-by-multiple-functions
* https://stackoverflow.com/questions/31632637/label-axes-on-seaborn-barplot
* https://stackoverflow.com/questions/12065885/filter-dataframe-rows-if-value-in-column-is-in-a-set-list-of-values/12065904
* https://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column
* https://stackoverflow.com/questions/36921951/truth-value-of-a-series-is-ambiguous-use-a-empty-a-bool-a-item-a-any-o
* https://www.inchcalculator.com/minutes-to-time-calculator/
* https://stackoverflow.com/questions/6402812/how-to-convert-an-hmmss-time-string-to-seconds-in-python/6402934
* https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#missing-data
* https://stmorse.github.io/journal/tidyverse-style-pandas.html
* https://cran.r-project.org/web/packages/egg/vignettes/Ecosystem.html
* https://yihui.name/knitr/options/#chunk-options
* https://blogdown-demo.rbind.io/2018/01/31/gif-animations/
* https://stackoverflow.com/questions/18884778/poor-resolution-in-knitr-using-rmd
* https://stackoverflow.com/questions/36783189/changing-the-appearance-of-facet-labels-size?rq=1
* https://stackoverflow.com/questions/20076195/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas
* https://stackoverflow.com/questions/38933071/group-by-two-columns-and-count-the-occurrences-of-each-combination-in-pandas
* http://www.datasciencemadesimple.com/reshape-long-wide-pandas-python-pivot-function/
* https://stackoverflow.com/questions/40185446/how-to-put-in-bold-the-title-in-a-seaborn-factorplot
* https://stackoverflow.com/questions/29067541/how-to-change-the-font-color

**Websites where data was retrieved:**

* https://results.flotrack.org/XC-PTT.html?mid=1469
* https://www.tfrrs.org/results/xc/14208/Twin_Cities_Twilight
* https://www.tfrrs.org/results/xc/14588/St._Olaf_Invitational
* https://www.tfrrs.org/results/xc/14671/Roy_Griak_Invitational
* https://www.tfrrs.org/results/xc/14944/MIAC_Championships
* https://www.tfrrs.org/results/xc/14517/NCAA_Division_III_Central_Region_Cross_Country_Championships
* https://www.tfrrs.org/results/xc/12042/Augsburg_Open
* https://www.tfrrs.org/results/xc/11951/Falcon_Invitational
* https://www.tfrrs.org/results/xc/12550/St._Olaf_Invitational
* https://www.tfrrs.org/results/xc/12804/Summit_Cup
* https://www.tfrrs.org/results/xc/12950/Carleton_Running_of_the_Cows
* https://www.tfrrs.org/results/xc/13226/UW_La_Crosse_Jim_DrewsTori_Neubauer_Invitational
* https://www.tfrrs.org/results/xc/13031/NCAA_Division_III_Central_Region_Cross_Country_Championships
* http://www.fastfinishtiming.com/2017RoadandCC/17Results/MIACMen.html
* http://wayzatatiming.com/crosscountry/2016/AugsburgAlumni/
* https://www.tfrrs.org/results/xc/9999/Falcon_Invitational
* https://www.tfrrs.org/results/xc/10620/Summit_Cup
* https://www.tfrrs.org/results/xc/10762/ROY_GRIAK_INVITATIONAL
* https://www.tfrrs.org/results/xc/10836/Blugold_Invitational
* https://www.tfrrs.org/results/xc/11045/Jim_DrewsTori_Neubauer_Invitational
* https://www.tfrrs.org/results/xc/11198/MIAC_Championships
* https://www.tfrrs.org/results/xc/11018/NCAA_Division_III_Central_Region_Cross_Country_Championships
* https://www.tfrrs.org/results/xc/16604/Jim_DrewsTori_Neubauer_Invitational
* https://www.tfrrs.org/results/xc/15821/Twin_Cities_Twilight
* https://www.tfrrs.org/results/xc/16404/Blugold_Invitational
* https://www.tfrrs.org/results/xc/16179/Running_of_the_Cows
* https://www.tfrrs.org/results/xc/16025/Summit_Cup
* https://www.tfrrs.org/results/xc/16678/MIAC_Conference_Championships
* https://www.tfrrs.org/results/xc/16562/NCAA_Division_III_Central_Region_Cross_Country_Championships

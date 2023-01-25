# Resources/Tips for writting a scientific paper/report

This provides some advices for writing a scientific paper (or lab report). It focus on writing using the LaTeX word-processing program. 

In LaTeX you can cross reference figure, equation, tale and algorithm so that the numerbering is automatically generated. A good practice is to use meaninggfull tags. For instance a figure could be tagged with the ```\label{fig:bunchDistribution}``` and latter called in the text as ```Figure.~\ref{fig:bunchDistribution} displayed the bunch distribution at the location [...]```. The same can be done for other object for instance ```\label{eq:bunchDistributionInit}``` or ```\label{tab:bunchDistributionInit}```. The convention to tag the object with a string defining the type of the object and the object label (separated with a ```:```) is good practice. For very long manuscript or thesis the lab can also have another tag refereing to the chapter, i.e.  ```\label{chapterIntro:tab:bunchDistributionInit}```. 

Generally when refering to figure, and equation you can use the abbreviated form ```[...] shown in Eq.~\ref{eq:bunchDistributionInit}``` or ```appears in Fig.~\ref{fig:bunchDistributionInit}```. The convenstion is however to spell out the object if it start the sentence, i.e. ``Figure ~\ref{fig:bunchDistributionInit} presents the [....]```.


## general
An excellent paper about scientific writing is availabe at XXX


## latex formating

### Symbols
**value and units:** Note that when quoting a value with unit the unit should be separated by an insecable space i.e. ```10.23~m``` (where ~ refers to the insecable space) to give the formating $10.23\mbox{~m}$. The use of the unit package (toggled by adding the line ```\usepackage{siunitx}
``` in your LaTeX file preamble) is also recommended; for instance ```$\SI{1}{\giga\electronvolt}$``` gives $1\mbox{~GeV}$.

**symbols in text body:** giving the value of a parameter in the text body should be done using an equation format. For instance the statement l=10.23 m should be written  ```$l=10.23$~m``` so to appear as $l=10.23\mbox{~m}$. 

**the special case of $\textmu{}$:** unit involving microns should use the ```\textmu{}``` command rather than the ```$\mu$``` mathematical symbol for instance ```10.23\mbox{~}\textmu{m}}``` is written as $10.23\mbox{~}\textmu{m}$ rather than ```$10.23\mbox{~$\mu${m}}$``` (which would results in an italicezed mu: $10.23\mbox{~$\mu${m}$)

## tables

## figure & plots
### general
In general the figure should have any title (e.g. above plots) as the caption should be use to describe the figure content. The caption should be self contain and explain the figure including meaning of abbreviated labels, meaning of traces, etc...

### plots
The labels of the plot should use LaTeX fonts similar to the one used in the text body. For matplotlib you can use the two mplg configuration files available in the directory matplotlib 

The labels should have clearly indicate the quantity plotted and its units in parentheses "(units)" (avoid using brackets or others symbols instead of parentheses). The typical value should be on the order of unity that is if you plot the frequency in Hz and it has value of $10^15$ then it should be rescaled to have units of PHz. 

In case of composite figure -- prepare the composite figure within the plotting pogram; see a matplotlib example at XXX. Avoid merging single-plot figure within LaTeX. The figure should also have a letter label so that it can be referenced in the caption and text body (using a letter label is better than refering the plot with respect to its location on the figure (e.g. top left...). 

# Resources/Tips for writting a good scientific paper
This provides some advices for writing a scientific paper (or lab report). It focus on writing using the LaTeX word-processing program. 

## general
An excellent paper about scientific writing is availabe at XXX


## latex formating

### Symbols
Note that the $\textmu{}$. 


## tables

## figure & plots
### general
In general the figure should have any title (e.g. above plots) as the caption should be use to describe the figure content. The caption should be self contain and explain the figure including meaning of abbreviated labels, meaning of traces, etc...

### plots
The labels of the plot should use LaTeX fonts similar to the one used in the text body. For matplotlib you can use the two mplg configuration files available in the directory matplotlib 

The label should have clearly indicate the quantity plotted and its units in parentheses "(units)" (avoid using brackets or others symbols instead of parentheses). 

In case of composite figure -- prepare the composite figure within the plotting pogram; see a matplotlib example at XXX. Avoid merging single-plot figure within LaTeX. The figure should also have a letter label so that it can be referenced in the caption and text body (using a letter label is better than refering the plot with respect to its location on the figure (e.g. top left...). 

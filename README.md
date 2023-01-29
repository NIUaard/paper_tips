# Resources/Tips for composing a scientific paper/report

This note provides some advices for writing a scientific paper (or lab report). It focuses on writing using the LaTeX word-processing program. 


## General
An excellent paper about scientific writing by George Gopen is availabe at [ https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf ] it appears in [American Scientist 78(6):550-558 (Nov-Dec 1990)]. There are many good references in the litterature including https://spie.org/news/photonics-focus/janfeb-2020/how-to-write-a-scientific-paper?SSO=1

There are a large number of LaTeX template for paper. Most often templates for conference proceedings are directly provided by the conference, while a large database of templates is available on OverLeaf at https://www.overleaf.com/latex/templates .

### Title
The title of the paer should be crisp and inform the nature of the work (experiment versus theory or simulations) and topic. Avoid using "first" or "novel" as paper are typically pushed based on the advances they support (so all paper should have some degree of novelty with resepect to prior work on the topic). 

### Authorship
There is no clear convention on authorship and list of authors. In our group the list of authors should have the main authors (the student in charge of the research who drafted the paper) followed by all contributors in alphabetical order. Effective 2023, refereed paper should have a athors contribution statement after the acknowledgement (some of the journals do require such a section). For paper published in reference proceedings this section should be omitted given the limited number of page. The main author can alo add her/his formal (institution) contact information (email). Avoid using personal e-mail address. 

## Latex formating

In LaTeX you can cross reference figure, equation, tale and algorithm so that the numerbering is automatically generated. A good practice is to use meaning full tags. For instance a figure could be tagged with the ```\label{fig:bunchDistribution}``` and latter called in the text as ```Figure~\ref{fig:bunchDistribution} displayed the bunch distribution at the location [...]```. The same can be done for other object for instance ```Eq.~\label{eq:bunchDistributionInit}``` or ```Table~\label{tab:bunchDistributionInit}```. The convention to tag the object with a string defining the type of the object and the object label (separated with a ```:```) is good practice. For very long manuscript or thesis the label can also have another tag refering to the chapter, i.e.  ```Eq.~\label{chapt1:tab:bunchDistributionInit}```. Similarly cross-referencing of section can be accomplished by adding the reference label in the section ```\section{Introduction and Motivation \ref{sec:intro}```. For Figures and Tables, it is best to insert the ```\ref{}``` command in the Figure or Table captions directly. 

Generally when refering to figure, and equation you can use the abbreviated form ```[...] described by Eq.~\ref{eq:bunchDistributionInit}``` or ```appears in Fig.~\ref{fig:bunchDistributionInit}```. The convention is however to spell out the object if it starts a sentence, i.e. ```Figure ~\ref{fig:bunchDistributionInit} presents the [....]```. The object "Table" and "Section" are rearely abbreviated. 


### Symbols
**value and units:** Note that when quoting a value with unit the unit should be separated by an insecable space i.e. ```10.23~m``` (where ~ refers to the insecable space) to give the formating $10.23\mbox{~m}$. The use of the unit package (toggled by adding the line ```\usepackage{siunitx}
``` in your LaTeX file preamble) is also recommended; for instance ```$\SI{1}{\giga\electronvolt}$``` gives $1\mbox{~GeV}$.

**symbols in text body:** giving the value of a parameter in the text body should be done using an equation format. For instance the statement l=10.23 m should be written  ```$l=10.23$~m``` so to appear as $l=10.23\mbox{~m}$. 

**the special case of $\textmu{}$:** unit involving microns should use the ```\textmu{}``` command rather than the ```$\mu$``` mathematical symbol for instance ```10.23\mbox{~}\textmu{m}}``` is written as $10.23\textmu{m}$ rather than ```$10.23\mbox{~$\mu${m}}$``` (which would results in an italicezed mu: $10.23\mbox{~$\mu${m}$)

### Equations
when writing an equation you should make sure all the symbol have been a-priori introduced. If new symbols appears in the equation they should be defined immediately dollowing the equation. For instance

>"[...] the optical retardance scaled with the aplied the electric field $E(t)$ folloing
$\Delta \phi (t) = \frac{\pi d n_0^3 r_{41} E(t)}{\lambda},$
where $\lambda$ is the wavelength of the optical pulse, $n_0$ the index of refraction and $r_{41}$ the electro-optics coefficient." 

The choice of indenting versus non-indenting an equation is dicated by the journal format and the importance of the equation. If indented the equation should be inserted between ```$``` signes as follows ```$ \Delta \phi (t) = \frac{\pi d n_0^3 r_{41} E(t)}{\lambda} ``` if non-indented the equation should be in a ```\eqnarray``` block as follows
```
\begin{eqnarray}
 \Delta \phi (t) &=& \frac{\pi d n_0^3 r_{41} E(t)}{\lambda}
\end{eqnarray}
```
Ponctuation around an equation should follow standard practice. That is is the equation is at the end of a sentence it should end with a period ```.``` directly in the block or between the ```$``` signs. 

## Tables

## Figure & plots
### General
In general the figure should not have any title (e.g. above plots) and the caption should be use to describe the figure content. The caption should be self contained and explain the figure including meaning of abbreviated labels, meaning of traces, etc...

### Graphical arts
A paper often include schematics. Simple schematics (electric circuits) can be done in openOffice (slide) or equivalent. For better results, open-source software like [InkScape](https://inkscape.org/)  and [Blender](https://www.blender.org/) are recommended. 

### Plots
A open-source versatile program for plotting purpose is the [matplotlib Python module](https://matplotlib.org/). Matplotlib has an extensive documentation with examples that can be modified to perform most of the plot you will neee to generate; see [matplotlib examples](https://matplotlib.org/stable/plot_types/index.html)
The plot axis label, legend and other annotations should all use LaTeX fonts similar to the one used in the text body. For matplotlib you can use or modify one of the several mplg configuration files available in the [matplotlibConfigExample sub-directory](matplotlibConfigExample)

The labels should have clearly indicate the quantity plotted and its units in parentheses "(units)" (avoid using brackets or others symbols instead of parentheses). The typical value should be on the order of unity that is if you plot the frequency in Hz and it has value of $10^15$ then it should be rescaled to have units of PHz. 

In case of composite figure, it is best to prepare the composite figure within the plotting pogram; see the directory [example_subplots sub-directory](example_subplots). Avoid merging single-plot figure within LaTeX, it usually waste and does not provide precise control over the sub-figures placements and sizes. The figures should also have a letter label using the command
```
ax1.plot (xx[:,0], (xx[:,4]/xx[2,4]-1),'d--', label=r'$\varepsilon_z$')  # create the subplots
ax1.text(0.075, 0.9,r'(a)', ha='center', va='center', transform=ax1.transAxes)  # add the tag (a) to the subplot

```
so that it can be unambigously referenced in the caption and text body (using a letter label is better than refering the plot with respect to its location on the figure (e.g. top left...). 

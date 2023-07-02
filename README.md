# Resources/Tips for composing a scientific paper/report

This note provides some advice for writing a scientific paper (or lab report). It focuses on writing using the LaTeX word-processing program. 


## General
An excellent paper about scientific writing by George Gopen is available at [ https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf ] it appears in [American Scientist 78(6):550-558 (Nov-Dec 1990)]. There are many good references in the literature including https://spie.org/news/photonics-focus/janfeb-2020/how-to-write-a-scientific-paper?SSO=1

There are a large number of LaTeX templates for paper. Most often templates for conference proceedings are directly provided by the conference, while a large database of templates is available on OverLeaf at https://www.overleaf.com/latex/templates .

### Title
The title of the paper should be crisp and inform the nature of the work (experiment versus theory or simulations) and topic. Avoid using "first" or "novel" as papers are typically published based on the advances they report (so all papers should have some degree of novelty over the prior work on the topic). 

### Authorship
There is no universal convention on authorship and list of authors. In our group, the list of authors should have the main authors [the student(s) in charge of the research who drafted the paper) followed by all contributors in alphabetical order. ```Effective 2023, refereed papers published by our group should have an author-contribution statement after the acknowledgment (an increasing number of the journals do require such a section) ```. For papers published in reference proceedings, this section should be omitted given the limited number of pages. The main author can also add her/his formal (institution) contact information (email). Avoid using personal e-mail addresses. 

### Bibliography
An important aspect of writing a paper is to credit historical development, related work, and previous research your paper builds on. This is the role of the bibliography. In LaTeX, the best way to manage the bibliography is to use the ```BibTeX ``` format. Specifically, you can create a file ```myreference.bib``` that lists the paper you wish to cite in the BibTeX format. An entry in the bib file may look like
```
@article{RevModPhys.94.025006,
  title = {Bunch shaping in electron linear accelerators},
  author = {Ha, G. and Kim, K.-J. and Power, J. G. and Sun, Y. and Piot, P.},
  journal = {Rev. Mod. Phys.},
  volume = {94},
  issue = {2},
  pages = {025006},
  numpages = {67},
  year = {2022},
  month = {May},
  publisher = {American Physical Society},
  doi = {10.1103/RevModPhys.94.025006},
  url = {https://link.aps.org/doi/10.1103/RevModPhys.94.025006}
}
```
The paper can then be cited in the text as follow "several methods of beam shaping exist as reviewed in~\cite{RevModPhys.94.025006}". When writing a paper with a large number of references (e.g. your dissertation)  it is convenient to organize the .bib file so that the references are listed in a given order to avoid duplication. One way of proceeding is to use a tag of the form ```author-year-letter``` in this convention the paper cited above would be tagged ```ha-2022-a``` instead of ```RevModPhys.94.025006```. If the author Ha had another paper in 2022, the second paper would be tagged ```ha-2022-b```, etc... The use of a bib file is very convenient: LaTeX will order the reference in the generation bibliography accordingly to the journal template format (often by order of appearance but some by first-author alphabetical order). 


## Latex formatting

In LaTeX, you can cross-reference figures, equations, tables, and algorithms so that the numbering is automatically generated. A good practice is to use meaningful full tags. For instance, a figure could be tagged with the ```\label{fig:bunchDistribution}``` and latter called in the text as ```Figure~\ref{fig:bunchDistribution} displayed the bunch distribution at the location [...]```. The same can be done for other objects for instance ```Eq.~\label{eq:bunchDistributionInit}``` or ```Table~\label{tab:bunchDistributionInit}```. The convention to tag the object with a string defining the type of the object and the object label (separated with a ```:```) is good practice. For a very long manuscript or thesis, the label can also have another tag referring to the chapter, i.e.  ```Eq.~\label{chapt1:tab:bunchDistributionInit}```. Similarly, cross-referencing of a section can be accomplished by adding the reference label in the section ```\section{Introduction and Motivation \ref{sec:intro}```. For Figures and Tables, it is best to insert the ```\ref{}``` command in the Figure or Table captions directly. 

Generally, when referring to figures, and equations you can use the abbreviated form ```[...] described by Eq.~\ref{eq:bunchDistributionInit}``` or ``` appears in Fig.~\ref{fig:bunchDistributionInit}```. The convention is however to spell out the object if it starts a sentence, i.e. ```Figure ~\ref{fig:bunchDistributionInit} presents the [....]```. The object "Table" and "Section" are rarely abbreviated. 


### Symbols
**value and units:** Note that when quoting a value with its unit, the unit symbol should be separated by an insecable space i.e. ```10.23~m``` (where ~ refers to the insecable space) to give the formatting $10.23\mbox{~m}$. The use of the unit package (toggled by adding the line ```\usepackage{siunitx}
``` in your LaTeX file preamble) is also recommended; for instance ```$\SI{1}{\giga\electronvolt}$``` gives $1\mbox{~GeV}$.

**symbols in text body:** giving the value of a parameter in the text body should be done using an equation format. For instance, the statement l=10.23 m should be written  ```$l=10.23$~m```to appear as $l=10.23\mbox{~m}$. 

**The special case of $\textmu{}$:** unit involving microns should use the ```\textmu{}``` command rather than the ```$\mu$``` mathematical symbol for instance ```10.23\mbox{~}\textmu{m}}``` is written as $10.23\textmu{m}$ rather than ```$10.23 \mu$m``` (which would result in an italicized mu, i.e., written as $10.23 \mu$m )

**The "dont's":**
- do not use scientific copmuter notations: for instance ```1E-10``` should be ```$1\times 10^{-10}$``` so that it appears as $1\times 10 ^{-10}$. 
- do not use the symbold ```*``` for multiplication but ```$\times$ ``` so that is appreas as $\times$.
- do not refer to an ucomping equation for instance ``` the model is described by the following Eq.~\ref{eq:model} [...]``` should just be ``` the model is described by the equation [...]```

### Equations
when writing an equation you should make sure all the symbols have been a priori introduced. If new symbols appear in the equation they should be defined immediately following the equation. For instance

>"[...] the optical retardance scaled with the aplied the electric field $E(t)$ folloing
$\Delta \phi (t) = \frac{\pi d n_0^3 r_{41} E(t)}{\lambda},$
where $\lambda$ is the wavelength of the optical pulse, $n_0$ the index of refraction and $r_{41}$ the electro-optics coefficient." 

The choice of indenting versus non-indenting an equation is dictated by the journal format and the importance of the equation. If indented the equation should be inserted between ```$``` signs as follows ```$ \Delta \phi (t) = \frac{\pi d n_0^3 r_{41} E(t)}{\lambda} ``` if non-indented the equation should be in a ```\eqnarray``` block as follows
```
\begin{eqnarray}
 \Delta \phi (t) &=& \frac{\pi d n_0^3 r_{41} E(t)}{\lambda}
\end{eqnarray}
```
Punctuation around an equation should follow standard practice. That is if the equation is at the end of a sentence it should end with a period ```.``` directly in the block or between the ```$``` signs. 

## Tables

## Figure & plots
### General
In general, the figure should not have any title (e.g. above plots) and the caption should be used to describe the figure content. The caption should be self-contained and explain the figure including the meaning of abbreviated labels, the meaning of traces, etc...

### Graphical arts
A paper often includes schematics. Simple schematics (electric circuits) can be done in OpenOffice (slide) or equivalent. For better results, open-source software like [InkScape](https://inkscape.org/)  and [Blender](https://www.blender.org/) are recommended. 

### Plots
An open-source versatile program for plotting purposes is the [matplotlib Python module](https://matplotlib.org/). Matplotlib has an extensive documentation with examples that can be modified to perform most of the plot you will need to generate; see [matplotlib examples](https://matplotlib.org/stable/plot_types/index.html)
The plot axis label, legend, and other annotations should all use LaTeX fonts similar to the one used in the text body. For matplotlib, you can use or modify one of the several mplg configuration files available in the [matplotlibConfigExample sub-directory](matplotlibConfigExample)

The labels should indicate the quantity plotted and its units in parentheses "(units)" (avoid using brackets or others symbols instead of parentheses). The typical value should be on the order of unity that is if you plot the frequency in Hz and it has a value of $10^15$ then it should be rescaled to have units of PHz. 

In the case of composite figures, it is best to prepare the composite figure within the plotting program; see the directory [example_subplots sub-directory](example_subplots). Avoid merging single-plot figure within LaTeX, it usually waste and does not provide precise control over the sub-figures placements and sizes. The figures should also have a letter label using the command
```
ax1.plot (xx[:,0], (xx[:,4]/xx[2,4]-1),'d--', label=r'$\varepsilon_z$')  # create the subplots
ax1.text(0.075, 0.9,r'(a)', ha='center', va='center', transform=ax1.transAxes)  # add the tag (a) to the subplot

```
so that it can be unambiguously referenced in the caption and text body (using a letter label is better than referring the plot to its location on the figure (e.g. top left...).  

When a plot includes many traces it is always good to add abbreviated labels that can be refered to/explained in the figure caption. 


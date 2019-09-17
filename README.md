# pepslog
a python program to processes log files of peps program and generates plots

## Usage

First `cd` to the directory that contains log files. Then use the command

`filenames|python3 [path/]process.py [mode]`

where mode is pyplot by default, and can be pyplot, plotly or android. If mode in pyplot, use matplotlib to draw the figure. If mode is plotly, use plotly to draw the figure. The figure is then shown in a web page. If mode is android, the figure is drawn by plotly and saved as a html file in ./iframe_figures.

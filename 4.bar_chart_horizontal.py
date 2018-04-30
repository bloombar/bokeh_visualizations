#!/usr/bin/env python3

from bokeh.plotting import figure, output_file, show

# prepare some data
# for a bar chart, the y axis positions where there are bars are storedin a list
# the length of each bar is in a second list in corresponding order
y=[1, 2, 3, 4, 5]
bar_lengths=[5, 7, 3, 5, 4]

# create a new plot with a title and axis labels
plot = figure(title="Example of a horizontal bar chart")

#render the horizontal bars, with bars at the specified y values
#note that colors of any glyph can be represented by hexadecimal color codes
plot.hbar(y, left=0, right=bar_lengths, height=0.5, color="#CAB2D6")

# output to static HTML file. 
output_file("4.bar_chart_horizontal.html", mode="inline")

#pop open in the browser
show(plot)
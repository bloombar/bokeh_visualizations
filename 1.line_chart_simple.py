from bokeh.plotting import figure, output_file, show

# prepare some data
# for a line, the x and y coordinates of all points are stored in separate lists
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [40, 30, 40, 50, 60, 70, 60, 50, 40, 40, 30, 30]

# create a new plot with a title and axis labels
plot = figure(title="Example of a line chart", x_axis_label='month', x_range=[min(x),max(x)],  y_axis_label='average temperature', y_range=[0, max(y)+20])

# add a line with legend, line color, and line thickness
plot.line(x, y, legend="2016 average temperature", line_color="blue", line_width=2)

# you could add more lines or other "renderer" elements to this same figure if you wanted

# output to static HTML file. 
output_file("line_1.html", mode="inline")

# show this figure in the default web browser
show(plot)
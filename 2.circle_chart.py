from bokeh.plotting import figure, output_file, show

# prepare some data
# for dots, the x and y coordinates of all points are stored in separate lists
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [40, 30, 40, 50, 60, 70, 60, 50, 40, 40, 30, 30]

# create a new plot with a title and axis labels
plot = figure(title="Example of a scatter plot", x_axis_label="month", y_axis_label="temperature  reading")

#render circles at all the x,y coordinates, with diameter of 10
plot.circle(x, y, size=10, fill_color="orange")

# output to static HTML file. 
output_file("circles.html", mode="inline")

#pop open in the browser
show(plot)
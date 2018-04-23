from bokeh.plotting import figure, show, output_file

# create a simple plot
plot = figure(
width=400,
height=300,
       title="An image example", 
       x_axis_label = "x axis",
       x_range=[0,5], 
       y_axis_label = "y axis",
       y_range=[0,5]
)

# add an image 
# the x and y coordinates position the image at the center of the 5x5 grid
# the width and height set the image to be the same size as the grid
plot.image_url(url=['slava_snow_show_400x300.png'], x=2.5, y=2.5, w=5.0, h=5.0, anchor="center")

# add a yellow line
x = [0, 1, 2, 2.5, 3, 4.5]
y = [1, 0, 0, 4, 1, 3]
plot.line(x, y, line_color="#f8ce3a", line_width=10 )

24 # save to a file
25 output_file('image.html')
26 
27 # pop open the web browser
28 show(plot)
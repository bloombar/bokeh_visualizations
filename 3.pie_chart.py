from bokeh.charts import Donut, show, output_file
import pandas as pd

#the data and the labels in a dictionary
data = {
        "This": 10, 
        "That": 50, 
        "The other": 100, 
        "... and this too": 75
}

#creating a pandas Series out of the data allows you to easily make a Donut chart
data = pd.Series(data)

#create the pie chart
pie_chart = Donut(data)

# output to static HTML file. 
output_file("pie.html", mode="inline")

#pop open in the browser
show(pie_chart)
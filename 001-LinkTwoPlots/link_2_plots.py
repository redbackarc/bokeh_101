import pandas as pd
from random import randint
import random
import numpy as np

from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource
from bokeh.layouts import row

output_file("out.html")

# list of tools
toolList = ['lasso_select', 'box_select', 'box_zoom', 'wheel_zoom', 'reset', 'save', 'undo', 'redo']

# load employee data onto a pandas dataframe
df = pd.read_csv('../data/employee_data_20.csv')

# print dataframe columns
print(df.columns)

# Store the data in a ColumnDataSource - linking of graphs happen through this datasource
ds = ColumnDataSource(df)

fig1 = figure(title='Employee ID vs Age', plot_height=600, plot_width=600, x_axis_label='Employee ID',
              y_axis_label='Age',tools= toolList)
fig1.circle(x='employee_id', y='age', source=ds,size=12, color='red')

fig2 = figure(title='employee_id vs height', plot_height=600, plot_width=600, x_axis_label='Employee ID', y_axis_label='Height',tools= toolList)
fig2.square(x='employee_id', y='height', source=ds,size=12, color='blue')

row = row(children=[fig1,fig2],sizing_mode = 'stretch_both')


show(row)
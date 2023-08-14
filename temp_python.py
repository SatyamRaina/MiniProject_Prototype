#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import plotly.graph_objs as go

# Step 1: Read the CSV file
val = pd.read_csv('C:\\Users\\HP\\Downloads\\test.csv')

# # Step 2: Convert the 'Time' column to datetime format
# val['Time'] = pd.to_datetime(val['Time'])

# Step 3: Create a line chart using Plotly
fig = go.Figure(data=go.Scatter(x=val['Time'], y=val['Temp'], mode='lines+markers'))

# Step 4: Customize the layout
fig.update_layout(
    title='Temperature Readings Over Time',
    xaxis_title='Time',
    yaxis_title='Temperature (°C)',
    font=dict(
        family='Arial',
        size=14,
        color='black'
    ),
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='Green',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='black'
        ),
#         tickformat='%H:%M:%S'  # Format x-axis ticks to show only time
    ),
    yaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='Green',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='black'
        ),
    ),
    plot_bgcolor='white',  # Background color of the plot
    paper_bgcolor='white',  # Background color of the paper
    margin=dict(l=60, r=40, t=60, b=40)  # Adjust margins for better spacing
)

# Step 5: Show the plot
fig.show()


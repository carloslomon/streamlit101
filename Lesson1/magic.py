import numpy as np 
import pandas as pd
import streamlit as st
import time as tt
import matplotlib.pyplot as plt
#This is a DF we will use to write
df = pd.DataFrame({'x': [1,2,3], 'x^2': [1,4,9], 'x^3': [1,8,27]})
#This is a normal distribution we will use to 
y = np.random.normal(0,1, 2024)
fig, ax = plt.subplots()
ax.hist(y, bins=24)
ax.set_title('Histogram of a Normal dist with mean =0, std =1 and 2024 data points')

# Multiple arguments and multiple data types can be used
"Bye Bye Bye", 2024, np.inf, -float('inf'), np.exp(1), np.log(np.exp(2024)), 'St bye bye bye'
#Write a title with the largest size
"""
# title H1
"""
#Write a title with the second largest Markdown title
'## Title H2'
#H3 Title
"### Title H3"
#Write a data frame
df
#Write a figure from matplotlib.pyplot figure or plot
fig






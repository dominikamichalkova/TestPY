import seaborn as sns
import pandas as pd
import numpy as np

#help(sns.heatmap)

import matplotlib.pyplot as plt

#help(plt.subplots)

df = pd.DataFrame(np.random.randn(10, 5)) #no of rows and columns, format df, relational table
uniform_data = np.random.rand(5,4) #format 5 arrays with 4 values

print df;
print uniform_data;

#limit on the scale [0,1], ticklabels if =int, every int-th label to plot, or list-like to choose specific
ax1 = sns.heatmap(uniform_data, xticklabels = True, yticklabels = True, annot = True, vmin=0, vmax=1, fmt ='.3f')

plt.show()

#define center of the colormap, square-shaped cells
ax2 = sns.heatmap(uniform_data, annot = True, center =0.5, square=True, linewidth =.5)

#ax = sns.heatmap(flights, center=flights.loc["January", 1955]) #center of map at a specific value

plt.show()

grid_kws = {"height_ratios": (.9, .05), "hspace": .3} #height of the cells, of the scale and the blank space between map and scale
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw = grid_kws)
ax = sns.heatmap(uniform_data, ax=ax, cbar_ax=cbar_ax, cbar_kws={"orientation": "horizontal"},annot=True, cmap="PiYG")


plt.show()


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv('C:/Users/IBM_ADMIN/PycharmProjects/Python1/data/hrdata.csv')

df.info()

print('# of people left = {}'.format(df[df['left']==1].size))
print('# of people stayed = {}'.format(df[df['left']==0].size))

corrmat = df.corr()
f, ax = plt.subplots(figsize=(5, 5))

# Draw the heatmap using seaborn
sns.heatmap(corrmat, vmax=.8, square=True,annot=True)
plt.yticks(rotation=0)  #seaborn uses matplotlib internally, as such we can use matplotlib functions to modify plots
plt.xticks(rotation=270)

plt.show()
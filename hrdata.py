import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv('C:/Users/IBM_ADMIN/PycharmProjects/Python1/data/hrdata.csv')

df.info() # summary of df

dn=df.head(2) #returns a dataframe holding first n rows of df, pandas pckg
print dn;

# print df.T; #transpose df

#panda attributes without applied on entire data set
# print df.T; #transpose df
print 'number of dimensions:',df.ndim;
print 'tuple representing dimensionality', df.shape;  #no of (rows,columns)
print df.ftypes; #indicator of ftypes - sparse/dense and dtype, in the object
print df.dtypes; #data types, int, float, char
print 'no of elements in the NDframe',df.size; #no of rows
print df.axes; #returns a list with row/column axis labels
print df['sales'].size;
print df['satisfaction_level'].dtype;


#methods
print 'unique sales fields:',df['sales'].unique();
print df.mean();
print df['average_montly_hours'].mean()/30 #daily working hours avg

print('# of people left = {}'.format(df[df['left']==1].size))
print('# of people stayed = {}'.format(df[df['left']==0].size))
print('# of people work for HR = {}'.format(df[df['sales']=='hr'].size))
print('protion of people who left in 5 years = {}%'.format(int(df[df['left']==1].size/df.size*100)))

corrmat = df.corr()
f, ax = plt.subplots(figsize=(5, 5))

# Draw the heatmap using seaborn
sns.heatmap(corrmat, vmax=.8, square=True,annot=True)
plt.yticks(rotation=0)  #seaborn uses matplotlib internally, as such we can use matplotlib functions to modify plots
plt.xticks(rotation=270)

plt.show()
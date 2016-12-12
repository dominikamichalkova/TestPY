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
print 'no of elements in the NDframe: ',df.size; #no of rows
print df.axes; #returns a list with row/column axis labels
print df['sales'].size;
print df['satisfaction_level'].dtype;


#methods
print 'unique sales fields:',df['sales'].unique();
print df.mean();
print df['average_montly_hours'].mean()/30 #daily working hours avg

#cautious with syntax!!
print('# of people left in 5 years = {}'.format(df[df['left']==1].size))
print('# of people stayed = {}'.format(df[df['left']==0].size))
print('# of people work for HR = {}'.format(df[df['sales']=='hr'].size))
print('protion of people who left in 5 years in % = {}%'.format(int(df[df['left']==1].size/df.size*100)))

#corelation matrix overall
corrmat = df.corr()


# Draw the heatmap using seaborn
sns.heatmap(corrmat, vmax=.8, square=True,annot=True)
plt.yticks(rotation=0)  #seaborn uses matplotlib internally, as such we can use matplotlib functions to modify plots
plt.xticks(rotation=270)

plt.close()
#df.savefig('df.png')


df_low = df[df['salary'] == 'low']
df_medium = df[df['salary'] == 'medium']
df_high = df[df['salary'] == 'high']

print '# of low salary employees= ',df_low.size;
print '# of medium salary employees= ',df_medium.shape[0]; #shape[0] prints out only 0==x axis value
print '# of high salary employees= ',df_high.shape[0];

fmt = '{:<22}{:<25}{}' #spaces between columns

print(fmt.format('FIELD', 'mean', 'std'))
for i, (mean, std) in enumerate(zip(df_low.mean(), df_low.std())):
    print(fmt.format(df_low.columns[i], mean, std))
print('\n')
for i, (mean, std) in enumerate(zip(df_medium.mean(), df_medium.std())):
    print(fmt.format(df_medium.columns[i], mean, std))
print('\n')
for i, (mean, std) in enumerate(zip(df_high.mean(), df_high.std())):
    print(fmt.format(df_high.columns[i], mean, std))

g=sns.factorplot(x="sales", col="salary", col_wrap=3, size=5.5, data=df, kind="count", aspect=0.8, color="green")
g.set_xticklabels(rotation=45)

plt.show()

p=sns.countplot(x="sales", hue="salary", data=df, palette="colorblind")
sns.plt.title('number of employees per salary level')

plt.show()

df.groupby(['sales','salary']).mean()['satisfaction_level'].plot(kind='bar', grid=False, stacked=True, title="satisfaction level per occupation") #all pandas methods

plt.show()


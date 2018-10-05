import seaborn as sns  # This is to import Seaborn. It's standard to import it as sns


##### Distribution plots:

tips = sns.load_dataset('tips')# "tips" is a built in dataset in Seaborn that contains dummy data to play around.

sns.distplot(tips['total_bill'])#This is a distribution plot in a histogram format, of the 'total_bill' column
sns.distplot(tips['total_bill'], kde=False, bins =30, color='red')#This disables the Kernel Density Estimation (blue line). bins sets the "resolution" of the plot

sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')#This is to plot a joint distribution plot of each of the two colmuns of the dataset. 
#kind is the way the plot is going to plot. By dfault it's scattered, hex is hexagon, reg is regression

sns.pairplot(tips)#Pair plot is a 'jointplot' of every single possible combination of the numerical colmuns of the dataset.
sns.pairplot(tips, hue='sex', palette='coolwarm')# hue will color the data as categorical (not numerical data). Pass in the category column to hue.

sns.rugplot(tips['total_bill'])#This plot just draws same size dash bar for every data point (where the density is).

sns.kdeplot(tips['total_bill'])#This will just plot the kde plot Kernel Density Estimation


##### Categorical plots:

import numpy as np

sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)# barplot is a bar plot for categorical data and numerical data. x is categorical and y is numerical. estimator is an estatistical function that can be passed, in this case, it's the Numpy standard deviation

sns.countplot(x='sex', data=tips)#This is just a count of the ocurrances of a categorical column. Just x is passed (categorical)

sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')#This will create a box plot. It can be used it hue.

sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker')# This will create a violin plot. It can be divided by hue
sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker', split=True)# Split will split in two the hue category.

sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', split=True)

sns.swarmplot(x='day', y='total_bill', data=tips)#This plot is a combination of a violin plot and a strip plot to show the distribution

## A way to overlap a violin plot with a swar plot in the same plot (put them toghther right after the other one):

sns.violinplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, color='black')

sns.factorplot(x='day',y='total_bill',data=tips, kind='bar')#Factorplot is the most general form of plots. kind is what describes the factor plot itself.

### Matrix plots:

flights = sns.load_dataset('flights')#This is another built-in dataset in Seaborn to play around. 

## To show heatmaps properly, the dataset format needs to be already in a matrix form, which means that the index name and the column name match to a particular cell relationship relevance. This means the index cannot be the index number itself. 
#To convert into that matrix:

cor = tips.corr()  # This is to create a correlation matrix between the index and columns

## There are two kinds of heeatmat plots:
#  1)  sns.heatmap()
#  2)  sns.clustermap()

sns.heatmap(cor, annot=True, cmap='coolwarm')# annot meanits annotations, which will add the numerical value  on top of the heatmap boxes. cmap is the color map. 

fp = flights.pivot_table(index='month', columns='year', values='passengers')#this crertes a pivot table on a matrix from (to be able to be used in the heatmapo)

sns.heatmap(fp, cmap='magma', linecolor='white', linewidths=1)#This sets the color map to 'magma'. The line color is the color of the division line between boxes, and linewidhts is it's width.

sns.clustermap(fp, cmap='coolwarm', standard_scale=1)# It will cluister and  organize similar groups are close to each other. Standard scale standarizes the data and the range to 1. 

#### Grid plots:
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')#Iris is another built-in dataset (about measurements of flowers) in Seaborn to play around

g = sns.PairGrid(iris)#This is like pairplot, but it can be customized to certain plots:
g.map_diag(sns.distplot)#This plots a distribution plot (from the matplotlib library) in the diagonal plots
g.map_upper(plt.scatter)#This plots a scatter plot (from the matplotlib library) in the upper plots
g.map_lower(sns.kdeplot)#This plots a kde plot in the lower plots


tips = sns.load_dataset('tips')#Loading dataset 'tips' again

g = sns.FacetGrid(data=tips, col='time',row='smoker')#This separate the plots in columns and rows. This is just a canvas (no data yet). The left two plots are "time"= lunch, the two top plots are 'smoker'=yes
g.map(sns.distplot, 'total_bill')#This is what 'time' and 'smoker' will plot against. This is 'total_bill' in the 'x' axes

g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(plt.scatter, 'total_bill', 'tip')#If more than one argument needs to be pased. (x and y)

##### Regresion plots:

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o','v'], scatter_kws={'s':50})#This plots the linear regression. It is slipt in categories with hue. The markes is to identify in the plot the categories, and the scatter_kws is to set the size ('s') of the markers and is passed as a dictionary

sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time')#This can alos be ploted by row and columns instead of hue. (Just like FacetGrid)

sns.lmplot(x='total_bill', y='tip', data=tips, col='day', row='time', hue='sex', aspect=0.6, size=10)#hue can also be added to row and columns, but the data get too packed. The aspect between height and widht can be changed with aspect and the size of the canvas  


## ----->>> CHECK the plot in the Jupter Notebook file in this folder!

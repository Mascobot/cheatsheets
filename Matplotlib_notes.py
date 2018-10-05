import matplotlib.pyplot as plt # This is to import the matplotlib library
import numpy as np

#%matplotlib inline #This is used just in Jupyter Notebook to print inline the graphs. 

#plt.show()# This is used to print the plots when NOT in Jupyter Notebook

x = np.linspace(0,5,11)# Create a list of items from 0 to 5 with 11 equally spaced numbers. 
y = x ** 2 # Expoential to the 2 of x list. 

fig = plt.figure()# this is to create (instanciate) a blank canvas. 

pardeejes1 = fig.add_axes([0.2,0.2,0.8,0.8])#This is to add a table to the fig object. The list takes 4 arguments: [left, bottom, width, height] which range from 0 to 1. (The percentage of the range of that fig convas) 
pardeejes2 = fig.add_axes([0.2,0.4,0.3,0.3])#This is to add another table. 

pardeejes1.set_xlabel('X label')#This is to set the name on the table on the axes X
pardeejes1.set_ylabel('Y label')#This is to set the name on the table on the axes Y

pardeejes2.set_xlabel('Eje X')#This is to set the name on the table on the axes X
pardeejes2.set_ylabel('Eje Y')#This is to set the name on the table on the axes Y

pardeejes1.set_title('Tabla 1')#This is to set the title on the table.
pardeejes2.set_title('Tabla 2')

pardeejes1.plot(x,y)#This is to plot the graph in the table with the x,y values.
pardeejes2.plot(y,x)

plt.show()#This is to show the tables when the python script is run. This is no used in Jupyter Notebook and it will print all tables. It just needs to be called at the end of the script.


##### How to do multiple tables (Subplots):

nuevocanvas = plt.figure()# This is to create/instanciate a new canvas. This will have dfault size and dpi. 

nuevocanvas = plt.figure(figsize=(3,2), dpi=600)#If parameters are pased, it will asign figsize of 3 by 2 inches. Dots per inch = 600

nuevocanvas, tablas = plt.subplots(nrows=1, ncols=2)#This is to create multiple tables in one canvas. The new variable "tablas" it ends up being a list. nrows and ncols defines the number of rows and columns (tables in the matrix) 
nuevocanvas, tablas = plt.subplots(nrows=1, ncols=2,figsize=(3,2))# It can also pass paratemers of size. If not, it assigns the default. 
tablas[0].set_title('First Table')#This is to access and set the title the first element in the list (the first table)
tablas[1].set_title('Second Table')#This is to access and set the title to the second element of the list (the second table)

tablas[0].plot(x,y)#Plot x and y in the first table
tablas[1].plot(y,x)#Plot y and x in the second table
plt.tight_layout()# This is to avoid the overlap pf the texts over the tables in the plots. Put at the end of the plot statements. 

####For a canvas with a  grid of 4 (2 x 2):
nuevocanvas, tablas = plt.subplots(nrows=2, ncols=2)#This is to create multiple tables in one canvas. The new variable "tablas" it ends up being a list. nrows and ncols defines the number of rows and columns (tables in the matrix) 
tablas[0,0].set_title('First Table')#This is to access and set the title the first element in the list (the first table)
tablas[0,1].set_title('Second Table')#This is to access and set the title to the second element of the list (the second table)
tablas[1,0].set_title('Third Table')#This is to access and set the title to the third element of the list (the third table)
tablas[1,1].set_title('Forth Table')#This is to access and set the title to the forth element of the list (the forth table)

tablas[0,0].plot(x,y)#Plot x and y in the first table
tablas[0,1].plot(y,x)#Plot y and x in the second table
tablas[1,0].plot(x,y)#Plot x and y in the third table
tablas[1,1].plot(y,x)#Plot y and x in the forth table
plt.tight_layout()# This is to avoid the overlap pf the texts over the tables in the plots. Put at the end of the plot statements. 

##How to save the plot into an image:
nuevocanvas.savefig('mi_picture.png', dpi=500)#This is to save a file with the ptos and with a defined dpi. I not dpi defined, it saves it with default. It can save png, jpeg or pdf. Just specify extension.

####Legends on the tables for the graphs:

#define new canvas:
fig = plt.figure()#Creat new canvas. 
ax = fig.add_axes([0,0,1,1])#Add a new table (set of axes)
ax.plot(x,y, label='First plot')#Plot in that table x and y. this will add a legend to this plot. 
ax.plot(y,x, label='Second plot', color='purple', linewidth=5, alpha=0.5, linestyle='--', marker='o')#Plot in that same table y and x. This will add a legend to this plot and the color of the graph will be purple. The thichnkess of the line will be 5 (default is 1). Aplha is the transparency. Linestyle will give you the form of the line. Marker is the points where the values are.

ax.set_xlim([0,1])#This is to "zoom in" in a sepcif range in the axis. It will just plot it in that area.
ax.set_ylim([0,2])#This is to "zoom in" in a sepcif range in the axis. It will just plot it in that area.

ax.legend()#This will print the legends on the graphs (defined above).

#if the legend box defined above this line over laps with the graps, it can be moved by passing a code. Example:
ax.legend(loc=0)#Pass location 0, which means "best" location. Check matplotlib website for other reference location codes based on the desired location.
 

## This is a good online tutorial for Matplotlib: https://www.labri.fr/perso/nrougier/teaching/matplotlib/








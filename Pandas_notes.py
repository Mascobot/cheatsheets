import numpy as np
import pandas as pd

#Panda Series are like Numpy arrays but they can be index/accessed with labels. They are similar to diccionaries, but can store pretty much any data.
#Examples

labels = ["a", "b", "c"] #- This is just a list of strings that will be used in a pandas Series as "index" or label
my_data = [10,20,30]# - This is a list of integers
arr = np.array(my_data)# This is just converting a python list into an array
d = {"a":10, "b":20,"c":30}# This is just a diccionary, just as example on how it can be converted into a pandas Series

my_series = pd.Series(data = my_data) #This creates a panda Series and asigns in the data column the my_data list declared previously. IT ASSIGNS THE DEFAULT INDEX (0,1,2,3, etc...)

my_series2 = pd.Series(data=my_data, index=labels)#This creates a panda Series and asigns in the data column the my_data list declared previously. THIS ASSIGNS THE labels STRING LIST AS THE INDEX.
my_series2 = pd.Series(my_data, labels)#-> Same as above. There's no need to declare "data" and "index" as long they are in the correct order.

my_series3 = pd.Series(arr, labels)# - This creates a Series out of the arr Numpy array. Same as before, it assigns labes as the index.

my_series4 = pd.Series(d)# - This creates a Series out of dictionary. The COOL part is that it automaticaaly assigns the data and the index based on the data in the diccionary.

# ONE BIG benefit of the Pandas Series vs a regular Numpy array, is that a Panda Series can hold pretty much any kind of data object, INCLUDING FUNCTIONS!

#Example:

my_funcSeries = pd.Series(data=[sum,print,len])# A Panda Series can also hold functions!

ser1 = pd.Series([1,2,3,4],["USA","Germany","USSR","Japan"])# This saves the numbers as data, and the countries as labels (indexes)
a = ser1["USA"]# This assigns the value of 'USA'. In this case, 1

ser2 = pd.Series([1,2,5,4],["USA","Germany","Italy","Japan"])# This saves the numbers as data, and the countries as labels (indexes)

a = ser1 + ser2 #This will match the labels and add them. So, USA will be 2.0, Germany = 4.0, USSR = NaN, Italy = NaN, Japan = 8.0
# Also note that the result in a will be conveterted from integer to float. This to avoid loosing data in the operations.

##################
##### DATA FRAMES:
#Data Frames are just a set of Pandas Series

numeros = np.random.randint(1,100, 20).reshape(5,4) #- This is just to create some random data to use. It's a matrix of 5 rows by 4 columns of total 20 random numbers from 1 to 100
index1 = ["A","B","C","D","E"]# - This is just a list of strings that will work as labels for the Data Frame of one axis
index2 = ["W","X","Y","Z"]# - This is just a list of strings that will work as labels for the Data Frame of the other axis

df = pd.DataFrame(numeros, index1, index2)# -> This is how a Data Frame is created (Data, Row labels, Column labels)

#Displaying columns from the data frame:
print df["W"] # - This will display the "W" Column and with each corresponding row label to each element
print df[["W","Z"]] # - This will show both "W" and "Z" columns and with each corresponding row label to each element. Note that needs to be passed as a list

#Adding a new column:
df["nueva_columna"] = [1,2,3,4,5] # - This adds a new column to the Data Frame. NOTE that number of items in diccionary need to match number of rows with Data Frame

#Dropping and Deleting a column or row:
print df.drop("nueva_columna", axis=1) # This drops the column "new". PLEASE NOTE THAT IT DOES NOT DELETE IT FROM THE ORIGINAL DATA FRAME "df". It is not inplace. Axis = 0 is for rows, axis = 1 is for columns
print df.drop("nueva_columna", axis=1, inplace=True) # THIS DOES DELETE THE COLUMN FROM THE ORIGINAL "df" DATA FRAME. Axis = 0 is for rows, axis = 1 is for columns

#Selecting rows from Data Frames:
print df.loc["C"]# This will get the ROW named "C"
print df.iloc[2]# This will get the ROW with index 2. The "i" at the begining is from index.

#Selecting subsets of the Data Frame:
print df.loc["B","Y"]# This will get the specific position of the crossing of "B" and "Y"
print df.loc[["A","B"],["W","Y"]]# This will get the subset of rows "A" and "B" and columns "W" and "Y"
print df.loc[:,"Y"]# This will get the entire column "Y"

print df.iloc[[0,2,4], [1,3]]# This will get the rows with index 0, 2, 4 and the columns with index 1 and 3

#######################################################################
#Conditionals:
## Continuation of Data Frames in Pandas. Conditionals in Data Frames:

numeros = np.random.randint(1,100, 20).reshape(5,4) #- This is just to create some random data to use. It's a matrix of 5 rows by 4 columns of total 20 random numbers from 1 to 100
index1 = ["A","B","C","D","E"]# - This is just a list of strings that will work as labels for the Data Frame of one axis
index2 = ["W","X","Y","Z"]# - This is just a list of strings that will work as labels for the Data Frame of the other axis

df = pd.DataFrame(numeros, index1, index2)# -> This is how a Data Frame is created (Data, Row labels, Column labels)

print df # df DataFrame:
	W	X	Y	Z
A	2.706850	0.628133	0.907969	0.503826
B	0.651118	-0.319318	-0.848077	0.605965
C	-2.018168	0.740122	0.528813	-0.589001
D	0.188695	-0.758872	-0.933237	0.955057
E	0.190794	1.978757	2.605967	0.683509


print df>0 # -> This will throw a BOOLEAN array with every element compared with > 0. (True or False), Like this one:
    W	X	Y	Z
A	True	True	True	True
B	True	False	False	True
C	False	True	True	False
D	True	False	False	True
E	True	True	True	True


print df[df>0] # - >This will throw the data Frame itself with some data, just where it is boolean "True" and NaN where it is False:
    W	X	Y	Z
A	2.706850	0.628133	0.907969	0.503826
B	0.651118	NaN	NaN	0.605965
C	NaN	0.740122	0.528813	NaN
D	0.188695	NaN	NaN	0.955057
E	0.190794	1.978757	2.605967	0.683509


print df['W']>0 # This will print the entire "W" column that is > 0
    W
A	2.706850
B	0.651118
D	0.188695
E	0.190794

print df[df['W']>0] # This will print the Data Frame, but just the row elements in the "W" column where the element in the row is > 0:
    W	X	Y	Z
A	2.706850	0.628133	0.907969	0.503826
B	0.651118	-0.319318	-0.848077	0.605965
D	0.188695	-0.758872	-0.933237	0.955057
E	0.190794	1.978757	2.605967	0.683509


print df[df['W']>0]['X'] # This, from the last filter ^, just the column 'X':
A    0.628133
B   -0.319318
D   -0.758872
E    1.978757


print df[df['W']>0][['X','Y']] #You can also pass multiple columns in a list. Note that it needs to be in a List:
	X			Z
A	0.628133	0.503826
B	-0.319318	0.605965
D	-0.758872	0.955057
E	1.978757	0.683509

print df[(df['W']>0) & (df['X']>1)] # This is to do additional conditions. Note that word "and" it will give an error. Instead, we need to use "&"
print df[(df['W']>0) | (df['X']>1)] # This is the same as above for the OR operator. It can't use the word "or". Instead, we need to use "|"

#To reset the index of the Data Frame to a numerical value:
df.reset_index() # - This Resets the index to a numerical value. Note that it is not inplace and it won't save it to the original df Data Frame, If deried to save to original Data Frame: df.reset_index(inplace=True)
Index   W			X			Y			Z
0    A	2.706850	0.628133	0.907969	0.503826
1    B	0.651118	-0.319318	-0.848077	0.605965
2    C	-2.018168	0.740122	0.528813	-0.589001
3    D	0.188695	-0.758872	-0.933237	0.955057
4    E	0.190794	1.978757	2.605967	0.683509

#Let's add one more column:
newind = 'CA NY WY OR CO'.split()# This will split the string wehre there are spaces and will convert it into a list. (It's faster than typing all commas and "")
df['States'] = newind #This just added the new column, newind, to the Data Frame. Please note that the number of elemens in the list in newind needs to match the number of rows in the Data Frame

#Now let's set the index to the new column that we just added:

df.set_index('States', inplace=True)#This just set the default index to States. Note that it's not a defualt inplace, so need to state it to save it. Also, note that it will overwirte the old index, and you won't be able to retain that information back

## Multi-index and index hierarchies:
#Index labels:
outside = 'G1 G1 G1 G2 G2 G2'.split() #This is to create a list with the 6 string elements inside for the label
inside = '1 2 3 1 2 3'.split() #This is to create a list with the 6 string elements inside for the label
hier_index = list(zip(outside, inside)) # This will match in a tuple pair every element in one list with the other one in order, and make it a list of tuples
print hier_index #This is what it will print:
[('G1', '1'), ('G1', '2'), ('G1', '3'), ('G2', '1'), ('G2', '2'), ('G2', '3')]
hier_index = pd.MultiIndex.from_tuples(hier_index)
print hier_index #This will print:
MultiIndex(levels=[[u'G1', u'G2'], [u'1', u'2', u'3']],
           labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])

df = pd.DataFrame(np.random.randn(6,2), hier_index,['A', 'B'])
print df #This will print:
		A	B
G1	1	-1.390311	-0.214507
	2	0.282232	0.836623
	3	0.643066	-0.250494
G2	1	2.017221	-1.783216
	2	-0.656551	0.777836
	3	1.528189	-0.328574

print df.loc['G1']#This will print:
	A	B
1	-1.390311	-0.214507
2	0.282232	0.836623
3	0.643066	-0.250494

print df.loc['G1'].loc['1']#This will print:
A   -1.390311
B   -0.214507
Name: 1, dtype: float64

print df.loc['G1'].loc['1']['A']#This will print:
-1.3903107025395443

print df.index.names #This will print the name of the indexes:
FrozenList([None, None]) # Currently there are no names assigned.

df.index.names = ['Groups', 'Numbers']# This assigns the names to the indexes
print df #This will print:
					A		B
Groups	Numbers
G1		1		-1.390311	-0.214507
		2		 0.282232	0.836623
		3		 0.643066	-0.250494
G2		1	     2.017221	-1.783216
		2	    -0.656551	0.777836
		3	     1.528189	-0.328574

print df.xs('1', level='Numbers') # This is for getting cross sectional data (xs), meaning that it can skip the Groups layer and get data straight from the Numbers index in both Groups:
			A	B
Groups
G1	-1.390311	-0.214507
G2	2.017221	-1.783216

print df.xs('1', level='Numbers')['A'] # This will get the data as above, and go one step more in just getting the Index 'A'

#############################################
## Manipulating missing data (Nan) on Pandas:

d = {'A':[1,2,pd.nan], 'B':[5, pd.nan,pd.nan], 'C':[1,2,3]} # Define a list to later convert it in a DataFrame

df = pd.DataFrame(d)# Convert the dictionary d in a pandas DataFrame:

print df # Print the entire DataFrame:
	A	B	C
0	1.0	5.0	1
1	2.0	NaN	2
2	NaN	NaN	3

print df.dropna()#This will print a DataFrame dropping all rows that have at least one NaN value:
	A	B	C
0	1.0	5.0	1

print df.dropna(axis=1)#This will print a DataFrame dropping all columns that have at least one NaN value:
	C
0	1
1	2
2	3

print df.dropna(thresh=2)  # This will Keep only the rows with at least <2 NaN values.
A	B	C
0	1.0	5.0	1
1	2.0	NaN	2

df.fillna(value='FILL IN VALUE') #This will fill in the Value assigned to the NaN values:
	A	B	C
0	1	5	1
1	2	FILL IN VALUE	2
2	FILL IN VALUE	FILL IN VALUE	3

df['A']# Print column 'A':
0    1.0
1    2.0
2    NaN

df['A'].fillna(value=0) # This will fill in the value 0 to all NaN values in column 'A':
0    1.0
1    2.0
2    0.0

df['A'].fillna(value=df['A'].mean()) # This will fill in the mean value of all the other values in column 'A' in all the NaN values:
0    1.0
1    2.0
2    1.5

###############################
##### Groupby method in Pandas:

data = {'Company': ['Google', 'Google', 'Microsoft', 'Microsoft', 'Facebook', 'Facebook'], 'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}## This is just a dictionary that will be converted in to a DataFrame

df = pd.DataFrame(data)# This converts the python dictionary into a Pandas DataFrame

print df #Printd the DataFrame:
	Company	Person	Sales
0	Google		Sam		200
1	Google		Charlie	120
2	Microsoft	Amy		340
3	Microsoft	Vanessa	124
4	Facebook	Carl	243
5	Facebook	Sarah	350

print df.groupby('Company')# This will print:
<pandas.core.groupby.DataFrameGroupBy object at 0x05E2F710 >

byComp = df.groupby('Company')

print byComp.mean()# This will give the mean of the string values found in the DataFrame under the 'Company' category. It will ignore the strings (in this case the names of the person) for the calculation:
			Sales
Company
Facebook	296.5
Google		160.0
Microsoft	232.0

print byComp.sum()# This will give the sum of the string values found in the DataFrame under the 'Company' category. It will ignore the strings(in this case the names of the person) for the calculation:
			Sales
Company
Facebook	593
Google		320
Microsoft	464

print byComp.std()# This will give the standard deviation of the string values found in the DataFrame under the 'Company' category. It will ignore the strings (in this case the names of the person) for the calculation:
			Sales
Company
Facebook	75.660426
Google		56.568542
Microsoft	152.735065

print byComp.sum().loc['Facebook']#This will print the sum of the integers in the column 'Facebook'. In this case Sales:
Sales    593

print df.groupby('Company').count()#This will print the count of items:
			Person	Sales
Company
Facebook	2	2
Google	2	2
Microsoft	2	2

# This will print the max value in company. Note that also it categorizes the stirngs based on their alphabetical order.
print df.groupby('Company').max()

print df.groupby('Company').describe()# This will give a whole set of predefined data outputs for the 'Company' category, from the numerical columns:
Sales
			count	mean	std			min		25 % 	50 % 	75 % 	max
Company
Facebook	2.0		296.5	75.660426	243.0	269.75	296.5	323.25	350.0
Google		2.0		160.0	56.568542	120.0	140.00	160.0	180.00	200.0
Microsoft	2.0		232.0	152.735065	124.0	178.00	232.0	286.00	340.0

print df.groupby('Company').describe().transpose()# This is to transpose it in case we want to have the comapnies as columns instead:
		Company	Facebook	Google	Microsoft
Sales	count	2.000000	2.000000	2.000000
		mean	296.500000	160.000000	232.000000
		std		75.660426	56.568542	152.735065
		min		243.000000	120.000000	124.000000
		25 % 	269.750000 140.000000 178.000000
		50 % 	296.500000 160.000000 232.000000
		75 % 	323.250000 180.000000 286.000000
		max		350.000000	200.000000	340.000000

print df.groupby('Company').describe().transpose()['Facebook']# This is the same as above, but just for 'Facebook':
Sales  count      2.000000
       mean     296.500000
       std       75.660426
       min      243.000000
       25 % 	269.750000
       50 %	 	296.500000
       75 % 	323.250000
       max      350.000000
Name: Facebook, dtype: float64

############################
## Merging, Joining and Concatenating DataFrames:

# CONCATENATING: 
#DataFrame examples for concatenating: 
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])


print df1
	A 	B 	C 	D
0 	A0 	B0 	C0 	D0
1 	A1 	B1 	C1 	D1
2 	A2 	B2 	C2 	D2
3 	A3 	B3 	C3 	D3

print df2
 	A 	B 	C 	D
4 	A4 	B4 	C4 	D4
5 	A5 	B5 	C5 	D5
6 	A6 	B6 	C6 	D6
7 	A7 	B7 	C7 	D7

print df3
 	A 		B 		C 		D
8 	A8 		B8 		C8 		D8
9 	A9 		B9 		C9 		D9
10 	A10 	B10 	C10 	D10
11 	A11 	B11 	C11 	D11

#Concatenation basically "glues" toghther DataFrames. Keep in mind that the dimensions should match along the axis you will be concatenating on. We will use
# pd.concat instruction and pass a list of DataFrames inside to concatenate toghther:

con = pd.concat([df1,df2,df3])# This by default glues on axis 0 (adds rows)
print con
	A 	B 	C 	D
0 	A0 	B0 	C0 	D0
1 	A1 	B1 	C1 	D1
2 	A2 	B2 	C2 	D2
3 	A3 	B3 	C3 	D3
4 	A4 	B4 	C4 	D4
5 	A5 	B5 	C5 	D5
6 	A6 	B6 	C6 	D6
7 	A7 	B7 	C7 	D7
8 	A8 	B8 	C8 	D8
9 	A9 	B9 	C9 	D9
10 	A10 	B10 	C10 	D10
11 	A11 	B11 	C11 	D11

con = pd.concat([df1,df2,df3], axis=1)# This glues on colmuns (adds columns to the right). PLEASE NOTE THAT IT DOESN'T DROP ANY DATA:
print con
	A 		B 		C 		D 		A 		B 		C 		D 		A 		B 		C 		D
0 	A0 		B0 		C0 		D0 		NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN
1 	A1 		B1 		C1 		D1 		NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN
2 	A2 		B2 		C2 		D2 		NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN
3 	A3 		B3 		C3 		D3 		NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN
4 	NaN 	NaN 	NaN 	NaN 	A4 		B4 		C4 		D4 		NaN 	NaN 	NaN 	NaN
5 	NaN 	NaN 	NaN 	NaN 	A5 		B5 		C5 		D5 		NaN 	NaN 	NaN 	NaN
6 	NaN 	NaN 	NaN 	NaN 	A6 		B6 		C6 		D6 		NaN 	NaN 	NaN 	NaN
7 	NaN 	NaN 	NaN 	NaN 	A7 		B7 		C7 		D7 		NaN 	NaN 	NaN 	NaN
8 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	A8 		B8 		C8 		D8
9 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	A9 		B9 		C9 		D9
10 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	A10 	B10 	C10 	D10
11 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	NaN 	A11 	B11 	C11 	D11


## MERGING:
#The merge function allows you to merge DataFrames together using similar logic as merging SQL tables together:
#DataFrame examples to merge:
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print left
 	A 	B 	key
0 	A0 	B0 	K0
1 	A1 	B1 	K1
2 	A2 	B2 	K2
3 	A3 	B3 	K3

print right
 	C 	D 	key
0 	C0 	D0 	K0
1 	C1 	D1 	K1
2 	C2 	D2 	K2
3 	C3 	D3 	K3

merg = pd.merge(left,right,how='inner',on='key')
print merg
	A 	B 	key 	C 	D
0 	A0 	B0 	K0 	C0 	D0
1 	A1 	B1 	K1 	C1 	D1
2 	A2 	B2 	K2 	C2 	D2
3 	A3 	B3 	K3 	C3 	D3

# A more complicated example on merging:
#More DataFrame examples to merge:
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

merg = pd.merge(left,right,on=['key1','key2'])#By default it will habe how to 'inner'. Note that the on= needs to pass a list if more than one element
print merg
	A 	B 	key1 	key2 	C 	D
0 	A0 	B0 	K0 	 	K0 		C0 	D0
1 	A2 	B2 	K1 	 	K0 		C1 	D1
2 	A2 	B2 	K1 	 	K0 		C2 	D2

merg = pd.merge(left,right,how='outer',on=['key1','key2'])
print merg

	A 	B 	key1 	key2 	C 	D
0 	A0 	B0 	K0 		K0 		C0 	D0
1 	A1 	B1 	K0 		K1 		NaN NaN
2 	A2 	B2 	K1 		K0 		C1 	D1
3 	A2 	B2 	K1 		K0 		C2 	D2
4 	A3 	B3 	K2 		K1 		NaN NaN
5 	NaN NaN K2 		K0 		C3 	D3


merg = pd.merge(left,right,how='left',on=['key1','key2'])
print merg
 	A 	B 	key1 	key2 	C 	D
0 	A0 	B0 	K0 		K0 		C0 	D0
1 	A1 	B1 	K0 		K1 		NaN NaN
2 	A2 	B2 	K1 		K0 		C1 	D1
3 	A2 	B2 	K1 		K0 		C2 	D2
4 	A3 	B3 	K2 		K1 		NaN NaN

## JOINING:
## Joining is like merging, but it joins in the index instead of a specific column (on=):
#DataFrame examples for joining:
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

j = left.join(right)
print j
 	A 	B 	C 	D
K0 	A0 	B0 	C0 	D0
K1 	A1 	B1 	NaN NaN
K2 	A2 	B2 	C2 	D2

j = left.join(right, how='outer')
print j
 	A 	B 	C 	D
K0 	A0 	B0 	C0 	D0
K1 	A1 	B1 	NaN NaN
K2 	A2 	B2 	C2 	D2
K3 	NaN NaN C3 	D3

##############
## Operations:

df = pd.DataFrame({'col1':[1,2,3,4],
					'col2':[444,555,666,444],
					'col3':['abc','deff','ghi','xyz']})

### To get Unique values out a DataFrame:

print df['col2'].unique()
[444 555 666]

print len(df['col2'].unique())# This will return the lenght of the unique elements on 'col2'.
3

print df['col2'].nunique()# This will return the lenght of the unique elements on 'col2'. The same as len(df['col2'].nunique())
3

print df['col2'].value_counts()# This will return all the values with their counts, organized from top to bottom (descendant) 
444    2
555    1
666    1

#Reminder on conditional selection:
print df['col1']>2
0    False
1    False
2     True
3     True

print df[df['col1']>2]
	col1	col2	col3
2	3		666		ghi
3	4		444		xyz

print df[(df['col1']>2) & (df['col2']==444)]
	col1	col2	col3
3	4		444		xyz

print df['col1']
0    1
1    2
2    3
3    4

print df['col1'].sum()  # This will print the entrie sum of 'col1' column
10

# The .apply() method is very useful to apply custom functions to entire dataframes, columns or indexes:

def times2(x):#This is just a custom fucntion that will be used with the .apply() method.
	return x*2

print df['col1'].apply(times2)#This will apply the times2 function to every element in the dataframe
0    2
1    4
2    6
3    8

print df['col3']
0    abc
1 	 deff
2    ghi
3    xyz

print df['col3'].apply(len)#This can also pass existing built-in python functions, like len 
0    3
1    4
2    3
3    3

#.apply() can be very useful for lambda expressions, to simplify writting def functions:
df['col1'].apply(lambda x: x*2)# This lambda expression is the same as the def fucntion times2 above.
0    2
1    4
2    6
3    8

print df.columns
Index([u'col1', u'col2', u'col3']

print df.index
RangeIndex(start=0, stop=4, step=1)

#How to find a coorelation between columns:
df[['col1','col2']].corr()


## How to sorter and order a DataFrame:

print df.sort_values(by='col2')#This will sort the values ascending in columun "col2"
	col1  col2 col3
0     1   444  abc
3     4   444  xyz
1     2   555  deff
2     3   666  ghi

print df.isnull()# This will return a dataframe of boolean values, whether the value is null or not:
	col1   col2   col3
0  False  False  False
1  False  False  False
2  False  False  False
3  False  False  False

### Pivot tables. A pivot table is a table that summarizes data from another table:
#New DataFrame:

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)

print df
	A	B	C	D
0	foo	one	x	1
1	foo	one	y	3
2	foo	two	x	2
3	bar	two	y	5
4	bar	one	x	4
5	bar	one	y	1

print df.pivot_table(values='D', index=['A','B'],columns=['C'])

	C	x	y
A	B		
bar	one	4.0	1.0
	two	NaN	5.0
foo	one	1.0	3.0
	two	2.0	NaN

########
######## Data Input and Output in Pandas
#Pandas can read and write data from:
#CSV 
#Excel 
#HTML
#SQL
#Some more...

#We need to install the following libraries using pip or conda:
#conda install sqlalchemy
#conda install lxml
#conda install html5lib
#conda install BeautifulSoup4

#CSV files:
archivo = pd.read_csv('example.csv')#This is how to read from a csv file:
#Pandas can read from multiple files, including clipboard, just type pd.read_(tab) and it will show up a list
#This is how to write to a csv file:
archivo.to_csv('Mynewfile.csv', index=False)#This will save a new csv file, with the name "Mynewfile.csv" and won't dave the index in the file in case there's one from a DataFrame.

#Excel files:
#Pandas can also read and write excel files. Please note that it can just read the date. It won't read formulas, images or other:
excelfile = pd.read_excel('Excel_sample.xlsx', sheetname='Sheet1')#This is to read from an excel file. it needs the Sheet name. 

excelfile.to_excel('NewExcelfile.xlsx', sheet_name='NewSheet')#This is how to write to an Excel sheet. 

#HTML:
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')#This is how to read from an webpage. This actually saves it as a list. 

print data[0].head()
#Table from the website will show up here. 

### map()

#This will replace items in an entire column, with the .map() function:
#Assuming df['Day of the Week'] column only has string values 0,1,2,3,4,5,6
dmap = {0:'Lun', 1:'Mar', 2:'Mier',3:'Juev', 4:'Vier', 5:'Sab', 6:'Dom'}
df['Day of the Week'] = df['Day of the Week'].map(dmap)



#SQL
#Pandas is not the best way to read a SQL database direclty. The best way, is to use the right library/SQL engine for the right database format (psycopg2, PyMySQL, etc)
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')#This is to create a simple local SQL databse engine running on memory. 
excelfile.to_sql('my_table', con=engine)#This will save the table to the engine variable wich is the local SQL database created in the line before. 
sqlread = pd.read_sql('my_table', con=engine)#This will read back from the SQL engine and save the table in variable sqlread. 









 






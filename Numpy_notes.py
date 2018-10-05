import numpy as np

##How to cast normal python lists, or litst of lists into Numpy arrays:

my_list = [1,2,3]
arr = np.array(my_list)

my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
matriz = np.array(my_matrix)

## How to use numpy built in arrays to create arrays faster (than casting normal python lists)

np.arange(0,10)#This is very similar to the python range function, but to create an array with a rangeself. (First number is start, second is stop)
np.arange(0,10,2)#(First number is start, second is stop, third is interval)

np.zeros(3)#This will create an array of zeros, which will have a one dimensional vector of 3 out.
np.zeros((3,4))#This will create a 2 dimensional array of zeros, with 3 rows and 4 columns
np.ones(3)#This will create an array of ones, which will have a one dimensional vector of 3 out.
np.ones((3,4))#This will create a 2 dimensional array of ones, with 3 rows and 4 columns

np.linspace(0,1,10)# This will create an array of range 0 to 1 with 10 evenly space points from 0 to 1. -> NOT TO BE CONFUSED WITH arange. linspace stands for "linearly spaced points"

np.eye(4)#This will create and identity matrix, a 2-dymensional square matrix (that columns and arrays can be flippled and it's the same matrix)

np.random.rand(5)#This will create a one dimensional array of 5 random elements that go from 0 to 1.
np.random.rand(5,6)#This will create a two dimensional array of 5 rows and 6 columns of random elements from 0 to 1.
np.random.randn(4,5)#This will return a two dimensional array of 4 rows and 5 columns of a standard normal distribution (Gaussian distribution)
np.random.randint(1,100,8)#This will generate 8 random numbers between 1 to 99

arr = np.arange(25)

arr.reshape(5,5)#This will re-arragne the format of the matrix, and convert it into a 5 by 5 array with the same numbers on the matrix arr. Please note that all columns anr rows need to be filled, otherwise it will give an error.

arr.max()# -> This will rerutn the max value in the array
arr.min()# -> This will return the min value in the array
arr.argmax()# -> This will return the Index location (position) of that max value (NOT THE MAX VALUE ITSELF)
arr.argmin()# -> This will return the index location (postion) of the min value (NOT THE MIN VALULE ITSELF)

arr = arr.reshape(5,5)# -> This reshapes the array to a 5 by 5 matrix
print arr.shape # This will print the size of the array as a 5 by array

print arr.dtype # This will print the data type that is in the array

#Indexing and getting data from the arrays:

arr = np.arange(10)

print arr[5]# - This will give me the index position 5
print arr[2:5]# - This will return the range of that Indexing
print arr[:5]# - This will retrun from the beginning to index 5
print arr[5:]# - This will return from index to until the end of the array

arr[0:5] = 100 #- This will assign the value 100 to each position in every index from 0 to 5, and will leave the remaining indexes with their previos data

#IMPORTANT!! MEMORY ISSUES WITH ARRAYS:
arr = np.arange(10)
slice_of_arr = arr[0:6] #This will DISPLAY the first 6 indexes of arr. THIS IS NOT A COPY OF THE ARRAY - IT IS JUST A VIEW OF THE ORIGINAL ARRAY
#IF WE Broadcast (assign) a new value to the slice array:
slice_of_arr[:] = 99 # This will assig to the index 0 to 6 the value 99. NOTE that the original arr array will be also changed to 99 values, as slice array is just a "VIEW" of the original array

#IF YOU ACTUALLY WANT A COPY OF THE ARRAY:
arr_copy = arr.copy()

#Calling indexes and data from arrays:
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])

#There are 2 ways of getting data from the arrays:
# 1:
arr_2d[0][0] # - This will get the first number in the 0 row 0 column (which is 5 if in this case)
arr_2d[1][2] # - This will get the  number in the 1 row 2 column (which is 30 if in this case)

# 2: (This is the recommended method):
arr_2d[0,0]# - This will get the first number in the 0 row 0 column (which is 5 if in this case)
arr_2d[1,2]# - This will get the  number in the 1 row 2 column (which is 30 if in this case)

# To get ranges of data:
# We use slice notation:
arr_2d[:2,1:] # - This will get the 0 and 1 row, and on top of that, it filters to just the 1index column top the end (right)

# The most common and useful way top get data from Arrays is the Conditional selection:
arr = np.arange(1,11)# This will generate a one dimensional array with vales range 1 to 10.

bool_arr = arr > 5 # This will return a Boolean array, for every single item in the array, it will compare it, and it will dave it as a True or False boolean value saved in that new boolean arrayself.

more_than_5_arr = arr[bool_arr] # - Here will only get the numbers in the array that happen to be boolean True (in this case 6, 7, 8, 9 and 10)
# ^ This is the same as:
arr[arr>5]
arr[arr<3]# - This will return only the elements that are less than the value 3

# This is how an array of values 0 to 50 in a shape 5 rows by 10 columns would be defined:
arr = np.arange(50).reshape(5,10)

#or if you want it filled with Random int numbers and rehshape it:
arr = np.random.randint(1,100, 20).rehshape(4,5)

###########################################################################################################################################
#### NUMPY OPERATIONS:

arr = np.arange(0,11)

print arr + arr #-> This is adding an array to another array. (it adds every elemenet with it's corresponding position element)
print arr - arr #-> This is substract an array to another array. (it substracts every elemenet with it's corresponding position element)
print arr * arr #-> This is multiplying an array to another array. (it multiplies every elemenet with it's corresponding position element)

print arr + 100 #-> This adds 100 to every single element in the array
print arr - 100 #-> This will substract 100 from every single element in the array
print arr * 100 #-> This will multiply by 100  every single element in the array
print arr ** 2 #-> This is to the 2
print np.sqrt(arr) #-> This will take the square root of every elemen in the array
print np.exp(arr) #-> This will give the exponential
print np.max(arr) #-> This will give the max value in the array. This is the same as arr.max()
print np.sin(arr) #-> This will give the sinous of all elements inside the arrays
print np.log(arr) #-> This will give you the logarithmic of every element

#-> If something could give an error like dividing by 0, Numpy will give a warning.

arr.sum() #-> This will add all the numbers in the array. This is the same as np.sum(arr)
print np.sum(arr)# -> This is same as above. It will add all the numbers in the array.

np.std(arr)# -> This will give the standard deviation of the array
arr.std() #-> Sames as above


#To find all the list of the Universal functions of Numpy, go here: https://docs.scipy.org/doc/numpy/reference/ufuncs.html

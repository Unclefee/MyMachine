import numpy as np
#creating an array
a= np.array([1,2,3,4,5])
print(a)
#creating a 2D array
b= np.array([[1,2,3],[4,5,6]])
print(b)
#creating an array with zeros
c= np.zeros((2,3))
print(c)
#creating an array with ones
d= np.ones((2,3))
print(d)
#creating an array with random values
e= np.random.random((2,3))  
#creating an array with defualt values
a_nul= np.emptyfull((3,4),9)
#creating an array with a range
x_values = np.arange(0, 10, 1)
print(x_values) 
print(a_nul)
print(e)
print(a_nul.shape)
print() 

#To load a python file in another python file.
a = np.load('numpy_basics.py')
print(a)

#to save a numpy array to a csv file
np.save('numpy_array.csv',a,delimiter=',')
#to load a numpy array from a csv file
b = np.load('numpy_array.csv.npy')
print(b)
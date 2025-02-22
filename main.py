import numpy as np
num = [1,2,3,4,5]
print(num)
print(type(num))

#np array
array1 = np.array(num)
print(array1)
print(type(array1))

#normal list
for i in num:
    i+=2
print(num)

#np array
array1 = array1 + 2
print(array1)

#np 0's array
zarray = np.zeros(60)
print(zarray)
print(zarray.dtype)

#np 1's array
orray = np.ones((4,5))
print(orray)

#finding dimension
print(zarray.ndim)
print(orray.ndim)

#finding shape
print(zarray.shape)
print(orray.shape)

#finding size (number of elements in array)
print(zarray.size)
print(orray.size)

#arrays with range
n = np.arange(0,101,2)
print(n)
n = np.arange(0,200,25)
print(n)

#prints evenly spaced numbers in a range
array2 = np.linspace(0,10,5)
print(array2)

#changing sshape of array
array3 = orray.reshape(10,2)
print(array3)

#Change order
array4 = np.random.permutation(n)
print(array4)

#choosing random number
array5 = np.random.randint(0,101)
print(array5)

#random arrays (always between 0 and 1)
array5 = np.random.rand(2,3)
print(array5)

#inbuilt properties--------------------------------------------------------------------------------
#sorting array
array6 = np.sort(array4)
print(array6)

#accesing elements
array7 = np.arange(0,16).reshape(4,4)
print(array7)
print(array6[0]) #One dimensional
print(array7[1,3]) #Multidimensional

#Doing operations with arrays (arrays have to be same size and shape)
array8 = np.arange(20,36).reshape(4,4)
print(array8)
array9 = array7 + array8
print(array9)

#selects elements randomly from an array (array must be one dimensional)
print(np.random.choice(n,5))

#selects random numbers between low and high
print(np.random.uniform(2,21,6))
# playing w libraries
import math, statistics

MyList = [2,4,6,8,10,34]
a = sum(MyList)

print(a)
b = math.sqrt(a) #returns the square root of a number
print(b)

#Return the ceiling of x
#The smallest integer greater than or equal to x.
c = math.ceil(b)
#The largest integer not greater than x.
d = math.floor(b)
print(c,d)

print(math.ceil(-23.11))
print(math.ceil(300.34))
print(math.floor(305.34))
print(math.floor(-12.65))

e = statistics.mean(MyList)
print(e)

# Numpy
# Python program for creation of Arrays
import numpy as np

# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n", arr)

# Creating a rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)

# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)
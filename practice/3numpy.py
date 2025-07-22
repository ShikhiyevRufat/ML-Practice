"""
EXERCISE 1
"""

import numpy as np

# a = np.array([1,2,3])
# print(a)
# print("*"*100)
# b = np.array([[1,2,3], [4,5,6]])
# print(b)
# print("*"*100)
# c = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
# print(c)
# print("*"*100)
# d = np.zeros([3,3], dtype='int')
# print(d)
# print("*"*100)
# e = np.ones([3,3], dtype='int')
# print(e)
# print("*"*100)
# f = np.random.rand(4,4)
# print(f)
# print("*"*100)
# h = np.eye(4,4,-1)
# print(h)
# print("*"*100)
# x = np.arange(1,10)
# print(x)
# print("*"*100)
# j = np.linspace(5,20,9,dtype='int')
# i = j.reshape([3,3])
# print(i)
# print("*"*100)
"""
EXERCISE 2
"""

# arr = np.arange(5,20)
# arr = arr.reshape([5,3])
# print(arr)
# print("*"*100)

"""
EXERCISE 3
"""

# arr1 = np.array([10, 20, 30, 40, 50])
# arr2 = np.array([2, 4, 6, 8, 10])

# print(arr1+arr2)
# print("*"*100)
# print(arr1-arr2)
# print("*"*100)
# print(arr1*arr2)
# print("*"*100)
# print(arr1/arr2)
# print("*"*100)
# print(arr1**2)
# print("*"*100)
# print(np.sqrt(arr1))
# print("*"*100)
# print(np.mean(arr1))
# print("*"*100)
# print(np.max(arr1))
# print("*"*100)
# print(np.min(arr1))
# print("*"*100)

"""
EXERCISE 4
"""

# arr = np.random.randint(10,50,10)
# print(arr)
# print("*"*100)
# arr = arr[arr>20]
# print(arr)
# print("*"*100)
# arr = arr[arr%2 == 0]
# print(arr)
# print("*"*100)

"""
EXERCISE 5
"""

# matrix = np.random.randint(1,10, (3,3))
# print(matrix)
# print("*"*100)
# transpose_matrix = matrix.T
# print(transpose_matrix)
# print("*"*100)
# determinant_matrix = np.linalg.det(matrix)
# print(determinant_matrix)
# print("*"*100)


"""
1. Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. 
Replace all the elements in the third column with 1.
2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal 
elements with 0.
"""

# arr = np.random.randint(1,20, size= (5,5))
# arr[:, 2] = 1
# print(arr)


# arr = np.arange(1,17).reshape(4,4)
# np.fill_diagonal(arr, 0)
# print(arr)

"""
1. Create a NumPy array of shape (6, 6) with values from 1 to 36. 
Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.
2. Create a NumPy array of shape (5, 5) with random integers. 
Extract the elements on the border.
"""

# arr = np.arange(1, 37).reshape(6,6)
# sub_arr = arr[2:5, 1:4]
# print(sub_arr)

"""
1. Create two NumPy arrays of shape (3, 4) filled with random integers. 
Perform element-wise addition, subtraction, multiplication, and division.
2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Compute the row-wise 
and column-wise sum.
"""

# array1 = np.random.randint(1, 11, size=(3, 4))
# array2 = np.random.randint(1, 11, size=(3, 4))
# print(array1)
# print(array2)
# multiply = np.multiply(array1, array2)
# print(multiply)

# array1 = np.random.randint(1, 11, size=(3, 4))
# array2 = np.random.randint(1, 11, size=(3, 4))
# print(array1)
# print(array2)
# divide = np.divide(array1, array2)
# print(divide)

# array = np.arange(1, 17).reshape((4, 4))
# print("Original array:")
# print(array)
# row_sum = np.sum(array, axis=1)
# column_sum = np.sum(array, axis=0)
# print("Row-wise sum:")
# print(row_sum)
# print("Column-wise sum:")
# print(column_sum)

"""
Create a NumPy array of shape (5, 5) filled with random integers. Compute the mean, 
median, standard deviation, and variance of the array.
2. Create a NumPy array of shape (3, 3) with values from 1 to 9.
Normalize the array (i.e., scale the values to have a mean of 0 and a standard deviation 
of 1).
"""

# arr = np.random.randint(1, 20, size = (5,5)).mean()
# print(arr)

# arr = np.random.randint(1, 20, size = (5,5)).std()
# print(arr)

# arr = np.random.randint(1, 20, size = (5,5)).var()
# print(arr)

# arr = np.random.randint(1, 20, size = (5,5))
# median = np.median(arr)
# print(median)

# array = np.arange(1, 10).reshape((3, 3))
# print("Original array:")
# print(array)
# mean = np.mean(array)
# std_dev = np.std(array)
# normalized_array = (array - mean) / std_dev
# print("Normalized array:")
# print(normalized_array)
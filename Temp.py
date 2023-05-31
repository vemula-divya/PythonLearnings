from numpy import *

arr1 = array([[1, 2, 3, 9, 8, 5], [4, 5, 6, 7, 12, 99]])
print(arr1)
print(arr1.dtype)  # to find data type
print(arr1.ndim)  # to find dimension of matrix
print(arr1.shape)  # no.of rows and columns (2,3)
print(arr1.size)  # size of entire block 3+3=6

arr2 = arr1.flatten()  # to convert 2d array to 1d array
print(arr2)

# 1d to 3d dim
arr3 = arr2.reshape(3, 4)  # rows,colu
print(arr3)

arr4 = arr2.reshape(2, 2, 3)  # 3d array-to 2- 2d arrys with 3 values(2d,2 single dime,3 values)
print(arr4)

# Matrices

n = array([[1, 2, 3, 4], [5, 6, 7, 8]])
m = matrix(n)  # similar to array but we can perform many operations &
print('matrix', m)
#or
m1=matrix('1 2  3 ;  4  5 6 ; 7 8 9')
print(m)
print(diagonal(m)) # to find siagonal
print(m.min())
print(m.max())
m2=matrix('1 2  3 ;  4  5 6 ; 7 8 9')
print(m1*m2)




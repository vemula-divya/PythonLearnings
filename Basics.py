#if loop
x = 6
if x == 1:
    print(1)
elif x == 2:
    print(2)
else:
    print('other')

# while loop-1
counter = 0
while counter < 10:
    print(counter)
    counter += 1

# while loop-2
i = 1
while i <= 5:
    print("Hello ", end="")
    j = 1
    while j <= 4:
        print("Divya ", end="")
        j += 1
    i += 1
    print()


# example 1 :print 1 to 100 and skip which are divisible by 3 and 5
i = 1
while i <= 100:
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    i += 1

# example 2: pattern
i = 1
while i <= 4:
    print('# ', end="")
    j = 1
    while j <= 4:
        print('# ', end="")
        j = j+1
    print()
    i = i+1


#example1
my = {"1": 3, "2": 2, "3": 5}
items = my.items()  # items()- will make list of tuples
r = sorted(items, key=lambda x: x[1])  # sorts based on 1 index
print(r)

#example2
for x in range(20, 23, 24):
    print(x)

#example3
L=['a','b','c','d']
r='-'.join(L)
print(r)


#example4
my=(1,2,3,4,5)
r=my[1:4:2]
print(r)

#example5
def func(x,y,z=5):
    print(x,y,z)

func(1,z=2,y=8)



# array
from array import *

# in list we can add multiple types of data but in array we need to specify the datatype with typecode
vals = array('i', [5, 4, 0, 6, 7])  # i will accept both positive and negative
print(vals)
print(vals.buffer_info())  # add,size
print(vals[0])
print(vals.reverse())
for e in vals:
    print(e)
newarr = array(vals.typecode, (a * a for a in vals))
print(newarr)

# from user we will take input for array
arr = array('i', [])
n = int(input('enter the len of array'))
for i in range(n):
    x = int(input('enter the next value'))
    arr.append(x)

print(arr)

val = int(input('enter the value for search'))
k = 0
for e in arr:
    if e == val:
        # print(k)
        print(arr.index(e))
        break
    k += 1


from numpy import *

# different ways of creating an array
# array() -from -numpy
# linspace() -from -numpy
# logspace()
# arange()
# zeros()
# ones()

# arr=array([1,2,3,4.8,5],int)
arr = array([1, 2, 3, 4.8, 5])
print(arr.dtype)  # provides the type of array if it contains 7.8 it will be float
print(arr)

# linspace(start,stop,step)
# arr=linspace(0,16) #it will be divided into 16 parts
arr = linspace(0, 16, 17)  # 16 inclusive
print(arr)

# arange
arr = arange(1, 15, 2)  # first el,2nd el,steps)
print(arr)

# logspace()
arr = logspace(1, 40, 5)  # space bewtween will depend on log
print('%.2f ' % arr[0])

#zeros() ones()
arr=zeros(5) #array size 5
arr=zeros(5,int) #array size 5
print(arr)

arr=ones(5) #array size 5
arr=ones(5,int) #array size 5
print(arr)

from numpy import *

# copy an array in python
arr1 = array([10, 2, 3, 4, 5])
print('arr1+5 :', arr1 + 5)
arr2 = array([5, 6, 7, 8, 9])
print('sum of arr1+arr2 :', arr1 + arr2)
print('sin of arr1 :', sin(arr1))  # sin value or similarly cos
print('sqrt of arr1 :', sqrt(arr1))
print('sum of arr2 :', sum(arr2))
print('min of arr1 :', min(arr1))
print('max of arr1 :', max(arr1))
print('sort of arr1 :', sort(arr1))
print('conc of arr1 +arr2:', sort(concatenate([arr1,arr2])))
arr3=arr2
print(arr2,id(arr2))
print(arr3,id(arr3))
arr4=arr2.view() # it will create new array --shallow copy
print('rev of arr2 :', copy(arr2)) #for deep clone
arr2[1]=7
print(arr4,id(arr4))
print(arr2,id(arr2))
arr6=copy(arr2)
arr2[0]=88
print(arr2,id(arr2))
print(arr6,id(arr6))


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









# function:is a helper define once call multiple times
# defining a function & calling a function
import sys
from sys import setrecursionlimit
from functools import reduce


def greet():  # def a function
    print('hello in function')


def add(x, y):
    return x + y


# to return multiple values
def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


greet()  # calling a fun explicitly
print(add(3, 4))
print(add_sub(3, 4))


# Functions Arguments in python


# pass by value:If the object is immutable (e.g., numbers, strings, tuples), you cannot modify its value within the
# function. Any changes made to the parameter will not affect the original object outside the function.

# pass by reference:If the object is mutable (e.g., lists, dictionaries), you can modify its contents within the
# function. Any modifications made to the parameter will be reflected in the original object outside the function.
def update(x):
    x = 3
    print(x)


a = 10
update(a)
print(a)  # it will not chane bcs of pass by value;they will share same reference


##################
def update(x):
    x.append(7)


list1 = [4, 8, 9]
update(list1)
print(list1)  # it will  change bcs of pass by reference


#####
# types of arguments(position,keyword,default,variable length)
def add(x, y):  # x,y are formal argunents
    c = x + y
    print(c)


add(4, 5)  # 4,5 are argument/actual arguments


def person(name, age):
    print(name, 'name')
    print(age, 'age')


person('divya', 20)  # we need to maintain seq /position while entering arguments
person(name='divya', age=20)  # keyword


# person(name='divya')  # default make fun person(name,age=18)


# variable length

def sum(a, *b):  # *b variable length
    c = a
    for i in b:
        c = c + i
    print(c)


sum(6, 4, 7, 9)


# keyword variable length arg(multiple variable data with keyword)
def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)


person('divya', age=22, city='mumbai', phone='89898989')

# global keyword variable
a = 10  # global variable
print(a)


def smtg():
    a = 22  # local variable if we comment it will get global
    # x = globals()['a']  # globals return all the val og global
    globals()['a'] = 9
    print(a)


smtg()
print(a)


# pass list to a function

def even_odd(list1):
    e = 0
    o = 0
    for i in list1:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    return e, o


even, odd = even_odd([1, 2, 3, 4, 5, 6])
print('even:{} and odd: {}'.format(even, odd))


# fibonacci sequence
def fib(x):
    a = 0
    b = 1
    if x == 1:
        print(a)
    else:
        print(a, end=" ")
        print(b, end=" ")
    for i in range(2, x):
        s = a + b
        print(s, end=" ")
        a = b
        b = s


fib(10)
print()


#
def fib(x):
    a = 0
    b = 1
    if x == 1:
        print(a)
    else:
        print(a, end=" ")
        print(b, end=" ")

    for i in range(2, x):
        s = a + b
        if s > x:
            break;
        print(s, end=" ")
        a = b
        b = s


fib(100)
print()


# factorial of a number
def fact(n):
    m = 1
    for i in range(2, n + 1):
        m = i * m
    print(m)


fact(5)

# recursion:
print(sys.getrecursionlimit())  # by default 1000
sys, setrecursionlimit(2000)  # we can set manually


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


r = fact(5)
print(r)

# anonymous functions(lambda)
f1 = lambda a: a * a
print(f1(6))

# filter-map reduce
nums = [8, 9, 7, 6, 4, 3, 2]
evens = list(filter(lambda n: n % 2 == 0, nums))
# every value is mapped
doubles = list(map(lambda n: n + 2, evens))
# reduce
sum1 = reduce(lambda x, y: x + y, doubles)
print(evens)
print(doubles)
print(sum1)

# decorators(change the behaviour of existing function
def div(a,b):
    print(a/b)

div(2,4) # 0.5 but if i need to change the logic of div but it is  present in other system we can use the concept
# called decorator

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div1=smart_div(div)
div1(2,4)




# swap 2 numbers
# def swap(a,b):
#     c=a
#     a=b
#     b=c
#     return a,b
# a,b=swap(3,4)
# print(a,b)
#or
def swap(a,b):
    a,b = b,a
    return a,b

a,b=swap(3,4)
print(a,b)



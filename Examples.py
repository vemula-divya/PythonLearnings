## while loop
# example 1 :print 1 to 100 and skip which are divisible by 3 and 5
i = 1
while i <= 100:
    if i % 3 != 0 and i % 5 != 0:
        print(i, end=",")
    i += 1
print()


## for  loop
x = {'div', 33, 5.5}
x1 = 'divya'

for i in x1:
    print(i, end=" ")
print()

for i in [4, 45, 55]:
    print(i, end=" ")
print()

for i in range(11, 27):
    print(i, end=" ")
print()

for i in range(20, 10, -1):  # for reverse
    print(i, end=" ")
print()

# to find perfect sqrt from 1 to 100
import math

for num in range(1, 101):
    square_root = math.sqrt(num)
    if square_root.is_integer():
        print(num, "is a perfect square.")

# Break
av = 10
x = int(input('How many Candies u want?'))

i = 1
while i <= x:
    if i > av:
        print('out of stock')
        break
    print('candy')
    i += 1
# continue statement: When the continue statement is encountered within a loop (such as for or while), it immediately jumps to the next iteration of the loop, skipping the remaining code inside the loop for the current iteration. It allows you to bypass certain iterations based on a specific condition.
# pass statement: The pass statement is a null operation, meaning it does nothing. It is used as a placeholder when a statement is syntactically required but you don't want to perform any action. It is commonly used as a placeholder in empty function or class definitions, allowing you to define the structure without adding any functionality.
#
# continue
for i in range(1, 101):
    if i % 3 == 0 or i%5==0:
        continue
    print(i)
#pass
for i in range(1, 101):
    if (i % 2 != 0) :
        pass
    else:
        print(i)
# pattern problems
# example 1: pattern
i = 1
while i <= 4:
    print('# ', end="")
    j = 1
    while j <= 4:
        print('# ', end="")
        j = j + 1
    print()
    i = i + 1
# or
for i in range(4):
    for j in range(4):
        print('*', end=" ")
    print()

# example 2: pattern
for i in range(4):
    for j in range(i + 1):
        print('*', end=" ")
    print()
# example 3: pattern

for i in range(4):
    for j in range(4 - i):
        print('*', end=" ")
    print()
# example 4: pattern
for i in range(4):
    for j in range(4 - i):
        print(j+i+1, end=" ")
    print()
# example 5: pattern
rows = 4
for i in range(4):
    char = ord('A')
    for j in range(i+1):
        print(chr(char), end=" ")
        char += 1
    for k in range(i+1, rows):
        print(chr(ord('A')+k), end=" ")
    print()
#prime or not
import math

n = int(input('Enter any number: '))

if n < 2:
    print('Not prime')
elif n == 2:
    print('Prime')
else:
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            print('Not prime')
            break
    else:
        print('Prime')


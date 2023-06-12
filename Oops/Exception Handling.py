# compile time error--syntax error like : missing
# logical error -- wrong output
# runtime--6/0; for particular input
a=5
b=2
print(a/b)
# a is normal stmt ,b is critical stmt
b=0
try:
    print('resource open')
    print(a/b)
    print('resource closed')  # if we get error in stmt  it will not print to avoid this we can use finally

except Exception as e:
    print('hey,u cannot divide a number by 0 :',e)
finally:
    print('resource closed')

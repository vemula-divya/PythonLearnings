class Car:
    wheels=4
    def __init__(self):
        self.mil = 10
        self.com = 'BMW'


# mil and com are called as instance variable because as the car /object changes the value changes
c1 = Car()
c2 = Car()
c1.mil=15  # it will change only for the c1 obj not the c2 .if we want to change for both the obj use static/class variable
print(c1.com,c1.mil,Car.wheels)
print(c2.com,c2.mil,Car.wheels)
# we can use both classname.var or obj.var

# NameSpace:namespcae is an area where you create and store object/variable
# classNamespace
# object/instance name space
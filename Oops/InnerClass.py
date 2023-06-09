class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = '12'
            self.ram = 6
        def show(self):
            print(self.cpu, self.brand,self.ram)


s1 = Student('divya', 2)
s1.show()
var = s1.lap.brand
print(var)

lap1=Student.Laptop()
print
# we can create object of inner class inside the outer class or
# we can create object of inner class outside the outer class provided u use outer class name to call it

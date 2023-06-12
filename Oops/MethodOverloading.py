class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


s1 = Student(6, 7)
# 3 methods are called method overloading in single method
# which is not direct as java but with none trick we can achieve .we can pass 1,2 or 3 arg.
print(s1.sum(8, 9, 7))
print(s1.sum(8, 9))
print(s1.sum(7))

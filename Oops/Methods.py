# 3 types: Instance,Class,Static Methods
class Student:
    school = 'Delhi-Public'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return self.m1 + self.m2 + self.m3

    @classmethod
    def getSchool(cls):
        return cls.school

    def get_m1(self):
        return self.m1

    def set_m1(self, val):
        self.m1 = val

    @staticmethod
    def info():
        print('this is student class...')


s1 = Student(1, 2, 3)
s2 = Student(4, 5, 6)

print(s1.avg())
print(s2.avg())
print(s1.m1, s1.m2, s1.m3, Student.school,Student.getSchool())
Student.info()
# Accessor Methods:getters(for fetching)
# Mutator Methods:setters(for modifying)
# if we work with instance var  we need to use self
# if we work with   class variable we need to use cls
# @classmethod:to create class method decorators
# if we are not consider about either class or instance method
# self --for instance var,cls-class and for static -empty
#  static methods @staticmethod
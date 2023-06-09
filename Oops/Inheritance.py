# parent-child relationship
class A:
    def feature1(self):
        print('feature1 working')

    def feature2(self):
        print('feature2 working')

# B is child class of A

class B(A):
    def feature3(self):
        print('feature3 working')

    def feature4(self):
        print('feature4 working')

class C(B):
    def feature5(self):
        print('feature5 working')


a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature3()
b1.feature4()
b1.feature1()
b1.feature2()

c1=C()
c1.feature1()

#super class -a and sub class -b
#single level inheritance
#multi level inhertance from c we can get methods of a as well
#multiple inheritance for ex a and b are two diff class and d wants all the features from a and b
class D(A,B):
    def feat11(self):
        print('multiple')

d1=D()
d1.feat11() #we cant all the features from a and b as well

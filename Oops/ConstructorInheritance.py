# parent-child relationship
class A:
    def __init__(self):
        print('a constructor')

    def feature1(self):
        print('feature1 working')

    def feature2(self):
        print('feature2 working')


# B is child class of A

class B(A):
    def feature3(self):
        print('feature3 working')

    def __init__(self):
        # super().__init__()
        print('b constructor')

    def feature4(self):
        print('feature4 working')


class C(A, B):
    def __init__(self):
        super().__init__()  # Call A's constructor
        super(B, self).__init__()  # Call B's constructor
        print('c init')


c1 = C()
a1 = A()  # A()-constructor init will be called

b1 = B()  # if b __init__ is not present a constructor will be called else b
# if we to call a constructor from b we candd super().__init__
# mro-C(A,B) from left to right it will execute for constructor-

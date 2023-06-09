class Computer:
    def __init__(self):
        self.name='divya'
        self.age=20

    def compare(self, c2):
        if self.age ==c2.age:
            return True
        else:
            return False


c1 =Computer()
c2=Computer()

c1.name='nnn' #changing name
print(c1.name)

if c1.compare(c2):
    print('same')
else:
    print('diff')


#
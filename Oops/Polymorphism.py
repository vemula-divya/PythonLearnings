# many forms:one thing can take multiple forms
# Duck Typing()
x = 5
x = 'div'


# x(var) is just name to it we are not adding type
class PyCharm:
    def execute(self):
        print('compile')
        print('running')

class Editor:
    def execute(self):
        print('compile')
        print('running')
        print('con check')


class Laptop:
    def code(self, ide):
        ide.execute()


ide =Editor()
lap1 = Laptop()
lap1.code(ide)
#can we change pycharm to some eclipse
#yes,it will only check for execute method
# As long as they have the required attributes and methods, they can be treated as same.

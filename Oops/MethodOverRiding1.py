class A:
   def show(self):
       print('in a show')

class B(A):
    def show(self):
        print('in b show')


a1=B()
# class B(A):
#   pass
a1.show() # as b don't have show method but we are extending a it prints A show
a1.show() #o/p in b show as we are overriding show method
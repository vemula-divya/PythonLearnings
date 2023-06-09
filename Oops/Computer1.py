class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('config', self.cpu, self.ram)


# com1 = Computer()
# Computer.config(com1) #com1 is argument
# or
# com1 = Computer()
# com1.config()
# or
#Computer().config()  # will call init method

com1 = Computer('i5',16)
com1.config()


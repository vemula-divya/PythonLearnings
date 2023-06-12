# ex for  loop to stop for loop we need to write exception
# to iterate list we need iterator
nums = [9, 7, 6]
# for i in nums:
#     print(i)

# using iterator
it = iter(nums)
# print(it.__next__()) #it gives first value
# print(it.__next__())  #it gives second value
# print(next(it)) # similar to previous ,it gives second value

'''example'''


class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = TopTen()
for i in values:
    print(i)

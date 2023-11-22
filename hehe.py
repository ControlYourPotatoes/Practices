#!/usr/bin/python3

class Hehe():
    def __init__(self, num):
        self.num = num

    def sum_each(self):
        current = self.num

        while isinstance(current, int):
            mul = (current * 2) + (previous * 2)
            sub = (current - 2) + (previous - 2)
            sum = (current + 2) + (previous + 2)
            pow2 = (current * current) + (previous )
            previous = current
            current = None

        print(mul)
        print(sub)
        print(sum)
        print(pow2)

my_Hehe1 = Hehe(2)
my_Hehe2 = Hehe(10)
my_Hehe3 = Hehe(15)
my_Hehe3.sum_each()


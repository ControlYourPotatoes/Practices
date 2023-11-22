#!/usr/bin/env python3


# Applying FizzBuzz logic to list of touples that has lists inside, add up all the values on each list in the touple
# then multiple the two results together and apply FizzBuzz logic to the result

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
list4 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
list5 = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
list6 = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

touplelist = [(list1, list2), (list3, list4), (list5, list6)]

def touplefizzbuzz():
    for tup in touplelist:
        sum1 = sum(tup[0])
        sum2 = sum(tup[1])
        result = sum1 * sum2

        if result % 3 == 0 and result % 5 == 0:
            print("FizzBuzz")
        elif result % 3 == 0:
            print("Fizz")
        elif result % 5 == 0:
            print("Buzz")
        else:
            print(result)

touplefizzbuzz()

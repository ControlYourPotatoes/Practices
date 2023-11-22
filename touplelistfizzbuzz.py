#!/usr/bin/env python3

#list of touples
list1 = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
list2 = [(11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]
list3 = [(21, 22), (23, 24), (25, 26), (27, 28), (29, 30)]

def touplefizzbuzz():
        # Iterate over each tuple in the current list
        for i in range(len(list1)):
            # Summing the values in the tuple
            total = sum(list1[i]) + sum(list2[i]) + sum(list3[i])
            
            print("The sum of the values in the tuple is:", total)
            # Applying FizzBuzz logic
            if total % 3 == 0 and total % 5 == 0:
                print("FizzBuzz")
            elif total % 3 == 0:
                print("Fizz")
            elif total % 5 == 0:
                print("Buzz")
            else:
                print(total)

print(touplefizzbuzz())


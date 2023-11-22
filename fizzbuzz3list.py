
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def fizzbuzz():
    
    for i in range(len(list1)):

        total = list1[i] + list2[i] + list3[i]

        if total % 3 == 0 and i % 5 == 0:
            print ("fizzbuzz")
        elif total % 3 == 0:
            print ("fizz")
        elif total % 5 == 0:
            print ("buzz")    
        else:
            print (total)

print (fizzbuzz())
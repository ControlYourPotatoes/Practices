#Print fizzbuzz

def fizzbuzzbyn(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")    
        else:
            result.append(i)
    return result

print(fizzbuzzbyn(20))

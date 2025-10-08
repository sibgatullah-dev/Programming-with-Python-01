def sum(number):    
    if number <= 0:
        return 0
    return number + sum(number-1)

number = int(input())
result = sum(number)
print(result)
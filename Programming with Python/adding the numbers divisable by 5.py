result = 0
for i in range(101):
    if i % 5 == 0:
        result += i
        
print(result)


result = 0
for num in range(5 , 101 , 5):
    result += num
print(result)
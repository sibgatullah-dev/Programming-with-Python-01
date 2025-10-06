result = 0
num = 1 
for i in range(50):
    result = result+num
    num += 1
    
print(result)

print('\t')

result = 0
for num in range(51): # num starting from 0 so the range is 51
    result += num
    
print(result)

print('\t')

result = 0
for num in range(1,51): #range(start , end)
    result += num
    
print(result)

def add(a,b): # taking input in parameter
    return a+b # returning the result

x = int(input("Enter the first number: ")) # input function always takes string input that's why the datatype needs to be changed to int
y = int(input("Enter the second number: "))

result = add(x,y) # sending argument
print(result)
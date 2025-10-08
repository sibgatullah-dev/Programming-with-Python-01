def times(n): # the factory/function that creates toys/child-functions which will multiply your given number with x
    return lambda x : x*n

double = times(2) # requesting the factory to create a toy which can multiply by 2

result = double(int(input("enter the number you wanna multiply: ")))
print(result) # printing the result of my toy 
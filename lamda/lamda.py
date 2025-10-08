# variable = lambda parameter: expressions (can be used without the variable or any kind of name)
# lambda is a oneline anonymous function which actually doesn't need a name 
add = lambda x: x+1
result = add(1)
print(result)

# lambda functions ca take any number of parameters and return any valid python expression
add2 = lambda x,y: x+y
result2 = add2(4,6)
print(result2)
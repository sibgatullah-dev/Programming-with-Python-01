# map function takes some list/iterable object and apply a function to every single value inside of it
my_numbers = [1,2,3,4,5,6,7,8,9,10]

squares = list(map(lambda x:x**2,my_numbers))
print(squares)

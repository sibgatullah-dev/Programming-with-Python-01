# filter function apply function to every single value inside of a list/iterable object
''' if it returns true then filter function will keep the value 
    if it returns false then filter function will reject the value '''
my_numbers = [1,2,3,4,5,6,7,8,9,10]

evens = list(filter(lambda x:x%2==0,my_numbers))
print(evens)
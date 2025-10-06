''' like list set is in between curly braces . there can be only one unic element for every elements in a set.
set doesn't follow any order or it doesn't come sorted '''

# Empty set
a = set()
print(type(a))

# filled set
b = {'pen','laptop','phone'}
print(type(b))

# we can also create a set from a list or a tuple
li = [1,2,3]
tup = (4,5,6)
a = set(li)
b = set(tup)
print(a)
print(b)

# we can also create a set form a string
str = "bangladesh"
x = set(str)
print(x)
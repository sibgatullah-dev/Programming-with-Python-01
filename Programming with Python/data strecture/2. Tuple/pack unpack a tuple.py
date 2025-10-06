''' we can pack multiple variable in a tuple or unpack a tuple and keep the elements in different variable '''
# Packing values into a tuple
numbers = (10,20,30,40,50)

# unpacking a tupple in different variable
n1,n2,n3,n4,n5 = numbers
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

# Packing n3 and n4 into a new tuple
t = n3,n4
print(t)
print(type(t))
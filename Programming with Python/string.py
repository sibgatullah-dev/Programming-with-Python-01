# string is one sort of list
string = " Bangladesh "
txt = string.strip()
print(string)
print(txt)
for c in string:
    print(c)

''' The only difference between list and string is that we can change a value of list but 
we can not change a value of a string '''
# use strip() method if need to remove all the space of both sides of the string
# use lstrip() method if need to remove the space on the left side
# use rstrip() method if need to remove the space on the right side
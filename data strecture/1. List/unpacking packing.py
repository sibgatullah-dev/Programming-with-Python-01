'''If you want to unpack the first few elements of a list and don’t care about the other elements, you can:

    1. First, unpack the needed elements to variables.
    2. Second, pack the leftover elements into a new list and assign it to another variable.'''

colors = ['red', 'blue', 'green','orange','yellow','teal']
r,b,g,*others = colors #putting the asterisk (*) in front of a variable name, it'll pack the leftover elements into a list and assign them to a variable.
print(r)
print(g)
print(b)
print(others)
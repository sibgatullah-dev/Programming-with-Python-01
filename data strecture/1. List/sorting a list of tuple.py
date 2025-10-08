# we will sort the list according to the sort key 
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

companies.sort(key=lambda s:s[2],reverse=True)
print(companies)

''' .sort() is a list method that sorts the list in place (modifies the original list) and returns None.

sorted() is a built-in function that creates and returns a new sorted list from any iterable (does not modify the original).'''
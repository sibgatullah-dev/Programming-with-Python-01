# using the lambda function as a key for sorting . 
values = [(1,'b',"hello"),(2,'a',"world"),(3,'c',"ok")]

sorted_values = list(sorted(values, key=lambda x:x[1]))# every single values will be sorted according to the index 1 of the tuples
print(sorted_values)

# But what if we had a tie in the values of the tuples of the list ?
values2 = [(1,'b',"hello"),(2,'a',"world"),(3,'c',"ok"),(4,'b',"zoo"),(5,'b',"joo")]

sorted_values2 = list(sorted(values2,key=lambda x:x[1]+x[2]))# then we can sort those tie items according to a second key
print(sorted_values2)

''' .sort() is a list method that sorts the list in place (modifies the original list) and returns None.

sorted() is a built-in function that creates and returns a new sorted list from any iterable (does not modify the original).'''
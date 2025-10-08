fruits = ['apple','mango','coconut','banana','orange']
item = input('Enter the fruit to removed: ')

if item in fruits:
    fruits.remove(item)
    print(fruits)
else:
    print(item,"not in list")
    

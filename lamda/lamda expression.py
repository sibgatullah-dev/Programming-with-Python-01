# Python lamda expression allows us to define any anonymous function
# Anonymous functions are functions without name 
''' lambda parameters: expressions

    def anonymous(parameters):
        return expressions '''

def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


full_name = get_full_name('John','Doe',lambda first_name, last_name: f"{first_name} {last_name}")
print(full_name)

full_name = get_full_name(
    'John',
    'Doe',
    lambda first_name, last_name: f"{last_name}, {first_name}"
)
print(full_name)
''' Think of it as get_full_name is a machine 
and it creates some toys like full_name which keeps a lambda function .
here the formatter is like a box which holds the toy function's request in the parant function 
and the full_name variable of the lambda function is the final toy it's self '''
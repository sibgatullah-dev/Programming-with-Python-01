''' In dictionary data keeps in pair. First part of the pari is key and second part of the pair is value '''
# Empty dictionary
empty = {}
print(type(empty))

# dictionary
marks = {
    1: 77,
    2: 75,
    3: 70,
    4: 69,
    5: 66
}
print(type(marks))

roll = int(input("enter your roll: "))
print("Your mark is: ",marks[roll])


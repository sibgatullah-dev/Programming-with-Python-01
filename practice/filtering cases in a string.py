string = input("enter a string")
str1 = ""
str2 = ""
str3 = ""
str4 = ""

for c in string:
    if c.isupper():
        str1 += c
    elif c.islower():
        str2 += c
    elif c.isdigit():
        str3 += c
    else:
        str4 += c

print(str1)
print(str2)
print(str3)
print(str4)
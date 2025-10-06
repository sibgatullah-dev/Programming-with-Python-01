string = input("enter: ")
txt = ""

n = 0
m = n+1

i = 0
while i <len(string):
    if i+1<len(string):
        txt += string[i+1]+string[i]
    else:
        txt += string[i]
    i+=2
    
print(txt)
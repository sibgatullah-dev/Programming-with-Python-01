string1 = input("Enter: ")
string2 = ""
# len(string1)-1 means the starting will be form the end of the string 
for c in range(len(string1)-1,-1,-1):# the loop stops before reaching -1 so it includes index 0
    string2 += string1[c]

if string1 == string2:
    print("Palindrome")
else:
    print("NOT Palindrome")
    
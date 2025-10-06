while True:
    num = int(input("Enter your positive number: "))
    if num < 0:
        print("Please enter a postive number.")
        continue
    if num == 0:
        print("exiting")
        break
    print("Square of", num , "is" , num*num)
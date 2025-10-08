import random

number = random.randint(1,100)
attempts = 0

while True:
    num = int(input("Guess the number: "))
    attempts += 1
    if number == num:
        print("You guessed it correct !")
        break
    elif number > num:
        print("Try guessing a bigger number")
    else:
        print('Try guessing a smaller number')
print("Your tried",attempts,'times to find the number')
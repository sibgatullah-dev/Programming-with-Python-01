import random

number = random.randint(1,100)
attempts = 0
low = 1
high = 100

while True:
    print("Guess the number (between 1 and 100): ")
    guess = (low + high) // 2 # // gives you only integer answer
    print("my guess is",guess)
    attempts += 1
    
    if guess == number:
        print("You guessed it correct !")
        break
    elif guess > number:
        print("Try guessing a smaller number")
        high = guess - 1
    else:
        print('Try guessing a bigger number')
        low = guess + 1
        
print("Your tried",attempts,'times to find the number')
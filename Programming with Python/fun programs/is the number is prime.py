import math

def is_prime(number): # foolish way 
    if number < 2:
        return False
    prime = True
    for i in range(2,number):
        if number % i == 0:
            print(number, " is divisable by ", i)
            prime = False
            return prime         
    return prime

def is_prime2(number): # removing the even numbers from the loop
    if number == 2:
        return True
    if number % 2 == 0:
        print(number,'is divisible by 2')
        return False
    if number < 2:
        return False
    prime = True
    for i in range(3,number,2):
        if number % i == 0:
            print(number, " is divisable by ", i)
            prime = False
            return prime         
    return prime

def is_prime3(number): # using root number of the input for maximum efficiency
    if number == 2:
        return True
    if number % 2 == 0:
        print(number,'is divisible by 2')
        return False
    if number < 2:
        return False
    prime = True
    
    m = math.sqrt(number)
    m = int(m)+1
    for i in range(3,number,2):
        if number % i == 0:
            print(number, " is divisable by ", i)
            prime = False
            return prime         
    return prime

while True:
    number = int(input("Enter your number (enter 0 to exit): "))
    prime = is_prime3(number)
    if number == 0:
        break
    if prime:
        print(number,"is a prime number")
    else:
        print(number,'is not a prime number')
        
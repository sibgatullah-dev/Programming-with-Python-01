import math

def is_prime2(number=1013): # removing the even numbers from the loop
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

def is_prime3(number=1013): # using root number of the input for maximum efficiency
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    if number < 2:
        return False
    
    m = math.sqrt(number)
    m = int(m)+1
    for i in range(3,m,2):
        if number % i == 0:
            return False         
    return True

import timeit
t1 = timeit.timeit(is_prime2)
t2 = timeit.timeit(is_prime3)

print('t1:',t1,' t2:',t2)
        
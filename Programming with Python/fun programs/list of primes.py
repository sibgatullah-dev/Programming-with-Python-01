import math
def is_prime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    root = int(math.sqrt(n))+1
    for i in range(3,root,2):
        if n%i==0:
            return False
    return True

primes = []
n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
for i in range(n1,n2+1):
    if is_prime(i):
        primes.append(i)
        
print(primes)
    
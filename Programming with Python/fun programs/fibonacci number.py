fib_x = 1
fib_next = 1

n = int(input())

fib_list = [fib_x,fib_next]
for i in range(2,n):
    fib_new = fib_x+fib_next
    fib_list.append(fib_new)
    fib_x = fib_next
    fib_next = fib_new
    
print(fib_list)
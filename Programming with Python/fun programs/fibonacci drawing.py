fib_x = 1
fib_next = 1

n = int(input())

fib_list = [fib_x,fib_next]
for i in range(2,n):
    fib_new = fib_x+fib_next
    fib_list.append(fib_new)
    fib_x = fib_next
    fib_next = fib_new
    
import turtle

for i in fib_list:
    r = i
    a = 180
    turtle.circle(r,a)

turtle.done()
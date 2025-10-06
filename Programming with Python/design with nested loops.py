import turtle
turtle.shape("turtle")
turtle.speed(8)
turtle.color("green")

counter = 0

while counter <= 36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(10)
    counter += 1

turtle.color("red")
counter = 0

while counter <= 36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(15)
    counter += 1
    
turtle.color("blue")
counter = 0

while counter <= 36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(20)
    counter += 1
    
turtle.exitonclick()
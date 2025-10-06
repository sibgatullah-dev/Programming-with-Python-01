import turtle

height = 5
width = 5

turtle.speed(1)

turtle.penup()
turtle.backward(10*width)
turtle.left(90)
turtle.forward(50)
turtle.right(90)


for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    
turtle.exitonclick()
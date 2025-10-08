import turtle
import random
turtle.speed(0)

# list of colors
colors = ['red','green','blue','yellow','orange','brown','purple','teal','pink']

turtle.penup()
for i in range(100):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    
    # set a random position
    turtle.setposition(x,y)
    # set a random color
    i = random.randint(0,len(colors)-1)
    
    turtle.dot(colors[i])
    
turtle.done()
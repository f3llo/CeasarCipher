import turtle
from math import *

#turtle.speed("fastest")
turtle.Screen().screensize(500,500)

'''
  /\
/    \
_   ___\
 |_|
'''

def drawTriangle(x, y, size):
    turtle.penup()
    turtle.color("green")
    turtle.goto(x,y)
    turtle.right(60)
    turtle.pendown()
    turtle.forward(size)
    turtle.goto(x,y)
    turtle.right(60)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    return (x,y-size/2/cos(pi/6))

size = 50
middle = (250,250)
for i in range(0,3):
    middle = drawTriangle(middle[0], middle[1],size)
    size*3

turtle.penup()
turtle.home()
turtle.goto(middle)
turtle.forward(size/4)
turtle.right(90)
turtle.forward(size/2)
turtle.pendown()
turtle.color("brown")
turtle.forward(size/3)
turtle.right(90)
turtle.forward(size/2)
turtle.right(90)
turtle.forward(size/3)

turtle.update()
turtle.done()

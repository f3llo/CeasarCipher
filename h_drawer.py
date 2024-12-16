import turtle

#set center to corner each time and size to half
turtle.speed("fastest")
turtle.tracer(0, 0)
turtle.Screen().screensize(1000, 1000)

def drawH(centre: [], size: int) -> []:
    print(centre)
    turtle.goto(centre[0]-size//2, centre[1])
    turtle.pendown()
    turtle.forward(size)
    turtle.penup()
    turtle.left(90)
    turtle.forward(size)
    turtle.right(180)
    turtle.pendown()
    turtle.forward(size * 2)
    turtle.penup()
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(size * 2)
    turtle.penup()
    turtle.home()

    children.append([centre[0]-size/2,centre[1]-size])
    children.append([centre[0]-size/2,centre[1]+size])
    children.append([centre[0]+size/2,centre[1]-size])
    children.append([centre[0]+size/2,centre[1]+size])

def iterateH(centre: [], size: int, iterations: int) -> None:

    global children

    children = [[0,0]] #stores points of all the places to draw H
    iteration = 1
    current_size = size
    counter = 0

    for i in range(iterations):
        current_children = children
        children = []
        for j in range(len(current_children)):
            drawH(current_children[j], current_size)
            print(current_children[j], counter)

        counter += len(current_children)
       
        iteration += 1
        current_size = current_size/2

    print(children)
    return None #recusion all the points

iterateH([0,0], 200, int(input("Enter iterations: ")))
turtle.update()
turtle.done()

import turtle

def initWindow(title = "Welcome to the turtle zoo!", bgColor = "white", delay = 10):
    # Initialises the window for drawing
    window = turtle.Screen()
    window.setup(width=600, height=500, startx=0, starty=0)
    window.title(title)
    window.bgcolor(bgColor)
    # Slow down the drawing speed
    window.delay(delay)
    return window

def initTurtle(shape = "turtle", strokeColor = "darkgreen"):
    # Initialises the turtle
    # Shape, size and strokeColor
    brad = turtle.Turtle()
    brad.shape(shape)
    brad.color(strokeColor)
    return brad

def moveTurtle(myTurtle, x = 0, y = 0):
    myTurtle.penup()
    myTurtle.setpos(x, y)
    myTurtle.pendown()

def draw_shape(myTurtle, shape = "line", length = 10, strokeColor = "blue", fillColor = ""):
    currentHeading = myTurtle.heading()
    myTurtle.color(strokeColor)
    if (fillColor):
        myTurtle.fillcolor(fillColor)
        myTurtle.fill(True)

    if shape == "square":
        for i in range(4):
            myTurtle.forward(length)
            myTurtle.right(90)
    elif shape == "circle":
        myTurtle.circle(length)
    elif shape == "triangle":
        # After 3 times back to the start point
        for i in range(3):
            myTurtle.left(120)
            myTurtle.forward(length)
    elif shape == "rhombus":
        for i in range(4):
            myTurtle.forward(length)
            myTurtle.right(60 + 60 * (i % 2))
    else:
        # draw a line as default
        myTurtle.forward(length)

    myTurtle.fill(False)
    myTurtle.setheading(currentHeading)

def draw_flower(myTurtle, shape, length = 10, petals = 36, strokeColor = "red"):
    myTurtle.speed("fastest")
    angle = 360 / (petals)
    for i in range(1, petals + 1):
        draw_shape(myTurtle, shape, length, strokeColor)
        myTurtle.right(angle)

    # Reset Turtle's heading to the south
    myTurtle.setheading(270)
    myTurtle.speed("slowest")
    myTurtle.forward(150)

def draw_pyradmin(myTurtle, shape, edge = 100, length = 5, strokeColor = "black", fillColor = "yellow"):
    preEdge = edge
    newEdge = edge / 2
    for i in range(1,4):
        if (newEdge <= length):
            newEdge = 2 * newEdge
            preEdge = 2 * preEdge
            break
        draw_shape(myTurtle, "triangle", newEdge)
        draw_pyradmin(myTurtle, "triangle", newEdge, length)
        myTurtle.left(120)
        myTurtle.forward(preEdge)

myWindow = initWindow()
myTurtle = initTurtle()
moveTurtle(myTurtle, -200, 0)
# A flower with 36 rhombuses
draw_flower(myTurtle, "rhombus", 30, 36, "red")

# A flower with 18 triangles
moveTurtle(myTurtle, -100, 0)
draw_flower(myTurtle, "triangle", 30, 18, "green")

# A flower with 72 squares
moveTurtle(myTurtle, 50, 0)
draw_flower(myTurtle, "square", 50, 72, "blue")

# A pyradmin
myTurtle.speed("fastest")
myTurtle.setheading(0)
moveTurtle(myTurtle, 250, -50)
draw_pyradmin(myTurtle, "triangle", 100, 5, "black", "yellow")

# Click the window to exit
myWindow.exitonclick()

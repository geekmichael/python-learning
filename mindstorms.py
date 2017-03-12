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

    myTurtle.color(strokeColor)

    if (fillColor):
        myTurtle.fill(True)
        myTurtle.fillcolor(fillColor)

    if shape == "square":
        for i in range(4):
            myTurtle.forward(length)
            myTurtle.right(90)
    elif shape == "circle":
        myTurtle.circle(length)
    elif shape == "triangle":
        for i in range(2):
            myTurtle.forward(length)
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

def draw_flower(myTurtle, shape, length = 10, strokeColor = "red"):
    myTurtle.speed("fastest")

    for i in range(1, 37):
        draw_shape(myTurtle, shape, length, strokeColor)
        myTurtle.right(10)

    # Reset Turtle's heading to the south
    myTurtle.setheading(270)
    myTurtle.speed("slowest")
    myTurtle.forward(150)

myWindow = initWindow()
myTurtle = initTurtle()
moveTurtle(myTurtle, -200, 0)
# draw_square(myTurtle, 100)
# draw_circle(myTurtle, 100)
# draw_triangle(myTurtle, 100)
# draw_square_art(myTurtle, 100)
draw_flower(myTurtle, "rhombus", 30, "red")
moveTurtle(myTurtle, -100, 0)
draw_flower(myTurtle, "triangle", 30, "green")
moveTurtle(myTurtle, 50, 0)
draw_flower(myTurtle, "square", 50, "blue")

# Click the window to exit
myWindow.exitonclick()

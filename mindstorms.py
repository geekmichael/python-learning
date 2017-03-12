import turtle

def initWindow(title = "Welcome to the turtle zoo!", bgcolor = "white", delay = 10):
    # Initialises the window for drawing
    window = turtle.Screen()
    window.setup(width=600, height=500, startx=0, starty=0)
    window.title(title)
    window.bgcolor(bgcolor)
    # Slow down the drawing speed
    window.delay(delay)
    return window

def initTurtle(shape = "turtle", color = "darkgreen"):
    # Initialises the turtle
    # Shape, size and color
    brad = turtle.Turtle()
    brad.shape(shape)
    brad.color(color)
    return brad

def moveTurtle(myTurtle, x = 0, y = 0):
    myTurtle.penup()
    myTurtle.setpos(x, y)
    myTurtle.pendown()

def draw_square(myTurtle, color = "green", length = 10):
    myTurtle.color(color)
    # Starts drawing the box
    i = 1
    for i in range(4):
        myTurtle.forward(length)
        myTurtle.right(90)

def draw_circle(myTurtle, color = "blue", radius = 100):
    myTurtle.color(color)
    myTurtle.circle(radius)

def draw_triangle(myTurtle, color = "red", length = 10):
    myTurtle.color(color)
    i = 1
    for i in range(2):
        myTurtle.forward(length)
        myTurtle.left(120)
    myTurtle.forward(length)

def draw_rhombus(myTurtle, color = "blue", length = 10):
    myTurtle.color(color)
    for i in range(4):
        myTurtle.forward(length)
        myTurtle.right(60 + 60 * (i % 2))

def draw_flower(shape, color, myTurtle, length = 10):
    currentPosition = myTurtle.position()
    myTurtle.speed("fastest")

    for i in range(1, 37):
        shape(myTurtle, color, length)
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
draw_flower(draw_rhombus, "red", myTurtle, 30)
moveTurtle(myTurtle, -100, 0)
draw_flower(draw_triangle, "green", myTurtle, 30)
moveTurtle(myTurtle, 50, 0)
draw_flower(draw_square, "blue", myTurtle, 50)

# Click the window to exit
myWindow.exitonclick()

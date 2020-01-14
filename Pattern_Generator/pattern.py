#Imports to test code

width = 1000
height = 1
centerX = 0
centerY = 0
offset = 0
rotation = 0
count = 2000
radius = 100

import random
import turtle
tr = turtle.Turtle()

#Erase all of the patterns and start over
def reset():
    tr.reset()
    #After resetting code it sets the turtle parameters to default so we need to redifine the speed and screensize
    # Hide the turtle so that the animation occurs faster
    tr.hideturtle()
    # Entering turtle as 0 making it draw as fast as possible
    tr.speed(0)
    # change the size of the turtle screen as requested
    tr.screen.screensize(1000, 800)
    # bring the turtle pen up before we move it anywhere
    tr.penup()

#Configure turtle to draw quickly
#Configure turtle to have a window of 1000 x 800
def setup():
    #Make it so the turtle window does not pop up until after we enter the input
    #global == tr = turtle.Turtle()
    #Hide the turtle so that the animation occurs faster
    tr.hideturtle()
    #Entering turtle as 0 making it draw as fast as possible
    tr.speed(0)
    #change the size of the turtle screen as requested
    tr.screen.screensize(1000,800)
    #bring the turtle pen up before we move it anywhere
    tr.penup()




#Use appropriate parameters
#It should call drawRectangle()
def drawRectanglePattern(width, height, centerX, centerY, offset, count, rotation):
    countRotation = 360 / count
    # Have turtle draw the amount of rectangles asked for
    for i in range(count):
        # Have the pen choose a new color
        setRandomColor()
        # Have turtle go to the center position
        tr.goto(centerX, centerY)
        # Have turtle move based off of the offset
        tr.setheading(countRotation)
        tr.forward(offset)
        # Have the turtle draw the rectangle
        drawRectangle(width, height, rotation)
        # Adjust the count rotation for the next print
        countRotation += 360 / count

#Use appropriate parameters
#Should draw a SINGLE rectangle
def drawRectangle(width, height, rotation):
    tr.left(rotation)
    for i in range (2):
        tr.pendown()
        tr.forward(width)
        tr.left(90)
        tr.forward(height)
        tr.left(90)
        tr.penup()

#Use appropriate parameters
def drawCirclePattern(centerX, centerY, offset, count, radius):
    countRotation = 360 / count
    # Have turtle draw the amount of rectangles asked for
    for i in range(count):
        # Have the pen choose a new color
        setRandomColor()
        # Pick up the pen
        tr.penup()
        # Have turtle go to the center position
        tr.goto(centerX, centerY)
        # Have turtle move based off of the offset
        tr.setheading(countRotation)
        #Have the turtle move to position
        tr.forward(offset)
        #turn the turtle right
        tr.right(90)
        # Have the turtle draw the circle
        drawCircle(radius)
        # Adjust the count rotation for the next print
        countRotation += 360 / count
        '''
        if count >0:
            tr.setheading(countRotation)
            tr.forward(offset)
            #now we need to se the turtle facing the opposite way it came
        '''

def drawCircle(radius):
    tr.pendown()
    tr.circle(radius)
    tr.penup()

# Use appropriate parameters
# Randomly draw Rectangle and Circle patterns. Each pattern should based on random values.
# Use reasonable random values (some can be negative) so patterns are drawn on the screen
def drawSuperPattern(num):
    #Have the user number decide how many random shapes to draw
    for i in range (num):
        randomChoice = random.randint(1, 2)
        if randomChoice == 1:
            drawCirclePattern\
                (
                centerX = random.randint(-250, 250),
                centerY = random.randint(-200, 200),
                offset = random.randint(-100, 100),
                count = random.randint(15, 100),
                radius = random.randint(1, 100)
                )
        else:
            drawRectanglePattern\
                (
                width = random.randint(1, 100),
                height = random.randint(1, 100),
                centerX = random.randint(-250, 250),
                centerY = random.randint(-200, 200),
                offset = random.randint(-100, 100),
                count = random.randint(15, 100),
                rotation = random.randint(-360, 360)
                )

#Do not use any parameters
#Set turtle to draw in a random color
#Use at least 3 colors
def setRandomColor():
    randColorChoice = 0
    randColorChoice = random.randint(1,8)
    if randColorChoice == 1:
        tr.pencolor("blue")
    elif randColorChoice == 2:
        tr.pencolor("red")
    elif randColorChoice == 3:
        tr.pencolor("orange")
    elif randColorChoice == 4:
        tr.pencolor("brown")
    elif randColorChoice == 5:
        tr.pencolor("green")
    elif randColorChoice == 6:
        tr.pencolor("pink")
    elif randColorChoice == 7:
        tr.pencolor("yellow")
    else:
        tr.pencolor("black")

#Called when user quits
#Keeps the turtle window open
def done():
    turtle.done()


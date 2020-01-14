import turtle
tr = turtle.Turtle()
tr.speed(.8)
width = 50
height = 25
centerX = -50
centerY = -50
offset = 50
rotation = 0
count = 2
radius = 100
tr.penup()

def drawRectanglePattern(width, height, centerX, centerY, offset, count, rotation):
    countRotation = 360 / count
    # Have turtle draw the amount of rectangles asked for
    for i in range(count):
        tr.setheading(countRotation)
        # Have the pen choose a new color
        # Have turtle go to the center position
        tr.goto(centerX, centerY)
        tr.forward(offset)
        # Have the turtle draw the rectangle
        drawRectangle(width, height, rotation)
        # Adjust the count rotation for the next print
        countRotation += 360 / count
        tr.setheading(countRotation)

#Use appropriate parameters
#Should draw a SINGLE rectangle
def drawRectangle(width, height, rotation):
    tr.left(rotation)
    for i in range(2):
        tr.pendown()
        tr.forward(height)
        tr.left(90)
        tr.forward(width)
        tr.left(90)
        tr.penup()

#drawRectangle(width, height, rotation)
drawRectanglePattern(width, height, centerX, centerY, offset, count, rotation)
turtle.done()
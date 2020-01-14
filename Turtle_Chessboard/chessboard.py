#Variables and functions to test code
'''
import turtle
tr = turtle.Turtle()
tr.penup()
tr.speed(300)
height=666
width=420
xPos= -250
yPos = 0

'''
import turtle
#Create a function thst will draw one box
def drawRectangle(width, height):
    for i in range(0,2):
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(height / 8)
        turtle.left(90)
        turtle.forward(width / 8)
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()


#Create a function that will print all boxes on the chessboard
def drawAllRectangles(xPos, yPos, width=250, height=250):
    #Repeat the draw (tip Mr. Mano suggested)
    for i in range (0,2):
        turtle.goto(xPos, yPos)
        rowIncrease = 0
        #move turtle to next row (of four) to draw 4 more squares
        for i in range(0,4):
            #move turtle over to draw the next square (of four) on  a row
            for i in range(0,4):
                #set turtle to the right before it draws one square
                turtle.setheading(0)
                #draw one square
                drawRectangle(width, height)
                #move turtle forward to draw next square (line:65)
                turtle.forward(height / 4)
            #put turtle back to start to begin next row (line:63)
            turtle.goto(xPos, yPos)
            turtle.setheading(90)
            rowIncrease += width/4
            turtle.forward(rowIncrease)
        #Put turtle up and to the right of the first box to redraw the grid (line:60)
        xPos += height / 8
        yPos += width / 8


#Create a function that will draw the chessboard outline
def drawChessboard(xPos, yPos, width, height):
    #Go to the X,Y position to draw the outline
    turtle.goto(xPos, yPos)
    turtle.pendown()
    # Begin draw and repeat strait length then rotate and straight height length then rotate
    for i in range (0,2):
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    turtle.penup()
    drawAllRectangles(xPos, yPos, width, height)
    turtle.done()




# Import turtle
import turtle
tr = turtle.Turtle()

# Create class
class Rectangle:

    # Create initializer
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    # Create method to draw the circle
    def draw(self):
        # Have turtle to go where the circle is
        tr.penup()
        tr.goto(self.x, self.y)
        # Have turtle draw the shape with color
        for i in range(2):
            tr.begin_fill()
            tr.fillcolor(self.color)
            tr.forward(self.height)
            tr.left(90)
            tr.forward(self.width)
            tr.left(90)
            tr.end_fill()
        tr.penup()

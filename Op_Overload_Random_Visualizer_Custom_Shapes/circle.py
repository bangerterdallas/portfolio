# Import turtle
import turtle
tr = turtle.Turtle()


# Create class
class Circle:

    # Create initializer
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.count = 0


    # Create method to draw the circle
    def draw(self):
        # Have turtle to go where the circle is
        tr.penup()
        tr.goto(self.x, (self.y - int(self.radius)))
        # Have turtle draw the shape with color
        tr.begin_fill()
        tr.fillcolor(self.color)
        tr.circle(self.radius)
        tr.end_fill()
        tr.penup()

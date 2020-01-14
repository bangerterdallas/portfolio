import turtle
tr = turtle.Turtle()
tr.speed(0)


class Chessboard:
    def __init__(self, tr, startX, startY, width=100, height=100):
        self.height = height
        self.width = width
        self.x_pos = startX
        self.y_pos = startY

    # create a method to draw a circle
    def __draw_rectangle(self):
        for i in range(0, 2):
            tr.pendown()
            tr.begin_fill()
            tr.forward(self.height / 8)
            tr.left(90)
            tr.forward(self.width / 8)
            tr.left(90)
            tr.end_fill()
            tr.penup()

    # Create a function that will print all boxes on the chessboard
    def __draw_all_rectangles(self):
        # Repeat the draw
        for i in range(0, 2):
            tr.goto(self.x_pos, self.y_pos)
            row_increase = 0
            # move turtle to next row (of four) to draw 4 more squares
            for o in range(0, 4):
                # move turtle over to draw the next square (of four) on  a row
                for j in range(0, 4):
                    # set turtle to the right before it draws one square
                    tr.setheading(0)
                    # draw one square
                    self.__draw_rectangle()
                    # move turtle forward to draw next square
                    tr.forward(self.height / 4)
                # put turtle back to start to begin next row
                tr.goto(self.x_pos, self.y_pos)
                tr.setheading(90)
                row_increase += self.width / 4
                tr.forward(row_increase)
            # Put turtle up and to the right of the first box to redraw the grid
            self.x_pos += self.height / 8
            self. y_pos += self.width / 8

    # Create a method that will draw the chessboard outline
    def draw(self):
        # Go to the X,Y position to draw the outline
        tr.penup()
        tr.goto(self.x_pos, self.y_pos)
        tr.pendown()
        # Begin draw and repeat strait length then rotate and straight height length then rotate
        for i in range(0, 2):
            tr.forward(self.height)
            tr.left(90)
            tr.forward(self.width)
            tr.left(90)
        tr.penup()
        self.__draw_all_rectangles()
        turtle.done()




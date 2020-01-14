import turtle
turtle = turtle.Turtle()

class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__dark_eyes = True
    #Create a method to draw the head
    def __draw_head(self):
        if self.__happy== True:
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("yellow")
            turtle.circle(100)
            turtle.end_fill()
            turtle.penup()
        else:
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("red")
            turtle.circle(100)
            turtle.end_fill()
            turtle.penup()
    #Create a method to draw the eyes
    def __draw_eyes(self):
        if self.__dark_eyes == True:
            x_pos = 115
            for i in range(2):
                x_pos -= 75
                turtle.goto(x_pos, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("black")
                turtle.circle(15)
                turtle.end_fill()
                turtle.penup()
        else:
            x_pos = 115
            for i in range(2):
                x_pos -= 75
                turtle.goto(x_pos, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("blue")
                turtle.circle(15)
                turtle.end_fill()
                turtle.penup()
    #Create a method to draw the mouth
    def __draw_mouth(self):
        if self.__smile == True:
            turtle.penup()
            turtle.goto(-60, 55)
            turtle.pencolor("black")
            turtle.pendown()
            turtle.setheading(315)
            turtle.width(10)
            turtle.circle(90, 90)
            turtle.width(1)
            turtle.setheading(0)
            turtle.penup()
        else:
            turtle.penup()
            turtle.goto(75, 50)
            turtle.pencolor("black")
            turtle.pendown()
            turtle.setheading(140)
            turtle.width(10)
            turtle.circle(90, 90)
            turtle.width(1)
            turtle.setheading(0)
            turtle.penup()

    def draw_face(self):
        turtle.clear()
        self.__draw_head()
        self.__draw_eyes()
        self.__draw_mouth()

    def is_smile(self):
        if self.__smile:
            return True
        else:
            return False

    def is_happy(self):
        if self.__happy:
            return True
        else:
            return False

    def is_dark_eyes(self):
        if self.__dark_eyes:
            return True
        else:
            return False

    def change_mouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def change_emotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def change_eyes(self):
        self.__dark_eyes = not self.__dark_eyes
        self.draw_face()


def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.is_smile() else "smile"
        emotion = "angry" if face.is_happy() else "happy"
        eyes = "blue" if face.is_dark_eyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.change_mouth()
        elif menu == 2:
            face.change_emotion()
        elif menu == 3:
            face.change_eyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()

# Import class files
from circle import Circle
from rectangle import Rectangle
import turtle
turtle = turtle.Turtle()

# Create function
def main():

    #define variables and objects
    list = []
    requiredColors = ["red", "yellow", "blue", "green"]

    # Create a loop
    loop = True
    while loop:

        # Create user menu
        print("(1)Enter Circle")
        print("(2)Enter Rectangle")
        print("(3)Remove Shape")
        print("(4)Draw Shapes")
        print("(5)Exit")
        menu = int(input("Select an option from the menu above (1-5): "))

        # Create menu for circle
            # User inputs position, radius, and color. The position is the CENTER of the circle
        if menu == 1:
            x, y, radius = eval(input("Enter the circles position (x,y) and radius: "))
            # Allow red, yellow, blue, and green only
            color = input("Enter the circles color (red, yellow, green, or blue): ")
            # Make sure that the color fits parameters
            while color != requiredColors:
                color = input("Must be red, yellow, green, or blue: ")
                if requiredColors.count(color) > 0:
                    break
            # Use the class
            circle = Circle(x, y, radius, color)
            # Add the object to the list
            list.append(circle)

        # Create menu for rectangle
            # User inputs position, height, width, color. The position is the lower left-hand corner
        elif menu == 2:
            x, y, height, width = eval(input("Enter the rectangles position (x,y), height and width: "))
            # Allow red, yellow, blue, and green only
            color = input("Enter the circles color (red, yellow, green, or blue): ")
            # Make sure that the color fits parameters
            while color != "red" or "yellow" or "green" or "blue":
                color = input("Must be red, yellow, green, or blue: ")
                if color == "red" or "yellow" or "green" or "blue":
                    break
            # Use the class
            rectangle = Rectangle(x, y, height, width, color)
            # Add the object to the list
            list.append(rectangle)

        # Show the number of items in the list and let the user enter a number and remove that shape from the list.
        elif menu == 3:
            # Show the list
            print(list)
            # Ask the user to remove an object from the list
            remove = int(input("What object would you like to remove from the list?: "))
            # Use pop to remove object from the list
            list.pop(remove - 1)
            print(list)

        elif menu == 4:
            # Clear the screen before drawing
            turtle.reset()
            for i in list:
                i.draw()
        # Exit the program
        else:
            break

main()
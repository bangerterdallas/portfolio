'''
   This is the starter file. Only fill in the areas indicated.
   Do not modify existing code.
   Replace this file header with the normal file header (name, etc)
'''
#### Add Import Statement(s) as needed ####
import pattern
#### End Add Import Statement(s) ####
def main():
    # Setup pattern
    pattern.setup()
    # Play again loop
    playAgain = True
    while playAgain:
        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))
        # If they choose 'Rectangle Patterns'
        if mode == 1:
            #### Add Input Statement(s) as needed ####
            centerX, centerY = eval(input("Enter the starting point (X, Y) for the pattern: "))
            offset = int(input("Enter the offset value: "))
            width, height = eval(input("Enter the width and height of the rectangle (10, 20): "))
            rotation = float(input("What rotation for the rectangles would you like? (-360 to 360): "))
            count = int(input("How many rectangles do you want?: "))
            #### End Add Inputs Statement(s) ####
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
            centerX, centerY = eval(input("Enter the starting point (X, Y) for the pattern: "))
            offset = int(input("Enter the offset value: "))
            radius = int(input("Enter the radius for the circle: "))
            count = int(input("How many circles do you want?: "))
            #### End Add Inputs Statement(s) ####
            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)
        # If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####
            num = (input("Enter a number: "))
            #### End Add Inputs Statement(s) ####
            if num == "":
                pattern.drawSuperPattern(num=1)
            else:
                pattern.drawSuperPattern(eval(num))
       # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))
        #### Add Statement(s) to clear drawings and play again ####
        if response == 1:
            playAgain = True
        elif response == 2:
            pattern.reset()
        else:
            break
        #### End Add Inputs Statement(s) ####
        # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()





'''
   This is the starter file. Only fill in the areas indicated.
   Do not modify existing code.
   Replace this file header with the normal file header (name, etc)
'''
#### Add Import Statement(s) as needed ####
import turtle
turtle.speed(0)
from chessboard import drawChessboard

#### End Add Import Statement(s) ####

def main():
   #### Add Code to get input from user ####
   # Have User give the start position
   xPos, yPos = eval(input("Enter where the chessboard is (x,y): "))

   # Test xPos and yPos
   '''
   print (xPos)
   print (yPos)
   '''
   # Have User give parameters for the chessboard
   width = eval(input("Give the width of the chessboard: "))
   height = eval(input("Give the height of the chessboard: "))

   # Test chessboardWidth and chessboardHeight
   '''
   print (chessboardWidth)
   print (chessboardHeight)
   '''

   # Make it so turtle only draws when functions are called
   turtle.penup()

   # Print the chessboard outline
   drawChessboard(xPos, yPos, width, height)

   #### End Add Code to get input from user ####
   if width == "" and height == "":
       drawChessboard(xPos, yPos)
   elif height == "":
       drawChessboard(xPos, yPos, width=eval(width))
   elif width == "":
       drawChessboard(xPos, yPos, height=eval(height))
   else:
       drawChessboard(xPos, yPos, eval(width), eval(height))
    # Let the turtle window remain open

main()
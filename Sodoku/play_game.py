import check_board
import copy
import random
from create_board import CreateBoard

class PlayGame:
    bold = "\033{1m"
    def __init__(self):
        # Menu for the user
        self.menu = None
        # Master lists
        self.masterList = []
        self.masterIndexList = []
        self.editMasterList = []
        # Display Lists
        self.displayList = []
        self.editDisplayList = []
        # Constructor for create_board
        self.firstFile = CreateBoard()
        # Loop for verifying input
        self.loop = True
        # List for solving the board
        self.solveList = []

    def setup(self):
        # Create the board
        check_board.validate()
        # Assign the list
        self.masterList = check_board.getList()
        self.displayList = copy.deepcopy(self.masterList)
        self.solveList = copy.deepcopy(self.masterList)
        # Iteration counter
        self.firstFile = check_board.getIterations()
        # Create the menu
        self.menuSetup()
        # Create the master index
        self.createMasterIndexList()

    # Create the menu
    def menuSetup(self):
        self.menu = "\n   MENU:\n"
        self.menu += "1) If you would like to edit a row\n"
        self.menu += "2) If you would like to edit a column\n"
        self.menu += "3) If you would like to edit a block\n"
        self.menu += "4) Check completion\n"
        self.menu += "5) Have computer solve\n"
        self.menu += "6) Quit"

    # Create the master index list
    def createMasterIndexList(self):
        # For each row
        for row in range(len(self.masterList)):
            # Reset the list and tuple list
            fixedCellsList = []
            enumerateList = list(enumerate(self.masterList[row]))
            # For each number in the tuple
            for numbers in range(len(self.masterList[row])):
                # If the number in the tuple couple is greater than 0
                if enumerateList[numbers][1] > 0:
                    # Add it to the fixedCellsList
                    fixedCellsList.append(enumerateList[numbers][0])
            # Add that list to the masterIndexList and run through the next row
            self.masterIndexList.append(fixedCellsList)

    # Functions for the game
    def game(self):
        # Begin a play loop
        play = "yes"
        while play == "yes":
            # Print the board
            self.printBoard()
            # Print the menu
            print(self.menu)
            # Ask for a selection and validate the choice
            while self.loop:
                choice = input("Enter a selection from the menu: ")
                choice = self.checkMenuInput(choice)
            # Reset the loop
            self.resetLoop()
            # If choice is 1 edit the rows
            if choice == 1:
                self.choiceOne()
            # If choice is 2 edit the columns
            elif choice == 2:
                self.choiceTwo()
            # If choice is 3 edit the blocks
            elif choice == 3:
                self.choiceThree()
            # If choice is 4 see if the board is solved
            elif choice == 4:
                play = self.choiceFour()
            elif choice == 5:
                self.choiceFive()
            # If choice is 6 exit the game
            else:
                play = "no"
                print("Thanks for playing! :)")
            # Reset the format list after editing to allow for formating
            self.resetFormatList()

    def printBoard(self):
        # Format the cells based off of the index list
        self.formatCells()
        counter = 0
        print("\n\n\n\n\n\n\n                     ##### SODOKU BOARD #####")
        print("                            column key")
        print("   1      2      3      4      5      6      7      8      9")
        for row in range(len(self.displayList)):
            board = str(self.displayList[row][0:3])
            board += str(self.displayList[row][3:6])
            board += str(self.displayList[row][6:9])
            board += ("-" + str(row))
            if row == 2:
                board += "  r"
            if row == 3:
                board += "  w"
            if row == 5:
                board += "  k"
            if row == 6:
                board += "  y"
            print(board)
            if row == 2:
                print("---------------------------------------------------------------    o")
            if row == 5:
                print("---------------------------------------------------------------    e")

    def formatCells(self):
        for row in range(len(self.masterList)):
            formatNumberIndexList = []
            numberList = []
            enumerateList = list(enumerate(self.masterList[row]))
            for numbers in range(len(self.masterList[row])):
                # If the right side of the tuple is gt or equal to 0 add its index to the index list
                if enumerateList[numbers][1] >= 0:
                    formatNumberIndexList.append(enumerateList[numbers][0])
            # For the amount of numbers' index's append the number itself to the numberList
            for numberIndex in range(len(formatNumberIndexList)):
                numberList.append(self.displayList[row][formatNumberIndexList[numberIndex]])
            for emptyCell in range(len(formatNumberIndexList)):
                # For each number in the masterIndexList add brackets in-between
                if emptyCell in self.masterIndexList[row]:
                    self.displayList[row][formatNumberIndexList[emptyCell]] = str(
                        "|" + str(numberList[emptyCell]) + "|")
                # For each number not in the masterIndexList add a space between
                else:
                    self.displayList[row][formatNumberIndexList[emptyCell]] = str(
                        " " + str(numberList[emptyCell]) + " ")

    # Method for validating input
    def checkMenuInput(self, input):
        if input.isdigit():
            input = int(input)
            if input <= 6 and input >= 1:
                self.loop = False
                return input
            else:
                print("Enter correct input (1-4)")
        else:
            print("Enter correct input (1-4)")

    # Method for resetting the loop
    def resetLoop(self):
        self.loop = True

    # If user enters one...
    def choiceOne(self):
        # Create a seperate edit list
        self.createEditRowList()
        # Ask and validate user input for a row to edit
        while self.loop:
            row = input("Select a row to edit (refer to row key): ")
            row = self.checkListOrNumber(row)
        # Reset the while loop and subtract one from the row count to be used as a index
        self.resetLoop()
        row -= 1
        # Create a list for displaying the row
        self.createDisplayRowList()
        # Print the user specified row
        self.printRow(row)
        # Ask and validate which cell the user would like to edit
        while self.loop:
            cell = input("Select a cell you would like to edit (refer to cell key): ")
            cell = self.checkEditInputList(cell, row)
        self.resetLoop()
        # Ask and validate what the user would like to edit the cell to
        while self.loop:
            number = input("What would you like to change cell " + str(cell) + " to? (if mistake enter none): ")
            number = self.checkListOrNumber(number)
        self.resetLoop()
        # Subtract one from the cell list to be used as an index
        cell -= 1
        self.editMasterList[row][cell] = number
        self.resetRowList()

    # Create the editRow list from the master list
    def createEditRowList(self):
        self.editMasterList = self.masterList

    # Verify the input for selecting and editing cells
    def checkEditInputList(self, input, inputList):
        if input.isdigit():
            input = int(input)
            if input - 1 in self.masterIndexList[inputList]:
                print("Can't assign a number the board created")
            elif 9 >= input >= 1:
                self.loop = False
                return input
            else:
                print("Enter correct input (1-9)")
        elif input.lower() == "none":
            self.loop = False
            return 0
        else:
            print("Enter correct input (1-9)")

    def checkListOrNumber(self, input):
        if input.isdigit():
            input = int(input)
            if 9 >= input >= 1:
                self.loop = False
                return input
            else:
                print("Enter correct input (1-9)")
        elif input.lower() == "none":
            self.loop = False
            return 0
        else:
            print("Enter correct input (1-9)")

    # Method for creating a list of rows
    def createDisplayRowList(self):
        self.editDisplayList = self.displayList

    # Method for printing the rows with a cell key
    def printRow(self, row):
        print("                            Cell Key")
        print("   1      2      3      4      5      6      7      8      9")
        for i in range(len(self.editDisplayList[row])):
            board = str(self.editDisplayList[row][0:3])
            board += str(self.editDisplayList[row][3:6])
            board += str(self.editDisplayList[row][6:9])
        print(board)

    # Method for resetting the lists manipulated and setting the manipulates list to the master list
    def resetRowList(self):
        self.masterList = self.editMasterList
        self.displayList = copy.deepcopy(self.masterList)
        self.resetEditList()

    # If the user chooses two...
    def choiceTwo(self):
        # Create an edit list from te master list
        self.createEditColumnList()
        # Ask and validate which column they would like to edit
        while self.loop:
            column = input("Select a column to edit (refer to column key): ")
            column = self.checkListOrNumber(column)
        # Reset the loop and subtract one from the column to be used as an index
        self.resetLoop()
        column -= 1
        # Create a edit list from the display list
        self.createDisplayColumnList()
        # Print the column the user selected
        self.printColumn(column)
        # Ask and validate what cell they would like to edit
        while self.loop:
            cell = input("Select a column you would like to edit (refer to cell key): ")
            cell = self.checkEditInputList(cell, column)
        self.resetLoop()
        # Ask and validate what they would like to change the selected cell to
        while self.loop:
            number = input("What would you like to change cell " + str(cell) + " to? (if mistake enter none): ")
            number = self.checkListOrNumber(number)
        # Reset loop and subtract one form the cell to be used as an index
        self.resetLoop()
        cell -= 1
        # Redefine the edit list from the master list
        self.editMasterList[column][cell] = number
        self.resetColumnList()

    # Method for creating the edit column list
    def createEditColumnList(self):
        newList = []
        # For each row
        for k in range(9):
            # Add each number to the new list
            for i in range(9):
                newList.append(self.masterList[i][k])
            # Add the new list to the big list
            self.editMasterList.append(newList)
            newList = []

    # Method for creating the edit display column list
    def createDisplayColumnList(self):
        newList = []
        # For each row
        for k in range(9):
            # Add each number to the new list
            for i in range(9):
                newList.append(self.displayList[i][k])
            # Add the new list to the big list
            self.editDisplayList.append(newList)
            newList = []

    # Method for printing the Columns
    def printColumn(self, column):
        for i in range(len(self.displayList[column])):
            # Print the key and each number
            message = ("|" + str(self.editDisplayList[column][i]) + "| -" + str(i + 1))
            if i == 0:
                message += "  c"
            if i == 1:
                message += "  e"
            if i == 2:
                message += "  l"
            if i == 4:
                message += "  k"
            if i == 5:
                message += "  e"
            print(message)
            if i == 2:
                print("-----     l")
            if i == 5:
                print("-----     y")

    # Method for resetting the edit list and assigning the master list
    def resetColumnList(self):
        # Rotate until the board is reset
        for i in range(2):
            self.masterList = self.editMasterList
            self.resetEditList()
            self.createEditColumnList()
        self.displayList = copy.deepcopy(self.masterList)

    # Method for reseting the edit lists
    def resetEditList(self):
        self.editDisplayList = []
        self.editMasterList = []

    # If the user selects three...
    def choiceThree(self):
        # Create a list for editing the master list
        self.createEditBlockList()
        # Ask and validate which block the user would like to edit
        while self.loop:
            block = input("Select a block to edit: ")
            block = self.checkListOrNumber(block)
        # Reset the loop and subtract one from the block to be used as an index
        self.resetLoop()
        block -= 1
        # Create the list for editing the display
        self.createDisplayBlockList()
        # Print the block the user selected
        self.printBlock(block)
        # Ask and validate which cell the user would like to edit
        while self.loop:
            cell = input("Select a block you would like to edit (refer to cell key): ")
            cell = self.checkEditInputList(cell, block)
        # Reset the loop and ask which the user would like to change the cell to
        self.resetLoop()
        while self.loop:
            number = input("What would you like to change cell " + str(cell) + " to? (if mistake enter none): ")
            number = self.checkListOrNumber(number)
        # Reset the loop and subtract one from the cell to be used as an index
        self.resetLoop()
        cell -= 1
        # Set the new number to the edit list
        self.editMasterList[block][cell] = number
        # Reset the block lists
        self.resetBlockList()

    # Method for creating the blockList for editing
    def createEditBlockList(self):
        newList = []
        # For the set of three, three rows
        for h in range(3):
            # For the set of three, three columns
            for z in range(3):
                # For the set of the 3 columns
                for column in range(3):
                    # For the set of three rows (column x row == 3 x 3)
                    for rows in range(3):
                        newList.append(self.masterList[column + (h * 3)][rows + (z * 3)])
                self.editMasterList.append(newList)
                newList = []

    # Method for creating the displayList for viewing
    def createDisplayBlockList(self):
        newList = []
        # For the set of three, three rows
        for h in range(3):
            # For the set of three, three columns
            for z in range(3):
                # For the set of the 3 columns
                for column in range(3):
                    # For the set of three rows (column x row == 3 x 3)
                    for rows in range(3):
                        newList.append(self.displayList[column + (h * 3)][rows + (z * 3)])
                self.editDisplayList.append(newList)
                newList = []

    # Method for printing the display block
    def printBlock(self, block):
        print("   KEY")
        newList = []
        keyList = []
        for i in range(3):
            newList.append(self.editDisplayList[block][i])
            keyList.append(i + 1)
        print(str(keyList) + " // " + str(newList))
        newList = []
        keyList = []
        for i in range(3, 6):
            newList.append(self.editDisplayList[block][i])
            keyList.append(i + 1)
        print(str(keyList) + " // " + str(newList))
        newList = []
        keyList = []
        for i in range(6, 9):
            newList.append(self.editDisplayList[block][i])
            keyList.append(i + 1)
        print(str(keyList) + " // " + str(newList))

    #Method for resetting the edit list and assigning the master list
    def resetBlockList(self):
        for i in range(2):
            self.masterList = self.editMasterList
            self.resetEditList()
            self.createEditBlockList()
        self.displayList = copy.deepcopy(self.masterList)
    # If the user selects four...
    def choiceFour(self):
        print("CHECKING")
        # Check and see if there are any repeating numbers
        errorCount = check_board.checkFinal()
        # If 0 errors, break loop and print win
        if errorCount == 0:
            print("YOU WIN!!!!")
            return "no"
        # Else, continue the loop
        else:
            print("Incorrect, contains " + str(errorCount) + " errors")
            return "yes"

    # If the user selects five...
    def choiceFive(self):
        # Show them the solved board
        print("Solving" + "." * random.randint(3, 5))
        while self.loop:
            # Add random numbers to cells
            self.addRandomCells()
            # Check row for errors
            errorCount = self.checkErrors()
            # Check columns for errors
            self.createSolveColumnList()
            errorCount += self.checkErrors()
            self.resetSolveColumnList()
            # Check blocks for errors
            self.createSolveBlockList()
            errorCount += self.checkErrors()
            self.resetSolveBlockList()
            # If theres 0 errors break the loop
            if errorCount == 0:
                self.loop = False
        self.resetLoop()
        # Print the board
        self.displayList = copy.deepcopy(self.solveList)


    def addRandomCells(self):
        for row in range(len(self.solveList)):
            counter = 0
            indexList = []
            oneToNineList = []
            # See how many zeros there are
            for number in range(len(self.solveList[row])):
                if self.solveList[row][number] > 0:
                    counter += 1
                    zeroCount = 9 - counter
                    # Add number to oneToNineList
                    oneToNineList.append(self.solveList[row][number])
            # If it is not a blank list
            if counter > 0:
                # Create index list
                enumerateList = list(enumerate(self.solveList[row]))
                for number in range(len(self.solveList[row])):
                    if enumerateList[number][1] > 0:
                        indexList.append(enumerateList[number][0])
                # For how many zeros there are append a random number to a zero
                for zeros in range(zeroCount):
                    randomIndex = random.randint(1, 9) - 1
                    randomNumber = random.randint(1, 9)
                    # Check repeating index or created board index
                    while randomIndex in indexList or randomIndex in self.masterIndexList:
                        randomIndex = random.randint(1, 9) - 1
                    # Check repeating number
                    while randomNumber in oneToNineList:
                        randomNumber = random.randint(1, 9)
                    # Add the random index to the index list
                    indexList.append(randomIndex)
                    oneToNineList.append(randomNumber)
                    self.solveList[row][randomIndex] = randomNumber

    def checkErrors(self):
        for row in range(len(self.solveList)):
            repeatInstance = 0
            errorCount = 0
            # For each row
            for row in range(len(self.solveList)):
                # Check number 1-9
                for oneToNine in range(9):
                    repeatInstance += self.solveList[row].count(oneToNine + 1)
                    # If there is a repeating number
                    if repeatInstance > 1:
                        # Add to the error count if it repeats
                        errorCount += 1
                    # Reset the counter
                    repeatInstance = 0
        # Return error count
        return errorCount

    # Method for creating the solve column list
    def createSolveColumnList(self):
        tempList = []
        newList = []
        # For each row
        for k in range(9):
            # Add each number to the new list
            for i in range(9):
                newList.append(self.solveList[i][k])
            # Add the new list to the big list
            tempList.append(newList)
            newList = []
        self.solveList = tempList

    def resetSolveColumnList(self):
        # Rotate until the board is reset
        for i in range(2):
            self.createSolveColumnList()

    def createSolveBlockList(self):
        newList = []
        tempList = []
        # For the set of three, three rows
        for h in range(3):
            # For the set of three, three columns
            for z in range(3):
                # For the set of the 3 columns
                for column in range(3):
                    # For the set of three rows (column x row == 3 x 3)
                    for rows in range(3):
                        newList.append(self.solveList[column + (h * 3)][rows + (z * 3)])
                tempList.append(newList)
                newList = []
        self.solveList = tempList

    def resetSolveBlockList(self):
        for i in range(2):
            self.createSolveBlockList()

    # Resetter for the format list
    def resetFormatList(self):
        self.displayList = copy.deepcopy(self.masterList)
from create_board import CreateBoard
grab = CreateBoard()

# Create the board
def setup():
    grab.createRows()
    grab.addFirstCells()
    grab.addEmptyCells()

# Function for checking repeating numbers
def checkList():
    grab.checkListDuplicates()
    grab.addEmptyCells()

# Function for checking the horizontal lists
def checkHorizontalList():
    grab.createColumnList()
    grab.resetManipulatedList()
    checkList()

# Function for checking the 3x3 boxes
def check3By3Blocks():
    grab.createBlockList()
    grab.resetManipulatedList()
    checkList()

# Check how many numbers are on the board
def checkDifficutlyNumberCount():
    grab.assignNumbers()
    grab.numberChecker()
    grab.addEmptyCells()
    checkList()

# Reset the error counts
def resetErrors():
    grab.resetErrorCount()

# Getter for the error count
def errorCount():
    return grab.getErrorCount()

# Getter for printing the board
def getList():
    return grab.getList()

def getIterations():
    return grab.getIterations()

def getDifficulty():
    grab.getDifficulty()
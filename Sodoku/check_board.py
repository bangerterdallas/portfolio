import create_checks
import random
check = create_checks

# Function for validating if the board can be used
def validate():
    check.getDifficulty()
    check.setup()
    # Create a loop to validate the Soduku list twice for redundancy
    for i in range(2):
        loop = True
        while loop:
            # Reset error count
            check.resetErrors()
            checkBoard()
            # If the error count is 0 break
            if check.errorCount() == 0:
                loop = False

# Function for checking if the randomly generated board has any repeating numbers
def checkBoard():
    # Check the rows
    check.checkList()
    # Check horizontals
    check.checkHorizontalList()
    # Check blocks
    check.check3By3Blocks()
    # Check Difficulty
    check.checkDifficutlyNumberCount()

# Function for validating if the user done board has any repeating numbers/errors
def checkFinal():
    check.resetErrors()
    checkBoard()
    return check.errorCount()

# Getter for the list
def getList():
    return check.getList()

# Getter for the amount of iterations
def getIterations():
    check.getIterations()




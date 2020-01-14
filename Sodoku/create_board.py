import random
# Create the class
class CreateBoard:
    def __init__(self):
        # List used for checking
        self.mainList = []
        # List used for rotating the board to ra-assign the mainList
        self.manipulatedList = []
        # Counter used to check the validity of the board
        self.errorCount = 0
        # Counter for iterations
        self.iterations = 0
        # Difficulty setting
        self.difficultly = 0
        # Difficulty range
        self.difficultyRange = 0
        # Loop for correct input
        self.loop = True
        # Counter for how many blank rows on the board
        self.blankRows = 0
        # Counter for how many numbers are on the board
        self.numbers = 0

    # Ask the user for difficulty
    def getDifficulty(self):
        while self.loop:
            difficulty = input("What difficulty would you like? (Easy, Normal, Hard, Impossible): ")
            self.setDifficulty(difficulty)
        self.setDifficultyRange()

    def setDifficulty(self, difficulty):
        # If input is all letters
        if difficulty.isalpha():
            # If easy set difficulty to 1
            if difficulty.lower() == "easy":
                print("This will take a while (10 seconds)")
                self.difficulty = 1
                self.loop = False
            # If normal set difficulty to 2
            elif difficulty.lower() == "normal":
                self.difficulty = 2
                self.loop = False
            # If hard set difficulty to 3
            elif difficulty.lower() == "hard":
                self.difficulty = 3
                self.loop = False
            # If impossible set difficulty to 4
            elif difficulty.lower() == "impossible":
                self.difficulty = 4
                self.loop = False
            else:
                print("Enter correct input (Easy, Normal, Hard)")
        else:
            print("Enter correct input (Easy, Normal, Hard)")

    # Create random number ranges based on difficulty
    def setDifficultyRange(self):
        if self.difficulty == 1:
            self.difficultyRange = 9
        elif self.difficulty == 2:
            self.difficultyRange = 6
        else:
            self.difficultyRange = 3

    # Assign how many numbers are on the board based on difficulty
    def assignNumbers(self):
        if self.difficulty == 1:
            self.numbers = 32
        elif self.difficulty == 2:
            self.numbers = 25
        elif self.difficulty == 3:
            self.numbers = 15
        else:
            self.numbers = 5


    def resetList(self, row):
        # Reset the current list
        self.mainList[row] = []
        # Create the new list
        for randomNumberAmount in range(random.randint(1,9), self.difficultyRange):
            self.mainList[row].append(random.randint(1, 9))

    # Create 9 empty lists
    def createRows(self):
        for rowCount in range(9):
            self.mainList.append([])
            self.iterations += 1
        # print("Created nine empty lists: ")
        # self.board()

    # Add random numbers to the empty list
    def addFirstCells(self):
        for row in range(len(self.mainList)):
            # Create the new list
            for randomNumberAmount in range(random.randint(1, 5)):
                self.mainList[row].append(random.randint(1, 9))
                self.iterations += 1
        # print("Added the first random cells: ")
        # self.board()

    # Add zeros to make each list = len(9) [0 imitates an empty cell]
    def addEmptyCells(self):
        # For each row
        for row in range(len(self.mainList)):
            # See how many numbers there are
            intCount = len(self.mainList[row])
            # Subtract 9 to get the amount of missing numbers
            missingNumbers = 9 - intCount
            # Randomly insert zeros in the list
            for zeros in range(missingNumbers):
                self.mainList[row].insert(random.randint(0,9), 0)
                self.iterations += 1
        # print("Added empty cells: ")
        # self.board()

    def checkListDuplicates(self):
        repeatInstance = 0
        # For each row
        for row in range(len(self.mainList)):
            # Check number 1-9
            for oneToNine in range(9):
                repeatInstance += self.mainList[row].count(oneToNine + 1)
                # If there is a repeating number
                while repeatInstance > 1:
                    self.iterations += 1
                    # Add to the error count if it repeats
                    self.errorCount += 1
                    # Reset the current list and counter
                    repeatInstance = 0
                    self.resetList(row)
                    for oneToNine in range(9):
                        repeatInstance += self.mainList[row].count(oneToNine + 1)
                        repeatInstance = 0
                # Reset the counter if original list works
                repeatInstance = 0
        # print("Checked for duplicates: ")
        # self.board()

    def createColumnList(self):
        newList = []
        # For each row
        for k in range(9):
            # Add each number to the new list
            for i in range(9):
                newList.append(self.mainList[i][k])
                self.iterations += 1
            # Add the new list to the big list
            self.manipulatedList.append(newList)
            # Reset new list
            newList = []
        # print("Created the columnList: ")
        # self.columnBoard()

    def createBlockList(self):
        newList = []
        # For the set of three, three rows
        for h in range(3):
            # For the set of three, three columns
            for z in range(3):
                # For the set of the 3 columns
                for column in range(3):
                    # For the set of three rows (column x row == 3 x 3)
                    for rows in range(3):
                        newList.append(self.mainList[column + (h * 3)][rows + (z * 3)])
                        self.iterations += 1
                self.manipulatedList.append(newList)
                newList = []
        # print("Created the blockList: ")
        # self.columnBoard()

    def insertRandomNumbers(self, row):
        counter = 0
        indexList = []
        oneToNineList = []
        # See how many zeros there are
        for number in range(len(self.mainList[row])):
            if self.mainList[row][number] > 0:
                counter += 1
                zeroCount = 9 - counter
                # Add number to oneToNineList
                oneToNineList.append(self.mainList[row][number])
        # If it is not a blank list
        if counter > 0:
            # Create index list
            enumerateList = list(enumerate(self.mainList[row]))
            for number in range(len(self.mainList[row])):
                if enumerateList[number][1] > 0:
                    indexList.append(enumerateList[number][0])
            # For how many zeros there are append a random number to a zero
            for zeros in range(zeroCount-3):
                randomIndex = random.randint(1, 9) - 1
                randomNumber = random.randint(1, 9)
                # Check repeating index
                while randomIndex in indexList:
                    randomIndex = random.randint(1, 9) - 1
                # Check repeating number
                while randomNumber in oneToNineList:
                    randomNumber = random.randint(1, 9)
                # Add the random index to the index list
                indexList.append(randomIndex)
                oneToNineList.append(randomNumber)
                # print("pre : " + str(self.mainList[row]))
                self.mainList[row][randomIndex] = randomNumber
                # print("post: " + str(self.mainList[row]))

    # Checks how many numbers are in the list
    def numberChecker(self):
        counter = 0
        for row in range(len(self.mainList)):
            for number in range(len(self.mainList[row])):
                # If the number is greater than 0 add to the counter
                if self.mainList[row][number] > 0:
                    counter += 1
                    self.iterations += 1
        # If the number counter is not within the range append random numbers
        if counter <= self.numbers - 5 or counter >= self.numbers + 5:
            self.errorCount += 1
            for row in range(len(self.mainList)):
                self.insertRandomNumbers(row)

    # Reseter for the manipulated list
    def resetManipulatedList(self):
        # Re-assign the main list
        self.mainList = self.manipulatedList
        # Reset the column list
        self.manipulatedList = []
        self.iterations += 1

    def getErrorCount(self):
        return self.errorCount

    def resetErrorCount(self):
        self.errorCount = 0

    def getList(self):
        return self.mainList

    def getIterations(self):
        print("Program ran  " + str(self.iterations) + " times to create the board")









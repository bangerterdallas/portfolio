import random
import copy
# color = "\033[0;1;7m"
# reset = "\033[0;30;29m"
# mainList = [["1","0","3"]]
# print(mainList)
# new = (color + mainList[0][1] + reset)
# print(new)
# print(type(new))
# mainList[0][1] = new
# print(mainList)
# print(mainList[0][1])

class Test:
    def __init__(self):
        self.masterList = [[0, 3, 0, 0, 0, 0, 0, 0, 9], [1, 3, 2, 4, 5, 6, 8, 7, 0], [1, 3, 2, 4, 5, 6, 8, 7, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.masterIndexList = []
        self.displayList = copy.deepcopy(masterList)

    def addFixedCells(self):
        for row in range(len(self.masterList)):
            fixedCellsList = []
            fixedList = []
            enumerateList = list(enumerate(self.masterList[row]))
            for numbers in range(len(self.masterList[row])):
                if enumerateList[numbers][1] > 0:
                    fixedCellsList.append(enumerateList[numbers][0])
            self.masterIndexList.append(fixedCellsList)
            for fixedCells in range(len(fixedCellsList)):
                fixedList.append(self.displayList[row][fixedCellsList[fixedCells]])
            for fixedCells in range(len(fixedCellsList)):
                self.displayList[row][fixedCellsList[fixedCells]] = str("|" + str(fixedList[fixedCells]) + "|")

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
            # For each number not in the masterIndexList add a space between
            for emptyCell in range(len(formatNumberIndexList)):
                if emptyCell in self.masterIndexList[row]:
                    pass
                else:
                    self.displayList[row][formatNumberIndexList[emptyCell]] = str(" " + str(numberList[emptyCell]) + " ")
        print(self.displayList)

test = Test()
test.addFixedCells()
test.formatCells()
masterIndexList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
isInList = [1, 0, 0, 0, 0, 0, 0, 0, 0]
for j in range(len(testList)):
    if j in testList:
        pass
    else:
        print("added space")











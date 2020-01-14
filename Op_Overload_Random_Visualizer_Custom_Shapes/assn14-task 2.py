# Import random to run the random function
import random

# Create a function
def randomCount():

    # Set variables
    randInt = ""
    number = 0

    # Create a range to check 1000 instances of random
    for i in range(1000):

        # Check random integers between 0 and 9
        randInt += (str(random.randint(0, 9)) + ',')

    # Create a list and split it by a comma
    list = randInt.split(',')

    # Tell the user the amount of number occurences in the list
    for i in range(10):
        count = "Number " + str(number) + " occurences: " + str(list.count(str(number)))
        countPercent = str((list.count(str(number)) / 1000) * 100) + "%"
        print (count + " or " + countPercent + " of the time")
        number += 1
randomCount()


















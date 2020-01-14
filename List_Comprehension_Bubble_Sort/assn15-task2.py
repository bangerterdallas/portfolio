def bubbleSort(inputList):
    loop = True
    while loop:
        loop = False
        for j in range(len(inputList) - 1):
            if inputList[j] > inputList[j + 1]:
                inputList[j], inputList[j + 1] = inputList[j + 1], inputList[j]
                loop = True
def main():
    numberList = []
    loop = True
    count = 0
    sum = 0
    max = None
    while loop:
        number = input("Enter a number to add to the list or enter nothing to review the list: ")
        if number.isdigit() == True:
            numberList.append(int(number))
            print("added number: " + number)
            count += 1
            sum += int(number)
        elif number == "":
            break
        else:
            print("Enter correct input >:(")
    print("Number of values entered: " + str(count))
    bubbleSort(numberList)
    print("Maximum value: " + str(numberList[-1]))
    print("Minimum value: " + str(min(numberList)))
    print("Sum of all values: " + str(sum))
    average = (sum / count)
    print("Average value: " + str(average))
main()
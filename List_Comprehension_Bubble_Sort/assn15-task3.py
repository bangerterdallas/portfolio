from deck import Deck

def linear_search(wholeDeck, key):
    for i in range(len(wholeDeck)):
        if key == wholeDeck[i]:
            return i
    return None

def main():
    deck = Deck()
    # Create user prompts
    menu = "1) Sort by value \n"
    menu += "2) Sort by id \n"
    menu += "3) Find card \n"
    menu += "4) New hand \n"
    menu += "5) Quit \n"
    print(menu)

    # Create loop for user input
    loop = True
    while loop:
        # Ask for user input
        userInput = int(input("Choose a selection: "))

        if userInput == 1:
            counter = 1
            for i in range(len(hand)):
                print("Card #" + str(counter) + ": " + str(hand[i]))
                counter += 1
            print(menu)

        elif userInput == 2:
            counter = 1
            for i in range(len(hand)):
                print("Card #" + str(counter) + ": " + str(hand[i]))
            print(menu)

        elif userInput == 3:
            wholeDeck = deck.getDeck()
            key = input("Enter a card to search for (ex. 20ScissorsTails): ")
            print(type(wholeDeck.pop(0)))
            print(wholeDeck)
            result = linear_search(wholeDeck, key)
            if result == None:
                print("Did not find card", key)
            else:
                print("Found ", key, " at position ", result)
            print(menu)

        elif userInput == 4:
            hand = []
            for i in range(2):
                hand.append(deck.draw())
            print(menu)

        else:
            break
main()
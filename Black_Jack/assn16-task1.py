from deck import Deck
import time

# Create a sort to sort winners
def insertionSort(inputList):
    for i in range(1, len(inputList)):
        currElement = inputList[i]
        j = i - 1
        while j >= 0 and inputList[j] > currElement:
            inputList[j + 1] = inputList[j]
            j -= 1

        inputList[j + 1] = currElement

def main():
    # Create variables and lists
    allCardsList = []
    dealer = 1
    loop = True

    # Tell the user to setup the round
    print("########## SETUP THE ROUND ##########")
    # Create a loop to validate and get the playerCount
    while loop:
        # Ask the user how many players there are in the game (1-5)
        playerCount = input("How many players are there? (1-5): ")
        # If the count is a digit
        if playerCount.isdigit():
            # if the player count is greater than 6 ask again
            if int(playerCount) > 6:
                print("That is too many players, enter a correct player count(1-5)")
            # if the count is in between 0 and 5 break
            elif int(playerCount) < 6 and int(playerCount) > 0:
                playerCount = int(playerCount)
                break
        # Ask again for anything else
        else:
            print("Either enter a valid number or enter a correct player count (1-5)")
    print("There are " + str(playerCount) + " players \n")

    # Create lists (for loop made to catagorize)
    for i in range(1):
        # Initialize one list per player including the dealer
        for totalPlayers in range(playerCount + dealer):
            hand = []
            allCardsList.append(hand)

        # Add the starting money to each player except the dealer
        counter = 0
        for totalPlayers in range(playerCount):
            allCardsList[counter].append([100])
            counter += 1

        # Add the bet list to the players
        counter = 0
        for totalPlayers in range(playerCount):
            allCardsList[counter].append([])
            counter += 1

        # Add the handscore lists to the players including the dealer
        counter = 0
        for totalPlayers in range(playerCount + dealer):
            allCardsList[counter].append([])
            counter += 1

        # Add the cards lists to the players including the dealer
        counter = 0
        for totalPlayers in range(playerCount + dealer):
            allCardsList[counter].append([])
            counter += 1

    # Begin the play again loop
    playAgain = "Yes"
    while playAgain == "yes" or playAgain == "Yes":

        # Initialize the deck
        deck = Deck()
        # Give each player their cards including the cards
        counter = 0
        for totalPlayers in range(playerCount + dealer):

            # Create two for loops to realistically divy out the cards
            for drawCard in range(1):
                allCardsList[counter][-1].append(deck.draw())
            for drawCard in range(1):
                allCardsList[counter][-1].append(deck.draw())
            counter += 1

        # Calculate scores (done in for loop for catagorization)
        for i in range(1):
            # Calculate players scores
            counter = 0
            for totalPlayers in range(playerCount):
                score = 0
                for card in allCardsList[counter][-1]:
                    # If the card returns 11-13 it is a royal and thus worth 10
                    if card.getCardValue() == 11 or card.getCardValue() == 12 or card.getCardValue() == 13:
                        score += 10
                    # If the card returns 1 it is an ace and thus worth 11 or until later changed back to 1
                    elif card.getCardValue() == 1:
                        score += 11
                    # If the card returns anything else it is its own value
                    else:
                        score += card.getCardValue()
                allCardsList[counter][2].append(score)
                counter += 1

            # Calculate the dealers score (done on its own as it has a different list count)
            for i in range(1):
                score = 0
                for card in allCardsList[-1][-1]:
                    # If the card returns 11-13 it is a royal and thus worth 10
                    if card.getCardValue() == 11 or card.getCardValue() == 12 or card.getCardValue() == 13:
                        score += 10
                    # If the card returns 1 it is an ace and thus worth 11 or until later changed back to 1
                    elif card.getCardValue() == 1:
                        score += 11
                    # If the card returns anything else it is its own value
                    else:
                        score += card.getCardValue()
                allCardsList[-1][0].append(score)

        # Ask and validate each players bet amount
        currentPlayer = 0
        for totalPlayers in range(playerCount):

            # Validate betAmount
            while loop:
                # Ask for the user for the bet amount
                print("Your current balance is: $" + str(allCardsList[currentPlayer][0][0]))
                betAmount = input("Player " + str(currentPlayer + 1) + " enter your bet amount (can't be less than $5): ")
                if betAmount.isdigit():
                    # If the bet amount is larger than what they have
                    if int(betAmount) > allCardsList[currentPlayer][0][0]:
                        print("The current bet exceeds your existing funds")
                    # If the bet amount is less than 5 but they have less than 5
                    elif int(betAmount) < 5 and allCardsList[currentPlayer][0][0] < 5:
                        betAmount = int(betAmount)
                        print("Since your current balance is less than 5 you are allowed to bet $" + str(betAmount))
                        break
                    # if the bet amount is less than 5 but they have more than 5
                    elif int(betAmount) < 5 and allCardsList[currentPlayer][0][0] > 5:
                        betAmount = int(betAmount)
                        print("You cannot bet less than $5")
                    # If the bet amount fits all parameters
                    elif int(betAmount) >= 5 and allCardsList[currentPlayer][0][0] > 5:
                        betAmount = int(betAmount)
                        break
                # If the bet amount does not fit any other parameters
                else:
                    print("Enter valid input")
            print("Added $" + str(betAmount) + " to player " + str(currentPlayer + 1) + "'s bet amount\n")
            # Add the bet amount to each player
            allCardsList[currentPlayer][1].append(betAmount)
            currentPlayer += 1

        print("\n\n########## BEGIN THE ROUND ############")
        print("#### DEAL THE CARDS TO EACH PLAYER ####\n\n")
        # Create a new round for each player
        playerCounter = 0
        for totalPlayers in range(playerCount):
            # Wait for the new player to begin their turn
            pauseInput = input("Player " + str(playerCounter + 1) + ", press or enter anything to begin your turn: ")
            # Show each player their stats
            print("PLAYER " + str(playerCounter + 1))
            print("Your balance is: $" + str(allCardsList[playerCounter][0][0]))
            print("Your bet amount is: $" + str(allCardsList[playerCounter][1][0]))
            print("The dealers card is: " + str(allCardsList[-1][-1][-1]))
            print("Your score is: " + str(allCardsList[playerCounter][2][0]))
            cards = ("Your cards are: " + str(allCardsList[playerCounter][3][0]) + " and " + str(allCardsList[playerCounter][3][1]))
            print(cards)

            # Create a loop to draw cards
            handCounter = 5
            while loop:
                # Validate and redefine hitStay
                while loop:
                    # Ask the player if they would like to hit or stay
                    hitStay = input("Would you like to hit or stay?: ")
                    # If hit reasign to 0
                    if hitStay == "hit" or hitStay == "Hit" or hitStay == 0:
                        hitStay = 0
                        break
                    # If stay reasign to 1
                    elif hitStay == "stay" or hitStay == "Stay" or hitStay == 1:
                        hitStay = 1
                        break
                    else:
                        print("Enter either hit or stay")
                # Add a card to the players hand if they hit
                if hitStay == 0:
                    print("\nYou would like to hit\n")

                    # Draw a card
                    allCardsList[playerCounter][3].append(deck.draw())

                    # Tell the user the new card and new score
                    print("You drew: " + str(allCardsList[playerCounter][-1][-1]))
                    cards += (" and " + str(allCardsList[playerCounter][-1][-1]))
                    print(cards)

                    # Add the new card score to the score count and tell the user
                    score = 0
                    for card in allCardsList[playerCounter][-1]:
                        # If the card returns 11-13 it is a royal and thus worth 10
                        if card.getCardValue() == 11 or card.getCardValue() == 12 or card.getCardValue() == 13:
                            score += 10
                        # If the card returns 1 it is an ace and thus worth 11 or until later changed back to 1
                        elif card.getCardValue() == 1:
                            score += 11
                        # If the card returns anything else it is its own value
                        else:
                            score += card.getCardValue()
                    # Reassign the score value
                    allCardsList[playerCounter][2][0] = score
                    print("Your score is: " + str(allCardsList[playerCounter][2][0]))

                    # If they draw a card and go over 21 then break
                    # ACE CHANGE
                    if allCardsList[playerCounter][2][0] > 21:
                        # Check if they have an ace in their hand
                        score = 0
                        for card in allCardsList[playerCounter][-1]:
                            # If the card returns 11-13 it is a royal and thus worth 10
                            if card.getCardValue() == 11 or card.getCardValue() == 12 or card.getCardValue() == 13:
                                score += 10
                            # If the card returns 1 it is now time to change it to a 1
                            elif card.getCardValue() == 1:
                                score += 1
                            # If the card returns anything else it is its own value
                            else:
                                score += card.getCardValue()
                        allCardsList[playerCounter][2][0] = score
                        # If they do not have an ace break the loop and have them bust
                        if allCardsList[playerCounter][2][0] > 21:
                            print("You busted as your score went over 21 :(\n\n")
                            break
                        # If they do have an ace let the player know and print the new score
                        else:
                            print("Changed the Ace from 11 to 1")
                            print("Your new score is: " + str(allCardsList[playerCounter][2][0]))
                    handCounter += 1
                # End the players turn if they want to stay
                else:
                    print("You chose to stay\n\n")
                    break
            playerCounter += 1
        # Allow the player to decide when the dealer begins thier turn
        run = input("Press or enter anything to end the round")
        print("\n\n\n########### END THE ROUND #############")
        print("##### DETERMINE WINNERS/LOSERS ########")

        # Show the dealers entire hand
        print(allCardsList[-1][-1])
        print("\n" + "The dealers cards are: " + str(allCardsList[-1][-1][0]) + " and " + str(allCardsList[-1][-1][1]) + "\n")
        # If the dealers hand is greater than or equal to 17 print the score and tell the player they hold
        if allCardsList[-1][0][0] >= 17:
            print("The dealers score is: " + str(allCardsList[-1][0][0]))
            # Wait for three seconds
            time.sleep(3)
            print("The dealer holds")
        # If the dealers hand is less than 17 have them take a new card
        elif allCardsList[-1][0][0] < 17:
            while allCardsList[-1][0][0] <= 17:
                # Tell the player the new score
                print("The dealers score is: " + str(allCardsList[-1][0][0]))
                time.sleep(3)
                # Draw a card
                allCardsList[-1][-1].append(deck.draw())
                # Tell the player what they drew
                print("The Dealer drew " + str(allCardsList[-1][-1][-1]))
                # Reset the score with the new hand
                score = 0
                for card in allCardsList[-1][-1]:
                    # If the card returns 11-13 it is a royal and thus worth 10
                    if card.getCardValue() == 11 or card.getCardValue() == 12 or card.getCardValue() == 13:
                        score += 10
                    # If the card returns 1 it is an ace and for now returns an 11
                    elif card.getCardValue() == 1:
                        score += 1
                    # If the card returns anything else it is its own value
                    else:
                        score += card.getCardValue()
                allCardsList[-1][0][0] = score
                time.sleep(2)
            # If the dealers hand is greater than 21
            if allCardsList[-1][0][0] > 21:
                # Check to see if their is an Ace in the dealers hand
                score = 0
                for card in allCardsList[-1][-1]:
                    # If the card returns 11-13 it is a royal and thus worth 10
                    if card.getCardValue() == 11 or card.getCardValue() == 12 or card.getCardValue() == 13:
                        score += 10
                    # If the card returns 1 it is now time to change it to a 1
                    elif card.getCardValue() == 1:
                        score += 1
                    # If the card returns anything else it is its own value
                    else:
                        score += card.getCardValue()
                allCardsList[-1][0][0] = score
                print("Preformed an Ace change")
                # If not break the code
                if allCardsList[-1][0][0] > 21:
                    print("The dealer busted as its total went over 21 >:)\n\n")
                    time.sleep(2)
                    allCardsList[-1][0][0] = 0
                # If so change the score and allow them to continue
                else:
                    print("The dealer busts")
                    allCardsList[-1][0][0] = 0
                    time.sleep(2)

        # Calculate the winners, tiers, losers
        playerCounter = 0
        removeCount = 0
        for totalPlayers in range(playerCount):

            # If they win
            if allCardsList[playerCounter][2][0] > allCardsList[-1][0][0] and allCardsList[playerCounter][2][0] <= 21:
                print("\n" + "Player " + str(playerCounter + 1) + " wins! :)")
                # Add the bet amount to the total cash
                betAmount = allCardsList[playerCounter][1][0]
                cashTotal = allCardsList[playerCounter][0][0]
                allCardsList[playerCounter][0][0] = cashTotal + betAmount
                # Reset the hand
                allCardsList[playerCounter][1] = []
                allCardsList[playerCounter][2] = []
                allCardsList[playerCounter][-1] = []

            # If they tie
            elif allCardsList[playerCounter][2][0] == allCardsList[-1][0][0]:
                print("\n" + "Player " + str(playerCounter + 1) + " ties :/")
                # Reset the hand
                allCardsList[playerCounter][1] = []
                allCardsList[playerCounter][2] = []
                allCardsList[playerCounter][-1] = []

            # If they lose
            else:
                print(("\n" + "Player " + str(playerCounter + 1) + " loses with a score of " + str(allCardsList[playerCounter][2][0]) + " :("))
                # Subtract the bet amount to the total cash
                betAmount = allCardsList[playerCounter][1][0]
                cashTotal = allCardsList[playerCounter][0][0]
                allCardsList[playerCounter][0][0] = cashTotal - betAmount
                # Reset the hand
                allCardsList[playerCounter][1] = []
                allCardsList[playerCounter][2] = []
                allCardsList[playerCounter][-1] = []
            playerCounter += 1

        # Reset the dealers hand
        allCardsList[-1][-1] = []
        allCardsList[-1][0] = []

        #Calculate if the player is out of the game
        playerCounter = 0
        for totalPlayers in range(playerCount):
            if allCardsList[playerCounter][0][0] < 1:
                print("Player " + str(playerCounter + 1) + " has been removed from the game")
                allCardsList[playerCounter].pop()
                removeCount += 1
            playerCounter += 1

        # Adjust the player count for those who were removed
        playerCount -= removeCount
        print(str(playerCount) + " players left")
        # Show all users current cash moneys
        counter = 0
        for totalPlayers in range(playerCount):
            print("Player " + str(counter + 1) + " has $" + str(allCardsList[counter][0][0]))
            counter += 1

        # Ask the user if they would like to play again
        print(allCardsList)
        playAgain = input("Would you like to play another round?: ")
        print("\n\n\n\n\n\n\n\n\n")
        if playAgain == "Yes" or playAgain == "yes":
            continue
        else:
            break
    print("Thanks for playing!")

    # Show who won
    # Create a new list
    winlist = []
    counter = 0
    for totalPlayers in range(playerCount):
        # Add each player along with thier earnings to the list
        winlist.append([allCardsList[counter][0][0], (counter + 1)])
        counter += 1
    # Sort the win list
    insertionSort(winlist)

    counter = 0
    # Tell the players who won from last to first
    for totalPlayers in range(playerCount):
        print("Player " + str(winlist[counter][-1]) + " is in #" + str(playerCount - counter) + " place with $" + str(winlist[counter][0]))
        counter += 1
main()
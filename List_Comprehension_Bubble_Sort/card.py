class Card:

    # Create lists with values for the deck
    __value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    __paw = ["Rock", "Paper", "Scissors"]
    __coin = ["Heads", "Tails"]

    def __init__(self, value):
        self.__value = value

    def getCardNumber(self):
        value1 = self.__value
        return Card.__value[value1 % 20]

    def getCardPaw(self):
        value2 = self.__value
        return Card.__paw[value2 // 20]

    def getCardCoin(self):
        value3 = self.__value
        return Card.__coin[value3 * 2 // 60]

    def getDeckValue(self):
        return self.__value % 20 + 1

    # Dunder to return a string representation to print() and format()
    def __str__(self):
        return str(self.getCardNumber()) + self.getCardPaw() + self.getCardCoin()

    # Dunder to return a string representation to other usages
    def __repr__(self):
        return self.__str__()
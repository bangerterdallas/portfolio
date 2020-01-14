import random
from card import Card

class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.__deck = []
        for i in range(60):
            self.__deck.append(Card(i))
        random.shuffle(self.__deck)
        print(self.__deck)

    def draw(self):
        return self.__deck.pop()

    def getDeck(self):
        return self.__deck
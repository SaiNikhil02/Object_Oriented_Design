class Hand:
    def __init__(self):
        self._score = 0
        self._cards = []

    def addCard(self, card):
        self._cards.append(card)
        if card.getValue() == 1:
            self._score += 11 if self._score + 11 <= 21 else 1
        else:
            self._score += card.getValue()
        print('Score: ', self._score)

    def getScore(self):
        return self._score

    def getCards(self):
        return self._cards

    def print(self):
        for card in self.getCards():
            print(card.getSuit(), card.getValue())

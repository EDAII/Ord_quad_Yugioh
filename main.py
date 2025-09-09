import random
from enum import Enum

def shuffle(deck):
    #embaralha o deque
    for i in range(len(deck)-1, 0, -1):
        randomi = random.randint(0, i-1)
        deck[i], deck[randomi] = deck[randomi], deck[i]

def dealToAll(deck, players, cardsPerPlayer):
    # Distribui cartas aos jogadores
    if len(deck) < len(players) * cardsPerPlayer:
        raise ValueError("Not enough cards for all players")
    for p in range(len(players)):
        for i in range(cardsPerPlayer):
            cardindex = p + len(players) * i
            players[p].addCard(deck[cardindex])

    # Remover as cartas distribuídas
    for r in range(len(players) * cardsPerPlayer):
        del deck[0]


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def addCard(self, card):
        self.hand.append(card)


def main():
    deck = ['A','A','A','B','B','B','C','C','C','D','D','D','E','E','F','H','H','H','I','I','J','J','J','J','K','M','N','O','P','P','R','U','U','U','V','V','W','W','W','Z']
    #print(len(deck))

    shuffle(deck)

    #print("Deque: " + str(deck))

    players = [Player("yugia"), Player("armando"), Player("beatriz"), Player("carlos")]
    dealToAll(deck, players, 5)

    print("Deque restante: " + str(deck))

    for p in players:
        print(p.name + ": " + str(p.hand))

if __name__ == "__main__":
    main()

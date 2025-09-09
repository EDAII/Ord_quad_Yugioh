import random
import os
from time import sleep

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

yugiDeck = []

def shuffleYugiDeck():
    #embaralha o deque
    for i in range(len(yugiDeck)-1, 0, -1):
        randomi = random.randint(0, i-1)
        yugiDeck[i], yugiDeck[randomi] = yugiDeck[randomi], yugiDeck[i]

class Deck:
    def __init__(self, nome, counterA, counterB, counterC):
        global yugiDeck
        if(counterA + counterB + counterC > 5):
            raise ValueError("Não é possível counterar o deck " + nome + " com uma só mão")
        
        self.name = nome
        self.counterA = counterA
        self.counterB = counterB
        self.counterC = counterC
        
class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

def main():

    global yugiDeck
    #yugiDeck = ['B', 'B', 'B', 'A', 'B']
    yugiDeck = ['A','A','B','B','C','D','D','D','E','E','F','H','H','H','I','I','J','J','J','K','M','N','Q', 'Q', 'O','P','P','R','U','U','U','V','V','W','W','W','X','X','Z','Z']
    shuffleYugiDeck()


    players = [
        Player("Eliana", Deck("Exodia", 0, 1, 0)),
        Player("Poly", Deck("Pot of Greed", 0, 2, 0)),
        Player("Trevor", Deck("Tryhard", 2, 2, 1)),
        Player("Toninho", Deck("Tenpai", 0, 0, 1)),
        Player("Marcos", Deck("Marcado", 1, 1, 0)),
        Player("Kalynne", Deck("Kashtira", 2, 1, 0))
    ]

    


    print("Oponentes na competição:")

    print("Nº | NOME      | BARALHO     | CONDIÇÃO PARA CONSEGUIR COUNTERAR")
    print("------------------------------------------------------------")

    i = 1
    for p in players:
        print(f"{i}  | {p.name:10}| {p.hand.name:13}| As:{p.hand.counterA}, Bs:{p.hand.counterB}, Cs:{p.hand.counterC}")
        i += 1

    num = int(input("\nIndique seu oponente: "))

    if(num < 1 or num > len(players)):
        raise ValueError("Esse Número não corresponde a nenhum oponente")

    cls()

    sortUntilCountered(players[num-1].hand)

def sortUntilCountered(deckToCounter):
    global yugiDeck
    i = 1


    while(i < len(yugiDeck) and verify(deckToCounter) == False):
        print(yugiDeck)
        sleep(0.5)

        j = i
        swap = False
        while(j >= 1 and yugiDeck[j] < yugiDeck[j-1]):
            swap = True
            yugiDeck[j], yugiDeck[j-1] = yugiDeck[j-1], yugiDeck[j]
            j -= 1
        
        #Visualize unchanged Item
        if(swap == False):
            print("  " +  " " * i * 5 + "|")
            print("  " +  " " * i * 5 + "|")
            print("  " +  " " * i * 5 + "V")
        else:
            
            print("  " +  " " * i * 5 + "|")
            print("  " +  (" " * (j) * 5) + "-" * (i-j) * 5 + "-")
            print("  " +  (" " * (j) * 5) + "|")
            print("  " +  (" " * (j) * 5) + "V")
        i+=1

    print(yugiDeck)



def verify(deckToCounter) -> bool:
    As = 0
    Bs = 0
    Cs = 0
    for i in range(5):
        if yugiDeck[i] == 'A':
            As += 1
        elif yugiDeck[i] == 'B':
            Bs += 1
        elif yugiDeck[i] == 'C':
            Cs += 1

    return As >= deckToCounter.counterA and Bs >= deckToCounter.counterB  and  Cs >= deckToCounter.counterC 


if __name__ == "__main__":
    main()

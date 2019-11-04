c = 'A'

single = 0
reverse = 1
skip = 2
null = 3
fail = 4

import random

index = 0

class Hand():
    def __init__(self, name):
        self.name = name
    def play(before, after):
        if random.random() < 0.01:
            return False
        if before == reverse:
            play
        if after == reverse:

        if random.random() < 1/3:

        pass
    def __repr__(self):
        return self.name
        
def p(hands):
    global index
    if index < 1:
        index = len(hands) - 1
    else:
        index -= 1
    return hands[index]

def n(hands):
    global index
    if index > len(hands) - 2:
        index = 0
    else:
        index += 1
    return hands[index]

def init(players):
    hands = []
    for i in range(len(players)):
        if i == 0:
            hands.append(Hand(players[i]+'0'))
            hands.append(Hand(players[i]+'1'))
        elif i == len(players) - 1:
            hands.insert(len(hands) - 1, Hand(players[i] +'0'))
            hands.insert(1, Hand(players[i]+'1'))
        else:
            hands.insert(len(hands) - 1, Hand(players[i] +'0'))
            hands.insert(len(hands), Hand(players[i]+'1'))
    return hands
players = ['A', 'B', 'C', 'D', 'E']

hands = init(players)

def display(hands):
    s = ''
    for x in hands:
        s += f'{x}   '
    print(s.strip())

from time import sleep

while len(hands) > 2:
    break

display(hands)
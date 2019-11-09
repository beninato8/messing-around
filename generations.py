"""intersteller repopulation"""
"""human population growth"""
from time import sleep
from random import random

class Human():
    def __init__(self, gender, cooldown=-1):
        self.gender = gender
        self.age = 0
        self.cooldown = cooldown
        if self.gender == 'female' and cooldown == -1:
            self.cooldown = (12 * 16) + 9
    def can_give_birth(self):
        return self.cooldown == 0
    def isFemale(self):
        return self.gender == 'female'

humans = [Human('female', 9)]
months = 0
previous = 1
while True:
    tmpHumans = []
    for x in humans:
        if x.isFemale():
            if x.can_give_birth():
                tmpHumans.append(Human(((random() > .5) * 'female' or 'male')))
                x.cooldown = 9
            else:
                x.cooldown -= 1
        x.age += 1
    humans = humans + tmpHumans
    months += 1
    # print(f'{len(humans)}\t{months}')
    # if len(humans) > 2*previous:
    #     print(months, len(humans))
    #     previous *= 2
    if len(humans) > 8000:
        print(f'{len(humans)}\t{months}')
        exit()

import sys
import numpy as np

args = sys.argv
if len(args) == 1:
    exit()
args = args[1:]
print(args)
if np.ceil(int(args[1])/int(args[0])) > 3:
    val = 4
else:
    val = 1
print(val)
i = 0
team1 = 0
team2 = 0
while True:
    if np.random.random() > .5:
        team1 += 1
    else:
        team2 += 1
    if team1 == int(args[0]):
        if i == val:
            print(args[0])
            exit()
        else:
            i += 1
            team1 = 0
            team2 = 0
    if team2 == int(args[1]):
        print(args[1])
        exit()
    print(team1, team2, i)
#!/usr/bin/env python3

from coinflip import do_thing

# teams = list(range(1, 17))
# teams = [[x, 17-x] for x in teams]
# teams = teams[:len(teams)//2]

teams = [[1, 16], [8, 9], [5, 12], [4, 13], [6, 11], [3, 14], [7, 10], [2, 15]]

# print(teams)
for i in range(4):
    for team in teams:
        print(team, end=' ')
        do_thing(team)
    print()


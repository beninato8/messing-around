#!/usr/bin/env python3

from coinflip2 import do_thing

# teams = list(range(1, 17))
# teams = [[x, 17-x] for x in teams]
# teams = teams[:len(teams)//2]

teams = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]*4

tmp = []
# print(teams)
while len(teams) > 1:
    tmp = []
    for i in range(0, len(teams), 2):
        tmp.append(do_thing([teams[i], teams[i+1]]))
    teams = tmp
    print('\n'.join(str(x) for x in teams))
    print()



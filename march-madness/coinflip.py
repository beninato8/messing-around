#!/usr/bin/env python3

import sys
import numpy as np

def do_thing(args):
    if np.ceil(int(args[1])/int(args[0])) > 3:
        val = 4
    else:
        val = 1
    # print(val)
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
                if args[0] == args[1]:
                    print('***0***')
                # print(args[0])
                return args[0]
            else:
                i += 1
                team1 = 0
                team2 = 0
        if team2 == int(args[1]):
            # print(args[1])
            if args[0] == args[1]:
                    print('***1***')
            return args[1]
        # print(team1, team2, i)

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        exit()
    args = args[1:]
    print(do_thing(args))
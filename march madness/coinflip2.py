#!/usr/bin/env python3

import sys
import numpy as np

def do_thing(args):
    total = sum(args)
    # print(total, args[0], args[1])
    x = np.random.random()
    # print(x)
    # print(args[0]/total)
    if x < .5:
        if args[0] == args[1]:
            print('***1***')
        return args[1]
    if args[0] == args[1]:
            print('***0***')
    return args[0]

if __name__ == '__main__':
    args = sys.argv
    args = ['', 4, 5]
    if len(args) == 1:
        exit()
    args = args[1:]
    print(do_thing(args))
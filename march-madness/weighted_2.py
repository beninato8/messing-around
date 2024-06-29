#!/usr/bin/env python3

# from coinflip2 import do_thing
import numpy as np
from random import choices

def do_thing(a, b):
    if np.random.random() > ( a/ 17):
        return a
    return b
    # print(x, y)

def do_thing(a, b):
    # return choices(population=[a,b], weights=[-a*np.random.random(),-(b - (b-a)/160)*np.random.random()], k=1)[0]
    return choices(population=[a,b], weights=[-a,-b], k=1)[0]

# one = 0
# ten = 0
# n = 17000
# for _ in range(n):
#     if do_thing(4,10) == 4:
#         one += 1
#     else:
#         ten += 1
# print(one, ten)
# # print(do_thing(8,10))
# exit()

# teams = list(range(1, 17))
# teams = [[x, 17-x] for x in teams]
# teams = teams[:len(teams)//2]

# print(teams)
idx = 0
while idx < 1000:
    r = 0
    teams = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]*4
    tmp = []
    out = []
    while len(teams) > 1:
        tmp = []
        for i in range(0, len(teams), 2):
            a, b = teams[i], teams[i+1]
            tmp.append(do_thing(min(a,b), max(a,b)))
        teams = tmp
        if r == 0:
            if teams[-3] != 3:
                # print('wi0')
                break
        if r == 1:
            if teams[-2] != 3:
                # print('wi1')
                break
        if r > 1:
            if teams[-1] != 3:
                # print(f'wi{r}')
                break
        out.append('\n'.join(str(x) for x in teams) + '\n')
        if len(teams) == 1:
            print('\n'.join(out))
            exit()
        # print('\n'.join(str(x) for x in teams))
        # print()
        r += 1
    idx += 1
    # break



# import string 
# from os.path import expanduser
# home = expanduser("~")
# import sys
# sys.path.insert(0, f'{home}/GitHub/random-email/')
# from names import get_name

# num_names = 8
# l1 = [get_name()[0].title() for i in range(num_names)]
# while len(l1) != len(set(l1)):
#     l1 = [get_name()[0].title() for i in range(num_names)]
# print(sorted(l1))

import random
from pprint import pprint

def available(person, options):
    return sorted([x[0] for x in list(options.items()) if x[0] != person and x[0] not in options.values()])

# l1 = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff', 'gggg', 'hhhh']
count = 20
num_chains = 0
runs = 100
for _ in range(runs):
    l1 = list(range(0, count))
    options = {x:None for x in l1}
    for i, x in enumerate(l1):
        remainder = available(x, options)
        chosen = random.choice(remainder)
        options[x] = chosen

    d = {x:options[x] for x in options}
    chains = []
    l = []
    start = list(d.keys())[0]
    while d:
        # print(l, chains)
        if start in d:
            l.append(start)
            tmp = d[start]
            d.pop(start)
            start = tmp
        else:
            chains.append(l)
            l = []
            start = list(d.keys())[0]
    if l:
        chains.append(l)
    # print(options)
    # print(chains)
    num_chains += len(chains)
print(num_chains/runs)
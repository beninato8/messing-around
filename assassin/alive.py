def cyclic_permutations(lst):
    yield lst
    for k in range(1, len(lst)):
        p = lst[k:] + lst[:k]
        if p == lst:
            break
        yield p

with open('alive.people', 'r') as f:
    chains = f.read().split('\n')

outcomes = cyclic_permutations(chains)

for x in outcomes:
    print(' -> '.join(x))
    print()
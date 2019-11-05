from random import randint, choice
# n = randint(0,255)
# print(n)
# s = f'{n:x}'
# print(s)

def h(n=1):
    s = ''
    for i in range(n):
        s += choice('0123456789abcdef')
    return s

size = 6
l = [h(n=2) for i in range(size)]
s = ':'.join(l)

print(s)
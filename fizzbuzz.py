import sys

args = sys.argv
big = 100

if len(args) > 1 and args[1].isdigit():
    big = int(args[1])

for i in range(1, big+1):
    out = ''
    if i % 3 == 0:
        out += 'fizz'
    if i % 5 == 0:
        out += 'buzz'
    if len(out) == 0:
        out = i
    print(i, out)

# print("%s\n" % x for x in [])
print('\n'.join(['Fizz'*(x % 3 == 2) + 'Buzz'*(x % 5 == 4) or str(x + 1) for x in range(100)]))

# first, *mid, mid2, last = [1,2,3,4,5,6,7]
# print(first, mid, mid2, last)

print(False*'asdf' or 8)
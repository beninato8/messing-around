#!/usr/bin/env python3

import time
import random
import sys

def r():
    return str(random.randint(0, 9))

def pad(digits, size):
    padding = size - len(digits)
    return ''.join(digits) + ''.join([r() for i in range(padding)])

args = sys.argv
if len(args) > 1 and args[1].isdigit():
    code = list(args[1])
else:
    code = list('0123456789')
    code = list('123')
size = len(code)
digits = []
iterations = 10000 * size
step = iterations/size
last = 0
for i in range(iterations):
    if len(digits) < size and i % step == 0:
        digits.append(code[int(i//step)])
    last = pad(digits, size)
    print(last, end='\r')
print(last)
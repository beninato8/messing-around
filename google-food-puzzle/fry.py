'''
K = (C + iT)^3 - 191i
K = C^3 + (3C^2)(iT) + (3C)(iT)^2 + (iT)^3 - 191i
K = C^3 + (3C^2)(iT) + (3C)(-1)(T^2) + (-1)(i)(T^3) - 191i
K = C^3 - (3C)(T^2) + (3C^2)(iT) - (i)(T^3) - 191i
K = C^3 - (3C)(T^2) + ((3C^2)(T) - (T^3) - 191)(i)
'''

def zero(c, t):
    return 3*c*c*t - (t*t*t) - 191 == 0

for c in range(-1000, 1000):
    for t in range(-1000, 1000):
        if zero(c, t):
            print(c, t)

# c = 8, t = 1
# k = 488
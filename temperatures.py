def fToC(f):
    return (f - 32) / (9/5)

def cToF(c):
    return (c * (9/5)) + 32

def roundit(n):
    num = str(n).split('.')
    dec = num[-1][0]
    if int(dec) >= 5:
        return float(str(num[0])+'.5')
    return float(num[0]+'.0')

def rFtoC(f):
    return roundit(fToC(f))

for i in range(40, 80):
    print(str(i) + 'ºF => ' + str(rFtoC(i)) + 'ºC')

path = './log/'
name = 'test.txt'
s = ''

while True:
    with open(path + name) as f:
        txt = f.read()
        l1 = len(s)
        l2 = len(txt)
        if l1 != l2:
            print(txt[len(s):], end='')
            s = txt
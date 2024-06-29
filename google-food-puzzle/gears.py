def forward(l):
    return [l[-1]] + l[:-1]

def backward(l):
    return l[1:] + [l[0]]

level = [8,9,10,11,12,13,14,15,16,0,1,2,3,4,5,6,7]
gear1 = list('abcdehlmnopst')
gear2 = list('taeuoshrdln')
gear3 = list('saemotn')
gear4 = list('elfta')

for step in range(100000000):
    level = backward(level)
    gear1 = forward(gear1)
    gear2 = backward(gear2)
    gear3 = forward(gear3)
    gear4 = backward(gear4)

    if gear1[0] == 'd':
        if gear2[0] == 'o':
            if gear3[0] == 'o':
                if gear4[0] == 'f':
                    print('food')
                    print(level)
                    print(step)
                    exit()


with open('ranking.txt', 'r') as f:
    colleges = f.read().split('\n')
colleges2 = []
for x in colleges:
    tmp = x.split(' ')
    colleges2.append([' '.join(tmp[:-1]), int(tmp[-1])])
colleges = colleges2
print(colleges)

while len(colleges) > 1:
    tmp = []
    for i in range(0, len(colleges), 2):
        if colleges[i][1] < colleges[i+1][1]:
            tmp.append(colleges[i])
        else:
            tmp.append(colleges[i+1])
    colleges = tmp
    print('\n'.join(x[0] for x in colleges))
    print()

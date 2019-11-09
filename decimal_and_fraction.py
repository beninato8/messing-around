mydict = {}
num = 30

for i in range(num):
    for j in range(1, i):
        if j/i not in mydict:
            mydict[j/i] = ["%s/%s" % (j, i)]
        else:
            mydict[j/i] = mydict[j/i] + ["%s/%s" % (j, i)]

for key in sorted(mydict):
    print("%s: %s" % (format(key, '.5f'), mydict[key]))

# print('%s' % float('%.g' % 0.2))
# print(format(key, '.5f'))
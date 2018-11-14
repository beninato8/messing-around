import time


# start = time.time()
# biglist = []
# with open('seniorbig.txt') as big:
#     for line in big:
#         biglist.append(line)
# smalllist = []
# with open('seniorsmall.txt') as small:
#     for line in small:
#         smalllist.append(line)

# for e in biglist:
#     if e not in smalllist:
#         print(e)
# print(time.time() - start)

start = time.time()
smalllist = []
with open('seniorsmall.txt') as small:
    for line in small:
        smalllist.append(line)
with open('seniorbig.txt') as small:
    for line in small:
        if line not in smalllist:
            print(line[:-1])

print(time.time() - start)
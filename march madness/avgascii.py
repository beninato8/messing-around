import sys
import numpy as np

args = sys.argv
if len(args) == 1:
    exit()
args = args[1:]
print(args)
avgall = []
nums = {}
for team in args:
    avg = []
    for c in team:
        avg.append(ord(c))
    nums[team] = np.mean(avg)
    avgall.append(np.mean(avg))

totalavg = np.mean(avgall)
for team in args:
    nums[team] = abs(nums[team] - totalavg)

for i, k in enumerate(nums):
    print(i, k, nums[k])
    if i % 2 == 1:
        print()
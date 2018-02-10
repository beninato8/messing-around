import numpy as np

arr = np.random.rand(3,3,3)*100
arr2 = np.ndarray.flatten(arr)
print(arr2)
print(max(arr2))

tmp = []
for i in range(1000):
    tmp.append(max(np.ndarray.flatten(np.random.rand(3,3,3)*100)))

print(min(tmp))
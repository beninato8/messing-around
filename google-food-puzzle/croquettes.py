def get_num(x):
    digits = list(str(x))
    digits = digits + ['0' for _ in range(4 - len(digits))]
    d1 = int(''.join(sorted(digits)[::-1]))
    d2 = int(''.join(sorted(digits)))
    d1, d2 = sorted([d1, d2])
    return d2 - d1

# output = set()
# for x in range(0, 10000):
#     prev = x
#     curr = x
#     print(x)
#     while True:
#         prev = curr
#         curr = get_num(curr)
#         print(f'    {curr}')
#         if prev == curr:
#             output.add(prev)
#             break

# print(len(output))
# print(output)

out2 = set()

for x in range(0, 10000):
    if get_num(x) == x:
        out2.add(x)

print(len(out2))
print(out2)
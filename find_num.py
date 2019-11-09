import string

def index_recursive(n, l, small, big, step):
    print((n, small, big, step))
    if small == big:
        return -1
    if l[small] == n:
        return small
    if l[big] == n:
        return big
    if l[small] < n:
        return index_recursive(n, l, small+step, big, step*2)
    if l[small] > n:
        return index_recursive(n, l, small-step//2, small, 1)

def index_of(n, l):
    print(l)
    if len(l) > 0:
        return index_recursive(n, l, 0, len(l)-1, 1)
    return -1

l = list(range(0, 11, 2))
l = list(string.ascii_lowercase)
n = 'c'
print(index_of(n, l))
import sys
max = 1111111111

def update(i, x):
    while i <= n:
        tree[i] = min(tree[i], x)
        i += (i & -i)

def update2(i, x):
    while i > 0:
        tree2[i] = min(tree2[i], x)
        i -= (i & -i)

def query(a, b):
    v = max
    prev = a
    curr = prev + (prev & -prev)
    while curr <= b:
        v = min(v, tree2[prev])
        prev = curr
        curr = prev + (prev & -prev)

    v = min(v, arr[prev])
    prev = b
    curr = prev - (prev & -prev)
    while curr >= a:
        v = min(v, tree[prev])
        prev = curr
        curr = prev - (prev & -prev)
    return v

n, m = map(int, sys.stdin.readline().split())
arr = [0] * (n + 1)
tree = [max] * (n + 2)
tree2 = [max] * (n + 2)

for i in range(1, n + 1):
    arr[i] = int(sys.stdin.readline())
    update(i, arr[i])
    update2(i, arr[i])

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(query(a, b))
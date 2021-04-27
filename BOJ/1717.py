import sys
input = sys.stdin.readline

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

def find(c):
    if(parent[c] == c): return c
    parent[c] = find(parent[c])
    return parent[c]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa

for i in range(m):
    flag, a, b = map(int,input().split())
    if flag == 0 :
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
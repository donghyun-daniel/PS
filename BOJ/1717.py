import sys

def find(v):
    if where[v]==v:
        return v
    else:
        where[v]=find(where[v])
        return find(where[v])

N,M=map(int, sys.stdin.readline().split())
where=[i for i in range(N+1)]
for _ in range(M):
    op, a, b = map(int, sys.stdin.readline().split())
    if op==0:
        if find(a)!=find(b):
            where[find(a)]=b
    elif op==1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
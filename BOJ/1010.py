import sys
input=sys.stdin.readline

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    r = min(r, n - r)  # take advantage of symmetry
    c = 1
    for i in range(r):
        c = c * (n - i) // (i + 1)
    return c

T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    print(nCr(M,N))

from itertools import combinations
import sys
from collections import deque
input=sys.stdin.readline

n, m = map(int, input().split())
arr = []
L=[]
virusList = []
d=[[1,0],[-1,0],[0,1],[0,-1]]

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            L.append([i,j])
        if arr[i][j]==2:
            virusList.append([i,j])

def safearea(arr):
    sum=0
    for i in arr:
        sum+=i.count(0)
    return sum

def spread(x, y):
    q = deque([[x, y]])
    while q:
        [a, b] = q.popleft()
        for [nr,nc] in d:
            r = a + nr
            c = b + nc
            if 0 <= r < n and 0 <= c < m and cp[r][c] == 0:
                cp[r][c]=2
                q.append([r,c])

max=0
for (r1,c1),(r2,c2),(r3,c3) in list(combinations(L,3)):
    cp=[arr[i][:] for i in range(n)] #deepcopy보다 빠르다
    cp[r1][c1],cp[r2][c2],cp[r3][c3]=1,1,1
    for x,y in virusList:
        spread(x,y)
    safe=safearea(cp)
    if max<safe:
        max=safe
print(max)
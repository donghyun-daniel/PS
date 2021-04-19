import sys
import heapq

def prim(v):
    q = []
    mst[v] = 1
    result = 0
    for i in adj[v]:
        heapq.heappush(q, i)

    while q:
        c, v = heapq.heappop(q)
        if not mst[v]:
            mst[v] = 1
            result += c
            for j in adj[v]:
                heapq.heappush(q, j)
        if sum(mst) == N:
            return result

input = sys.stdin.readline
N = int(input())
M = int(input())

adj = [[] for _ in range(N + 1)]
mst = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append([c, b])
    adj[b].append([c, a])

print(prim(1))
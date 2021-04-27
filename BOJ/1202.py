import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
info = []
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(info, (M, V))

bag = sorted([int(input()) for _ in range(K)])
ans = 0
tmp = []
for i in bag:
    while info and info[0][0] <= i:
        heapq.heappush(tmp, -heapq.heappop(info)[1])
    if tmp:
        ans -= heapq.heappop(tmp)
print(ans)
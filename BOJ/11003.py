from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
nums = list(map(int, input().split()))
q = deque([])

for i in range(N):
    while q and q[0][0] <= i - L:
        q.popleft()
    while q and q[-1][1] >= nums[i]:
        q.pop()
    q.append((i, nums[i]))
    print(q[0][1], end = ' ')
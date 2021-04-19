import sys
from collections import deque
input = sys.stdin.readline

M, N = list(map(int, input().split()))
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))

def bfs(box):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    v = set([])
    q = deque([])

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append([i, j])
    cnt = 0

    while q:
        nowr, nowc = q.popleft()
        v.add((nowr, nowc))
        for dr, dc in d:
            newr, newc = nowr + dr, nowc + dc
            if 0 <= newr < N and 0 <= newc < M and box[newr][newc] == 0:
                q.append([newr, newc])
                box[newr][newc] = box[nowr][nowc] + 1

    ans = 0
    for i in box:
        if 0 in i:
            return -1
        tmp_max = max(i)
        if ans <= tmp_max:
            ans = tmp_max
    return ans - 1

print(bfs(box))
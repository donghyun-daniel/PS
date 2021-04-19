import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))
adj = [[] for _ in range(n)]
v = [False for _ in range(n)]

for _ in range(int(input())):
    p, c = list(map(int, input().split()))
    adj[p - 1].append(c - 1)
    adj[c - 1].append(p - 1)

def bfs(q1, q2):
    cnt = 0
    q = deque([[q1, cnt]])
    while q:
        now, cnt = q.popleft()
        if now == q2:
            return cnt
        if not v[now]:
            cnt += 1
            v[now] = True
            for cand in adj[now]:
                if not v[cand]:
                    q.append([cand, cnt])
    return -1

print(bfs(target[0] - 1, target[1] - 1))

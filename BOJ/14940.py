from sys import stdin, stdout
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
                q.append((nx, ny))
                a[nx][ny] = a[x][y]+1

for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            q.append((i, j))
            break

bfs()
for i in range(n):
    for j in range(m):
        d = a[i][j]
        if d:
            print(d-2, end=' ')
        else:
            print(0, end=' ')
    print()
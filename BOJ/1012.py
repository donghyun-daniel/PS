import sys
input=sys.stdin.readline

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [[x,y]]
    while queue:
        a, b = queue[-1][0], queue[-1][1]
        del queue[-1]
        for i in range(4):
            r = a + dx[i]
            c = b + dy[i]
            if 0 <= r < n and 0 <= c < m and s[r][c] == 1:
                s[r][c] = 0
                queue.append([r, c])

for i in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1
    for r in range(n):
        for c in range(m):
            if s[r][c] == 1:
                bfs(r, c)
                s[r][c] = 0
                cnt += 1
    print(cnt)
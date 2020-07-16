import sys
from collections import deque
input=sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([[x,y]])
    while queue:
        [a, b] = queue.popleft()
        for i in range(4):
            r = a + dx[i]
            c = b + dy[i]
            if 0 <= r < N and 0 <= c < M and maze[r][c]=="1":
                maze[r][c] = int(maze[a][b])+1
                queue.append([r, c])

N,M = map(int, input().split())
maze=[list(input())[:-1]]
for i in range(N-1):
    maze.append(list(input())[:-1])
bfs(0,0)
print(maze[-1][-1])
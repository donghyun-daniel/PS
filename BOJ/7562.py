import sys
from collections import deque
input = sys.stdin.readline

def bfs(f:list, t:list):
    d = [(-1, -2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, 1), (2, -1), (-1, 2)]
    q = deque([])
    q.append(f)
    while q:
        now = q.popleft()
        if now == t:
            return board[now[0]][now[1]]
        for dr, dc in d:
            nr, nc = dr + now[0], dc + now[1]
            if 0 <= nr < len(board) and 0 <= nc < len(board) and board[nr][nc] == 0:
                board[nr][nc] = board[now[0]][now[1]] + 1
                q.append((nr, nc))
    return board[t[0]][t[1]]

for _ in range(int(input())):
    I = int(input())
    board = [[0 for _ in range(I)] for _ in range(I)]
    f = list(map(int, input().split()))
    t = list(map(int, input().split()))
    print(bfs(f, t))
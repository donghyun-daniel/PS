from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def air(board, N, M):
    chk = False
    q = deque([[0, 0]])
    v = set([])
    while q:
        now = q.popleft()
        for dr, dc in dir:
            newr, newc = now[0] + dr, now[1] + dc
            if 0 <= newr < N and 0 <= newc < M and board[newr][newc] > 0:
                board[newr][newc] += 1
            elif 0 <= newr < N and 0 <= newc < M and board[newr][newc] == 0 and (newr, newc) not in v:
                q.append([newr, newc])
                v.add((newr, newc))

    for i in range(N):
        for j in range(M):
            if board[i][j] >= 3:
                board[i][j] = 0
            elif board[i][j] != 0:
                board[i][j] = 1
                chk = True

    return board, chk

cnt = 0
while True:
    cnt += 1
    board, chk = air(board, N, M)
    if not chk:
        print(cnt)
        break




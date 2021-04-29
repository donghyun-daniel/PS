import sys
from collections import deque
input = sys.stdin.readline

def Cleaner_Pos(board):
    for r in range(len(board)):
        for c in range(len(row)):
            if board[r][c] == -1:
                return (r, c), (r + 1, c)

def air(board, r, c):
    afterBoard = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] > 4:
                spreadAmount = board[i][j] // 5
                cnt = 0
                for x, y in zip(dx, dy):
                    nx = j + x
                    ny = i + y
                    if nx < 0 or nx >= c or ny < 0 or ny >= r or board[ny][nx] == -1:
                        continue
                    afterBoard[ny][nx] += spreadAmount
                    cnt += 1
                afterBoard[i][j] += (board[i][j] - (spreadAmount * cnt))
            else:
                afterBoard[i][j] += board[i][j]
    return afterBoard

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

upWind, downWind = Cleaner_Pos(board)
for i in range(t):
    board = airSpread(board, r, c)
    workingAirCleaner(board, r, c, upWind[0], upWind[1], 0, 1)
    workingAirCleaner(board, r, c, downWind[0], downWind[1], 0, -1)
ans = 0
for row in board:
    for item in row:
        ans += item
print(ans+2)
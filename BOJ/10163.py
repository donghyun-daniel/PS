import sys
input = sys.stdin.readline

N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
for num in range(N):
    *pos, w, h = map(int, input().split())
    for i in range(pos[0], pos[0] + w):
        for j in range(pos[1], pos[1] + h):
            board[i][j] = num + 1
color = [0 for _ in range(N)]
for row in board:
    for element in row:
        if element > 0:
            color[element - 1] += 1
for c in color:
    print(c)
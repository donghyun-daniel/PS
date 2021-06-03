R, C, M = map(int, input().split())
board = [[[] for _ in range(C)] for _ in range(R)]
dir = {1 : (-1, 0), 2 : (1, 0), 3 : (0, 1), 4: (0, -1)}

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1].append([s, dir[d], z]) # False is for check move fin or not

fisher = 0
ans = 0

def move_fish(board, R, C):
    new_board = [[[] for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            print(board[r][c])
            for k in range(len(board[r][c])):
                new_R = r + board[r][c][k][1][0] * board[r][c][k][0]
                new_C = c + board[r][c][k][1][1] * board[r][c][k][0]
                new_R = r - (new_R % R) if new_R // R % 2 == 1 else new_R % R
                new_C = c - (new_C % C) if new_C // C % 2 == 1 else new_C % C
                new_board[new_R][new_C].append(board[r][c][k])
                new_board[new_R][new_C] = sorted(new_board[new_R][new_C], key = lambda x : x[2])[-1]
    return new_board

while fisher < C:
    for i in board:
        print(i)
    for i in range(R): # catch fish
        if len(board[i][fisher]) == 3:
            ans += board[i][fisher][2]
            board[i][fisher] = []
    board = move_fish(board, R, C)
    fisher += 1

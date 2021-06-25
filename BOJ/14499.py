N, M, r, c, K = map(int, input().split())
board = []
dice = [0 for _ in range(6)]
for _ in range(N):
    board.append(list(map(int, input().split())))

def move(dice, move):
    if move == 1: # 동
        return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif move == 2: # 서
        return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif move == 3 : # 북
        return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif move == 4 : # 남
        return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

op = list(map(int, input().split()))
dir = {1 : [0, 1], 2 : [0, -1], 3 : [-1, 0], 4: [1, 0]}
for o in op:
    r += dir[o][0]
    c += dir[o][1]
    if 0 <= r < N and 0 <= c < M:
        dice = move(dice, o)
        if board[r][c] == 0:
            board[r][c] = dice[5]
        else:
            dice[5] = board[r][c]
            board[r][c] = 0
        print(dice[0])
    else:
        r -= dir[o][0]
        c -= dir[o][1]
        continue
board = [list(map(int, input().split())) for _ in range(int(input()))]

dp_max = [[0 for _ in range(3)] for _ in range(2)]
dp_max[0] = board[0]
dp_min = [[99999999 for _ in range(3)] for _ in range(2)]
dp_min[0] = board[0]

for row in range(0, len(board) - 1):
    for now in range(3):
        for d in range(-1, 2):
            if 0 <= now + d < 3:
                dp_max[(row + 1) % 2][now + d] = max(dp_max[row % 2][now])
                    max(dp_max[row % 2][now] + board[row + 1][now + d], dp_max[(row + 1) % 2][now + d])
                dp_min[(row + 1) % 2][now + d] = \
                    min(dp_min[row % 2][now] + board[row + 1][now + d], dp_min[(row + 1) % 2][now + d])
                print("max", dp_max)
                print("min", dp_min)

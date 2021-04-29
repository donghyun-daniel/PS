N = int(input())
board = [[0] * 101 for _ in range(101)]

dc = (0, -1, 0, 1)
dr = (1, 0, -1, 0)

for _ in range(N):
    c, r, d, g = map(int, input().split())
    arr = [(r, c), (r+dc[d], c+dr[d])]
    board[r][c] = 1
    board[r+dc[d]][c+dr[d]] = 1
    for gen in range(g):
        tmp_arr = []
        tc, tr = arr[-1][0], arr[-1][1]
        for ttc, ttr in arr[len(arr)-2::-1]:
            nx = tc - (tr - ttr)
            ny = tr + (tc - ttc)
            if not(0 <= nx <= 100 and 0 <= ny <= 100):
                break
            board[nx][ny] = 1
            tmp_arr.append((nx, ny))
        arr += tmp_arr
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            cnt += 1
print(cnt)
def solution(maps, p, r):
    N = len(maps)
    ans = [0]
    for tmp_r in range(N - 1):
        for tmp_c in range(N - 1):
            tmp_result = 0
            tr, tc = tmp_r + 0.5, tmp_c + 0.5
            inner = []
            outer = []
            for i in range(int(tr) - r//2 + 1, int(tr) + r//2 + 1):
                for j in range(int(tc) - r//2 + 1, int(tc) + r//2 + 1):
                    for k in range(1, r//2): # inner area
                        if 0 <= i < N and 0 <= j < N and \
                                int(abs(tr - i) + abs(tc - j)) == k and maps[i][j] <= p:
                            tmp_result += 1
                    k = r // 2  # boundary
                    if 0 <= i < N and 0 <= j < N and \
                            int(abs(tr - i) + abs(tc - j)) == k and maps[i][j] <= p/2:
                        tmp_result += 1
            ans.append(tmp_result)

    return max(ans)


maps = [[9, 8, 17, 55, 19, 7], [1, 25, 5, 39, 28, 8], [88, 19, 28, 3, 2, 9], [76, 73, 7, 18, 16, 14], [99, 8, 8, 7, 11, 9], [1, 18, 4, 10, 3, 6]]
p = 16
r = 4
print(solution(maps, p, r))
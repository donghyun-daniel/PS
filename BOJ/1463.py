N=int(input())
dp=[0, 0, 1, 1]
while len(dp) <= N:
    pos = len(dp)
    cand = [dp[pos - 1] + 1]
    if pos % 3 == 0:
        cand.append(dp[pos // 3] + 1)
    if pos % 2 == 0:
        cand.append(dp[pos // 2] + 1)
    dp.append(min(cand))
print(dp[N])
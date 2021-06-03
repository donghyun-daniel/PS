N = int(input())
dp = [0 for _ in range(N + 1)]
tp = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 1, -1 , -1):
    if i + tp[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(tp[i][1] + dp[i + tp[i][0]], dp[i + 1])
    print(dp)
print(dp[0])
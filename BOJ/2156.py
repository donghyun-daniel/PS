import sys
input = sys.stdin.readline

n = int(input())
wine = [0]
for i in range(n):
    wine.append(int(input()))

dp = [[0, 0, 0] for i in range(n + 1)]
dp[1] = [0, wine[1], 0]
for i in range(2, n + 1):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + wine[i]
    dp[i][2] = dp[i - 1][1] + wine[i]
print(max(dp[n]))
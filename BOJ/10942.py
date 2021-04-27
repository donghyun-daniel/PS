import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1 # 1자리 펠린드롬
    if i < N - 1 and nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1 # 2자리 펠린드롬

# 3자리 이상 펠린드롬
for i in range(2, N):
    for j in range(N - i):
        if nums[j] == nums[j + i] and dp[j + 1][j + i - 1]: # 양 끝같고, 하나씩 안쪽 조회해보면 펠린드롬
            dp[j][j + i] = 1

for _ in range(int(input())):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])
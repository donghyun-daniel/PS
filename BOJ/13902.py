N, M = map(int, input().split())
s = list(map(int, input().split()))
can = set(s)
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] + s[j] <= N:
            can.add(s[i] + s[j])
can = sorted(can)
dp = [11111 for i in range(N+1)]
dp[0] = 0
for i in range(1, N+1):
    for j in can:
        if i - j < 0:
            break
        dp[i] = min(dp[i], dp[i - j] + 1)
if dp[N] >= 11111:
    print(-1)
else:
    print(dp[N])
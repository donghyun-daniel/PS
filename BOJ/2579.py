N = int(input())
s = [int(input()) for i in range(N)]
if N<3:
    if N==1:
        print(s[0])
    elif N==2:
        print(s[0]+s[1])
else:
    dp = [s[0]]
    dp.append(s[0]+s[1])
    dp.append(max(dp[0] + s[2], s[1] + s[2]))
    for i in range(3, N):
        dp.append(max(s[i] + s[i - 1] + dp[i - 3], s[i] + dp[i - 2]))
    print(dp[-1])
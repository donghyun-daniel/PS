N=int(input())
dp=[-1,-1,-1,1,-1,1]
i=6
while i<=N:
    if dp[i-5]!=-1:
        dp.append(dp[i-5]+1)
    elif dp[i-3]!=-1:
        dp.append(dp[i-3]+1)
    else:
        dp.append(-1)
    i+=1
print(dp[N])
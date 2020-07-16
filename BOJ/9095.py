import sys
input = sys.stdin.readline
t = int(input())
dp=[0,1,2,4]
for i in range(0, t):
    a = int(input())
    if len(dp)>a:
        print(dp[a])
    else:
        for j in range(a-len(dp)+1):
            dp.append(dp[-1]+dp[-2]+dp[-3])
        print(dp[-1])
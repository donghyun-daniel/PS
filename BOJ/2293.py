n,k=map(int,input().split())
coin=[]
dp=[0]*(k+1)
for _ in range(n):
    coin.append(int(input()))

for i in coin:
    if i<=k:
        dp[i]+=1
    else:
        continue
    j=i
    while j<=k:
        dp[j]+=dp[j-i]
        j+=1

print(dp[k])
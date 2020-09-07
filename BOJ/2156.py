cup=[]
for _ in range(int(input())):
    cup.append(int(input()))
dp=[0 for i in range(len(cup))]
for i in range(len(dp)):
    dp[i]=max(cup[i])
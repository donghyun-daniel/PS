R,C=map(int,input().split())
num=R*C//5+1
L=[1,2,2,1,2]*num
index=0
L2=[]
for i in range(R):
    L2.append(L[index:index+C])
    index+=C
del L
v=[]
target=[1,2,2,1,2]
cnt=0

def dfs(r,c,now, now2):
    global cnt
    v.append((r,c))
    if len(now)<5 and L2[r][c]==target[len(now)]:
        now.append([r,c])
        now2.append(L2[r][c])
        if now2==target:
            cnt+=1
        if r>0 and (r-1, c) not in v: #Up
            dfs(r-1,c,now,now2)
        if r+1<len(L2) and (r+1,c) not in v: #Down
            dfs(r+1,c, now,now2)
        if c>0 and (r, c-1) not in v: #Left
            dfs(r,c-1,now,now2)
        if c+1<len(L2[0]) and (r,c+1) not in v: #Right
            dfs(r,c+1,now,now2)
        del now[-1], now2[-1]
    del v[-1]

for i in range(R):
    for j in range(C):
        if L2[i][j]==1:
            dfs(i,j,[],[])
print(cnt)
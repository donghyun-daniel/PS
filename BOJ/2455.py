now,max=0,10000
ans=0
for i in range(4):
    off,on=map(int,input().split())
    now=now-off+on
    if now>ans:
        ans=now
print(ans)
N,K=map(int,input().split())
l=[i+1 for i in range(N)]
ans=[]
num=0
for i in range(N):
    num+=K-1
    if num>=len(l):
        num=num%len(l)
    ans.append(str(l.pop(num)))
print(f"<{', '.join(ans)}>")
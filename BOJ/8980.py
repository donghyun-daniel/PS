N,C=map(int,input().split())
M=int(input())
T=[0 for i in range(N)]
ans=0
info=[]
for _ in range(M):
    info.append(list(map(int,input().split())))
info=sorted(info, key=lambda x:(x[1]-x[0], x[0]))
for [f,t,n] in info:
    if max(T[f-1:t-1])+n<=C:
        val=n
    else:
        val=C-max(T[f-1:t-1])
    for i in range(f-1, t-1):
        T[i]+=val
    ans+=val
print(ans)
N=int(input())
P=[]
for i in range(N):
    P.append(list(map(int,input().split())))
for i in range(N):
    rank=1
    for j in range(N):
        if i!=j:
            if P[i][0]<P[j][0] and P[i][1]<P[j][1]:
                rank+=1
    print(f"{rank} ", end='')
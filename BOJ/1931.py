N=int(input())
C=[]
for i in range(N):
    C.append(list(map(int, input().split())))
C=sorted(C, key=lambda C: (C[1], C[0]))

cnt,start=0,0
for i in C:
    if i[0]>=start:
        cnt+=1
        start=i[1]
print(cnt)
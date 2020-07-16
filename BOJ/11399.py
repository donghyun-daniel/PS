N=int(input())
P=list(map(int,input().split()))
P=sorted(P)
sum=P[0]
for i in range(1,len(P)):
    P[i]=P[i-1]+P[i]
    sum+=P[i]
print(sum)
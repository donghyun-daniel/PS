C=list(map(int,input().split()))
C[1]*=2; C[2]*=3
car=[0 for i in range(100)]
for i in range(3):
    S,E=map(int,input().split())
    for j in range(S,E):
        car[j-1]+=1
cost=0
for i in range(99):
    if car[i]!=0:
        cost+=C[car[i]-1]
print(cost)
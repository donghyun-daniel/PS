N=int(input())
L=list(map(int,input().split()))
L2=[L[0]]
for i in range(len(L)-1):
    L2.append(max(L2[i]+L[i+1], L[i+1]))
print(max(L2))
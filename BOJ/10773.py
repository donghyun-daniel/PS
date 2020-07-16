import sys
input = sys.stdin.readline
K=int(input())
N=[]
for _ in range(K):
    tmp=int(input())
    if tmp!=0:
        N.append(tmp)
    else:
        del N[-1]

sum=0
for i in N:
    sum+=i
print(sum)
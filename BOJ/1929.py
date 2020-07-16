import math

M,N=map(int,input().split())
limit=int(math.sqrt(N))
num=[True for i in range(N+2)]
num[0],num[1]=False,False

start=2
while start<=limit:
    for i in range(2*start, N+1, start):
        num[i]=False
    start+=1
    while not num[start]:
        start+=1

for i in range(M, len(num)):
    if num[i]:
        print(i)
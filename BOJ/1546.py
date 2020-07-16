N=int(input())
S=list(map(int,input().split()))
max=0
for i in S:
    if max<i:
        max=i
avg=0
for i in S:
    avg+=((i/max)*100)
print(round(avg/N,3))
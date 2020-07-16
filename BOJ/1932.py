import sys
input=sys.stdin.readline

n=int(input())
prev=list(map(int,input().split()))
now=[]

def sum(i):
    now[i]+=max(prev[i], prev[i+1])

for i in range(n-1):
    prev=[0]+prev+[0]
    now=list(map(int,input().split()))
    for j in range(len(now)):
        sum(j)
    prev=now
print(max(now))
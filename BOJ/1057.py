N,A,B=map(int,input().split())
A,B,cnt=A-1,B-1,0
while A!=B:
    A,B,cnt=A//2,B//2,cnt+1
print(cnt)
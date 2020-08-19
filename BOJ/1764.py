import sys
input=sys.stdin.readline
N,M=map(int,input().split())
A,B=set(),set()
for i in range(N):
    A.add(input())
for j in range(M):
    B.add(input())
ans = sorted(A&B)
print(len(ans))
for i in ans:
    print(i, end='')
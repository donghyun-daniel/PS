import sys
input=sys.stdin.readline

N,M=map(int,input().split())
minP,minE=1111,1111
for _ in range(M):
    P,E=map(int,input().split())
    minP=min(minP,P)
    minE=min(minE,E)
print(min(minP*(N//6)+minE*(N%6), minP*(N//6+1), minE*N))
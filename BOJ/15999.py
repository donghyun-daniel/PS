import sys
input=sys.stdin.readline
A,B=map(int,input().split())
s=[list(input()) for i in range(A)]
d=[[1,0],[-1,0],[0,1],[0,-1]]
cnt=0
for i in range(A):
    for j in range(B):
        for k in d:
            r=i+k[0]
            c=j+k[1]
            if 0<=r<A and 0<=c<B:
                if s[r][c]!=s[i][j]:
                    cnt+=1
                    break
print(pow(2,(A*B-cnt))%1000000007)
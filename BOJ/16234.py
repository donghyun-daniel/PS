import sys

N,L,R=map(int,input().split())
C=[]
for _ in range(N):
    C.append(list(map(int,input().split())))
G=[[C[0][0], C[0][0], 0]]
G_i=[[[0,0]]]
def check_dif(A,B):
    if L<=abs(A-B) and abs(A-B)<=R:
        return True
    else:
        return False

def adj(r,c):
    ans=[]
    if r-1>=0:
        ans.append([r-1,c])
    if r+1>=0:
        ans.append([r+1,c])
    if c-1>=0:
        ans.append([r,c-1])
    if c+1<N:
        ans.append([r,c+1])
    return ans

G[0][0]=1
for i in range(N):
    for j in range(N):
        cand=adj(i,j)
        for [r,c] in cand:
            if G[r][c]!=G[i][j]:
                pass


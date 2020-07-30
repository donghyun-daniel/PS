import sys
sys.setrecursionlimit(10000)

N,L,R=map(int,input().split())
C=[]
for _ in range(N):
    C.append(list(map(int,input().split())))

def check_dif(A,B):
    if L<=abs(A-B)<=R:
        return True
    else:
        return False

def immigrate(rc, snc):
    people=snc[0]//snc[1]
    for r,c in rc:
        C[r][c]=people
    if len(rc)>1:
        return True
    else: return False

def DFS(r,c):
    chk[r][c]=False
    q=[[r,c]]
    dir=[[1,0],[-1,0],[0,1],[0,-1]]
    while q:
        nowr,nowc=q.pop()
        for dx,dy in dir:
            newr,newc=nowr+dx,nowc+dy
            if 0<=newr<N and 0<=newc<N and chk[newr][newc] and check_dif(C[nowr][nowc],C[newr][newc]):
                sumandcnt[0]+=C[newr][newc]
                sumandcnt[1]+=1
                rc.append([newr,newc])
                DFS(newr,newc)

cnt=0
stop=False
while not stop:
    chk = [[True for i in range(N)] for i in range(N)]
    stop=True
    for i in range(N):
        for j in range(N):
            if chk[i][j]:
                sumandcnt=[C[i][j],1]
                rc=[[i,j]]
                DFS(i,j)
                if immigrate(rc,sumandcnt):
                    stop=False
    if not stop:
        cnt+=1
print(cnt)
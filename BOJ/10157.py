C,R=map(int,input().split())
K=int(input())
nowR,nowC=0,1
RL,CL=R,C-1
ans=0
if K>R*C:
    print(0)
else:
    while K>=0:
        nowR,nowC,K,RL,ans=nowR+RL,nowC,K-RL,RL-1,1
        if K <= 0: break
        nowR,nowC,K,CL,ans=nowR,nowC+CL,K-CL,CL-1,2
        if K <= 0: break
        nowR,nowC,K,RL,ans=nowR-RL,nowC,K-RL,RL-1,3
        if K <= 0: break
        nowR,nowC,K,CL,ans=nowR,nowC-CL,K-CL,CL-1,4
        if K <= 0: break
    if ans==1: nowR+=K
    elif ans==2: nowC+=K
    elif ans==3: nowR-=K
    elif ans==4: nowC-=K
    print(nowC,nowR)
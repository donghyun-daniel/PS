T=int(input())
for _ in range(T):
    H,W,N=map(int,input().split())
    stair=str((N-1)%H+1)
    ho=str((N-1)//H+1).zfill(2)
    print(stair+ho)
N,M,K=map(int,input().split())
team_max=min(N//2,M)
N-=team_max*2
M-=team_max
K=max(K-M-N, 0)
print(team_max-((K+2)//3))
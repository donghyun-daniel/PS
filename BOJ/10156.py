K,N,M=map(int,input().split())
cost=K*N-M
if cost<0:
    print(0)
else:
    print(cost)
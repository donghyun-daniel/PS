import itertools
N,M=map(int,input().split())
L=[[i for i in range(M)],[j for j in range(N)]]
itertools.combinations(list(itertools.product(*L)),3)
import itertools
N,M=map(int,input().split())
num=[str(i+1) for i in range(N)]
num=list(itertools.combinations_with_replacement(num, M))
for i in num:
    print(' '.join(i))
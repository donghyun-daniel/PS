import itertools
N,M=map(int,input().split())
num=[str(i+1) for i in range(N)]
num=list(itertools.product(num, repeat=M))
for i in num:
    print(' '.join(i))
import collections
N=int(input())
num=collections.deque([i for i in range(N,1,-1)])
if N==1:
    print(1)
else:
    while len(num)!=1:
        num.rotate(1)
        num.pop()
    print(num[0])
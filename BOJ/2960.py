N,K=map(int,input().split())
l=[False for i in range(2,N+1)]
while K:
    P=l.index(False)+2
    for i in range(P-2,len(l),P):
        if not l[i]:
            l[i]=True
            K -= 1
            if K==0:
                print(i+2)
    if K<=0:
        break
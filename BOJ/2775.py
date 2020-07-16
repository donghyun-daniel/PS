for _ in range(int(input())):
    k=int(input())
    n=int(input())
    apt = [i + 1 for i in range(n)]
    now=0
    while now<k:
        tmp=apt
        sum=1
        for i in range(1, n):
            sum+=tmp[i]
            apt[i]=sum
        now+=1
    print(apt[n-1])
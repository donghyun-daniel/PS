num=int(input())
N=list(map(int,input().split()))
if len(N)==1:
    print("A")
elif len(N)==2:
    if N[0]!=N[1]:
        print("A")
    else:
        print(N[0])
else:
    ans = True
    x=N[1]-N[0]
    y=N[2]-N[1]
    a=0
    b=0
    if x!=0:
        if int(y/x)!=y/x:
            ans=False
            print("B")
        else:
            a=y/x
    if ans:
        b = N[1] - a * N[0]
        for i in range(1,len(N)):
            if (N[i-1]*a+b)!=N[i]:
                ans=False
                print("B")
                break
    if ans:
        print(int(N[-1]*a+b))
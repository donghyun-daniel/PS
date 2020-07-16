N=int(input())
if N<2:
    print(1)
else:
    ans=1
    for i in range(2,N+1):
        ans*=i
    print(ans)
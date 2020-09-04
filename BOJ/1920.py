N=int(input())
A=sorted(list(map(int,input().split())))
M=int(input())
num=list(map(int,input().split()))
for target in num:
    low=0
    high=N-1
    mid=(low+high)//2
    while A[mid]!=target and low<high:
        if A[mid]>target:#target이 좌측에 있을 때
            high=mid-1
            mid=(high+low)//2
        elif A[mid]<target:#target이 우측에 있을 때
            low=mid+1
            mid=(high+low)//2
    if A[mid]==target:
        print(1)
    else:
        print(0)
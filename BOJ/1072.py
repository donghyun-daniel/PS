X,Y = map(int,input().split())
win = int(Y*100/X)
target=win+1
if win>=99:
    print(-1)
else:
    low,high=0,1000000000
    mid=(low+high)//2
    min=mid
    while low<mid<high:
        if int((Y+mid)/(X+mid)*100)>=target:
            high = mid
            mid = (low+high)//2
        else:
            low = mid
            mid = (low+high)//2
    for i in range(low,high+1):
        if int((Y+i)*100/(X+i))>=target:
            print(i)
            break
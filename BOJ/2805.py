def cut(low,mid,high,M):
    ans = []
    while low!=mid and mid!=high:
        sum = 0
        for height in T:
            if height>mid:
                sum+=height-mid
        if M>sum:
            high=mid
            mid=(low+high)//2
        elif M<=sum:
            ans = mid
            low=mid
            mid=(low+high)//2
    return ans

N,M=map(int,input().split())
T=sorted(list(map(int,input().split())))
print(cut(0,T[-1]//2,T[-1],M))
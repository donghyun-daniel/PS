def get_cost(land,P,Q,target,N):
    cost=0
    for i in range(N):
        for j in range(N):
            diff=target-land[i][j]
            if diff>0:
                cost+=P*diff
            else:
                cost-=Q*diff
    return cost


def solution(land, P, Q):
    N=len(land)
    min_v,max_v=1111111111,0
    for row in land:
        if min(row) < min_v:
            min_v = min(row)
        if max(row) > max_v:
            max_v = max(row)
    mid=(min_v+max_v)//2
    while min_v<mid<max_v:
        l=get_cost(land,P,Q,mid-1,N)
        h=get_cost(land,P,Q,mid+1,N)
        if l<h:
            max_v=mid
        else:
            min_v=mid
        mid = (min_v + max_v) // 2
    ans=[get_cost(land,P,Q,mid,N),get_cost(land,P,Q,mid-1,N),get_cost(land,P,Q,mid+1,N)]

    return min(ans)

land=[[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]]
P=5
Q=3
print(solution(land,P,Q))
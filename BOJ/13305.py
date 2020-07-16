import sys

N=int(sys.stdin.readline())
dist=list(map(int, sys.stdin.readline().split()))
cost=list(map(int, sys.stdin.readline().split()))
i=1
min=cost[0]
total=min*dist[0]
while i<N-1:
    new_cost = cost[i]
    if min<new_cost:
        total+=min*dist[i]
    else:
        total+=new_cost*dist[i]
        min=new_cost
    i+=1
print(total)
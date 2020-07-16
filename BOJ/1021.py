import collections
n,m=map(int,input().split())
idk=list(map(int,input().split()))
total=0
que=collections.deque(list(map(int,range(1,n+1))))

for i in range(len(idk)):
    ins=idk[i]
    if ins==que[0]:
        que.popleft()
    else:
        index = que.index(ins)
        min = -index if index<len(que)-index else len(que)-index
        que.rotate(min)
        total+=abs(min)
        que.popleft()
print(total)
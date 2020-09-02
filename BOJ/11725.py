from collections import deque

N=int(input())
dic = {i+1 : [] for i in range(N)}
visit = [False for i in range(N+1)]
parent = {i+2 : False for i in range(N-1)}
for i in range(N-1):
    A,B=map(int,input().split())
    dic[A].append(B)
    dic[B].append(A)
print(dic)

def bfs(v):
    q = deque([v])
    visit[v] = False
    while q:
        v = q.popleft()
        for i in dic[v]:
            if not visit[i]:
                visit[i]=True
                q.append(i)

bfs(1)


import sys
input=sys.stdin.readline
N, M = map(int, input().split())
order = []
S = [[] for i in range(N + 1)]
indegree = [0 for i in range(N + 1)]
q = []
result = []

for i in range(M): #순서 쌍으로 입력
    order.append(list(map(int, input().split())))

for [i, j] in order: #들어오는 간선 수 count
    S[i].append(j)
    indegree[j] += 1

for i in range(1, len(indegree)):
    if indegree[i]==0:
        q.append(i)

while q:
    for i in q:
        temp = i
        q.remove(i)
        result.append(temp)
        for j in S[temp]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)

for i in result:
    print(i, end=' ')
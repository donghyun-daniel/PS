N = int(input())

graph = [[0 for c in range(N)] for r in range(N)]

for i in range(N):
    for j, k in enumerate(map(int, input().split())):
        graph[i][j] = k

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for i in range(0, N):
    print(' '.join(list(map(str, graph[i]))))
L = []
N, M = map(int, input().split(' '))
for i in range(N):
    L.append(list(map(int, input())))

MAX = min(N, M)
max = 0
for i in range(N):
    for j in range(M):
        for k in range(MAX):
            if i + k < N and j + k < M:
                if L[i][j] == L[i][j + k] and L[i][j] == L[i + k][j] and L[i][j] == L[i + k][j + k]:
                    if max < k:
                        max = k
print((max + 1) * (max + 1))
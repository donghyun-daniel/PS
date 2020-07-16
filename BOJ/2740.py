import sys
input=sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

result = []
tmp = 0
tmp_l = []
for i in range(N):
    for j in range(K):
        for k in range(M):
            tmp += A[i][k] * B[k][j]
        tmp_l.append(tmp)
        tmp = 0
    result.append(tmp_l)
    tmp_l = []

for l in result:
    for p in l:
        print(p, end=' ')
    print()
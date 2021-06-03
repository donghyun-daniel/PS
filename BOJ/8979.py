import sys
input = sys.stdin.readline
N, K = map(int, input().split())
country, target = [], []
for _ in range(N):
    idx, *medal = list(map(int, input().split()))
    tmp = medal[0] * 1111111 * 111111 + medal[1] * 111111 + medal[2]
    country.append([tmp, idx])
    if idx == K:
        target = tmp
country = sorted(country, key = lambda x : (-x[0]))
print([row[0] for row in country].index(target) + 1)
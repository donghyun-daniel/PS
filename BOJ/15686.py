from itertools import combinations
N, M = map(int, input().split())
town = []
chicken = []
house = []
for r in range(N):
    tmp = list(map(int, input().split()))
    for c, v in enumerate(tmp):
        if v == 2:
            chicken.append([r, c])
        elif v == 1:
            house.append([r, c])
house = sorted(house, key = lambda x : (x[0], x[1]))

ans = 999999
for tmp in list(combinations(chicken, M)):
    cand = []
    for i in house:
        min = 999
        for t in tmp:
            dist_tmp = abs(i[0] - t[0]) + abs(i[1] - t[1])
            if dist_tmp < min:
                min = dist_tmp
        cand.append(min)
    ans_tmp = sum(cand)
    if ans_tmp < ans:
        ans = ans_tmp
print(ans)
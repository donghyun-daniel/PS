import sys
input = sys.stdin.readline

N, C = map(int, input().split())
pos = sorted([int(input()) for _ in range(N)])
if C == 2:
    print(pos[-1] - pos[0])
else:
    result = 0
    l, r = 1, pos[-1] - pos[0]
    while l <= r:
        m = (l + r) // 2
        cnt = 1
        now = pos[0]
        for i in range(1, len(pos)):
            if pos[i] >= now + m:
                now = pos[i]
                cnt += 1
        if cnt >= C:
            l = m + 1
            result = m
        else:
            r = m - 1
    print(result)
import sys
input = sys.stdin.readline
testcase = int(input())

for _ in range(testcase):
    n = int(input())
    choice = [0] + list(map(int, input().split()))
    visit = [0 for _ in range(n+1)]
    group = 1

    for i in range(1, n+1):
        if visit[i] == 0:
            while visit[i] == 0:
                visit[i] = group
                i = choice[i]
            while visit[i] == group:
                visit[i] = -1
                i = choice[i]
            group += 1
    cnt = 0

    for v in visit:
        if v > 0:
            cnt += 1
    print(cnt)
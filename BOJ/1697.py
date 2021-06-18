from collections import deque

N, K = map(int, input().split())
MAX = 111111
time = [0 for _ in range(MAX)]
d = deque([N])
while d:
    now = d.popleft()
    if now == K:
        print(time[now])
        break
    for i in [now-1, now+1, now*2]:
        if 0 <= i < MAX and time[i] == 0:
            time[i] = time[now] + 1
            d.append(i)
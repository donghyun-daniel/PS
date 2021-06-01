from collections import deque

def solution(t, r):
    ans = []
    l = deque([])
    time = set([])
    ans = []
    for tmp_t, tmp_r, idx in zip(t, r, range(len(t))):
        l.append([tmp_t, tmp_r, idx])
        time.add(tmp_t)
    l = deque(sorted(l, key = lambda x : (x[0], x[1])))
    cand = deque([])
    time = 0
    while len(ans) < len(t):
        while l and l[0][0] <= time:
            cand.append(l.popleft())
        print(time, l, cand)
        if cand:
            cand = deque(sorted(cand, key=lambda x: x[1]))
            ans.append(cand.popleft()[2])
        time += 1
    return ans

t = [7,6,8,1]
r = [0,1,2,3]
print(solution(t, r))
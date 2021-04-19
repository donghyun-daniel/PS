import sys
from collections import deque
input = sys.stdin.readline

def solution(L, R, C):
    d = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    s, e = 0, 0
    bd = []
    for i in range(L):
        f = []
        for j in range(R):
            tmp_bd = list(input().strip())
            l = []
            for k in range(C):
                l.append(tmp_bd[k])
                if tmp_bd[k] == 'S':
                    s = (i, j, k)
                if tmp_bd[k] == 'E':
                    e = (i, j, k)
            f.append(l)
        bd.append(f)
        input()

    visited = set([])
    q = deque([])
    q.append(s)

    cnt = -1
    while q:
        l = len(q)
        cnt += 1
        for _ in range(l):
            z, y, x = q.popleft()
            if (z, y, x) == e:
                return f"Escaped in {cnt} minute(s)."

            for dz, dy, dx in d:
                if 0 <= x + dx < C and 0 <= y + dy < R and 0 <= z + dz < L:
                    if (z + dz, y + dy, x + dx) not in visited and (bd[z + dz][y + dy][x + dx] != "#"):
                        visited.add((z + dz, y + dy, x + dx))
                        q.append((z + dz, y + dy, x + dx))
    return "Trapped!"

while True:
    L, R, C = map(int, input().split())
    if L and R and C:
        print(solution(L, R, C))
    else:
        break

import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())
maps = []
for r in range(n):
    arr = list(map(int, input().split()))
    maps.append(arr)

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            start = (i, j, 0)


def find_min_dist(start, maps, current_size):
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    queue = deque()
    queue.append(start)

    r, c, cnt = start
    maps[r][c] = 0
    # min_dist (cnt, r, c) 형태로 저장
    min_dist = []
    visited = set()
    while queue:
        r, c, cnt = queue.popleft()
        visited.add((r, c))
        for dr, dc in dirs:
            ny, nx = r + dr, c + dc
            if 0 <= ny < len(maps) and 0 <= nx < len(maps) and (ny, nx) not in visited:
                visited.add((ny, nx))
                # 다음 칸으로 이동할 수 있는 경우
                if maps[ny][nx] == 0 or maps[ny][nx] == current_size:
                    queue.append((ny, nx, cnt + 1))
                    continue
                # 지나갈 수 없는 경우
                if maps[ny][nx] > current_size:
                    continue
                else:
                    # 먹을 수 있는 경우
                    heapq.heappush(min_dist, (cnt + 1, ny, nx))

    # 먹을 수 있는 후보군 중 조건에 부합하는 것
    if min_dist:
        return min_dist[0]
    else:
        return None


time = 0
current_size = 2
already_eat = 0
while True:
    next_value = find_min_dist(start, maps, current_size)
    if next_value is None:
        break
    cnt, ny, nx = next_value
    time += cnt

    already_eat += 1
    if already_eat == current_size:
        current_size += 1
        already_eat = 0

    start = (ny, nx, 0)

print(time)

from collections import deque

def bfs(start, end, dic, traps):
    ans = 100000000000
    q = deque([[start, 0, 0]]) # pos, total cost, roads num
    v = set([])
    v.add((start, 0))
    while q:
        now, tot, num = q.popleft()
        v.add((now, num))
        print(q, now, tot, num, v)
        if now in dic[num]:
            for dest, cost in dic[num][now]:
                if dest in traps and (dest, (num + 1) % 2) not in v:
                    q.append([dest, tot + cost, (num + 1) % 2])

                elif (dest, num) not in v:
                    q.append([dest, tot + cost, num])
                if dest == end and ans > tot + cost:
                    ans = tot + cost
    return ans



def solution(n, start, end, roads, traps):
    dic = []
    tmp_1, tmp_2 = {}, {}
    for b, e, s in roads:
        if b not in tmp_1:
            tmp_1[b] = []
        if e not in tmp_2:
            tmp_2[e] = []
        tmp_1[b].append([e, s])
        tmp_2[e].append([b, s])
    for i in tmp_1:
        tmp_1[i] = sorted(tmp_1[i], key = lambda x : x[1])
    for i in tmp_2:
        tmp_2[i] = sorted(tmp_2[i], key = lambda x : x[1])
    dic = [tmp_1, tmp_2]
    print(dic)
    return bfs(start, end, dic, traps)

n = 3
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
print(solution(n, start, end, roads, traps))
n = int(input())
l = [9] + list(map(int, input().split()))

for _ in range(int(input())):
    s, num = map(int, input().split())
    if s == 1: # 남
        while num <= n:
            l[num] = 0 if l[num] else 1
            num += num

    else: # 여
        cand = [num]
        for i in range(1, n//2):
            if 0 < num - i <= n and 0 < num + i <= n:
                if l[num - i] == l[num + i]:
                    cand.append(num - i)
                    cand.append(num + i)
                else:
                    break
            else:
                break

        for c in cand:
            l[c] = 0 if l[c] else 1

l = l[1:]
for i in range(0, len(l), 20):
    print(*l[i:i+20])
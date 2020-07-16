N, r, c = map(int, input().split())
num = 0
while N > 0:
    tmp = (2 ** N) // 2
    if N > 1:
        if tmp > r and tmp <= c:
            num += tmp ** 2
            c -= tmp
        elif tmp <= r and tmp > c:
            num += (tmp ** 2) * 2
            r -= tmp
        elif tmp <= r and tmp <= c:
            num += (tmp ** 2) * 3
            r, c = r - tmp, c - tmp
    elif N == 1:
        if r == 0 and c == 1: num += 1
        elif r == 1 and c == 0: num += 2
        elif r == 1 and c == 1: num += 3
    N -= 1
print(num)
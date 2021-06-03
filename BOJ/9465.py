for _ in range(int(input())):
    N = int(input())
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))
    for i in range(1, N):
        if i == 1:
            r1[i] += r2[i-1]
            r2[i] += r1[i-1]
        else:
            r1[i] += max(r2[i-1], r2[i-2])
            r2[i] += max(r1[i-1], r1[i-2])
    print(max([r1[-1], r2[-1]]))
def color(t, n, k, r, c):
    if t == 0:
        return '0'
    l = n ** (t-1)
    new_r, new_c = r // l, c // l
    if (n-k)//2 <= new_r < (n+k)//2 and (n-k)//2 <= new_c < (n+k)//2:
        return '1'
    return color(t-1, n, k, r%l, c%l)

s,N,K,R1,R2,C1,C2 = map(int, input().split())

for r in range(R1, R2+1):
    for c in range(C1, C2+1):
        print(color(s, N, K, r, c), end='')
    print()
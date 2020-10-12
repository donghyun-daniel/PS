N, S = map(int, input().split())
A = list(map(int, input().split()))
l, r, sum, result, t = 0, 0, A[0], 0, 0
while l <= r and r < N:
    if sum < S:
        r += 1
        if r < N:
            sum += A[r]
    elif sum >= S:
        t = r - l + 1
        if result == 0:
            result = t
        else:
            result = min(result, t)
        if l < r:
            sum -= A[l]
            l += 1
        else:
            r += 1
            if r < N:
                sum += A[r]
print(result)
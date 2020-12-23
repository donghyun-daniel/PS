N, K = map(int, input().split())
A = [str(i) for i in range(1, N + 1)]
idx = K - 1
ans = []
while A:
    ans.append(A.pop(idx))
    if len(A) == 0:
        break
    idx = (idx + K - 1) % len(A)
print("<" + ', '.join(ans) + ">")

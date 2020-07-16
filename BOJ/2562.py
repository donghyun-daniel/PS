N=[int(input())]
for _ in range(8):
    N.append(int(input()))
ans=max(N)
print(ans, N.index(ans)+1)
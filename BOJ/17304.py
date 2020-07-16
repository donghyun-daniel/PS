def rec(S):
    min=222222
    for i in S:
        if min>len(i):
            return min

N,M=map(int,input().split())
S=[[]for i in range(N)]

for i in range(0,M):
    a,b=map(int,input().split())
    S[b-1].append(a-1)

print(S)

for i in S:
    if len(i)==0: #변호받을 사람이 아예 없는 사람이 존재할 때
        print("NO")
        break

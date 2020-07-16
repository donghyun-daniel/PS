from itertools import combinations

def sum(l):
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return sum

N,M=map(int,input().split())
card=list(map(int,input().split()))
cand=list(combinations(card,3))
max=0
for i in range(len(cand)):
    s=sum(cand[i])
    if s>max and s<=M:
        max=s
        if s==M:
            break
print(max)
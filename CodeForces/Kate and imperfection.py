from itertools import combinations

def powerset(items):
    combo = []
    for r in range(len(items) + 1):
        #use a list to coerce a actual list from the combinations generator
        combo.append(list(combinations(items,r)))
    return combo

def gcd(a,b):
    a,b=max(a,b),min(a,b)
    while b>0:
        a,b=b,a%b
    return a

n=int(input())
S=[i+1 for i in range(n)]
p=powerset(S)
ans=[]

for i in range(n-1):
    #i+2개 선택한 걸 뽑아줘야함
    num=list(p[i+2])
    for i in range(len(num)):
        num[i] = list(num[i])
        while len(num[i])>=2:
            num[i][-2]=gcd(num[i][-1], num[i][-2])
            del num[i][-1]
    print(num)
    ans.append(min(num))
print(ans)

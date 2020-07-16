def arr_merge(l, cnt):
    i=0
    while i < (len(l)):
        if arr_sum(l[i:i+cnt]):
            l.append(l[i:i+cnt])
        i+=1
    del l[-1]
    return l

def arr_sum(l):
    sum=0
    for i in l:
        sum+=i
    if sum!=0:
        return True
    else:
        return False

t=int(input())
l=list(map(int, input().split()))
i=0
ans=0
while i<len(l):
    if l[i]==0:
        del l[i]
        i-=1
    i+=1
ans+=len(l)
arr_merge(l,2)
print(l)

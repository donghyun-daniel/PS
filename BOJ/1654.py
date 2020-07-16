def count(b,mid):
    cnt=0
    for i in range(len(b)):
        cnt+=b[i]//mid
    return cnt

k,n=map(int,input().split())
a=0
b=[]
for i in range(k):
    b.append(int(input()))

#초기 setting
start=1
end=(max(b))+1
mid=(start+end)//2
ans=[1]
while end-start!=1:
    cnt = count(b, mid)
    if cnt>=n:
        ans.append(mid)
        start=mid
        mid=(start+end)//2
    elif cnt<n:
        end=mid
        mid=(start+end)//2
print(max(ans))
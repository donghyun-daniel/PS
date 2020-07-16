def search(l1,l2,start):
    score=0
    for i in range(0, len(l2)):
        if start+i<len(l1):
            if (l1[start+i]=='R' and l2[i]=='P') or (l1[start+i]=='S' and l2[i]=='R') or (l1[start+i]=='P' and l2[i]=='S'):
                score+=1
    return score

N,M=map(int,input().split())
rsp=input()
my=list(input())
max=0
for i in range(0,N):
    p=search(rsp,my,i)
    if max<p:
        max=p
print(max)
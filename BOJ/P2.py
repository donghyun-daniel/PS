N=int(input())
num=[]
while N:
    tmp=1
    cnt=0
    while N>=tmp:
        tmp*=2
        cnt+=1
    tmp//=2
    cnt-=1
    num.append(pow(3,cnt))
    N-=tmp
print(sum(num))
def check(N):
    num=[]
    while N>0:
        num.append(N%10)
        N//=10
    d=num[0]-num[1]
    prev=num[1]
    for i in range(2,len(num)):
        if d!=prev-num[i]:
            return False
    return True

N=int(input())
if N<100:
    print(N)
else:
    sum=99
    for i in range(111,N+1):
        if check(i):
          sum+=1
    print(sum)
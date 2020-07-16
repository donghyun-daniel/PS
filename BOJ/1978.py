import math

def check_prime(n):
    limit=int(math.sqrt(n))
    if n==1:
        return False
    elif n==2 or n==3:
        return True
    for i in range(2, limit+1):
        if n%i==0:
            return False
    return True

N=int(input())
num=list(map(int,input().split()))
cnt=0
for i in num:
    if check_prime(i):
        cnt+=1
print(cnt)
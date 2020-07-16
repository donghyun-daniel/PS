import sys
import math

N,K=map(int,sys.stdin.readline().split())
doll=list(map(int,sys.stdin.readline().split()))
c_sum=[0, doll[0]]
c_exp_sum=[0, doll[0]*doll[0]]

for i in range(1, N):
    c_sum.append(c_sum[-1]+doll[i])
    c_exp_sum.append(c_exp_sum[-1]+(doll[i]*doll[i]))

if K==1:
    print(0)
else:
    min=100000000000000000000
    for a in range(K,N+1):
        for i in range(a,N+1):
            sum=c_sum[i]-c_sum[i-a]
            sqr_sum=c_exp_sum[i]-c_exp_sum[i-a]
            mean=sum/a
            dev=(sqr_sum+(a*mean*mean)-(2*mean*sum))/a
            if min>dev:
                min=dev

    print(format(math.sqrt(min), ".10f"))
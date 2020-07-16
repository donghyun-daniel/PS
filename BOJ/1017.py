n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

N=int(input())
num=list(map(int,input().split()))

ans=[]
start = num[0]
for i in range(1, len(num)):
    if start + num[i] in primes:
        ans.append(num[i])
print(ans)

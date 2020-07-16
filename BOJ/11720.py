N=int(input())
num=int(input())
ans=0
while num>0:
    ans+=num%10
    num//=10
print(ans)
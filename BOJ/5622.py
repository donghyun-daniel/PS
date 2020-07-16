S=input()
ans=0
N=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,8,8,8,8]
for i in S:
    num = (ord(i)-65)
    ans+=N[num]+2
print(ans)
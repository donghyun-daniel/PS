Q=input()
l=list(Q.split("-"))

for i in range(len(l)):
    l[i]=l[i].split("+")

for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] = l[i][j].lstrip("0")

for i in range(len(l)):
    sum=0
    for j in range(len(l[i])):
        sum+=eval(l[i][j])
    l[i]=sum

ans=l[0]

for i in range(1,len(l)):
    ans-=l[i]
print(ans)
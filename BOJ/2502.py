def get_coef(n):
    list=[[1,0],[0,1]]
    for i in range(3,n+1):
        a=list[i-3][0]+list[i-2][0]
        b=list[i-3][1]+list[i-2][1]
        list.append([a,b])
    return list[-1][0], list[-1][1]

D,K=map(int,input().split())
a,b=get_coef(D)
ans=False
for i in range(1,int(K/a)):
    for j in range(i+1,int(K/b)):
        if a*i+b*j==K:
            ans=True
            print(i)
            print(j)
            break
    if ans:
        break
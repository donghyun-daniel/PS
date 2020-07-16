import copy

def fin(l):
    sum=0
    for i in l:
        for j in i:
            sum+=j
    if sum==(len(l[0])*len(l[0])):
        return True
    else: return False

N,M=map(int,input().split())
friend=[[0 for i in range(0,N)] for i in range(0,N)]
for i in range(0,M):
    A,B=map(int,input().split())
    friend[A-1][B-1]=1
    friend[B-1][A-1]=1
for i in range(0,N):
    friend[i][i]=1
new=copy.deepcopy(friend)

day=0
ans=[]

while not fin(new):
    new_num=0
    for i in range(0,N):
        for j in range(0,N):
            if friend[i][j]:
                for k in range(0,N):
                    if friend[j][k]:
                        if friend[i][k]==0 and friend[k][i]==0 and new[i][k]==0 and new[k][i]==0:
                            new[i][k]=1
                            new[k][i]=1
                            new_num+=1
    friend=copy.deepcopy(new)
    day+=1
    ans.append(new_num)

print(day)
for i in ans:
    print(i)
import sys
input=sys.stdin.readline
num=[]
size=int(input())
for i in range(size):
    num.append(list(map(int,input().split())))
AB,CD={},{}
for i in range(size):
    for j in range(size):
        ans1=num[i][0]+num[j][1]
        if ans1 in AB:
            AB[ans1]+=1
        else:
            AB[ans1]=1
for i in range(size):
    for j in range(size):
        ans2 = num[i][2] + num[j][3]
        if ans2 in CD:
            CD[ans2]+=1
        else:
            CD[ans2]=1
ans=0
for i in AB.keys():
    CD_target=-1*i
    if CD_target in CD.keys():
        ans+=(AB[i]*CD[CD_target])
print(ans)
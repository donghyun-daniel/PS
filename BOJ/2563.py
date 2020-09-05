pos=[]
for i in range(int(input())):
    x,y=map(int,input().split())
    tmp=[[x,y],[x+10,y+10]]
    pos.append(tmp)
print(pos)
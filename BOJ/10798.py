str=[]
max=0
for _ in range(5):
    str.append(input())
    if max<len(str[-1]):
        max=len(str[-1])
index=0
while index<=max:
    for i in range(5):
        if len(str[i])>index:
            print(str[i][index], end='')
    index+=1
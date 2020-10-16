max, max_idx=0,0
for i in range(5):
    s=sum(list(map(int,input().split())))
    if max<s:
        max,max_idx=s,i+1
print(max_idx, max)
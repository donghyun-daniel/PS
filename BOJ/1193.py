N=int(input())
i=1
d=0
save=1
while N>=i:
    d+=1
    i+=d
    if i<=N:
        save=i
diff=N-save
if d%2==0:
    print(f"{1 + diff}/{d - diff}")
else:
    print(f"{d - diff}/{1 + diff}")
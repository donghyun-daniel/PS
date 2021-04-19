num=[]
for i in range(7):
    n=int(input())
    if n%2==1:
        num.append(n)
if num:
    print(sum(num))
    print(min(num))
else:
    print(-1)
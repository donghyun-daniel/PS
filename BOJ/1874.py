import sys
input = sys.stdin.readline

N=int(input())
new=int(input())
ans=[]
ans_bool=True
num=[i+1 for i in range(new-1)]
chk=new+1
for _ in range(new):
    ans.append("+")
ans.append("-")
for _ in range(N-1):
    new = int(input())
    if new >= chk:
        while chk<=new:
            num.append(chk)
            chk+=1
            ans.append("+")
    if new==num[-1]:
        ans.append("-")
        del num[-1]
    else:
        ans_bool=False
        break
if ans_bool:
    for i in ans:
        print(i)
else:
    print("NO")
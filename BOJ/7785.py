import sys
input=sys.stdin.readline
L={}
for _ in range(int(input())):
    name,check=input().split()
    if check=="enter":
        L[name]=True
    else:
        del L[name]
for i in sorted(L,reverse=True):
    print(i)
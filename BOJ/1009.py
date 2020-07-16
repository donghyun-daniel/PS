import sys
input=sys.stdin.readline

cycle=[1,1,4,4,2,1,1,4,4,2]

for _ in range(int(input())):
    a,b=map(int,input().split())
    a%=10
    result=a
    for i in range((b-1)%cycle[a]):
        result*=a
        result%=10
    if result==0:
        print(10)
    else: print(result)
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    N=list(map(int,input().split()))
    avg=sum(N[1:])/N[0]
    cnt=0
    for chk in N[1:]:
        if chk>avg:
            cnt+=1
    print(f"{cnt/N[0]*100:.3f}%")
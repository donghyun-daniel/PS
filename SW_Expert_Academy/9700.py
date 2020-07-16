import sys
input = sys.stdin.readline
TC=int(input())
for cnt in range(TC):
    p,q=map(float, input().split())
    a=(1-p)*q
    b=p*(1-q)*q
    print(f"#{cnt+1} ", end='')
    if a<b: print("YES")
    else: print("NO")

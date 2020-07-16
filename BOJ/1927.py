import heapq
import sys
input=sys.stdin.readline
N=int(input())
H=[]
for _ in range(N):
    tmp = int(input())
    if tmp==0:
        if len(H)==0:
            print("0")
        else:
            print(heapq.heappop(H))
    else:
        heapq.heappush(H, tmp)
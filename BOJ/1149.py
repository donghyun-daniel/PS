import sys
input=sys.stdin.readline
N=int(input())
RGB=list(map(int,input().split()))
for i in range(1,N):
    tmp = list(map(int,input().split()))
    R=tmp[0]+min(RGB[1], RGB[2])
    G=tmp[1]+min(RGB[0], RGB[2])
    B=tmp[2]+min(RGB[0], RGB[1])
    RGB=[R,G,B]
print(min(RGB))
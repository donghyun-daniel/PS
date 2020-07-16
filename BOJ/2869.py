import math
A,B,V = map(int, input().split())
V-=B
move=A-B
ans=V/move
print(math.ceil(ans))
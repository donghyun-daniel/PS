import math
N,K=map(int, input().split())
num=[[0, 0] for i in range(6)]
for i in range(N):
    S,G=map(int, input().split())
    num[G-1][S]+=1
room=0
for i in num:
    for j in i:
        room += math.ceil(j/K)
print(room)
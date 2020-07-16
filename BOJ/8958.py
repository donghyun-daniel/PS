import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    Q=input()
    score=0
    s=0
    for i in Q:
        if i=="O":
            s+=1
            score+=s
        else:
            s=0
    print(score)
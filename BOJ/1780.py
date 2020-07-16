import sys

def rec(l,s_x, s_y, n, ans):
    if check(l, s_x, s_y, n):
        ans[l[s_x][s_y]]+=1
    else: #divide to 9 pieces
        for i in range(3):
            for j in range(3):
                rec(l, s_x+(i*n//3), s_y+(j*n//3),n//3, ans)

def check(l, s_x, s_y, n):
    val=l[s_x][s_y]
    for i in range(n):
        for j in range(n):
            if val != l[s_x+i][s_y+j]:
                return False
    return True

N=int(sys.stdin.readline())
P=[]
ans=[0,0,0] #0, 1, -1 cnt
for i in range(N):
    P.append(list(map(int, sys.stdin.readline().split())))
rec(P,0,0,N,ans)
print(ans[-1])
print(ans[0])
print(ans[1])
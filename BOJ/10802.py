import time

def max_369_digit(N):
    L = reversed(str(N))
    for i in range(len(L)):
        L.find('3')
        if L[i]=='3' or L[i]=='6' or L[i]=='9':
            return 10**i
    return False, 1

F,T=map(int,input().split())
now=F
cnt=0
while now<=T:
    d = max_369_digit(now)
    if d>1:
        cnt+=d
        now+=d
    else:
        if now%3==0:
            cnt+=1
        now+=d
    print(now-1, cnt, d)
    time.sleep(1)
if now>T:
    cnt-=now-T
print(cnt)
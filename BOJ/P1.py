def solution(P):
    P=list(str(P))
    P=list(map(int,P))
    P[-1]+=1
    prev=P[0]
    chk = False
    while not chk:
        chk=True
        for i in range(len(P)-1,0,-1):
            if P[i] in P[:i]:
                P[i]+=1
                chk=False
                break
        for i in range(len(P)):
            if P[i] == 10:
                P[i - 1] += 1
                P[i] = 0
    ans="".join(map(str, P))
    return ans
P=2015
print(solution(P))

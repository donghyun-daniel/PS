def solution(p):
    ans=[0 for i in range(len(p))]
    stk=[[0,p[0]]]
    for i in range(1,len(p)):
        if p[i] < stk[-1][1]:
            while stk and stk[-1][1]>p[i]:
                tmp=stk.pop()
                ans[tmp[0]]=i-tmp[0]
        stk.append([i, p[i]])
    for [idx, v] in stk:
        ans[idx]+=len(p)-1-idx
    return ans

solution([5, 1, 3, 2, 4, 5])
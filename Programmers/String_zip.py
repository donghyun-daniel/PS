from collections import deque

def solution(s):
    ans=0
    for stk_size in range(1,len(s)//2+1):
        stk = deque([])
        for j in s:
            if stk_size*2<=len(stk):
                stk.popleft()
            stk.append(j)
            print(stk)
            print(stk[:])


            print(stk_size, stk)
    return ans

solution("ababcdcdababcdcd")
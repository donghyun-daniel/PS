def solution(total_sp, skills):
    ans = []
    S=[0 for i in range(len(skills)+1)]
    son=[[] for i in range(len(skills)+1)]
    parent=[False for i in range(len(skills)+1)]
    chk=[False for i in range(len(skills)+1)]
    for a,b in skills:
        a,b=a-1,b-1
        print(son, parent, S)
        if parent[b]==False:
            parent[b]=[]
        parent[b].append(a)
        son[a].append(b)
        if son[b]==[]:
            S[b]=1
        rec_add_parents(parent,S,b)
    return ans

def rec_add_parents(parent,S,n):
    if parent[n]!=False:
        for i in range(len(parent[n])):
            print(i)
            S[parent[n][i]]+=S[n]
            rec_add_parents(parent,S,parent[n][i])



total_sp=121
skills=[[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]
solution(total_sp,skills)
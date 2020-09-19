from itertools import combinations

def solution(num):
    ans=set([])
    for i in list(combinations(num,2)):
        ans.add(sum(i))
    return sorted(list(ans))

num=[5,0,2,7]
solution(num)
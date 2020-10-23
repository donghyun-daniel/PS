def solution(words, queries):
    q={}
    w_idx=1
    check=True
    while check:
        check=False
        for i in range(len(words)):
            if w_idx<=len(words[i]):
                check=True
                s=words[i][:w_idx] + "?" * (len(words[i]) - w_idx)
                if s not in q:
                    q[s]=[i]
                else:
                    q[s]+=[i]
        for i in reversed(range(len(words))):
            if w_idx<=len(words[i]):
                check=True
                s="?" * (len(words[i]) - w_idx) + words[i][len(words[i])-w_idx:]
                if s not in q:
                    q[s]=[i]
                else:
                    q[s]+=[i]
        w_idx+=1
    ans=[]
    for i in queries:
        if i in q:
            ans+=[len(q[i])]
        else:
            ans+=[0]
    return ans

words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

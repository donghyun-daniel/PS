def check(s):
    l = set()
    prev=s[0]
    for i in range(1,len(s)):
        if prev!=s[i]:
            l.add(prev)
            prev=s[i]
        if prev in l:
            return False
    return True

N=int(input())
cnt=0
for _ in range(N):
    str = input()
    if check(str):
        cnt+=1
print(cnt)
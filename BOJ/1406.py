s=input()
cursor=len(s)
for _ in range(int(input())):
    *param = input().split()
    print(param[0], param)
    if param[0]=='L':
        cursor=cursor-1 if cursor>0 else 0
    elif param[0]=='D':
        cursor=cursor+1 if cursor<len(s) else len(s)
    elif param[0]=='B':
        if cursor>0:
            del s[cursor-1]
    else:
        s+=param[1]
    print(s)

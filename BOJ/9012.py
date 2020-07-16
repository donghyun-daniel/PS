N=int(input())
for i in range(N):
    str=list(input())
    open, close= 0,0
    ans=True
    for j in range(len(str)):
        if str[j]=="(":
            open+=1
        elif str[j]==")":
            close+=1
        if open<close:
            print("NO")
            ans=False
            break
    if ans and open==close:
        print("YES")
    elif ans and open!=close:
        print("NO")
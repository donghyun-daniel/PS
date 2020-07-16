t=int(input())
for i in range(t):
    r,c=map(int,input().split())
    str=[]
    for j in range(r*c):
        if j%2==0:
            str.append("B")
        else:
            if j==r*c-1:
                str.append("B")
            else:
                str.append("W")
    for a in range(r):
        print("".join(str[a*c:a*c+c]))
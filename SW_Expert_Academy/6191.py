def ok(n, N):
    n=bin(n)[2:].zfill(2*N)
    if n.count("1")==n.count("0"):
        cnt_z, cnt_o = 0, 0
        for i in range(2*N):
            if n[i]=="0":
                cnt_z+=1
            else:
                cnt_o+=1
            if cnt_z<cnt_o:
                return False
        return n
    return False

TC=int(input())
for tc in range(TC):
    print(f"#{tc+1} ", end='')
    N,K = map(int, input().split())
    val, d = 0, 1
    for i in range(N):
        val+=d
        d*=2
    start=val
    max=pow(2,N*2)-1-start
    cnt=0
    ans=False
    for i in range(start,max+1):
        num=ok(i,N)
        if num:
            cnt+=1
        if cnt==K:
            ans=True
            cnt=num
            break
    if not ans:
        print(")(")
    else:
        for i in num:
            if i=="0":
                print("(", end='')
            else:
                print(")", end='')
        print()
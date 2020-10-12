N=int(input())
request=sorted(list(map(int,input().split())))
M=int(input())
if sum(request)<=M:
    print(request[-1])
else:
    l, h = 1, request[-1]
    m = (l + h) // 2
    while l<m<h:
        tmp=M
        for i in request:
            tmp -= m if i >= m else i
        if tmp<0:
            h=m
            m = (l + h) // 2
        else:
            l=m
            m = (l + h) // 2
    print(m)
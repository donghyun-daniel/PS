def solution(n):
    l = [[0] * (i+1) for i in range(n)]
    x, y = -1, 0
    val = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            l[x][y] = val
            val += 1
    ans=[]
    for i in l:
        ans+=i
    return ans

solution(4)
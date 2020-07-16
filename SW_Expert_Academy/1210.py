for _ in range(10):
    N = int(input())
    print(f"#{N} ", end='')
    L=[]
    for _ in range(100):
        tmp = list(map(int, input().split()))
        tmp.insert(0,0)
        tmp.append(0)
        L.append(tmp)

    col = L[-1].index(2)

    for row in range(99, -1, -1):
        if L[row][col - 1]:
            while L[row][col - 1]:
                col -= 1
        elif L[row][col + 1]:
            while L[row][col + 1]:
                col += 1
    print(col-1)
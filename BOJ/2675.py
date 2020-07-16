T=int(input())
for i in range(T):
    R,S=input().split()
    R=int(R)
    S=list(S)
    for i in S:
        for j in range(R):
            print(i, end='')
    print()
for _ in range(int(input())):
    print("Distances:", end=" ")
    A,B=input().split()
    for i in range(len(A)):
        c=ord(B[i])-ord(A[i])
        if c<0:
            c+=26
        print(c, end=" ")
    print()
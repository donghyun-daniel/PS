L1=list(map(int,input().split()))
L2=list(map(int,input().split()))

if L1[0] == L2[2] or L1[2] == L2[0]:
    if L1[1] == L2[3] or L1[3] == L2[1] : print("POINT")
    elif (L1[3] - L1[1]) + (L2[3] - L2[1]) > max(L2[3] - L1[1], L1[3] - L2[1]): print("LINE")
    else: print("NULL")

elif (L1[2] - L1[0])+(L2[2] - L2[0]) > max(L2[2]-L1[0], L1[2]-L2[0]):
    if L1[1] == L2[3] or L1[3] == L2[1]: print("LINE")
    elif (L1[3] - L1[1]) + (L2[3] - L2[1]) > max(L2[3] - L1[1], L1[3] - L2[1]): print("FACE")
    else: print("NULL")

else: print("NULL")
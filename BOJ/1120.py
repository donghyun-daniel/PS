A,B=input().split()
min=len(B)
for i in range(len(B)-len(A)+1):
    dist=0
    for j in range(len(A)):
        if A[j]!=B[j+i]:
            dist+=1
    if min>dist:
        min=dist
print(min)
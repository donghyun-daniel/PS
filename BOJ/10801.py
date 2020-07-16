A=list(map(int, input().split()))
B=list(map(int, input().split()))
Awin,Bwin=0,0
for i in range(10):
    Awin += A[i] > B[i]
    Bwin += B[i] > A[i]
str="A" if Awin>Bwin else ("B" if Bwin>Awin else "D")
print(str)
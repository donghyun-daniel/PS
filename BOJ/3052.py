C=[0]*42
for _ in range(10):
    N=int(input())
    C[N%42]+=1
print(42-C.count(0))
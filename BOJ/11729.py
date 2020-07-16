N=int(input())
sum=0

def rec(N,a,b,c):
    if N==1:
        print(a,c)
    else:
        rec(N-1,a,c,b)
        print(a,c)
        rec(N-1,b,a,c)

print(2**N-1)
rec(N,1,2,3)
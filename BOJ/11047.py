N,K=map(int,input().split())
A=[]
cnt=0
for _ in range(N):
    A.append(int(input()))
for i in reversed(A):
    cnt += K // i
    K%=i
print(cnt)
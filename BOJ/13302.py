N,M=map(int,input().split())
ban=list(map(int,input().split()))
vacation=[True for i in range(N)]
for i in ban:
    vacation[i-1]=False
print(vacation)
dp=[[0,0,0,0] for i in range(N+1)] #1,3,5일,쿠폰수
for i in range(1,len(dp)):
    if 0<i-5<len(dp):
        pass


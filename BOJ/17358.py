N=int(input())
ans=[1,3] #2개, 4개 일 경우 가짓 수
p=5
for i in range(0,int((N-4)/2)):
    ans.append(p*ans[-1]%1000000007)
    p+=2
if N==2:
    print(1)
else:
    print(ans[-1])
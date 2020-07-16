N=int(input())
num=[0,0,1,1]
while len(num)<=N:
    cand=[]
    if (len(num)%3==0 and num[len(num)//3]!=0):
        cand.append(num[len(num)//3]+1)
    if (len(num)%2==0 and num[len(num)//2]!=0):
        cand.append(num[len(num)//2]+1)
    if num[len(num)-1]!=0:
        cand.append(num[len(num)-1]+1)
    num.append(min(cand))
print(num[N])
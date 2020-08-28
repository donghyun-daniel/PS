n=int(input())
stack=[]
ngf=['-1']*n
nums=list(map(int,input().split()))
cnt=[0]*(max(nums)+1)
for i in nums:
    cnt[i]+=1
for i in range(n):
    while stack and cnt[nums[stack[-1]]]<cnt[nums[i]]:
        ngf[stack.pop()]=str(nums[i])
    stack.append(i)
print(' '.join(ngf))
N = int(input())
nums = list(map(int, input().split()))
stk = []
ans = [-1 for _ in range(N)]

for i, v in enumerate(nums):
    while stk and nums[stk[-1]] < nums[i]:
        ans[stk.pop()] = nums[i]
    stk.append(i)

print(' '.join(list(map(str, ans))))
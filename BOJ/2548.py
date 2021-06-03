N = int(input())
nums = sorted(list(map(int, input().split())))
set_num = set(nums)
ans = []
for n in set_num:
    ans.append([n, sum([abs(i - n) for i in nums])])
print(sorted(ans, key = lambda x : x[1])[0][0])
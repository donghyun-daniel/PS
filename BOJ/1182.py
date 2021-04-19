from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

def chk(nums, S):
    ans = 0
    for i in range(1, len(nums) + 1):
        for l in list(combinations(nums, i)):
            if sum(l) == S:
                ans += 1
    return ans

print(chk(nums, S))

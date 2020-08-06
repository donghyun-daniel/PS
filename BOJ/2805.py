N,M = map(int,input().split())
tree = list(map(int,input().split()))

def treeSum(M):
    sum = 0
    for height in tree:
        if height>M:
            sum+=(height-M)
    return sum

def cut(target):
    start,end=0,max(tree)
    ans = 0
    while start<=end:
        mid = (start+end)//2
        sum = treeSum(mid)
        if sum < target :
            end = mid -1
        if sum >= target:
            ans = mid
            start = mid + 1
    return ans

print(cut(M))
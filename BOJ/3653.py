#not fin..... fail...

def update(index, value, array, bi_tree):
    while index < len(array):
        bi_tree[index] += value
        index += index & -index

def get_sum(index, bi_tree):
    ans = 0
    while index > 0:
        ans += bi_tree[index]
        index -= index & -index
    return ans

def get_range_sum(left, right, bi_tree):
    ans = get_sum(right, bi_tree) - get_sum(left - 1, bi_tree)
    return ans

import sys
input=sys.stdin.readline

test=int(input())
for i in range(test):
    n,m=map(int,input().split())
    movie=list(map(int,input().split()))
    floor=[n-i+1 in range(n)] #dvd 아래에 쌓인 dvd 갯수
    floor.insert(0,0)
    bit = [0 for i in range(n + 1)]
    for index in range(1, n+1):
        update(index, floor[index], floor, bit)
    for j in movie:
        print(n-get_range_sum(0,floor[j]))
    l, r = map(int, input('Enter the left and right indices for the range sum: ').split())
    print(get_range_sum(l, r, bit))
    #update(index, new_val - arr[index], arr, bit)

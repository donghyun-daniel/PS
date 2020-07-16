int(input())
a=list(map(int,input().split()))
int(input())
b=list(map(int,input().split()))
a.sort()

def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True # 찾고 True Return
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return False

for i in b:
    if binary_search(i,a):
        print("1 ", end='')
    else:
        print("0 ", end='')

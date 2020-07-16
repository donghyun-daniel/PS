import sys
input = sys.stdin.readline

T = int(input())

arr = [0] * 100
arr[:8] = [1,1,1,2,2,3,4,5]

for i in range(8, 100):
    arr[i] = arr[i - 2] + arr[i - 3]

for _ in range(T):
    N = int(input())
    print(arr[N - 1])
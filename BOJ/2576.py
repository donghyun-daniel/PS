num = list(filter(lambda x : x % 2 == 1, [int(input()) for i in range(7)]))
if num:
    print(sum(num))
    print(min(num))
else:
    print(-1)
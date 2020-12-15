num=[int(input()) for i in range(7)]
num = list(filter(lambda x : x%2 == 1, num))
if num:
    print(sum(num))
    print(min(num))
else:
    print(-1)
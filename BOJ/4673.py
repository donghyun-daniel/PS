def selfnum(num):
    numstr=str(num)
    start = max(num - 9 * len(numstr), 0)
    for i in range(start, num):
        if num == sum(map(int, str(i))) + i:
            return False
    return True

for i in range(1,10001):
    if selfnum(i):
        print(i)
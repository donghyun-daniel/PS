n = input()
num = int(n)
start = max(num - 9*len(n),0)
res = []
for i in range(start, num):
    if num == sum(map(int,str(i)))+i:
        res.append(i)
if len(res) == 0:
    print(0)
else:
    print(min(res))
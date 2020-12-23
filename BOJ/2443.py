N = int(input())
for i in reversed(range(N)):
    space, star = " ", "*"
    print(f"{space * (i - 1)}*{space * (i - 1)}")
def square(n): return int(n)*int(n)
print(sum(list(map(square,input().split())))%10)
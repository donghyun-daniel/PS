import sys
import math
input=sys.stdin.readline

min, max = map(int, input().split())
validation = [1 for _ in range(min, max+1)]
squares = [v**2 for v in range(2, int(math.sqrt(max))+1)]
for square in squares:
    cur_idx = (math.ceil(min / square) * square) - min
    while cur_idx <= max - min:
        validation[cur_idx] = 0
        cur_idx += square

result = sum(validation)
print(result)
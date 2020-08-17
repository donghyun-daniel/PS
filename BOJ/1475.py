import math
room=input()
num=[0 for i in range(10)]
for n in room:
    num[int(n)]+=1
num[6]=math.ceil((num[6]+num[9])/2)
print(max(num[:9]))
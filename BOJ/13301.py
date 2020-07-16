N=int(input())
l=[4,6,10,16,26]
for i in range(5,N):
    l.append(l[-2]+l[-1])
print(l[N-1])
x=int(input())
piece=0
while x!=0:
    if x%2==1:
        piece+=1
    x//=2
print(piece)
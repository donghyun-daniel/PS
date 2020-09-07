import sys
input=sys.stdin.readline
check=[0 for i in range(26)]
for _ in range(int(input())):
    check[ord(input()[0])-97]+=1
check = [chr(x+97) for x in range(len(check)) if check[x]>=5]
if check:
    print(''.join(check))
else:
    print("PREDAJA")
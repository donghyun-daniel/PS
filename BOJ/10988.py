str=input()
l1=[]
l2=[]
for i in str:
    l1.append(i)
for i in reversed(str):
    l2.append(i)
if l1==l2:
    print("1")
else:
    print("0")
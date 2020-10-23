A=list(map(int,input().split()))
B=list(map(int,input().split()))
dic={"A":0, "B":0}
win="D"
for i in range(len(A)):
    if A[i]>B[i]:
        dic["A"]+=3
        win="A"
    elif A[i]<B[i]:
        dic["B"]+=3
        win="B"
    else:
        dic["A"]+=1
        dic["B"]+=1
print(dic["A"], dic["B"])
if dic["A"]==dic["B"]:
    print(win)
elif dic["A"]>dic["B"]:
    print("A")
else:
    print("B")
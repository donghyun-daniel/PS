test=int(input())
for i in range(test):
    n = int(input())
    key_1=(input().split())
    key_2=input().split()
    pw=input().split()
    recover=[0 for i in range(n)]
    for k in range(0,len(key_2)):
        recover[key_1.index(key_2[k])]=pw[k]
    print(" ".join(recover))
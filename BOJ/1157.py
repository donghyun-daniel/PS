s=input()
check=[0 for i in range(26)] #0 26개, check[0]에 있는 숫자가 a의 갯수를 의미
for i in s:
    num=ord(i)
    if num>96:
        num-=32
    check[num-65]+=1

max=1
ans=[]
for i in range(len(check)):
    if check[i]>max:
        ans=[i]
        max=check[i]
    elif check[i]==max:
        ans.append(i)

if len(ans)==1:
    print(chr(ans[0]+65))
else:
    print("?")
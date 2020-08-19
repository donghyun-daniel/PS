str =input()
ans=[]
for i in range(len(str)):
    ans.append(str[i:])
ans=sorted(ans)
for i in ans:
    print(i)
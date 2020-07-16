str = input()
str = list(str.lower())
found=[]
count=[]
for i in str:
    if i in found:
        count[found.index(i)]+=1
    else:
        found.append(i)
        count.append(1)
max=0
cnt=0
max_alphabet=0
for i in range(len(count)):
    if max<count[i]:
        cnt=1
        max=count[i]
        max_alphabet=found[i]
    elif max==count[i]:
        cnt+=1

if cnt>1:
    print("?")
else:
    print(max_alphabet.upper())
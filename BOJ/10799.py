str = input()

def check(s,i):
    if s[i]=="(":
        return 1
    else: return 2

stick=0
sum=0
i=0
while i<len(str):
    if check(str, i)==1 and check(str, i+1)==2:
        sum+=stick
        i+=2
        continue
    if check(str,i)==1:
        stick+=1
        sum+=1
    elif check(str,i)==2:
        stick-=1
    i+=1
print(sum)
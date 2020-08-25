s=[]
for _ in range(5):
    score = int(input())
    s.append(score if score>40 else 40)
print(sum(s)//5)
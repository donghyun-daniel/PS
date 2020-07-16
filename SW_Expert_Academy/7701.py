T=int(input())
for t in range(T):
    print(f"#{t+1} ")
    N=int(input())
    word=[]
    for _ in range(N):
        new=input()
        word.append((new, len(new)))
    word=list(set(word))
    word=sorted(word, key=lambda x : (x[1],x[0]))

    for i in word:
        print(i[0])
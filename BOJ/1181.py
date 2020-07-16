import sys
input=sys.stdin.readline

words=set()
for _ in range(int(input())):
    words.add(input())
words=list(words)
words=sorted(words, key = lambda x : (len(x), x))
print(''.join(words))
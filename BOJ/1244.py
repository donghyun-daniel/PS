N = int(input())
s = [0] + list(input().split())
for _ in range(int(input())):
    sex, num = map(int, input().split())
    if sex == 1: # 남자
        for i in range(num, N + 1, num):
            s[i] = "0" if s[i] == "1" else "1"
    else: # 여자
        tmp = 0
        for i in range(1, N):
            if 0 < num-i < N+1 and 0 < num+i < N+1 and s[num-i] == s[num+i]:
                tmp = i
            else:
                break
        for i in range(num-tmp, num+tmp+1):
            s[i] = "0" if s[i] == "1" else "1"
s = s[1:]
for i in range(0, N, 20):
    print(' '.join(s[i:i+20]))
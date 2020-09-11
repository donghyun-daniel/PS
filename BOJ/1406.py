import sys
input=sys.stdin.readline
stk1 = list(input().rstrip())
stk2 = []
for _ in range(int(input())):
    cmd=list(input().split())
    if cmd[0] == 'L':
        if stk1:
            stk2.append(stk1.pop())
        else:
            continue
    elif cmd[0] == 'D':
        if stk2:
            stk1.append(stk2.pop())
        else:
            continue
    elif cmd[0] == 'B':
        if stk1:
            stk1.pop()
        else:
            continue
    elif cmd[0] == 'P':
        stk1.append(cmd[1])
print(''.join(stk1 + list(reversed(stk2))))
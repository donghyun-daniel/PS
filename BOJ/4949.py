import sys
input=sys.stdin.readline
while True:
    s = input().rstrip()
    if s == '.':
        break
    stack = []
    tmp = True
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                tmp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                tmp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if tmp == True and not stack:
        print('yes')
    else:
        print('no')
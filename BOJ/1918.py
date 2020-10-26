p = {'*': 2,'/': 2,'+': 1,'-': 1,'(': 0}
stk = []
for c in '('+input()+')':
    if 'A' <= c <= 'Z':
        print(c, end='')
    elif c == '(':
        stk.append(c)
    elif c == ')':
        while True:
            o = stk.pop()
            if o == '(':
                break
            print(o, end='')
    else:
        while stk[-1] != '(' and p[c] <= p[stk[-1]]:
            print(stk.pop(), end='')
        stk.append(c)
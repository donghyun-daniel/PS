N = int(input())
for i in range(N*2 - 1):
    row = abs((N - 1) - i)
    if row == N - 1: # 위아래 양 끝
        print(f"{'*'*N}{' '*(1 + 2*(row - 1))}{'*'*N}")
    elif row == 0: # 중앙
        print(f"{' ' * (N-1)}*{' ' * (N - 2)}*{' ' * (N - 2)}*")
    else: # 나머지
        print(f"{' ' * abs(N - 1 - row)}*{' ' * (N-2)}*{' '*(1 + 2*(row - 1))}*{' ' * (N-2)}*")
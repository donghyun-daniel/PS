def chk(key, lock, r, c, m, n):
    for i in range(m):
        for j in range(m):
            if lock[i + r][j + c] > -1:
                lock[i + r][j + c] += key[i][j]
    for i in lock:
        print(i)
        if 0 in i:
            return False
    return True

def solution(key, lock):
    m, n = len(key), len(lock)
    lock_padding = [[-1 for n in range(3*n - 2)] for i in range(n - 1)] + \
                   [[-1 for _ in range(n - 1)] + l + [-1 for _ in range(n - 1)] for l in lock] + \
                   [[-1 for n in range(3*n - 2)] for i in range(n - 1)]

    for r in range(0, (3*n - 2 - m + 1)):
        for c in range(0, (3*n - 2 - m + 1)):
            print(f"r = {r}, c = {c}")
            if chk(key, lock_padding, r, c, m, n):
                print(r, c, "ans")
                return True

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
n=int(input())

def multiply(x, y):
    a, b = x
    c, d = y
    return (a*c + b*d, a*d + b*c + b*d)

def power(x, n):
    if n is 0:
        return (1, 0)
    if n % 2 == 0:
        return power(multiply(x, x), n // 2)
    return multiply(power(multiply(x, x), n // 2), x)

def fib_fast(n):
    return power((1, 1), n)[0]

print(fib_fast(10))
for i in range(n+1):
    print(fib_fast(i), end='->')
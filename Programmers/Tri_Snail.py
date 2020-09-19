import timeit
start=timeit.default_timer()
def solution(n):
    l=[[i+1] for i in range(n)]
    val=n+1
    while n:
        n-=1
        l[-1]+=[l[-1][0] for i in range(n)]
        for i in reversed(range((n-1)):


    print(l)
    return l

solution(4)
print(f"working time : {timeit.default_timer()-start:.8f}")
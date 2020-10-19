def getPi(P, m):
    j = 0
    k = -1
    pi = [0] * (m+1)
    pi[j] = k
    while j < m:
        if k == -1 or P[j] == P[k]:
            j += 1
            k += 1
            pi[j] = k
        else:
            k = pi[k]
    return pi


def kmp(A, P, n, m, res):
    i = j = 0
    pi = getPi(P, m)
    while i < n:
        if j == -1 or A[i] == P[j]:
            i += 1
            j += 1
        else:
            j = pi[j]
        if j == m:  # Success
            res.append(i-m+1)
            j = pi[j]

def findPattern(A,P): #res의 pattern의 시작 idx를 담아 return
    res = []
    kmp(A, P, len(A), len(P), res)
    return res

P = "I"+"OI"*int(input())
N=int(input())
A = input()
print(len(findPattern(A,P)))
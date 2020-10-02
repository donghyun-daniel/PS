from math import gcd
def solution(W,H):
    return (W-1)*(H-1)-1+gcd(W,H)

solution(8,12)
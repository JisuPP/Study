import math

def solution(numer1, denom1, numer2, denom2):

    y = (numer1*denom2)+(numer2*denom1)
    x = (denom1*denom2)

    n = math.gcd(y, x)
    
    return [y//n, x//n]
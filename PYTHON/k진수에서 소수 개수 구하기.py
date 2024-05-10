import numpy as np
from sympy import isprime

def solution(n, k):
    # numpy 라이브러리 이용하여 n을 k진수로 변환하기
    n_to_k  = np.base_repr(n, base=k)

    # sympy 라이브러리 이용하여 소수 확인
    answer = 0
    for num in n_to_k.split('0'):
        if num and int(num) > 1:
            if isprime(int(num)):
                answer = answer + 1
    return answer
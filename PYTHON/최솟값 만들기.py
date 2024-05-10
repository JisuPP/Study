def solution(A,B):
    n = len(A)
    answer = 0
    
    A.sort()
    B.sort(reverse=True)

    for i in range(0, n):
        answer = answer + (A[i]*B[i])

    return answer
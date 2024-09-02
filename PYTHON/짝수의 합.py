def solution(n):
    answer = 0
    for r in range(0,n+1,2):
        answer = answer + r
    return answer

####################################

def solution(n):
    return sum([i for i in range(2, n+1, 2)])

def soltuion(n):
    return sum(range(0, n+1, 2))
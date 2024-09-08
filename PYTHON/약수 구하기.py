def solution(n):
    answer = []
    for x in range(1, n+1):
        if n%x == 0:
            answer.append(x)
    return answer

############################

def solution(n):
    answer = [i for i in range(1, n+1) if n%i == 0]
    return answer
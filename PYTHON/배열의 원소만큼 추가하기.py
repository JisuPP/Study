def solution(arr):
    answer = []
    for a in arr:
        answer = answer + [a]*a
    return answer

################################

def solution(arr):
    answer = []
    for n in arr:
        answer.extend([n]*n)
    return answer
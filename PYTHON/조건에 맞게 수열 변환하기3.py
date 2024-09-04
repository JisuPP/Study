def solution(arr, k):
    answer = []
    for a in arr:
        if k%2 != 0:
            answer.append(a*k)
        else:
            answer.append(a+k)
    return answer

################################

def solution(arr, k):
    return [i*k if k%2!=0 else i+k for i in arr]
    
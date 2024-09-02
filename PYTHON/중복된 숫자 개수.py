def solution(array, n):
    answer = 0
    for ar in array:
        if ar == n:
            answer += 1
    return answer

#############################

def solution(array, n):
    return array.count(n)

def solution(array, n):
    return sum(1 for x in array if x == n)
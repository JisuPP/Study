def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(num*2)
    return answer

##############################

def solution(numbers):
    return [num*2 for num in numbers]

def solution(numbers):
    return list(map(lambda x: x*2, numbers))
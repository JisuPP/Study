def solution(n, numlist):
    answer = []
    for num in numlist:
        if num%n == 0:
            answer.append(num)
    return answer
    
################################

def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))

def solution(n, numlist):
    answer = [i for i in numlist if i%n==0]
    return answer
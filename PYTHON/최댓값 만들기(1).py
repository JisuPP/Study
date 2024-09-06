def solution(numbers):
    numbers.sort()
    return numbers[-1]*numbers[-2]

##################################

def solution(numbers):
    numbers.sort(reversse=True)
    return numbers[0]*numbers[1]
def solution(a, b):
    answer = 0
    if (a%2 != 0) and (b%2 != 0):
        answer = (a*a) + (b*b)
    elif ((a%2 != 0) and (b%2 ==0)) or ((a%2 == 0) and (b%2 != 0)):
        answer = 2*(a+b)
    else:
        answer = abs(a-b)
    return answer

##################################################

def solution(a, b):
    if a%2 and b%2: return a*a+b*b
    elif a%2 or b%2: return 2*(a+b)
    return abs(a-b)
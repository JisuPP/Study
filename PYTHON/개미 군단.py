# 장군개미 : 5
# 병정개미 : 3
# 일개미 : 1

def solution(hp):
    A = hp//5
    a = hp%5

    B = a//3
    b = a%3

    C = b

    return A+B+C

#######################

def solution(hp):
    return hp//5 + (hp%5//3) + ((hp%5)%3)

def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer
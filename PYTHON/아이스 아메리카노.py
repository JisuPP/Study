def solution(money):
    return [int(money//5500), money-(int(money//5500)*5500)]

############################################################

def solution(money):
    return [money//5500, money%5500]

def solution(money):
    return divmod(money, 5500)
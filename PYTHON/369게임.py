def solution(order):
    ans = 0

    for o in str(order):
        if o == '3' or o == '6' or o == '9':
            ans += 1
    
    return ans

###############################

def solution(order):
    return sum(map(lambda x: str(order).count(str(x), [3, 6, 9])))

def solution(order):
    ans = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')

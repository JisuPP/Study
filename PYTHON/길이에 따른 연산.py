def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        ans = 1
        for num in num_list:
            ans *= num
        return ans
    
################################
    
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))
    
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>11 else prod(num_list)
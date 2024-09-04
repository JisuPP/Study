def solution(num_list):
    A = 1
    B = 0

    for num in num_list:
        A *= num
        B += num

    if A < B**2:
        return 1
    else:
        return 0
    
############################
    
def solution(num_list):
    s = sum(num_list)**2
    m = eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0

def solution(num_list):
    mul = 1
    for n in num_list:
        mul *= n

    return int(mul < sum(num_list) ** 2)
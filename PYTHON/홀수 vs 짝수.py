def solution(num_list):
    
    a = num_list[0::2]
    b = num_list[1::2]
    
    a = sum(a)
    b = sum(b)
    
    if a > b:
        answer = a
    else:
        answer = b
    
    return answer

####################################

def solution(num_list):
    odd_sum  = sum(num_list[0::2])
    even_sum = sum(num_list[1::2])

    return max(odd_sum, even_sum)
    
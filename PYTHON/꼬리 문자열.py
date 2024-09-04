def solution(str_list, ex):
    answer = ''
    for s in str_list:
        if ex not in s:
            answer += s
    return answer

###########################

def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))

def solution(str_list, ex):
    return ''.join([i for i in str_list if ex not in i])
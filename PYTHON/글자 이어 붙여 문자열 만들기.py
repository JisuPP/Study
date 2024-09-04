def solution(my_string, index_list):
    answer = ''
    for idx in index_list:
        answer += my_string[idx]
    return answer

#######################################

def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])

def solution(my_string, index_list):
    lst = []
    for i in index_list:
        lst.append(my_string[i])
    return ''.join(lst)
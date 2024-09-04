def solution(arr, delete_list):
    answer = []
    for a in arr:
        if a not in delete_list:
            answer.append(a)
    return answer

####################################

def solution(arr, delete_list):
    return [i for i in arr if i not in delete_list]

def solution(arr, delete_list):
    answer = []
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr
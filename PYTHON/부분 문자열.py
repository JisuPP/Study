def solution(str1, str2):
    if str1 in str2:
        return 1
    else:
        return 0

##########################

def solution(str1, str2):
    return int(str1 in str2)

def solution(str1, str2):
    return [0,1][str1 in str2]
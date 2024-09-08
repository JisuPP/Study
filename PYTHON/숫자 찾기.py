def solution(num, k):
    num = str(num)
    for i in range(0, len(num)):
        if int(num[i]) == k:
            return i+1
    return -1

##############################

def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) +1

def solution(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i+1
    return -1
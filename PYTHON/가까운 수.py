def solution(array, n):
    array.sort()
    diff = [abs(a - n) for a in array]
    min_idx = diff.index(min(diff))
    return array[min_idx]

###############################


def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer


def solution(array, height):
    answer = 0
    for arr in array:
        if arr > height:
            answer += 1
    return answer

##############################

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

def solution(array, height):
    return sum(1 for a in array if a > height)
def solution(my_string, pat):
    answer = 0
    for i in range(0, len(my_string)):
        if my_string[i:i+len(pat)] == pat:
            answer += 1
    return answer

####################################

def solution(my_string, pat):
    ans = 0
    for idx, s in enumerate(my_string):
        if my_string[idx:].startswith(pat):
            ans += 1
    return ans

def solution(my_string, pat):
    return sum(my_string[i:i+len(pat)] == pat for i in range(len(my_string)))

def solution(my_string, m, c):
    return my_string[c-1::m]

##############################

def solution(my_string, m, c):
    ans = ''
    for i in range(c-1, len(my_string), m):
        ans += my_string[i]
    return ans
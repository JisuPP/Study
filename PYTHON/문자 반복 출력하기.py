def solution(my_string, n):
    ans = ''
    for char in my_string:
        ans += char*n
    return ans

#############################

def solution(my_string, n):
    return ''.join(i*n for i in my_string)
def solution(str1, str2):
    ans = ''
    for i in range(len(str1)):
        ans = ans + str1[i] + str2[i]
    return ans

################################

def solution(str1, str2):
    ans = ''.join([str1[i] + str2[i] for i in range(len(str1))])
    return ans

def solution(str1, str2):
    ans = ''
    for s1, s2 in zip(str1, str2):
        ans += s1+s2
    return ans

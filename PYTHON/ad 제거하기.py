def solution(str_arr):
    return [a for a in str_arr if 'ad' not in a]

#############################################

def solution(str_arr):
    ans = []

    for a in str_arr:
        if 'ad' not in a:
            ans.append(a)

    return ans
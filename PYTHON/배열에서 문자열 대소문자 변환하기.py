def solution(str_arr):
    ans = []
    
    for l in range(len(str_arr)):
        if l%2 != 0:
            ans.append(str_arr[l].upper())
        else:
            ans.append(str_arr[l].lower())
    
    return ans

################################################

def solution(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]
def solution(int_strs, k, s, l):
    ans = []
    for i in int_strs:
        if int(i[s:s+l]) > k:
            ans.append(int(i[s:s+l]))
    return ans

##################################

def solution(intStrs, k, s, l):
    return [int(intstr[s:s+l]) for intstr in intStrs if int(intstr[s:s+l]) > k]
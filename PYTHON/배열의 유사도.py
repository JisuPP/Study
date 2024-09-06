def solution(s1, s2):
    ans = 0
    for a in s1:
        for b in s2:
            if a == b:
                ans += 1
    return ans

###########################

def solution(s1, s2):
    return len(set(s1)&set(s2))
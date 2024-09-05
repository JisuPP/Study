def solution(num_log):
    ans = ''
    for idx in range(1, len(num_log)):
        k = num_log[idx] - num_log[idx-1]

        if k == 1:
            ans += 'w'
        elif k == -1:
            ans += 's'
        elif k == 10:
            ans += 'd'
        else:
            ans += 'a'
    
    return ans

###########################################

def solution(log):
    ans = ''
    joy = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))

    for i in range(1, len(log)):
        ans += joy[log[i] - log[i-1]]
    
    return ans
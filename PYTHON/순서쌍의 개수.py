def solution(n):
    ans = 0
    for x in range(1, n+1):
        if n%x == 0:
            ans += 1
    return ans

###############################

def solution(n):
    return len(list(filter(lambda v: n%(v+1) == 0, range(n))))

def solutoin(n):
    return len([number for number in range(1, n+1) if n%number == 0])
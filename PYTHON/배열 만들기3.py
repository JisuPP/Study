def solution(arr, intervals):
    a, b = intervals[0][0], intervals[0][1]
    x, y = intervals[1][0], intervals[1][1]
    return arr[a:b+1] + arr[x:y+1]

###########################################

def solution(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]
    return arr[s1:e1+1]+arr[s2:e2+1]

def solution(arr,interevals):
    answer = []
    for a, b in interevals:
        answer += arr[a:b+1]
        return answer
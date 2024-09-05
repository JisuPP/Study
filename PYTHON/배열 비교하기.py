def solution(arr1, arr2):
    ans = 0
    a = len(arr1)
    b = len(arr2)

    if a > b:
        ans = 1
    elif a < b:
        ans = -1
    else:
        if sum(arr1) > sum(arr2):
            ans = 1
        elif sum(arr1) < sum(arr2):
            ans = -1
        else:
            ans = 0
    return ans

########################################

def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))
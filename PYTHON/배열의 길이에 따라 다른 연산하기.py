def solution(arr, n):
    if len(arr)%2 != 0:
        for x in range(len(arr)):
            if x%2 == 0:
                arr[x] = arr[x] + n
    else:
        for y in range(len(arr)):
            if y%2 != 0:
                arr[y] = arr[y] + n
    
    return arr

#########################################

def solution(arr, n):
    N = len(arr)
    
    if N%2:
        for i in range(0, N, 2):
            arr[i] += n
    else:
        for i in range(1, N, 2):
            arr[i] += n
    
    return arr
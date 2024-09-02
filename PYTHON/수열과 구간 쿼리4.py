def solution(arr, queries):
    answer = []
    
    for query in queries:
        a, b, c = query
        for i in range(a, b+1):
            if i%c == 0:
                arr[i] = arr[i] + 1
            
        
    return arr
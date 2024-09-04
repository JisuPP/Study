def solution(a, b):
    X = int(str(a) + str(b))
    Y = 2*a*b

    if X >= Y:
        return X
    else:
        return Y
    
##############################
    
def solution(a, b):
    return max(int(str(a) + str(b)), 2*a*b)

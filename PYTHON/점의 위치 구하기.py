def solution(dot):
    x, y = dot[0], dot[1]
    if x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    else:
        return 4
    
########################
    

def solution(dot):
    x, y = dot
    if x*y > 0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2
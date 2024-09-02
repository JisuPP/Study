def solution(angle):
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle < 180:
        return 3
    else:
        return 4

#################################################
    
def solution(angle):
    answer = (angle//90)*2 + (angle%90>0) * 1

def solution(angle):
    if angle <= 90:
        return 1 if angle < 90 else 2
    else:
        return 3 if angle < 180 else 4
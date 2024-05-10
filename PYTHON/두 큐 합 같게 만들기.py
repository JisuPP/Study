def solution(queue1, queue2):
    answer = -1
    q1 = sum(queue1)
    q2 = sum(queue2)
    avg = (q1+q2)//2
    x = 0
    y = 0
    l = len(queue1)
    while x<2*l and y<2*l and q1!=q2:
        if q1 < avg:
            q1 = q1 + queue2[y]
            q2 = q2 - queue2[y]
            queue1.append(queue2[y])
            y = y+1
        else:
            q1 = q1 - queue1[x]
            q2 = q2 + queue1[x]
            queue2.append(queue1[x])
            x = x+1
    if q1 == avg:
        answer = x + y
    return answer
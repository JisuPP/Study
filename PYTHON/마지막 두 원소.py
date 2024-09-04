def solution(num_list):
    X = num_list[len(num_list)-1]
    Y = num_list[len(num_list)-2]

    if X > Y:
        num_list.append(X-Y)
    else:
        num_list.append(X*2)
    
    return num_list

######################################

def solution(l):
    l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
    return l

def solution(num_list):
    a = num_list[-1]
    b = num_list[-2]
    if a > b:
        num_list.append(a-b)
    else:
        num_list.append(2*a)
    return num_list
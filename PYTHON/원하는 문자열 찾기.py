def solution(my_string, pat):
    my_string = my_string.lower()
    pat = pat.lower()

    if pat in my_string:
        return 1
    else:
        return 0

#####################################
    
def solution(my_string, pat):
    return int(pat.lower() in my_string.lower())
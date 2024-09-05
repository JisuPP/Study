def solution(my_string, pat):
    my_string = my_string.replace('A', 'C')
    my_string = my_string.replace('B', 'A')
    my_string = my_string.replace('C', 'B')

    if pat in my_string:
        return 1
    else:
        return 0
    
##############################################
    
def solution(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))


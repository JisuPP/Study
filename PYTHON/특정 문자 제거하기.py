def solution(my_string, letter):
    return my_string.replace(letter, '')

#########################################

def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string
    return answer

def solution(my_string, letter):
    return ''.join([c for c in my_string if c!= letter])
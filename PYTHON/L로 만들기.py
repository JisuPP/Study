def solution(my_string):
    ans = ''
    for char in my_string:
        if char < 'l':
            ans += 'l'
        else:
            ans += char
    return ans 

###########################

def solution(my_string):
    return my_string.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

def solution(my_string):
    ans = [x if x > 'l' else 'l' for x in my_string]
    return ''.join(ans)
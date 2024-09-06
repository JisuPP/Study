def solution(my_string):
    return my_string.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

##################################

def solution(my_string):
    return ''.join([i for i in my_string if not (i in 'aeiou')])

def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string
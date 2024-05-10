def solution(word):
    answer = 0
    alphabet = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    
    
    num_word = [alphabet[char] for char in word]
    
  
    sorted_word = sorted(num_word)
    
    
    answer = sorted_word.index(num_word) + 1
    
    return answer
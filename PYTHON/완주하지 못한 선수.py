def solution(participant, completion):
    
    for name in completion:
        participant.remove(name)
        
    return participant[0]
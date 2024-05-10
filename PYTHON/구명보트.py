def solution(people, limit):
    answer = 0
    people.sort()
    first = 0
    last = len(people)-1
    
    while first <= last:
        if people[first] + people[last] <= limit:
            answer = answer + 1
            first = first + 1
        last = last - 1
            
    return len(people) - answer
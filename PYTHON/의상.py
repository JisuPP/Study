def solution(clothes):
    clothes_dict = {}
    for item, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = 1
        else:
            clothes_dict[category] += 1
    
    total_combinations = 1
    for count in clothes_dict.values():
        total_combinations *= (count + 1)  
    
    
    return total_combinations - 1
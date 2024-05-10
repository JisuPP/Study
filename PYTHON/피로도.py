def solution(k, dungeons):
    
    dungeons.sort(key=lambda x: x[0])
    
    
    explored_dungeons = 0
    
    
    for dungeon in dungeons:
        if k >= dungeon[0]:
            k -= min(dungeon[0], dungeon[1])  
            explored_dungeons += 1
            
    return explored_dungeons
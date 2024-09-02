from collections import deque

def solution(bridge_length, weight, truck_weights):

    # 다리 큐
    bridge = deque([0] * bridge_length)

    # 대기 트럭 큐
    waiting_trucks = deque(truck_weights)

    # 시간
    time = 0

    total_weight = 0

    while waiting_trucks or total_weight > 0:
        time = time + 1
        total_weight = total_weight - bridge.popleft()

        if waiting_trucks and (total_weight+waiting_trucks[0]) <= weight:
            truck_weights = waiting_trucks.popleft()
            bridge.append(truck_weights)
            total_weight = total_weight + truck_weights
        else:
            bridge.append(0)
    
    return time
# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    bridge, now_weight, count = [], 0, 0
    answer = 0
    for i in range(len(truck_weights)):

    while count < len(truck_weights):
        bridge.append(truck_weights[count])
        now_weight += truck_weights[count]
        count, answer = (count + 1), (answer + 1)
        if count == len(truck_weights):
            # 마지막 인덱스는 그냥 다리 탈출
            answer += bridge_length



        bridge += truck_weights[count]
        count, answer = (count + 1), (answer + 1)
        if count == len(truck_weights):
            # 마지막 인덱스는 그냥 다리 탈출
            answer += bridge_length
        elif bridge >= weight:
            answer += bridge_length
            if bridge > weight:
                bridge, answer = truck_weights[count - 1], (answer - 1)
            else:
                bridge = 0
        print(answer, bridge, truck_weights[count:], count)
    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
print(solution(5,5,[2, 2, 2, 2, 1, 1, 1, 1, 1]))
# 올라가고 내려가는데 총 bridge_length + 1 초가 걸림
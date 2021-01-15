# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    bridge, count = 0, 0
    answer = 0
    while count < len(truck_weights):
        bridge += truck_weights[count]
        count, answer = (count + 1), (answer + 1)
        if bridge >= weight:
            answer += bridge_length
            if bridge > weight:
                bridge, answer = truck_weights[count - 1], (answer - 1)
            else:
                bridge = 0
        if count == len(truck_weights):
            answer += bridge_length
        print(answer, bridge, truck_weights[count:], count)
    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
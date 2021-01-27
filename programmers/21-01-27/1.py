# 스킬 체크 테스트 Level 3
def solution(genres, plays):
    answer = []
    # 장르 재생수 기록, 장르 속한 레코드 기록
    ranks, disk = dict(), dict()
    for i in range(len(genres)):
        if genres[i] not in ranks:
            ranks[genres[i]] = 0
            disk[genres[i]] = dict()
        if plays[i] not in disk[genres[i]]:
            disk[genres[i]][plays[i]] = list()
        ranks[genres[i]] += plays[i]
        disk[genres[i]][plays[i]].append(i)
    # 모든 데이터를 정리
    total_data = dict()
    for key in ranks.keys():
        total_data[ranks[key]] = dict()
        for key2 in disk[key].keys():
            total_data[ranks[key]][key2] = disk[key][key2]
    for key in reversed(sorted(total_data.keys())):
        if len(answer) > (len(total_data) * 2):
            break
        count = 0
        for key2 in reversed(sorted(total_data[key].keys())):
            if len(answer) > (len(total_data) * 2):
                break
            if count > 2:
                break
            for index in reversed(sorted(total_data[key][key2])):
                if len(answer) > (len(total_data) * 2):
                    break
                if count > 2:
                    break
                count += 1
                answer.append(index)
    return answer
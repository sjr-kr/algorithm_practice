# 2019 카카오 블라인드 코테 / 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
# Dictionary and List

# 내 풀이
def mySolution(N, stages):
    answer = []
    # rate = uncleared / reached
    cleared = {}
    uncleared = {}
    failure_rate = {}
    
    for i in range(N):
        cleared.update({i+1 : 0})
        uncleared.update({i+1 : 0})
        
    for stage in stages:
        for i in range(stage-1):
            cleared[i+1] += 1
        if stage <= N:
            uncleared[stage] += 1

    for i in range(N):
        if uncleared[i+1] == 0:
            failure_rate.update({i+1 : 0})
        else:
            failure_rate.update({i+1 : uncleared[i+1]/(cleared[i+1]+uncleared[i+1])})
    
    sorted_failure_rate = sorted(failure_rate.items(), key=lambda x:x[1], reverse=True)
    
    for element in sorted_failure_rate:
        answer.append(element[0])
        
    return answerStr

# 베스트 풀이
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
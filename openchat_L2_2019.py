# 2019 카카오 블라인드 코테 / 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888
# 2D Array, String Formatting

# 내 풀이
def mySolution(record):
    log_list = []
    answer = []
    id_name = {}
    # changing each log from str to list [action, id, name]
    for log in record:
        log = log.split()
        log_list.append(log)
        if log[0] == "Enter" or log[0] == "Change":
            id_name[log[1]] = log[2]
    for i in range(len(record)):
        if log_list[i][0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(id_name[log_list[i][1]]))
        elif log_list[i][0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(id_name[log_list[i][1]]))
    return answer

# 베스트 풀이
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
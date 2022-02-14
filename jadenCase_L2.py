# 프로그래머스 코딩테스트 연습
# https://programmers.co.kr/learn/courses/30/lessons/12951

# 내 풀이
def mySolution(s):
    s_list = s.split(' ')
    ans_list = []
    for word in s_list:
        ans_list.append(word.capitalize())
    answer = ' '.join(ans_list)
    return answer

# 베스트 풀이
def solution(s):
    return s.title()
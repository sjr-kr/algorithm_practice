# 프로그래머스 코딩테스트 연습
# https://programmers.co.kr/learn/courses/30/lessons/42862
# Greedy

# 내 풀이
def mySolution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for num in reserve[:]:
        if num-1 in lost:
            lost.remove(num-1)
        elif num+1 in lost:
            lost.remove(num+1)
        elif num in lost:
            lost.remove(num)
            reserve.remove(num)
    return n - len(lost)

# 베스트 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
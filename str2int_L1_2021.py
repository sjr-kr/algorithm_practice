# 2021 카카오 채용연계형 인턴십
# https://programmers.co.kr/learn/courses/30/lessons/81301
# Data Types

# 내 풀이
def mySolution(s):
    answer = 0
    answerStr = ""
    word2num = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9", "" : ""}
    word_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digit2num = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9}
    temp = ""
    for char in s:
        # 숫자인 경우
        if char in "0123456789":
            answerStr += word2num[temp]
            answerStr += char
            temp = ""
        # 단어인 경우
        else:
            if temp in word_list:
                answerStr += word2num[temp]
                temp = char
            else:
                temp += char
    answerStr += word2num[temp]
    for i in range(len(answerStr)):
        answer += digit2num[answerStr[i]] * 10**(len(answerStr)-(i+1))
    return answer

# 베스트 풀이
num_dic = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
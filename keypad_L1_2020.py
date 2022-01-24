# 2020 카카오 인턴십 / 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256
# 2D Array

# 내 풀이
def mySolution(numbers, hand):
    # 1  2  3
    # 4  5  6
    # 7  8  9
    # *  0  #
    keypad_pos = [[1, 0], [0, 3], [1, 3], [2, 3], [0, 2], [1, 2], [2, 2], [0, 1], [1, 1], [2, 1]]
    left_pos = [0, 0]
    right_pos = [2, 0]
    answer = ""
    for num in numbers:
        # 1, 4, 7 (left)
        if num % 3 == 1:
            answer += 'L'
            left_pos = keypad_pos[num]
        # 3, 6, 9 (right)
        elif num % 3 == 0 and num != 0:
            answer += 'R'
            right_pos = keypad_pos[num]
        # 2, 5, 8, 0 (center)
        else:
            if abs(right_pos[0]-keypad_pos[num][0]) + abs(right_pos[1]-keypad_pos[num][1]) < abs(left_pos[0]-keypad_pos[num][0]) + abs(left_pos[1]-keypad_pos[num][1]):
                answer += 'R'
                right_pos = keypad_pos[num]
            elif abs(right_pos[0]-keypad_pos[num][0]) + abs(right_pos[1]-keypad_pos[num][1]) > abs(left_pos[0]-keypad_pos[num][0]) + abs(left_pos[1]-keypad_pos[num][1]):
                answer += 'L'
                left_pos = keypad_pos[num]
            else:
                if hand == "right":
                    answer += 'R'
                    right_pos = keypad_pos[num]
                else:
                    answer += 'L'
                    left_pos = keypad_pos[num]
    return answerStr

# 베스트 풀이
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer
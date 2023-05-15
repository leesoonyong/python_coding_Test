handHis = []
rightHandDis = 0
leftHandDis = 0
# 키패드 좌표값
pad ={
    '1' : (0,0), '2' : (0,1), '3' : (0,2),
    '4' : (1,0), '5' : (1,1), '6' : (1,2),
    '7' : (2,0), '8' : (2,1), '9' : (2,2),
    '*' : (3,0), '0' : (3,2), '#' : (3,3)
}

left = pad['*']   #처음 왼손의 위치
right = pad['#']  #처음 오른손의 위치

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]

for num in numbers:
    if num == 1 or num == 4 or num == 7 :
        handHis.append('L')        
        left = pad[str(num)]   #해당 번호를 눌렀을 때 왼손의 위치 저장
    
    #오른손이 누를 번호
    elif num == 3 or num == 6 or num == 9 :
        handHis.append('R')      
        right = pad[str(num)]    #해당 번호를 눌렀을 때 오른손의 위치 저장
    else:
        #번호와 왼손의 거리 계산
        left_dis = abs(left[0] - pad[str(num)][0]) + abs(left[1] - pad[str(num)][1])
        #번호와 오른손의 거리 계산
        right_dis = abs(right[0] - pad[str(num)][0]) + abs(right[1] - pad[str(num)][1])
        #왼쪽이더 가까울때
        #print("L: ",leftHandDis," R",rightHandDis)
        if left_dis < right_dis:
            handHis.append("L")
            left = pad[str(num)]
        #오른쪽이더 가까울때
        elif left_dis > right_dis:
            handHis.append("R")
            right = pad[str(num)]
        else:
            if hand == 'left':
                handHis.append("L")
                left = pad[str(num)]
            else:
                handHis.append("R")
                right = pad[str(num)]
print("".join(handHis))

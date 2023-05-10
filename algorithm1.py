board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]];
stacklist = []
answer = 0
moves = [1,5,3,5,1,2,1,4]

for move in moves:
    for j in range(len(board)):
        #자연수 move에서 -1을해서 인덱스 형식을 맞춘다
        #0(아무것도 없는상태가 아닐떄) 1개를 바구니에 넣는다 그후 넣은 요소를 뺴준다
        if board[j][move-1] > 0:
            stacklist.append(board[j][move-1])
            board[j][move-1] = 0
            print(stacklist)     
            if len(stacklist) > 1:
                if(stacklist[-1] == stacklist[-2])
                    stacklist.pop(-1)
                    stacklist.pop(-1)
                    answer +=2
            break
print(answer)
# answer = []


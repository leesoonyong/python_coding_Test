# [백준][10799] 번
#풀이 예시 
# stack = [(,(,(] 여는 괄호가 세 번 나왔습니다.
# ()  레이저가 나오면
# 개수 = len(stack)
ir = input()
stack = []
cnt = 0
for i in range(len(ir)):
    if ir[i] == "(":
        stack.append("(")
    else:  #')'일때
        if ir[i-1] == "(": #')'의 전이 ( 괄호가있을때
            stack.pop()
            cnt += len(stack)
        else: # ')'괄호 다음에 ')'괄호가 왔을때
            stack.pop()
            cnt+=1
print(cnt)

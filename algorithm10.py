import sys
#백준 
n = int(sys.stdin.readline())

count = 1
temp = True
stack = []
op = []

for i in range(n):
    num = sys.stdin.readline()
    #num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
    #num이랑 stack의 제일 맨위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    #만약에 위에숫자가 현재숫자랑 맞지않으면 수열만들기 실패임
    else:
        temp = False
        break
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)


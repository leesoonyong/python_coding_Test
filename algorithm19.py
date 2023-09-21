#백준 1918번
#풀이
#https://chanmuzi.tistory.com/247
back_number = list(input())
stack = []
res = ''

for i in back_number:
    if i.isalpha(): #문자는 바로 정답에 문자열에 추가
        res += i
    elif i == '(': # 여는 괄호는 스택에추가
        stack.append(i)
    elif i == '*' or i == '/' :
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            res += stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()
while stack :
    res += stack.pop()
print(res)
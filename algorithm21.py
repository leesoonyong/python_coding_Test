#백준 1935번
N = int(input())
word = list(input()) #후위표기식을 word에 저장한다.
stack = []
num = [int(input()) for _ in range(N)]  # 변수에 값을 저장하는 리스트

for i in word:
    if i.isalpha():
         stack.append(num[ord(i) - ord('A')])  # 알파벳을 숫자로 변환하여 스택에 저장 이게대박..
    else:
        a = stack.pop()
        result = stack.pop()
        
        print("a = ",a)
        print("b = ", result)
        
        if i == '+':
            result += a
        elif i == '-':
            result -= a
        elif i == '*':
            result *= a
        elif i == '/':
            result /=a
        
        stack.append(result)
print('%.2f' %stack[-1])
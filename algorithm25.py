# 백준11655번
alpha = input()  # input 함수를 사용하여 문자열을 받습니다
string = ''
result = []

for i in alpha:
    if i.isupper():
        string = chr(((ord(i) - ord('A') + 13) % 26) + ord('A'))
        result.append(string)
    elif i.islower():
        string = chr(((ord(i) - ord('a') + 13) % 26) + ord('a'))
        result.append(string)
    else:
        result.append(i)

print(''.join(result))

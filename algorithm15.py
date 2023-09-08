#백준 9093 
import sys
str1 = list(sys.stdin.readline())
tag = False
word_stack = []
res = []

for char in str1:
    if char == "<":
        tag = True
        while word_stack:
            res.append(word_stack.pop())
        res.append(char)
    elif char == ">":
        tag = False
        res.append(char)
    elif tag:
        res.append(char)
    elif char == " ":
        while word_stack:
            res.append(word_stack.pop())
        res.append(char)
    else:
        word_stack.append(char)

while word_stack:
    res.append(word_stack.pop())

result = ''.join(res)
print(result)
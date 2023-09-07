#백준 1158번 문제
import sys
n, k = map(int, input().split())
data = [i for i in range(1, n+1)]

index = 0
result = []

for _ in range(n):
    index += (k - 1)
    if index >= len(data):
        index %= len(data)
    result.append(str(data[index]))
    data.pop(index) 
print('<', end='')
print(', '.join(result), end='')
print('>')

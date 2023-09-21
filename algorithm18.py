#백준 17299번
#풀이 https://honggom.tistory.com/68
from collections import Counter
from sys import stdin

n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
nums_count = Counter(nums)
result = [-1] * n
stack = [0]

for i in range(1,n):
    print(stack[-1])
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
            result[stack.pop()] = nums[i]
    stack.append(i)
print(*result)

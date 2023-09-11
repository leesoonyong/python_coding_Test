#백준17298번
# 풀이참조 https://night-knight.tistory.com/entry/%EB%B0%B1%EC%A4%8017298-%EC%98%A4%ED%81%B0%EC%88%98-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
ans = [-1]*n
stack = [] 
for i in range(n):
    while stack and arr[i] > arr[stack[-1]]:
            ans[stack[-1]] = arr[i]
            stack.pop()
    stack.append(i)
print(*ans)
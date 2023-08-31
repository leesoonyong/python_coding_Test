import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    str = sys.stdin.readline().rstrip()
    for j in str:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
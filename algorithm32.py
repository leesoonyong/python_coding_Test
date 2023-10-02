n = int(input())
check = 0
num = 1
for i in range(2, n + 1):
    num *= i

num_str = str(num)
for i in num_str[::-1]:
    if i == '0':
        check += 1
    else:
        break
print(check)

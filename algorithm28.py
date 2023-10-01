# 백준10430번
a, b, c = map(int, input().split())

d = (a + b) % c
e = ((a % c) + (b % c)) % c
f = (a * b) % c
g = ((a % c) * (b % c)) % c

result = f"{d}\n{e}\n{f}\n{g}"
print(result)

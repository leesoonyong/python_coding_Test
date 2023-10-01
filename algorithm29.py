import math

a, b = map(int, input().split())

c = math.gcd(a, b)  # 최대공약수
d = (a * b) // c  # 최소공배수

result = f"{c}\n{d}"
print(result)

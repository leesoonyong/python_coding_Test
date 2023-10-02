import math
# import sys

# # 시간초과
# b, c = map(int, input().split())
# num_list = []
# for num in range(b, c+1):
#     if num > 1:
#         is_prim = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prim = False
#                 break
#         if is_prim:
#             num_list.append(num)
# print("\n".join(map(str, num_list)))

# 에라토스테네스의 체

b, c = map(int, input().split())
is_prime = [True] * (c + 1)
is_prime[0] = is_prime[1] = False

for p in range(2, int(math.sqrt(c)) + 1):
    if is_prime[p]:
        for i in range(p * p, c + 1, p):
            is_prime[i] = False

prime_numbers = [p for p in range(2, c + 1) if is_prime[p]]
print("\n".join(map(str, prime_numbers)))

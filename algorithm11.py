import sys
str = sys.stdin.readline()
list = list(str)
num = int(sys.stdin.readline())
total_index = len(list) - 1

#백준 1406번내풀이
# for i in range(num):
#     key = list(sys.stdin.readline())
#     if key[0] == 'P':
#         list.append(key[1])
#     elif key[0] == 'L':
#         total_index =- 1
#         if total_index == 0:
#             total_index = 0
#     elif key[0] == 'B':
#         if total_index == 0:
# 
import sys
# strlist = list(sys.stdin.readline())
# num = int(sys.stdin.readline())
# leng = len(strlist) 

#백준 1406번내풀이
# for _ in range(int(input)):
#     key = list(sys.stdin.readline())
#     if key[0] == 'P':
#         list.append(key[1])
#     elif key[0] == 'L':
#         total_index =- 1
#         if total_index == 0:
#             total_index = 0
#     elif key[0] == 'B':
#         if total_index == 0:

#풀이1
# for _ in range(num):
#     command = list(input().split())
#     if(command[0] == 'P'):
#         strlist.insert(leng, command[1])
#         leng += 1
#     elif(command[0] == 'L'):
#         if leng > 0:
#             leng -= 1
#     elif(command[0] == 'D'):
#         if leng < len(strlist):
#             leng += 1
#     else:
#         if leng > 0:
#             strlist.remove(strlist[leng-1])
# print(''.join(strlist))

#풀이2
st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif command[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(command[1])
st1.extend(reversed(st2))
print(''.join(st1))
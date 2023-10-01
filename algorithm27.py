# 백준 11656번
a = input()
a_list = []
for idx, char in enumerate(a, start=0):
    a_list.append(a[idx:])
a_list.sort()
print('\n'.join(a_list))

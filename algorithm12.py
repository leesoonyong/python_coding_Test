import sys
#백준 10845번
num = int(sys.stdin.readline())
strs = []
for i in range(num):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        strs.append(command[1])
    elif command[0] == 'front':
        if strs:
            print(strs[0])
        else:
            print('-1')
    elif command[0] == 'back':
        if strs:
            print(strs[-1])
        else:
            print('-1')
    elif command[0] == 'pop':
        if strs:
            print(strs[0])
            strs.pop(0)
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(strs))
    elif command[0] == 'empty':
        if strs:
            print(0)
        else:
            print(1)
